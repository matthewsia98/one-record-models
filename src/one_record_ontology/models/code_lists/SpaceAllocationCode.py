from enum import Enum

from rdflib import URIRef


class SpaceAllocationCode(str, Enum):
    """
    label: SpaceAllocationCode
    comment: Restricted code list corresponding to CIMP code list 1.7 Space Allocation Codes
    """

    # label: CA
    # comment: Action code - Selling Space Allocation Against Allotment
    CA = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#CA")
    # label: CN
    # comment: Advice Code - Cancellation Noted
    CN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#CN")
    # label: HK
    # comment: Status Code - Holding Confirmed
    HK = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#HK")
    # label: HL
    # comment: Status Code - Holding Wait List
    HL = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#HL")
    # label: HN
    # comment: Status Code - Have Requested Space Allocation
    HN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#HN")
    # label: KK
    # comment: Advice Code - Confirming
    KK = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#KK")
    # label: LL
    # comment: Advice Code - Wait List
    LL = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#LL")
    # label: NA
    # comment: Action code - Requesting Space Allocation, if Not Available Will Accept Alternative
    NA = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#NA")
    # label: NL
    # comment: Action Code - Requesting Space Allocation, for Wait List
    NL = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#NL")
    # label: NN
    # comment: Action Code - Requesting Space Allocation, Will Not Accept Alternative
    NN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#NN")
    # label: SS
    # comment: Action Code - Reporting Sale
    SS = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#SS")
    # label: UN
    # comment: Advice Code - Unable, Flight Does Not Operate
    UN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#UN")
    # label: UU
    # comment: Advice Code - Unable
    UU = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#UU")
    # label: XX
    # comment: Action Code - Cancel Any Previous Space Allocation
    XX = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#XX")
