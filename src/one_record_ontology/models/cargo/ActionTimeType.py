from enum import Enum

from rdflib import URIRef


class ActionTimeType(str, Enum):
    """
    label: ActionTimeType
    comment: Restricted code list for acceptable action times
    """

    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: PLANNED
    # comment: Used when a time is planned
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")
    # label: REQUESTED
    # comment: Used when a time is requested
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")
