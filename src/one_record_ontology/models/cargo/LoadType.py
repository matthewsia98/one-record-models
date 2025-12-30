from enum import Enum

from rdflib import URIRef


class LoadType(str, Enum):
    """
    label: LoadType
    comment: Restricted code list for the Load Type of a piece or shipment
    """

    # label: BULK
    # comment: Indicates the load type as bulk
    BULK = URIRef("https://onerecord.iata.org/ns/cargo#BULK")
    # label: LOOSE
    # comment: Indicates the load type as loose
    LOOSE = URIRef("https://onerecord.iata.org/ns/cargo#LOOSE")
    # label: PALLET
    # comment: Indicates the load type as pallet
    PALLET = URIRef("https://onerecord.iata.org/ns/cargo#PALLET")
    # label: UNIT_LOAD_DEVICE
    # comment: Indicates the load type as uld
    UNIT_LOAD_DEVICE = URIRef("https://onerecord.iata.org/ns/cargo#UNIT_LOAD_DEVICE")
