from enum import Enum

from rdflib import URIRef


class ChargeCode(str, Enum):
    """
    label: ChargeCode
    comment: Restricted code list corresponding to cXML code list 1.1 Charge Codes
    """

    # label: CA
    # comment: Partial Collect Credit — Partial Prepaid Cash
    CA = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CA")
    # label: CB
    # comment: Partial Collect Credit — Partial Prepaid Credit
    CB = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CB")
    # label: CC
    # comment: All Charges Collect
    CC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CC")
    # label: CE
    # comment: Partial Collect Credit Card — Partial Prepaid Cash
    CE = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CE")
    # label: CG
    # comment: All Charges Collect by GBL
    CG = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CG")
    # label: CH
    # comment: Partial Collect Credit Card — Partial Prepaid Credit
    CH = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CH")
    # label: CM
    # comment: Destination Collect by MCO
    CM = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CM")
    # label: CP
    # comment: Destination Collect Cash
    CP = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CP")
    # label: CX
    # comment: Destination Collect Credit
    CX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CX")
    # label: CZ
    # comment: All Charges Collect by Credit Card
    CZ = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CZ")
    # label: NC
    # comment: No Charge
    NC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NC")
    # label: NG
    # comment: No Weight Charge — Other Charges Prepaid by GBL
    NG = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NG")
    # label: NP
    # comment: No Weight Charge — Other Charges Prepaid Cash
    NP = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NP")
    # label: NT
    # comment: No Weight Charge — Other Charges Collect
    NT = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NT")
    # label: NX
    # comment: No Weight Charge — Other Charges Prepaid Credit
    NX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NX")
    # label: NZ
    # comment: No Weight Charge — Other Charges Prepaid by Credit Card
    NZ = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NZ")
    # label: PC
    # comment: Partial Prepaid Cash — Partial Collect Cash
    PC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PC")
    # label: PD
    # comment: Partial Prepaid Credit — Partial Collect Cash
    PD = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PD")
    # label: PE
    # comment: Partial Prepaid Credit Card — Partial Collect Cash
    PE = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PE")
    # label: PF
    # comment: Partial Prepaid Credit Card — Partial Collect Credit Card
    PF = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PF")
    # label: PG
    # comment: All Charges Prepaid by GBL
    PG = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PG")
    # label: PH
    # comment: Partial Prepaid Credit Card — Partial Collect Credit
    PH = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PH")
    # label: PP
    # comment: All Charges Prepaid Cash
    PP = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PP")
    # label: PX
    # comment: All Charges Prepaid Credit
    PX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PX")
    # label: PZ
    # comment: All Charges Prepaid by Credit Card
    PZ = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PZ")
