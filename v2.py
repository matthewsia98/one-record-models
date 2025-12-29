from __future__ import annotations

import json
from devtools import debug
from pydantic import BaseModel, Field, AnyUrl, PrivateAttr
from typing import ClassVar, List, Optional, Any, cast

import pyld.jsonld
from rdflib import Graph, URIRef, BNode, Literal, RDF
from rdflib.graph import _SubjectType


# ---------------------------
# RDF Property definitions
# ---------------------------


class DataProperty:
    def __init__(self, iri: URIRef):
        self.iri = iri


class ObjectProperty:
    def __init__(self, iri: URIRef):
        self.iri = iri


# ---------------------------
# Base Graphable
# ---------------------------


class Graphable(BaseModel):
    _types: ClassVar[List[URIRef]]
    id: Optional[AnyUrl] = Field(default=None, serialization_alias="@id")
    _id: Optional[URIRef] = PrivateAttr(default=None)

    def model_post_init(self, __context):
        if self.id is not None:
            self._id = URIRef(str(self.id))

    def subject(self) -> URIRef | BNode:
        return self._id if self._id is not None else BNode()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls is Graphable:
            return
        if not hasattr(cls, "_types") or not cls._types:
            raise TypeError(
                f"{cls.__name__} must define a non-empty class attribute `_types`"
            )

    @classmethod
    def from_graph(cls, g: Graph, subject: _SubjectType) -> Graphable:
        kwargs: dict[str, Any] = {}
        for name, field in cls.model_fields.items():
            json_extra = field.json_schema_extra
            if callable(json_extra):
                json_extra = {}
            rdf_meta: Optional[DataProperty | ObjectProperty] = cast(
                Optional[DataProperty | ObjectProperty],
                json_extra.get("rdf") if isinstance(json_extra, dict) else None,
            )
            if rdf_meta is None:
                continue

            if isinstance(rdf_meta, DataProperty):
                for _, _, o in g.triples((subject, rdf_meta.iri, None)):
                    if not isinstance(o, Literal):
                        raise TypeError(
                            f"Expected Literal for {rdf_meta.iri}, got {type(o)}"
                        )
                    base_type = field.annotation
                    py_value = o.toPython()
                    if base_type in (str, int, float, bool):
                        value = base_type(py_value)
                    elif base_type is AnyUrl:
                        value = AnyUrl(py_value)
                    else:
                        value = py_value
                    kwargs[name] = value

            elif isinstance(rdf_meta, ObjectProperty):
                base_type = field.annotation
                if isinstance(base_type, type) and issubclass(base_type, Graphable):
                    for _, _, o in g.triples((subject, rdf_meta.iri, None)):
                        if not isinstance(o, (URIRef, BNode)):
                            raise TypeError(
                                f"Expected URIRef or BNode for {rdf_meta.iri}, got {type(o)}"
                            )
                        kwargs[name] = base_type.from_graph(g, o)

        id_value: Optional[AnyUrl] = None
        if isinstance(subject, URIRef):
            id_value = AnyUrl(str(subject))

        return cls(id=id_value, **kwargs)

    def to_graph(self) -> Graph:
        g = Graph()
        subject = self.subject()

        # Add rdf:type triples
        for t in self._types:
            g.add((subject, RDF.type, t))

        for name, field in self.__class__.model_fields.items():
            # json_schema_extra may be a dict or a callable
            json_extra = field.json_schema_extra
            if callable(json_extra):
                json_extra = {}
            rdf_meta: Optional[DataProperty | ObjectProperty] = cast(
                Optional[DataProperty | ObjectProperty],
                json_extra.get("rdf") if isinstance(json_extra, dict) else None,
            )
            if rdf_meta is None:
                continue

            value = getattr(self, name)
            if value is None:
                continue

            if isinstance(rdf_meta, DataProperty):
                g.add((subject, rdf_meta.iri, Literal(value)))
            elif isinstance(rdf_meta, ObjectProperty):
                # value is a Graphable
                obj_graph = value.to_graph()
                g += obj_graph
                g.add((subject, rdf_meta.iri, list(obj_graph.subjects())[0]))

        return g

    def serialize(self, frame, context) -> str:
        g = self.to_graph()
        serialized = g.serialize(format="json-ld")
        framed = pyld.jsonld.frame(json.loads(serialized), frame)
        compacted = pyld.jsonld.compact(framed, context)
        return json.dumps(compacted, indent=4)


