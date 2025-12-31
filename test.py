from rdflib import Graph

from one_record_ontology.models.generated.api import ServerInformation

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
g.parse(data=data, format="json-ld")


obj = ServerInformation.from_graph(g)
print(repr(obj))

print(
    obj.to_graph().serialize(
        format="json-ld",
        context={
            "api": "https://onerecord.iata.org/ns/api#",
            "cargo": "https://onerecord.iata.org/ns/cargo#",
        },
    )
)
