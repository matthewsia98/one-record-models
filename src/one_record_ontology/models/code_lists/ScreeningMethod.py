from enum import Enum

from rdflib import URIRef


class ScreeningMethod(str, Enum):
    """
    label: ScreeningMethod
    comment: Restricted code list corresponding to cXML code list 1.102 Screening Methods
    """

    # label: AOM
    # comment: Subjected to Any Other Means
    AOM = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#AOM")
    # label: CMD
    # comment: Cargo Metal Detection
    CMD = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#CMD")
    # label: EDD
    # comment: Explosive Detection Dogs
    EDD = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#EDD")
    # label: EDS
    # comment: Explosive Detection System
    EDS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#EDS")
    # label: ETD
    # comment: Explosives Trace Detection Equipment - Particles or Vapor
    ETD = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#ETD")
    # label: PHS
    # comment: Physical Inspection and/or Hand Search
    PHS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#PHS")
    # label: VCK
    # comment: Visualcheck
    VCK = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#VCK")
    # label: XRY
    # comment: X-ray Equipment
    XRY = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#XRY")
