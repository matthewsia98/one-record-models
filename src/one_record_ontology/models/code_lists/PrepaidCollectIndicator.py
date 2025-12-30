from enum import Enum

from rdflib import URIRef


class PrepaidCollectIndicator(str, Enum):
    """
    label: PrepaidCollectIndicator
    comment: Restricted code list corresponding to cXML code list 1.5 Prepaid/Collect Indicators
    """

    # label: C
    # comment: Collect Indicator
    C = URIRef("https://onerecord.iata.org/ns/code-lists/PrepaidCollectIndicator#C")
    # label: P
    # comment: Prepaid Indicator
    P = URIRef("https://onerecord.iata.org/ns/code-lists/PrepaidCollectIndicator#P")
