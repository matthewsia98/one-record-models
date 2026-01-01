import logging
import subprocess
from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import cast

from pydantic import AnyUrl
from rdflib import OWL, RDF, RDFS, XSD, BNode, Graph, Literal, URIRef
from rdflib.namespace import split_uri

XSD_TO_PYTHON = {
    XSD.anyURI: AnyUrl,
    XSD.boolean: bool,
    XSD.dateTime: datetime,
    XSD.string: str,
    XSD.int: int,
    XSD.integer: int,
    XSD.nonNegativeInteger: int,
    XSD.positiveInteger: int,
    XSD.double: float,
    XSD.duration: timedelta,
}

MODULE_TO_ONTOLOGY = {
    "api": "https://onerecord.iata.org/ns/api/ontology.ttl",
    "cargo": "https://onerecord.iata.org/ns/cargo/ontology.ttl",
    "code_lists": "https://onerecord.iata.org/ns/code-lists/ontology.ttl",
}

OUT_DIR = Path("src/one_record_ontology/models/generated")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR.joinpath("__init__.py").touch()


def uri_to_module_name(uri: URIRef) -> str:
    if uri.startswith("https://onerecord.iata.org/ns/api"):
        return "api"
    elif uri.startswith("https://onerecord.iata.org/ns/cargo"):
        return "cargo"
    elif uri.startswith("https://onerecord.iata.org/ns/code-lists"):
        return "code_lists"
    else:
        raise ValueError(f"Unknown namespace for URI: {uri}")


def topo_sort(classes: set[URIRef], parents: dict[URIRef, set[URIRef]]) -> list[URIRef]:
    """
    Topological sort classes so that base classes come before subclasses.
    """
    children = defaultdict(set)
    indegree = {cls: 0 for cls in classes}

    for child, ps in parents.items():
        for p in ps:
            if p in classes:
                children[p].add(child)
                indegree[child] += 1

    queue = deque(sorted(c for c in classes if indegree[c] == 0))
    result: list[URIRef] = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for ch in sorted(children[node]):
            indegree[ch] -= 1
            if indegree[ch] == 0:
                queue.append(ch)

    if len(result) != len(classes):
        raise RuntimeError("Cycle detected in class hierarchy")

    return result


