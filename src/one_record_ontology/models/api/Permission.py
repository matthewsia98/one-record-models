from enum import Enum
from rdflib import URIRef
class Permission(str, Enum):
    # label: GET_LOGISTICS_EVENT
    GET_LOGISTICS_EVENT = URIRef("https://onerecord.iata.org/ns/api#GET_LOGISTICS_EVENT")
    # label: GET_LOGISTICS_OBJECT
    GET_LOGISTICS_OBJECT = URIRef("https://onerecord.iata.org/ns/api#GET_LOGISTICS_OBJECT")
    # label: PATCH_LOGISTICS_OBJECT
    PATCH_LOGISTICS_OBJECT = URIRef("https://onerecord.iata.org/ns/api#PATCH_LOGISTICS_OBJECT")
    # label: POST_LOGISTICS_EVENT
    POST_LOGISTICS_EVENT = URIRef("https://onerecord.iata.org/ns/api#POST_LOGISTICS_EVENT")