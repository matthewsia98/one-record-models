from enum import Enum
from rdflib import URIRef
class ModeQualifier(str, Enum):
    # label: MAIN_CARRIAGE
    MAIN_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#MAIN_CARRIAGE")
    # label: ON_CARRIAGE
    ON_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#ON_CARRIAGE")
    # label: PRE_CARRIAGE
    PRE_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#PRE_CARRIAGE")