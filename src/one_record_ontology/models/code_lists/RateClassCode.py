from enum import Enum

from rdflib import URIRef


class RateClassCode(str, Enum):
    """
    label: RateClassCode
    comment: Restricted code list corresponding to cXML code list 1.4 Rate Class Codes
    """

    # label: B
    # comment: Basic Charge
    B = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#B")
    # label: C
    # comment: Specific Commodity Rate
    C = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#C")
    # label: E
    # comment: Unit Load Device Additional Rate
    E = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#E")
    # label: K
    # comment: Rate per Kilogram
    K = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#K")
    # label: M
    # comment: Minimum Charge
    M = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#M")
    # label: N
    # comment: Normal Rate
    N = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#N")
    # label: P
    # comment: International Priority Service Rate
    P = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#P")
    # label: Q
    # comment: Quantity Rate
    Q = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#Q")
    # label: R
    # comment: Class Rate Reduction
    R = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#R")
    # label: S
    # comment: Class Rate Surcharge
    S = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#S")
    # label: U
    # comment: Unit Load Device Basic Charge or Rate
    U = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#U")
    # label: W
    # comment: Weight Increase
    W = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#W")
    # label: X
    # comment: Unit Load Device Additional Information
    X = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#X")
    # label: Y
    # comment: Unit Load Device Discount
    Y = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#Y")
