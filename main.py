from __future__ import annotations

from typing import Annotated, ClassVar, List, Optional, cast

from pydantic import AnyUrl, BaseModel, Field, PrivateAttr
from rdflib import RDF, BNode, Graph, Literal, URIRef
from rdflib.graph import _SubjectType


class Graphable(BaseModel):
    _types: ClassVar[List[URIRef]]
    id: AnyUrl | None = Field(default=None, serialization_alias="@id")
    _id: URIRef | None = PrivateAttr(default=None)

    def model_post_init(self, __context):
        if self.id is not None:
            self._id = URIRef(str(self.id))

    def subject(self) -> URIRef | BNode:
        return self._id if self._id is not None else BNode()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls is Graphable:
            return  # base class itself is allowed

        if not hasattr(cls, "_types") or not cls._types:
            raise TypeError(
                f"{cls.__name__} must define a non-empty class attribute `_types`"
            )

    @classmethod
    def from_graph(cls, g: Graph, subject: _SubjectType) -> Graphable:
        kwargs = {}

        for name, field in cls.model_fields.items():
            base_type = field.annotation
            metadata = field.metadata

            for meta in metadata:
                if isinstance(meta, DataProperty):
                    for _, _, o in g.triples((subject, meta.iri, None)):
                        if not isinstance(o, Literal):
                            raise ValueError(...)
                        kwargs[name] = o.toPython()
                if isinstance(meta, ObjectProperty):
                    if isinstance(base_type, type) and issubclass(base_type, Graphable):
                        for _, _, o in g.triples((subject, meta.iri, None)):
                            obj = base_type.from_graph(g, cast(URIRef | BNode, o))
                            kwargs[name] = obj

        id_value = None
        if isinstance(subject, URIRef):
            id_value = AnyUrl(subject)

        return cls(id=id_value, **kwargs)

    def to_graph(self) -> Graph:
        g = Graph()
        subject = self.subject()

        for t in self._types:
            g.add((subject, RDF.type, t))

        for name, field in self.__class__.model_fields.items():
            base_type = field.annotation
            metadata = field.metadata

            for meta in metadata:
                if isinstance(meta, DataProperty):
                    value = getattr(self, name)
                    if value is None:
                        continue
                    g.add((subject, meta.iri, Literal(value)))
                if isinstance(meta, ObjectProperty):
                    obj = getattr(self, name)
                    if obj is None:
                        continue
                    obj_graph = obj.to_graph()
                    g += obj_graph
                    g.add((subject, meta.iri, list(obj_graph.subjects())[0]))

        return g

    def serialize(self, frame, context) -> str:
        g = self.to_graph()
        serialized = g.serialize(format="json-ld")
        return serialized


class ServerInformation(Graphable):
    _types = [
        URIRef("https://onerecord.iata.org/ns/api#ServerInformation"),
    ]

    hasServerEndpoint: Annotated[
        AnyUrl,
        DataProperty(
            iri=URIRef("https://onerecord.iata.org/ns/api#hasServerEndpoint"),
        ),
    ]
    hasDataHolder: Annotated[
        Organization,
        ObjectProperty(
            iri=URIRef("https://onerecord.iata.org/ns/api#hasDataHolder"),
        ),
    ]


class Organization(Graphable):
    _types = [
        URIRef("https://onerecord.iata.org/ns/cargo#Organization"),
    ]

    name: Annotated[
        Optional[str],
        DataProperty(
            iri=URIRef("https://onerecord.iata.org/ns/cargo#name"),
        ),
    ] = None


class DataProperty:
    def __init__(self, iri: URIRef):
        self.iri = iri


class ObjectProperty:
    def __init__(self, iri: URIRef):
        self.iri = iri


server_info = ServerInformation(
    hasServerEndpoint=AnyUrl("https://api.example.com/endpoint"),
    hasDataHolder=Organization(
        id=AnyUrl("https://example.com/organizations/1"),
        name="Example Organization",
    ),
)


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


assert server_info == server_info_from_graph, (
    "Deserialized object does not match the original"
)


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
