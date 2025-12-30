from enum import Enum

from rdflib import URIRef


class ExecutionStatus(str, Enum):
    """
    label: ExecutionStatus
    comment: Restricted code list for the execution status of activities
    """

    # label: ACTIVE
    # comment: Used when a LogisticsActivity is active
    ACTIVE = URIRef("https://onerecord.iata.org/ns/cargo#ACTIVE")
    # label: CANCELLED
    # comment: Used when a LogisticsActivity is cancelled
    CANCELLED = URIRef("https://onerecord.iata.org/ns/cargo#CANCELLED")
    # label: COMPLETE
    # comment: Used when a LogisticsActivity is complete
    COMPLETE = URIRef("https://onerecord.iata.org/ns/cargo#COMPLETE")
    # label: PENDING
    # comment: Used when a LogisticsActivity is pending
    PENDING = URIRef("https://onerecord.iata.org/ns/cargo#PENDING")
