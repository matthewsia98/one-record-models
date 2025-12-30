from enum import Enum

from rdflib import URIRef


class BookingStatus(str, Enum):
    """
    label: BookingStatus
    comment: Restricted code list containing the possible statuses of a booking
    """

    # label: CONFIRMED
    # comment: Used when a booking is confirmed
    CONFIRMED = URIRef("https://onerecord.iata.org/ns/cargo#CONFIRMED")
    # label: DELETED
    # comment: Used when a booking is deleted
    DELETED = URIRef("https://onerecord.iata.org/ns/cargo#DELETED")
    # label: QUEUED
    # comment: Used when a booking or booking option is queued or pending
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")
    # label: REJECTED
    # comment: Used when a booking is rejected
    REJECTED = URIRef("https://onerecord.iata.org/ns/cargo#REJECTED")
