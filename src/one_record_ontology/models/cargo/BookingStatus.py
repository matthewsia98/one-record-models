from enum import Enum
from rdflib import URIRef
class BookingStatus(str, Enum):
    # label: CONFIRMED
    CONFIRMED = URIRef("https://onerecord.iata.org/ns/cargo#CONFIRMED")
    # label: DELETED
    DELETED = URIRef("https://onerecord.iata.org/ns/cargo#DELETED")
    # label: QUEUED
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")
    # label: REJECTED
    REJECTED = URIRef("https://onerecord.iata.org/ns/cargo#REJECTED")