for module_name, url in MODULE_TO_ONTOLOGY.items():
    g = Graph()
    g.parse(url)

    docstring_lines = [
        '"""',
        "This file was automatically generated from the ONE Record API ontology.",
        "",
        f"Ontology source: {url}",
    ]
    ontology = next(g.subjects(RDF.type, OWL.Ontology))
    if (version_iri := g.value(ontology, OWL.versionIRI)) is not None:
        docstring_lines.append(f"Ontology version: {version_iri}")
    docstring_lines.append(f"Generated on: {datetime.now(timezone.utc).isoformat()}")

    docstring_lines.extend(
        [
            "",
            "DO NOT EDIT MANUALLY.",
            '"""',
        ]
    )

    # Collect properties
    properties: dict[URIRef, dict] = defaultdict(dict)

    for dp, _, _ in g.triples((None, RDF.type, OWL.DatatypeProperty)):
        dp = cast(URIRef, dp)
        properties[dp][RDF.type] = g.value(dp, RDF.type)

        dp_domain = g.value(dp, RDFS.domain)
        if isinstance(dp_domain, URIRef):
            properties[dp][RDFS.domain] = dp_domain
        elif isinstance(dp_domain, BNode):
            for _, _, union in g.triples((dp_domain, OWL.unionOf, None)):
                properties[dp][RDFS.domain] = list(g.items(union))

        range = g.value(dp, RDFS.range)
        if isinstance(range, URIRef):
            properties[dp][RDFS.range] = g.value(dp, RDFS.range)
        elif isinstance(range, BNode):
            properties[dp][RDFS.range] = g.value(range, OWL.onDatatype)
            with_restrictions = g.value(range, OWL.withRestrictions)
            if with_restrictions is not None:
                for restriction in g.items(with_restrictions):
                    properties[dp][XSD.pattern] = g.value(restriction, XSD.pattern)
                    properties[dp][XSD.minLength] = g.value(restriction, XSD.minLength)
                    properties[dp][XSD.maxLength] = g.value(restriction, XSD.maxLength)
        properties[dp][RDFS.comment] = g.value(dp, RDFS.comment)
        properties[dp][RDFS.label] = g.value(dp, RDFS.label)

    for op, _, _ in g.triples((None, RDF.type, OWL.ObjectProperty)):
        op = cast(URIRef, op)
        properties[op][RDF.type] = g.value(op, RDF.type)

        op_domain = g.value(op, RDFS.domain)
        if isinstance(op_domain, URIRef):
            properties[op][RDFS.domain] = op_domain
        elif isinstance(op_domain, BNode):
            for _, _, union in g.triples((op_domain, OWL.unionOf, None)):
                properties[op][RDFS.domain] = list(g.items(union))

        properties[op][RDFS.range] = g.value(op, RDFS.range)
        properties[op][RDFS.comment] = g.value(op, RDFS.comment)
        properties[op][RDFS.label] = g.value(op, RDFS.label)

    enums: dict[URIRef, set[URIRef]] = defaultdict(set)
    for individual, _, _ in g.triples((None, RDF.type, OWL.NamedIndividual)):
        if not isinstance(individual, URIRef):
            continue
        types = set(g.objects(individual, RDF.type))
        types.discard(OWL.NamedIndividual)

        for t in types:
            enums[cast(URIRef, t)].add(individual)

    classes: set[URIRef] = set()
    parents: dict[URIRef, set[URIRef]] = defaultdict(set)
    for cls in g.subjects(RDF.type, OWL.Class):
        if isinstance(cls, BNode):
            continue

        cls = cast(URIRef, cls)
        if uri_to_module_name(cls) != module_name:
            continue

        classes.add(cls)

        for _, _, eq in g.triples((cls, OWL.equivalentClass, None)):
            one_of = g.value(eq, OWL.oneOf)
            if one_of is not None:
                enums[cls].update(cast(set[URIRef], set(g.items(one_of))))

        for _, _, sc in g.triples((cls, RDFS.subClassOf, None)):
            if isinstance(sc, URIRef):
                parents[cls].add(sc)

    header_lines = [
        "from __future__ import annotations",
        "",
        "from pydantic import AnyUrl, BaseModel, Field",
        "from pydantic.json_schema import SkipJsonSchema",
        "from typing import Any, List, Optional, Union, ClassVar",
        "from rdflib import URIRef",
        "from datetime import datetime, timedelta",
        "from enum import Enum",
        "from one_record_ontology.models.base_model import OneRecordBaseModel",
    ]
    import_lines: set[str] = set()
    enum_lines: list[str] = []
    class_lines: list[str] = []
    ordered_classes = topo_sort(classes, parents)
    for cls in ordered_classes:
        cls_name = split_uri(cls)[1]

        if cls in enums or cls in {
            URIRef("https://onerecord.iata.org/ns/code-lists/CurrencyCode")
        }:
            enum_lines.append("")
            enum_lines.append(f"class {cls_name}(str, Enum):")

            if not enums[cls]:
                logging.warning(f"Enum class {cls_name} has no members")
                enum_lines.append("    pass")
                continue

            for enum_value in enums[cls]:
                enum_name = split_uri(enum_value)[1]
                if not enum_name.isidentifier():
                    enum_name = f"_{enum_name}"
                if (label := g.value(enum_value, RDFS.label)) is not None:
                    label_str = str(cast(Literal, label).toPython()).strip()
                    enum_lines.append(f"    # label: {label_str}")
                if (comment := g.value(enum_value, RDFS.comment)) is not None:
                    comment_lines = str(cast(Literal, comment).toPython()).splitlines()
                    comment_str = " ".join(line.strip() for line in comment_lines)
                    enum_lines.append(f"    # comment: {comment_str}")
                enum_lines.append(f'    {enum_name} = URIRef("{enum_value}")\n')
            continue

        base_names: list[str] = []
        for p in parents.get(cls, []):
            if p in classes:
                base_class_name = split_uri(p)[1]
                base_names.append(base_class_name)

        bases = ", ".join(base_names) if base_names else "OneRecordBaseModel"
        class_lines.append("")
        class_lines.append(f"class {cls_name}({bases}):")

        cls_properties: dict[URIRef, dict] = {}
        for _, _, sc in g.triples((cls, RDFS.subClassOf, None)):
            if g.value(sc, RDF.type) != OWL.Restriction:
                continue

            on_property = cast(URIRef, g.value(sc, OWL.onProperty))

            if on_property not in cls_properties:
                cls_properties[on_property] = {**properties[on_property]}

            # Type constraints
            cls_properties[on_property][OWL.allValuesFrom] = cls_properties[
                on_property
            ].get(OWL.allValuesFrom) or g.value(sc, OWL.allValuesFrom)
            cls_properties[on_property][OWL.onDataRange] = cls_properties[
                on_property
            ].get(OWL.onDataRange) or g.value(sc, OWL.onDataRange)
            cls_properties[on_property][OWL.onDatatype] = cls_properties[
                on_property
            ].get(OWL.onDatatype) or g.value(sc, OWL.onDatatype)
            cls_properties[on_property][OWL.onClass] = cls_properties[on_property].get(
                OWL.onClass
            ) or g.value(sc, OWL.onClass)

            # Cardinality constraints
            cls_properties[on_property][OWL.cardinality] = cls_properties[
                on_property
            ].get(OWL.cardinality) or g.value(sc, OWL.cardinality)
            cls_properties[on_property][OWL.qualifiedCardinality] = cls_properties[
                on_property
            ].get(OWL.qualifiedCardinality) or g.value(sc, OWL.qualifiedCardinality)
            cls_properties[on_property][OWL.minCardinality] = cls_properties[
                on_property
            ].get(OWL.minCardinality) or g.value(sc, OWL.minCardinality)
            cls_properties[on_property][OWL.minQualifiedCardinality] = cls_properties[
                on_property
            ].get(OWL.minQualifiedCardinality) or g.value(
                sc, OWL.minQualifiedCardinality
            )
            cls_properties[on_property][OWL.maxCardinality] = cls_properties[
                on_property
            ].get(OWL.maxCardinality) or g.value(sc, OWL.maxCardinality)
            cls_properties[on_property][OWL.maxQualifiedCardinality] = cls_properties[
                on_property
            ].get(OWL.maxQualifiedCardinality) or g.value(
                sc, OWL.maxQualifiedCardinality
            )

        if not cls_properties:
            class_lines.append("    pass")
            continue

        type_uris = []
        for t in [cls, *parents[cls]]:
            type_uris.append(f'URIRef("{t}")')
        class_lines.append(f'    _type: ClassVar[URIRef] = URIRef("{cls}")')
        class_lines.append(
            f"    _types: ClassVar[List[URIRef]] = [{', '.join(type_uris)},]\n"
        )

        for prop, prop_attrs in cls_properties.items():
            prop_name = split_uri(prop)[1]
            prop_type = prop_attrs.get(RDF.type)
            prop_range = prop_attrs.get(RDFS.range)

            python_type: str
            predicates_for_type = [
                RDFS.range,
                OWL.onDatatype,
                OWL.allValuesFrom,
                OWL.onDataRange,
            ]
            for pred in predicates_for_type:
                if (value := prop_attrs.get(pred)) is not None:
                    if isinstance(value, URIRef):
                        if prop_type == OWL.DatatypeProperty:
                            python_type = XSD_TO_PYTHON[value].__name__
                            break
                        elif prop_type == OWL.ObjectProperty:
                            python_type = split_uri(value)[1]
                            if uri_to_module_name(value) != module_name:
                                import_lines.add(
                                    f"from one_record_ontology.models.generated.{uri_to_module_name(value)} import {python_type}"
                                )
                            break
            else:
                logging.warning(
                    f"Unknown type for property {prop_name} in class {cls_name}; defaulting to Any"
                )
                python_type = "Any"

            is_optional = True
            is_list = True
            if (
                (c := prop_attrs.get(OWL.cardinality)) is not None and c.toPython() == 1
            ) or (
                (c := prop_attrs.get(OWL.qualifiedCardinality)) is not None
                and c.toPython() == 1
            ):
                is_optional = False
                is_list = False
            elif (
                (min_c := prop_attrs.get(OWL.minCardinality)) is not None
                and min_c.toPython() == 1
            ) or (
                (min_c := prop_attrs.get(OWL.minQualifiedCardinality)) is not None
                and min_c.toPython() == 1
            ):
                is_optional = False
            if (
                (max_c := prop_attrs.get(OWL.maxCardinality)) is not None
                and max_c.toPython() == 1
            ) or (
                (max_c := prop_attrs.get(OWL.maxQualifiedCardinality)) is not None
                and max_c.toPython() == 1
            ):
                is_list = False

            field_info: dict[str, str] = {}
            if (min_length := prop_attrs.get(XSD.minLength)) is not None:
                field_info["min_length"] = min_length.toPython()
            if (max_length := prop_attrs.get(XSD.maxLength)) is not None:
                field_info["max_length"] = max_length.toPython()
            if (pattern := prop_attrs.get(XSD.pattern)) is not None:
                field_info["pattern"] = pattern.toPython()

            match (is_optional, is_list):
                case (False, False):
                    field_info["annotated_type"] = (
                        f"Union[{python_type}, SkipJsonSchema[None]]"
                    )
                    field_info["default"] = "None"
                case (False, True):
                    field_info["annotated_type"] = f"List[{python_type}]"
                    field_info["default_factory"] = "list"
                case (True, False):
                    field_info["annotated_type"] = (
                        f"Union[{python_type}, SkipJsonSchema[None]]"
                    )
                    field_info["default"] = "None"
                case (True, True):
                    field_info["annotated_type"] = f"List[{python_type}]"
                    field_info["default_factory"] = "list"

            annotated_type = field_info["annotated_type"]
            property_definition = f"    {prop_name}: {annotated_type}"
            field_params = []
            field_params.append(f'serialization_alias="{prop}"')
            if "default" in field_info:
                field_params.append(f"default={field_info['default']}")
            if "default_factory" in field_info:
                field_params.append(f"default_factory={field_info['default_factory']}")
            if "min_length" in field_info:
                field_params.append(f"min_length={field_info['min_length']}")
            if "max_length" in field_info:
                field_params.append(f"max_length={field_info['max_length']}")
            if "pattern" in field_info:
                field_params.append(f'pattern=r"{field_info["pattern"]}"')
            field_definition = f"Field({',\n'.join(field_params)},)"
            property_definition += f" = {field_definition}\n"

            if (label := prop_attrs.get(RDFS.label)) is not None:
                label_str = str(label.toPython()).strip()
                class_lines.append(f"    # label: {label_str}")
            if (comment := prop_attrs.get(RDFS.comment)) is not None:
                comment_lines = str(comment.toPython()).splitlines()
                comment_str = " ".join(line.strip() for line in comment_lines)
                class_lines.append(f"    # comment: {comment_str}")
            class_lines.append(property_definition)

    footer_lines = [
        "for _cls in list(locals().values()):",
        "    if isinstance(_cls, type) and issubclass(_cls, OneRecordBaseModel):",
        "        result = _cls.model_rebuild()",
        "        if result is False:",
        "            raise RuntimeError(f'Failed to rebuild model for class {_cls.__name__}')",
    ]

    file_lines = (
        docstring_lines
        + header_lines
        + list(import_lines)
        + enum_lines
        + class_lines
        + footer_lines
    )
    OUT_DIR.joinpath(f"{module_name}.py").write_text(
        "\n".join(file_lines), encoding="utf-8"
    )


subprocess.run(
    [
        "uvx",
        "ruff",
        "check",
        "--fix",
        "src/one_record_ontology/models/",
    ],
    check=True,
)
subprocess.run(
    [
        "uvx",
        "ruff",
        "format",
        "src/one_record_ontology/models/",
    ],
    check=True,
)
