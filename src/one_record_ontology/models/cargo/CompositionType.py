from enum import Enum

from rdflib import URIRef


class CompositionType(str, Enum):
    """
    label: CompositionType
    comment: Restricted code list for Composing subtypes
    """

    # label: COMPOSITION
    # comment: Describes a composition, for example the loading of a container or the build-up of an ULD
    COMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#COMPOSITION")
    # label: DECOMPOSITION
    # comment: Describes a decomposition, for example the unloading of a container or the break-down of an ULD
    DECOMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#DECOMPOSITION")
