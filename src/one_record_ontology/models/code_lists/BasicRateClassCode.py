from enum import Enum

from rdflib import URIRef


class BasicRateClassCode(str, Enum):
    """
    label: BasicRateClassCode
    comment: Restricted sub-code list corresponding to elements of cXML code list 1.4 Rate Class Codes
    """

    # label: C
    # comment: Specific Commodity Rate
    C = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#C")
    # label: M
    # comment: Minimum Charge
    M = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#M")
    # label: N
    # comment: Normal Rate
    N = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#N")
    # label: Q
    # comment: Quantity Rate
    Q = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#Q")
    # label: U
    # comment: Unit Load Device Basic Charge or Rate
    U = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#U")
