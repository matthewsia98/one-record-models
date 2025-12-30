from enum import Enum

from rdflib import URIRef


class MovementTimeType(str, Enum):
    """
    label: MovementTimeType
    comment: Restricted code list for MovementTime subtypes
    """

    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: ESTIMATED
    # comment: Used when a time is estimated
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")
    # label: SCHEDULED
    # comment: Used when a time is scheduled
    SCHEDULED = URIRef("https://onerecord.iata.org/ns/cargo#SCHEDULED")
