from enum import Enum
from rdflib import URIRef
class MovementTimeType(str, Enum):
    # label: ACTUAL
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: ESTIMATED
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")
    # label: SCHEDULED
    SCHEDULED = URIRef("https://onerecord.iata.org/ns/cargo#SCHEDULED")