from enum import Enum
from rdflib import URIRef
class EventTimeType(str, Enum):
    # label: ACTUAL
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: ESTIMATED
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")
    # label: EXPECTED
    EXPECTED = URIRef("https://onerecord.iata.org/ns/cargo#EXPECTED")
    # label: PLANNED
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")
    # label: REQUESTED
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")