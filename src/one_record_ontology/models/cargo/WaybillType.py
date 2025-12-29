from enum import Enum
from rdflib import URIRef
class WaybillType(str, Enum):
    # label: DIRECT
    DIRECT = URIRef("https://onerecord.iata.org/ns/cargo#DIRECT")
    # label: HOUSE
    HOUSE = URIRef("https://onerecord.iata.org/ns/cargo#HOUSE")
    # label: MASTER
    MASTER = URIRef("https://onerecord.iata.org/ns/cargo#MASTER")