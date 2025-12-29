from enum import Enum
from rdflib import URIRef
class CompositionType(str, Enum):
    # label: COMPOSITION
    COMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#COMPOSITION")
    # label: DECOMPOSITION
    DECOMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#DECOMPOSITION")