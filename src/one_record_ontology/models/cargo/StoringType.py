from enum import Enum

from rdflib import URIRef


class StoringType(str, Enum):
    """
    label: StoringType
    comment: Restricted code list for Storing subtypes
    """

    # label: STORE_IN
    # comment: Describes a store-in process, where a physical object is assigned to a specific location
    STORE_IN = URIRef("https://onerecord.iata.org/ns/cargo#STORE_IN")
    # label: STORE_OUT
    # comment: Describes a store-out process, where a physical object leaves a specific location
    STORE_OUT = URIRef("https://onerecord.iata.org/ns/cargo#STORE_OUT")
