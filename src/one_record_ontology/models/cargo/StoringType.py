from enum import Enum
from rdflib import URIRef
class StoringType(str, Enum):
    # label: STORE_IN
    STORE_IN = URIRef("https://onerecord.iata.org/ns/cargo#STORE_IN")
    # label: STORE_OUT
    STORE_OUT = URIRef("https://onerecord.iata.org/ns/cargo#STORE_OUT")