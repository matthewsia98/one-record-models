from enum import Enum
from rdflib import URIRef
class ExecutionStatus(str, Enum):
    # label: ACTIVE
    ACTIVE = URIRef("https://onerecord.iata.org/ns/cargo#ACTIVE")
    # label: CANCELLED
    CANCELLED = URIRef("https://onerecord.iata.org/ns/cargo#CANCELLED")
    # label: COMPLETE
    COMPLETE = URIRef("https://onerecord.iata.org/ns/cargo#COMPLETE")
    # label: PENDING
    PENDING = URIRef("https://onerecord.iata.org/ns/cargo#PENDING")