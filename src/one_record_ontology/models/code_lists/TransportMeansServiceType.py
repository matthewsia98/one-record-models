from enum import Enum

from rdflib import URIRef


class TransportMeansServiceType(str, Enum):
    """
    label: TransportMeansServiceType
    comment: Restricted code list of possible transport means in transport legs in carrier bookings
    """

    # label: FREIGHTER
    # comment: Transport leg performed by freighter aircraft
    FREIGHTER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#FREIGHTER"
    )
    # label: MIXED_CONFIGURATION_COMBI
    # comment: Transport leg performed by mixed configuration combi aircraft
    MIXED_CONFIGURATION_COMBI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#MIXED_CONFIGURATION_COMBI"
    )
    # label: PASSENGER
    # comment: Transport leg performed by passenger aircraft
    PASSENGER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#PASSENGER"
    )
    # label: TRUCK
    # comment: Transport leg performed by truck
    TRUCK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#TRUCK"
    )
