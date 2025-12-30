from enum import Enum

from rdflib import URIRef


class EntitlementCode(str, Enum):
    """
    label: EntitlementCode
    comment: Restricted code list corresponding to cXML code list 1.3 Entitlement Codes
    """

    # label: A
    # comment: Other Charges due Agent
    A = URIRef("https://onerecord.iata.org/ns/code-lists/EntitlementCode#A")
    # label: C
    # comment: Other Charges due Carrier
    C = URIRef("https://onerecord.iata.org/ns/code-lists/EntitlementCode#C")
