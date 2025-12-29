from enum import Enum
from rdflib import URIRef
class ActionTimeType(str, Enum):
    # label: ACTUAL
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: PLANNED
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")
    # label: REQUESTED
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")