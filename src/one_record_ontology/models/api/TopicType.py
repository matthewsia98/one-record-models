from enum import Enum
from rdflib import URIRef
class TopicType(str, Enum):
    # label: LOGISTICS_OBJECT_IDENTIFIER
    LOGISTICS_OBJECT_IDENTIFIER = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_IDENTIFIER")
    # label: LOGISTICS_OBJECT_TYPE
    LOGISTICS_OBJECT_TYPE = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_TYPE")