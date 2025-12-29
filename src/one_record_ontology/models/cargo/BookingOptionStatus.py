from enum import Enum
from rdflib import URIRef
class BookingOptionStatus(str, Enum):
    # label: BOOKABLE
    BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#BOOKABLE")
    # label: BOOKED
    BOOKED = URIRef("https://onerecord.iata.org/ns/cargo#BOOKED")
    # label: EXPIRED
    EXPIRED = URIRef("https://onerecord.iata.org/ns/cargo#EXPIRED")
    # label: NONBOOKABLE
    NONBOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NONBOOKABLE")
    # label: NOT_BOOKABLE
    NOT_BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NOT_BOOKABLE")
    # label: ON_REQUEST
    ON_REQUEST = URIRef("https://onerecord.iata.org/ns/cargo#ON_REQUEST")
    # label: QUEUED
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")