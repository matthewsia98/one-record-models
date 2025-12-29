from enum import Enum
from rdflib import URIRef
class PatchOperation(str, Enum):
    # label: ADD
    ADD = URIRef("https://onerecord.iata.org/ns/api#ADD")
    # label: DELETE
    DELETE = URIRef("https://onerecord.iata.org/ns/api#DELETE")