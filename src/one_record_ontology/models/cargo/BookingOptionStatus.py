from enum import Enum

from rdflib import URIRef


class BookingOptionStatus(str, Enum):
    """
    label: BookingOptionStatus
    comment: Restricted code list containing the statuses of a booking option
    """

    # label: BOOKABLE
    # comment: Used when a booking option (or proposal) is bookable
    BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#BOOKABLE")
    # label: BOOKED
    # comment: Used when a booking option proposal is booked
    BOOKED = URIRef("https://onerecord.iata.org/ns/cargo#BOOKED")
    # label: EXPIRED
    # comment: Used when a booking option proposal is expired
    EXPIRED = URIRef("https://onerecord.iata.org/ns/cargo#EXPIRED")
    # label: NONBOOKABLE
    # comment: Used when a booking option is nonbookable
    NONBOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NONBOOKABLE")
    # label: NOT_BOOKABLE
    # comment: Used when a booking option proposal is not bookable
    NOT_BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NOT_BOOKABLE")
    # label: ON_REQUEST
    # comment: Used when a booking option proposal is on request
    ON_REQUEST = URIRef("https://onerecord.iata.org/ns/cargo#ON_REQUEST")
    # label: QUEUED
    # comment: Used when a booking or booking option is queued or pending
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")
