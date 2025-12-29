from enum import Enum
from rdflib import URIRef
class DirectionType(str, Enum):
    # label: INBOUND
    INBOUND = URIRef("https://onerecord.iata.org/ns/cargo#INBOUND")
    # label: OUTBOUND
    OUTBOUND = URIRef("https://onerecord.iata.org/ns/cargo#OUTBOUND")
    # label: UNPLANNED_STOP
    UNPLANNED_STOP = URIRef("https://onerecord.iata.org/ns/cargo#UNPLANNED_STOP")