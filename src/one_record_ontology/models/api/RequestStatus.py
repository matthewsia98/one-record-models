from enum import Enum
from rdflib import URIRef
class RequestStatus(str, Enum):
    # label: REQUEST_ACCEPTED
    REQUEST_ACCEPTED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_ACCEPTED")
    # label: REQUEST_FAILED
    REQUEST_FAILED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_FAILED")
    # label: REQUEST_PENDING
    REQUEST_PENDING = URIRef("https://onerecord.iata.org/ns/api#REQUEST_PENDING")
    # label: REQUEST_REJECTED
    REQUEST_REJECTED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_REJECTED")
    # label: REQUEST_REVOKED
    REQUEST_REVOKED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_REVOKED")