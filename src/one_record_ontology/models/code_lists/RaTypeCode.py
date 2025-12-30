from enum import Enum

from rdflib import URIRef


class RaTypeCode(str, Enum):
    """
    label: RaTypeCode
    comment: Restricted code list based on cXML code list 1.84 Category Colour
    """

    # label: III_YELLOW
    # comment: III-Yellow
    III_YELLOW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RaTypeCode#III_YELLOW"
    )
    # label: II_YELLOW
    # comment: II-Yellow
    II_YELLOW = URIRef("https://onerecord.iata.org/ns/code-lists/RaTypeCode#II_YELLOW")
    # label: I_WHITE
    # comment: I-Yellow
    I_WHITE = URIRef("https://onerecord.iata.org/ns/code-lists/RaTypeCode#I_WHITE")
