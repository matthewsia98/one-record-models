from enum import Enum

from rdflib import URIRef


class EventTimeType(str, Enum):
    """
    label: EventTimeType
    comment: Restricted code list for acceptable event times
    """

    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: ESTIMATED
    # comment: Used when a time is estimated
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")
    # label: EXPECTED
    # comment: Used when a time is expected
    EXPECTED = URIRef("https://onerecord.iata.org/ns/cargo#EXPECTED")
    # label: PLANNED
    # comment: Used when a time is planned
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")
    # label: REQUESTED
    # comment: Used when a time is requested
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")
