from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

from pydantic import AnyUrl
from rdflib import OWL, RDF, RDFS, XSD, BNode, Graph, URIRef
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


g = Graph()
g.parse("https://onerecord.iata.org/ns/api/ontology.ttl")


properties = defaultdict(dict)

for dp, _, _ in g.triples((None, RDF.type, OWL.DatatypeProperty)):
    properties[dp][RDF.type] = g.value(dp, RDF.type)

    dp_domain = g.value(dp, RDFS.domain)
    if isinstance(dp_domain, URIRef):
        properties[dp][RDFS.domain] = dp_domain
    elif isinstance(dp_domain, BNode):
        for _, _, union in g.triples((dp_domain, OWL.unionOf, None)):
            properties[dp][RDFS.domain] = list(g.items(union))

    properties[dp][RDFS.range] = g.value(dp, RDFS.range)
    properties[dp][RDFS.comment] = g.value(dp, RDFS.comment)
    properties[dp][RDFS.label] = g.value(dp, RDFS.label)

for op, _, _ in g.triples((None, RDF.type, OWL.ObjectProperty)):
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


for cls in g.subjects(RDF.type, OWL.Class):
    if isinstance(cls, BNode):
        continue

    # if cls != URIRef("https://onerecord.iata.org/ns/api#ServerInformation"):
    #     continue

    ns, cls_name = split_uri(cls)
    ns_prefix = ns.rpartition("/")[-1].rstrip("#")
    Path(f"src/one_record_ontology/models/{ns_prefix}").mkdir(
        parents=True, exist_ok=True
    )
    Path(f"src/one_record_ontology/models/{ns_prefix}/__init__.py").touch()

    cls_properties = defaultdict(dict)

    is_enum = False
    for _, _, equivalent_class in g.triples((cls, OWL.equivalentClass, None)):
        one_of = g.value(equivalent_class, OWL.oneOf)
        if one_of is not None:
            is_enum = True
            enum_values = list(g.items(one_of))

            lines = []
            lines.append("from enum import Enum")
            lines.append("from rdflib import URIRef")
            lines.append(f"class {cls_name}(str, Enum):")
            for ev in enum_values:
                _, ev_name = split_uri(ev)
                label = g.value(ev, RDFS.label)
                if label is not None:
                    lines.append(f"    # label: {label}")
                lines.append(f'    {ev_name} = URIRef("{(ev)}")')
            Path(
                f"src/one_record_ontology/models/{ns_prefix}/{cls_name}.py"
            ).write_text("\n".join(lines))

    if is_enum:
        continue

    base_class_uris = []
    base_classes = []
    for _, _, super_class in g.triples((cls, RDFS.subClassOf, None)):
        if isinstance(super_class, URIRef):
            _, super_class_name = split_uri(super_class)
            base_class_uris.append(super_class)
            base_classes.append(super_class_name)

        if g.value(super_class, RDF.type) != OWL.Restriction:
            continue

        on_prop = g.value(super_class, OWL.onProperty)
        cls_properties[on_prop] = {**properties[on_prop]}

        # Value type constraints
        cls_properties[on_prop][OWL.allValuesFrom] = cls_properties[on_prop].get(
            OWL.allValuesFrom
        ) or g.value(super_class, OWL.allValuesFrom)
        cls_properties[on_prop][OWL.onDataRange] = cls_properties[on_prop].get(
            OWL.onDataRange
        ) or g.value(super_class, OWL.onDataRange)
        cls_properties[on_prop][OWL.onClass] = cls_properties[on_prop].get(
            OWL.onClass
        ) or g.value(super_class, OWL.onClass)

        # Cardinality constraints
        cls_properties[on_prop][OWL.qualifiedCardinality] = cls_properties[on_prop].get(
            OWL.qualifiedCardinality
        ) or g.value(super_class, OWL.qualifiedCardinality)
        cls_properties[on_prop][OWL.minQualifiedCardinality] = cls_properties[
            on_prop
        ].get(OWL.minQualifiedCardinality) or g.value(
            super_class, OWL.minQualifiedCardinality
        )
        cls_properties[on_prop][OWL.maxQualifiedCardinality] = cls_properties[
            on_prop
        ].get(OWL.maxQualifiedCardinality) or g.value(
            super_class, OWL.maxQualifiedCardinality
        )

    lines = [
        "from pydantic import AnyUrl, BaseModel, Field",
        "from typing import List, Optional",
        "from rdflib import URIRef",
    ]

    if base_classes:
        for base_class_uri in base_class_uris:
            ns, base_class_name = split_uri(base_class_uri)
            ns_prefix = ns.rpartition("/")[-1].rstrip("#")
            lines.append(
                f"from one_record_ontology.models.{ns_prefix}.{base_class_name} import {base_class_name}"
            )
        lines.append(f"class {cls_name}({', '.join(base_classes)}):")
    else:
        lines.append(f"class {cls_name}(BaseModel):")

    if not cls_properties:
        lines.append("    ...")

    for prop, attrs in cls_properties.items():
        _, prop_name = split_uri(prop)

        # print(prop_name)
        # print(json.dumps(attrs, indent=4))

        prop_type = attrs.get(RDF.type)
        prop_range = attrs.get(RDFS.range)

        if prop_type == OWL.DatatypeProperty:
            python_type = XSD_TO_PYTHON[prop_range].__name__
        elif prop_type == OWL.ObjectProperty:
            if prop_range is None:
                python_type = "Any"
            else:
                prop_ns, python_type = split_uri(prop_range)

            prop_ns_prefix = prop_ns.rpartition("/")[-1].rstrip("#")
            lines.insert(
                0,
                f"from one_record_ontology.models.{prop_ns_prefix}.{python_type} import {python_type}",
            )

        is_optional = True
        is_list = True
        if (c := attrs.get(OWL.qualifiedCardinality)) is not None and c.toPython() == 1:
            is_optional = False
            is_list = False
        elif (
            min_c := attrs.get(OWL.minQualifiedCardinality)
        ) is not None and min_c.toPython() == 1:
            is_optional = False
        if (
            max_c := attrs.get(OWL.maxQualifiedCardinality)
        ) is not None and max_c.toPython() == 1:
            is_list = False

        match (is_optional, is_list):
            case (False, False):
                python_type = f'{python_type} = Field(serialization_alias="{prop}")'
            case (False, True):
                python_type = (
                    f'List[{python_type}] = Field(serialization_alias="{prop}")'
                )
            case (True, False):
                python_type = f'Optional[{python_type}] = Field(default=None, serialization_alias="{prop}")'
            case (True, True):
                python_type = f'List[{python_type}] = Field(default_factory=list, serialization_alias="{prop}")'

        if (label := attrs.get(RDFS.label)) is not None:
            lines.append(f"    # label: {label}")
        if (comment := attrs.get(RDFS.comment)) is not None:
            lines.append(f"    # comment: {comment}")
        lines.append(f"    # iri: {prop}")

        lines.append(f"    {prop_name}: {python_type}")

    Path(f"src/one_record_ontology/models/{ns_prefix}/{cls_name}.py").write_text(
        "\n".join(lines)
    )


