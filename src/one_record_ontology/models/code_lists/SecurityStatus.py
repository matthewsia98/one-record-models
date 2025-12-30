from enum import Enum

from rdflib import URIRef


class SecurityStatus(str, Enum):
    """
    label: SecurityStatus
    comment: Restricted code list corresponding to cXML code list 1.103 Security Statuses
    """

    # label: NSC
    # comment: Cargo Has Not Been Secured Yet for Passenger or All-Cargo Aircraft
    NSC = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#NSC")
    # label: SCO
    # comment: Cargo Secure for All-Cargo Aircraft Only
    SCO = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#SCO")
    # label: SHR
    # comment: Secure for Passenger, All-Cargo and All-Mail Aircraft in Accordance with High Risk Requirements
    SHR = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#SHR")
    # label: SPX
    # comment: Cargo Secure for Passenger and All-Cargo Aircraft
    SPX = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#SPX")
