from enum import Enum

from rdflib import URIRef


class AWBUseIndicator(str, Enum):
    """
    label: AWBUseIndicator
    comment: Restricted code list to describe Revenue, Service and Void AWBs based on CASS 2.0
    """

    # label: R
    # comment: Revenue AWB
    R = URIRef("https://onerecord.iata.org/ns/code-lists/AWBUseIndicator#R")
    # label: S
    # comment: Service AWB
    S = URIRef("https://onerecord.iata.org/ns/code-lists/AWBUseIndicator#S")
    # label: V
    # comment: Void AWB
    V = URIRef("https://onerecord.iata.org/ns/code-lists/AWBUseIndicator#V")
