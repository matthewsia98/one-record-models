from enum import Enum

from rdflib import URIRef


class ULDConditionCode(str, Enum):
    """
    label: ULDConditionCode
    comment: Restricted code list corresponding to cXML code list 1.21 ULD Condition Codes
    """

    # label: DAM
    # comment: Damaged But Still Serviceable
    DAM = URIRef("https://onerecord.iata.org/ns/code-lists/ULDConditionCode#DAM")
    # label: SER
    # comment: Serviceable
    SER = URIRef("https://onerecord.iata.org/ns/code-lists/ULDConditionCode#SER")
