from enum import Enum

from rdflib import URIRef


class ULDLoadingIndicator(str, Enum):
    """
    label: ULDLoadingIndicator
    comment: Restricted code list corresponding to cXML code list 1.47 ULD Loading Indicators
    """

    # label: L
    # comment: ULD Height below 160 centimetres
    L = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#L")
    # label: M
    # comment: Main Deck Loading only
    M = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#M")
    # label: N
    # comment: Nose Door Loading only
    N = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#N")
    # label: R
    # comment: ULD Height above 244 centimetres
    R = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#R")
    # label: U
    # comment: ULD Height between 160 centimetres and 244 centimetres
    U = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#U")
