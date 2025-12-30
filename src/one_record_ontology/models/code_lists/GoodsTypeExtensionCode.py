from enum import Enum

from rdflib import URIRef


class GoodsTypeExtensionCode(str, Enum):
    """
    label: GoodsTypeExtensionCode
    comment: Restricted code list referring to the CITES source codes
    """

    # label: A
    # comment: Artificially propagated plant
    A = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#A")
    # label: C
    # comment: Bred in captivity
    C = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#C")
    # label: D
    # comment: Captive-bred animal or artificially propagated plant
    D = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#D")
    # label: F
    # comment: Born in captivity
    F = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#F")
    # label: I
    # comment: Confiscated or seized
    I = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#I")
    # label: O
    # comment: Pre-Convention
    O = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#O")
    # label: R
    # comment: Ranched animal
    R = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#R")
    # label: U
    # comment: Unknown
    U = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#U")
    # label: W
    # comment: Wild
    W = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#W")
    # label: X
    # comment: Marine environment
    X = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#X")
