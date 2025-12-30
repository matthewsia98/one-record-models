from enum import Enum

from rdflib import URIRef


class ChargeIdentifier(str, Enum):
    """
    label: ChargeIdentifier
    comment: Restricted code list corresponding to cXML code list 1.33 Charge Identifiers
    """

    # label: CN
    # comment: CASS Net Amount
    CN = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#CN")
    # label: CO
    # comment: Commission
    CO = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#CO")
    # label: CT
    # comment: Charge Summary Total
    CT = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#CT")
    # label: IN
    # comment: Insurance
    IN = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#IN")
    # label: NI
    # comment: CASS Invoice Amount
    NI = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#NI")
    # label: OA
    # comment: Total Other Charges Due Agent
    OA = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#OA")
    # label: OC
    # comment: Total Other Charges Due Carrier
    OC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#OC")
    # label: SI
    # comment: Sales Incentive
    SI = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#SI")
    # label: TX
    # comment: Taxes
    TX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#TX")
    # label: VC
    # comment: Valuation Charge
    VC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#VC")
    # label: WT
    # comment: Total Weight Charge
    WT = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#WT")
