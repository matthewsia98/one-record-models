from enum import Enum

from rdflib import URIRef


class ModeQualifier(str, Enum):
    """
    label: ModeQualifier
    comment: Open code list for transport modes
    """

    # label: MAIN_CARRIAGE
    # comment: Indicates the mode qualifier as main carriage
    MAIN_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#MAIN_CARRIAGE")
    # label: ON_CARRIAGE
    # comment: Indicates the mode qualifier as on carriage
    ON_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#ON_CARRIAGE")
    # label: PRE_CARRIAGE
    # comment: Indicates the mode qualifier as pre carriage
    PRE_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#PRE_CARRIAGE")
