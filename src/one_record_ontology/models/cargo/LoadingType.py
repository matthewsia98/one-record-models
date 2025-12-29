from enum import Enum
from rdflib import URIRef
class LoadingType(str, Enum):
    # label: LOADING
    LOADING = URIRef("https://onerecord.iata.org/ns/cargo#LOADING")
    # label: UNLOADING
    UNLOADING = URIRef("https://onerecord.iata.org/ns/cargo#UNLOADING")