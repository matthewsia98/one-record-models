from enum import Enum

from rdflib import URIRef


class GoodsTypeCode(str, Enum):
    """
    label: GoodsTypeCode
    comment: Restricted code list referring to the CITES appendices
    """

    # label: I
    # comment: Species included in Appendix I of CITES
    I = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeCode#I")
    # label: II
    # comment: Species included in Appendix II of CITES
    II = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeCode#II")
    # label: III
    # comment: Species included in Appendix III of CITES
    III = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeCode#III")
