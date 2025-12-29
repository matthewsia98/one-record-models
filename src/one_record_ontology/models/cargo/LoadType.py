from enum import Enum
from rdflib import URIRef
class LoadType(str, Enum):
    # label: BULK
    BULK = URIRef("https://onerecord.iata.org/ns/cargo#BULK")
    # label: LOOSE
    LOOSE = URIRef("https://onerecord.iata.org/ns/cargo#LOOSE")
    # label: PALLET
    PALLET = URIRef("https://onerecord.iata.org/ns/cargo#PALLET")
    # label: UNIT_LOAD_DEVICE
    UNIT_LOAD_DEVICE = URIRef("https://onerecord.iata.org/ns/cargo#UNIT_LOAD_DEVICE")