### CARGO ONTOLOGY ###


g = Graph()
g.parse("https://onerecord.iata.org/ns/cargo/ontology.ttl")


properties = defaultdict(dict)

for dp, _, _ in g.triples((None, RDF.type, OWL.DatatypeProperty)):
    properties[dp][RDF.type] = g.value(dp, RDF.type)

    dp_domain = g.value(dp, RDFS.domain)
    if isinstance(dp_domain, URIRef):
        properties[dp][RDFS.domain] = dp_domain
    elif isinstance(dp_domain, BNode):
        for _, _, union in g.triples((dp_domain, OWL.unionOf, None)):
            properties[dp][RDFS.domain] = list(g.items(union))

    properties[dp][RDFS.range] = g.value(dp, RDFS.range)
    properties[dp][RDFS.comment] = g.value(dp, RDFS.comment)
    properties[dp][RDFS.label] = g.value(dp, RDFS.label)

for op, _, _ in g.triples((None, RDF.type, OWL.ObjectProperty)):
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


for cls in g.subjects(RDF.type, OWL.Class):
    if isinstance(cls, BNode):
        continue

    if cls != URIRef("https://onerecord.iata.org/ns/cargo#Waybill"):
        continue

    ns, cls_name = split_uri(cls)
    ns_prefix = ns.rpartition("/")[-1].rstrip("#")
    Path(f"src/one_record_ontology/models/{ns_prefix}").mkdir(
        parents=True, exist_ok=True
    )
    Path(f"src/one_record_ontology/models/{ns_prefix}/__init__.py").touch()

    cls_properties = defaultdict(dict)

    is_enum = False
    for _, _, equivalent_class in g.triples((cls, OWL.equivalentClass, None)):
        one_of = g.value(equivalent_class, OWL.oneOf)
        if one_of is not None:
            is_enum = True
            enum_values = list(g.items(one_of))

            lines = []
            lines.append("from enum import Enum")
            lines.append("from rdflib import URIRef")
            lines.append(f"class {cls_name}(str, Enum):")
            for ev in enum_values:
                _, ev_name = split_uri(ev)
                label = g.value(ev, RDFS.label)
                if label is not None:
                    lines.append(f"    # label: {label}")
                lines.append(f'    {ev_name} = URIRef("{(ev)}")')
            Path(
                f"src/one_record_ontology/models/{ns_prefix}/{cls_name}.py"
            ).write_text("\n".join(lines))

    if is_enum:
        continue

    base_class_uris = []
    base_classes = []
    for _, _, super_class in g.triples((cls, RDFS.subClassOf, None)):
        if isinstance(super_class, URIRef):
            _, super_class_name = split_uri(super_class)
            base_class_uris.append(super_class)
            base_classes.append(super_class_name)

        if g.value(super_class, RDF.type) != OWL.Restriction:
            continue

        on_prop = g.value(super_class, OWL.onProperty)
        cls_properties[on_prop] = {**properties[on_prop]}

        # Value type constraints
        cls_properties[on_prop][OWL.allValuesFrom] = cls_properties[on_prop].get(
            OWL.allValuesFrom
        ) or g.value(super_class, OWL.allValuesFrom)
        cls_properties[on_prop][OWL.onDataRange] = cls_properties[on_prop].get(
            OWL.onDataRange
        ) or g.value(super_class, OWL.onDataRange)
        cls_properties[on_prop][OWL.onClass] = cls_properties[on_prop].get(
            OWL.onClass
        ) or g.value(super_class, OWL.onClass)

        # Cardinality constraints
        cls_properties[on_prop][OWL.cardinality] = cls_properties[on_prop].get(
            OWL.cardinality
        ) or g.value(super_class, OWL.cardinality)
        cls_properties[on_prop][OWL.qualifiedCardinality] = cls_properties[on_prop].get(
            OWL.qualifiedCardinality
        ) or g.value(super_class, OWL.qualifiedCardinality)
        cls_properties[on_prop][OWL.minCardinality] = cls_properties[on_prop].get(
            OWL.minCardinality
        ) or g.value(super_class, OWL.minCardinality)
        cls_properties[on_prop][OWL.minQualifiedCardinality] = cls_properties[
            on_prop
        ].get(OWL.minQualifiedCardinality) or g.value(
            super_class, OWL.minQualifiedCardinality
        )
        cls_properties[on_prop][OWL.maxCardinality] = cls_properties[on_prop].get(
            OWL.maxCardinality
        ) or g.value(super_class, OWL.maxCardinality)
        cls_properties[on_prop][OWL.maxQualifiedCardinality] = cls_properties[
            on_prop
        ].get(OWL.maxQualifiedCardinality) or g.value(
            super_class, OWL.maxQualifiedCardinality
        )

    lines = [
        "from pydantic import AnyUrl, BaseModel, Field",
        "from typing import List, Optional",
        "from rdflib import URIRef",
    ]

    if base_classes:
        for base_class_uri in base_class_uris:
            ns, base_class_name = split_uri(base_class_uri)
            ns_prefix = ns.rpartition("/")[-1].rstrip("#")
            lines.append(
                f"from one_record_ontology.models.{ns_prefix}.{base_class_name} import {base_class_name}"
            )
        lines.append(f"class {cls_name}({', '.join(base_classes)}):")
    else:
        lines.append(f"class {cls_name}(BaseModel):")

    if not cls_properties:
        lines.append("    ...")

    for prop, attrs in cls_properties.items():
        _, prop_name = split_uri(prop)

        # print(prop_name)
        # print(json.dumps(attrs, indent=4))

        prop_type = attrs.get(RDF.type)
        prop_range = attrs.get(RDFS.range)

        if prop_type == OWL.DatatypeProperty:
            if isinstance(prop_range, URIRef):
                python_type = XSD_TO_PYTHON[prop_range].__name__
            elif isinstance(prop_range, BNode):
                on_data_type = g.value(prop_range, OWL.onDatatype)
                python_type = XSD_TO_PYTHON[on_data_type].__name__
        elif prop_type == OWL.ObjectProperty:
            prop_ns, python_type = split_uri(prop_range)

            prop_ns_prefix = prop_ns.rpartition("/")[-1].rstrip("#")
            if "code-lists" in prop_ns:
                print(prop_ns)
            lines.insert(
                0,
                f"from one_record_ontology.models.{prop_ns_prefix}.{python_type} import {python_type}",
            )

        is_optional = True
        is_list = True
        if ((c := attrs.get(OWL.cardinality)) is not None and c.toPython() == 1) or (
            (c := attrs.get(OWL.qualifiedCardinality)) is not None and c.toPython() == 1
        ):
            is_optional = False
            is_list = False
        elif (
            (min_c := attrs.get(OWL.minCardinality)) is not None
            and min_c.toPython() == 1
        ) or (
            (min_c := attrs.get(OWL.minQualifiedCardinality)) is not None
            and min_c.toPython() == 1
        ):
            is_optional = False
        if (
            (max_c := attrs.get(OWL.maxCardinality)) is not None
            and max_c.toPython() == 1
        ) or (
            (max_c := attrs.get(OWL.maxQualifiedCardinality)) is not None
            and max_c.toPython() == 1
        ):
            is_list = False

        match (is_optional, is_list):
            case (False, False):
                python_type = f'{python_type} = Field(serialization_alias="{prop}")'
            case (False, True):
                python_type = (
                    f'List[{python_type}] = Field(serialization_alias="{prop}")'
                )
            case (True, False):
                python_type = f'Optional[{python_type}] = Field(default=None, serialization_alias="{prop}")'
            case (True, True):
                python_type = f'List[{python_type}] = Field(default_factory=list, serialization_alias="{prop}")'

        if (label := attrs.get(RDFS.label)) is not None:
            lines.append(f"    # label: {label}")
        if (comment := attrs.get(RDFS.comment)) is not None:
            lines.append(f"    # comment: {comment}")
        lines.append(f"    # iri: {prop}")

        lines.append(f"    {prop_name}: {python_type}")

    Path(f"src/one_record_ontology/models/{ns_prefix}/{cls_name}.py").write_text(
        "\n".join(lines)
    )
