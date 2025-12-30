from enum import Enum

from rdflib import URIRef


class DemurrageCode(str, Enum):
    """
    label: DemurrageCode
    comment: Restricted code list based on RP 1654
    """

    # label: BCC
    # comment: BCC
    BCC = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#BCC")
    # label: HHH
    # comment: HHH
    HHH = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#HHH")
    # label: XXX
    # comment: XXX
    XXX = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#XXX")
    # label: ZZZ
    # comment: ZZZ
    ZZZ = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#ZZZ")
