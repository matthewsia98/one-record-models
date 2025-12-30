from enum import Enum

from rdflib import URIRef


class LoadingType(str, Enum):
    """
    label: LoadingType
    comment: Restricted code list for Loading subtypes
    """

    # label: LOADING
    # comment: Describes a loading process, for example putting an ULD on an aircraft or a piece in a truck
    LOADING = URIRef("https://onerecord.iata.org/ns/cargo#LOADING")
    # label: UNLOADING
    # comment: Describes an unloading process, for example removing an ULD from an aircraft or a piece from a truck
    UNLOADING = URIRef("https://onerecord.iata.org/ns/cargo#UNLOADING")
