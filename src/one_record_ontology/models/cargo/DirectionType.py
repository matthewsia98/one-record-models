from enum import Enum

from rdflib import URIRef


class DirectionType(str, Enum):
    """
    label: DirectionType
    comment: Restricted code list for the direction of a MovementTime
    """

    # label: INBOUND
    # comment: Indicates the described direction in a movement time as inbound
    INBOUND = URIRef("https://onerecord.iata.org/ns/cargo#INBOUND")
    # label: OUTBOUND
    # comment: Indicates the described direction in a movement time as outbound
    OUTBOUND = URIRef("https://onerecord.iata.org/ns/cargo#OUTBOUND")
    # label: UNPLANNED_STOP
    # comment: Indicates the that the movement time describes an unplanned stop
    UNPLANNED_STOP = URIRef("https://onerecord.iata.org/ns/cargo#UNPLANNED_STOP")