# ---------------------------
# Models
# ---------------------------


class Organization(Graphable):
    _types = [URIRef("https://onerecord.iata.org/ns/cargo#Organization")]

    name: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "rdf": DataProperty(URIRef("https://onerecord.iata.org/ns/cargo#name"))
        },
    )


class ServerInformation(Graphable):
    _types = [URIRef("https://onerecord.iata.org/ns/api#ServerInformation")]

    hasServerEndpoint: AnyUrl = Field(
        json_schema_extra={
            "rdf": DataProperty(
                URIRef("https://onerecord.iata.org/ns/api#hasServerEndpoint")
            )
        }
    )
    hasDataHolder: Organization = Field(
        json_schema_extra={
            "rdf": ObjectProperty(
                URIRef("https://onerecord.iata.org/ns/api#hasDataHolder")
            )
        }
    )


# ---------------------------
# Example usage
# ---------------------------

server_info = ServerInformation(
    hasServerEndpoint=AnyUrl("https://api.example.com/endpoint"),
    hasDataHolder=Organization(
        id=AnyUrl("https://example.com/organizations/1"),
        name="Example Organization",
    ),
)
debug(server_info)


result = server_info.serialize(
    {
        "@type": "https://onerecord.iata.org/ns/api#ServerInformation",
    },
    {
        "@context": {
            "api": "https://onerecord.iata.org/ns/api#",
            "cargo": "https://onerecord.iata.org/ns/cargo#",
        }
    },
)
print(result)


data = """\
{
    "@context": {
        "api": "https://onerecord.iata.org/ns/api#",
        "cargo": "https://onerecord.iata.org/ns/cargo#"
    },
    "@type": "api:ServerInformation",
    "api:hasDataHolder": {
        "@id": "https://example.com/organizations/1",
        "@type": "cargo:Organization",
        "cargo:name": "Example Organization"
    },
    "api:hasServerEndpoint": "https://api.example.com/endpoint"
}
"""
g = Graph()
g.parse(data=result, format="json-ld")
subject = next(
    g.subjects(RDF.type, URIRef("https://onerecord.iata.org/ns/api#ServerInformation"))
)
server_info_from_graph = ServerInformation.from_graph(g, subject)
debug(server_info_from_graph)


assert (
    server_info == server_info_from_graph
), "Deserialized object does not match the original"


data = """\
{
    "@context": {
        "cargo": "https://onerecord.iata.org/ns/cargo#",
        "api": "https://onerecord.iata.org/ns/api#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "api:hasServerEndpoint": {
            "@type": "xsd:anyURI"
        },
        "api:hasSupportedOntology": {
            "@type": "xsd:anyURI"
        }
    },
    "@id": "https://1r.example.com/",
    "@type": "api:ServerInformation",
    "api:hasDataHolder": {
        "@type": "cargo:Company",
        "@id": "https://1r.example.com/logistics-objects/957e2622-9d31-493b-8b8f-3c805064dbda"
    },
    "api:hasServerEndpoint": "http://1r.example.com",
    "api:hasSupportedApiVersion": [
        "2.2.0"
    ],
    "api:hasSupportedContentType": [
        "application/ld+json"
    ],
    "api:hasSupportedLanguage": [
        "en-US"
    ],
    "api:hasSupportedOntology": [
        "https://onerecord.iata.org/ns/cargo/3.2.0",
        "https://onerecord.iata.org/ns/api/2.2.0"
    ]
}
"""
g = Graph()
g.parse(data=data, format="json-ld")
subject = next(
    g.subjects(RDF.type, URIRef("https://onerecord.iata.org/ns/api#ServerInformation"))
)
server_info_from_graph = ServerInformation.from_graph(g, subject)
debug(server_info_from_graph)
