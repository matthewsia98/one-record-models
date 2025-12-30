from enum import Enum

from rdflib import URIRef


class WaybillType(str, Enum):
    """
    label: WaybillType
    comment: Restricted code list for Waybill types
    """

    # label: DIRECT
    # comment: Indicates a Direct waybill
    DIRECT = URIRef("https://onerecord.iata.org/ns/cargo#DIRECT")
    # label: HOUSE
    # comment: Indicates a House Waybill
    HOUSE = URIRef("https://onerecord.iata.org/ns/cargo#HOUSE")
    # label: MASTER
    # comment: Indicates a Master Waybill
    MASTER = URIRef("https://onerecord.iata.org/ns/cargo#MASTER")
