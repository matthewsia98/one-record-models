from enum import Enum

from rdflib import URIRef


class ULDChargeCode(str, Enum):
    """
    label: ULDChargeCode
    comment: Restricted code list corresponding to cXML code list 1.44 ULD Charge Codes
    """

    # label: A
    # comment: Pivot Rate per kilogram
    A = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#A")
    # label: B
    # comment: First Minimum Charge — minimum weight
    B = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#B")
    # label: C
    # comment: First over pivot rate per kilogram
    C = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#C")
    # label: D
    # comment: Second Minimum Charge — minimum weight
    D = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#D")
    # label: E
    # comment: Second over pivot rate per kilogram
    E = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#E")
    # label: F
    # comment: Third Minimum Charge — minimum weight
    F = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#F")
    # label: G
    # comment: Third over pivot rate per kilogram
    G = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#G")
    # label: H
    # comment: Flat Charge — (without weight or with minimum weight)
    H = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#H")
    # label: I
    # comment: Flat Charge — maximum weight
    I = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#I")
