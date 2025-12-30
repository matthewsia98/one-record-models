from enum import Enum

from rdflib import URIRef


class StatusCode(str, Enum):
    """
    label: StatusCode
    comment: Restricted code list corresponding to cXML code list 1.18 Status Codes, including DIS discrepancy codes
    """

    # label: ARR
    # comment: The consignment has arrived on a scheduled flight at this location
    ARR = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#ARR")
    # label: AWD
    # comment: The arrival documentation has been physically delivered to the consignee or the consignee’s agent on this date at this location
    AWD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#AWD")
    # label: AWR
    # comment: The arrival documentation has been physically received from a scheduled flight at this location
    AWR = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#AWR")
    # label: BKD
    # comment: The consignment has been booked for transport between these locations on this scheduled date and this flight
    BKD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#BKD")
    # label: CCD
    # comment: The consignment has been cleared by the Customs authorities on this date at this location
    CCD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#CCD")
    # label: CRC
    # comment: The consignment has been reported to the Customs authorities on this date at this location
    CRC = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#CRC")
    # label: DDL
    # comment: The consignment has been physically delivered to the consignee’s door on this date at this location
    DDL = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DDL")
    # label: DEP
    # comment: The consignment has physically departed this location on this scheduled date and flight for transport to the arrival location
    DEP = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DEP")
    # label: DIS_DFLD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Definitely Loaded
    DIS_DFLD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_DFLD")
    # label: DIS_FDAV
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Mail Document
    DIS_FDAV = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDAV")
    # label: DIS_FDAW
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Air Waybill
    DIS_FDAW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDAW")
    # label: DIS_FDCA
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Cargo
    DIS_FDCA = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDCA")
    # label: DIS_FDMB
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Mailbag
    DIS_FDMB = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDMB")
    # label: DIS_MSAV
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Mail Document
    DIS_MSAV = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSAV")
    # label: DIS_MSAW
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Air Waybill
    DIS_MSAW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSAW")
    # label: DIS_MSCA
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Cargo
    DIS_MSCA = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSCA")
    # label: DIS_MSMB
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Mailbag
    DIS_MSMB = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSMB")
    # label: DIS_OFLD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Offloaded
    DIS_OFLD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_OFLD")
    # label: DIS_OVCD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Overcarried
    DIS_OVCD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_OVCD")
    # label: DIS_SSPD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Shortshipped
    DIS_SSPD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_SSPD")
    # label: DLV
    # comment: The consignment has been physically delivered to the consignee or the Consignee’s agent on this date at this location
    DLV = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DLV")
    # label: DOC
    # comment: Documents Received by Handling Party
    DOC = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DOC")
    # label: DPU
    # comment: The consignment has been physically picked up from the shipper’s door on this date at this location
    DPU = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DPU")
    # label: FIW
    # comment: Freight Into Warehouse Control
    FIW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#FIW")
    # label: FOH
    # comment: The consignment is on hand on this date at this location pending “ready for carriage” determination
    FOH = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#FOH")
    # label: FOW
    # comment: Freight Out of Warehouse Control
    FOW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#FOW")
    # label: MAN
    # comment: The consignment has been manifested for this flight on this scheduled date for transport between these locations
    MAN = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#MAN")
    # label: NFD
    # comment: The consignee or the consignee’s agent has been notified, on this date at this location, of the arrival of the consignment
    NFD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#NFD")
    # label: OCI
    # comment: Other Customs, Security and Regulatory Control Information
    OCI = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#OCI")
    # label: OSI
    # comment: Other Service Information
    OSI = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#OSI")
    # label: PRE
    # comment: The consignment has been prepared for loading on this flight for transport between these locations on this scheduled date
    PRE = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#PRE")
    # label: RCF
    # comment: The consignment has been physically received from a given flight or surface transport of the given airline
    RCF = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#RCF")
    # label: RCS
    # comment: The consignment has been physically received from the shipper or the shipper’s agent and is considered by the carrier as ready for carriage on this date at this location
    RCS = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#RCS")
    # label: RCT
    # comment: The consignment has been physically received from this carrier on this date at this location
    RCT = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#RCT")
    # label: TFD
    # comment: The consignment has been physically transferred to this carrier on this date at this location
    TFD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#TFD")
    # label: TGC
    # comment: The consignment has been transferred to Customs/Government control
    TGC = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#TGC")
    # label: TRM
    # comment: The consignment has been manifested and/or will be physically transferred to this carrier at this location
    TRM = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#TRM")
