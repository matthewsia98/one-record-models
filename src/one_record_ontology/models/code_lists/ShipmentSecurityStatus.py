from enum import Enum

from rdflib import URIRef


class ShipmentSecurityStatus(str, Enum):
    """
    label: ShipmentSecurityStatus
    comment: Restricted code list indicating whether a shipment is secured or not secured
    """

    # label: NCR
    # comment: Screened
    NCR = URIRef("https://onerecord.iata.org/ns/code-lists/ShipmentSecurityStatus#NCR")
    # label: SCR
    # comment: Not Screened
    SCR = URIRef("https://onerecord.iata.org/ns/code-lists/ShipmentSecurityStatus#SCR")
