from enum import Enum

from rdflib import URIRef


class VolumeUnitCode(str, Enum):
    """
    label: VolumeUnitCode
    comment: Restricted sub-code list of volume units from MeasurementUnitCode
    """

    # label: CMQ
    # comment: Cubic Centimetre
    CMQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CMQ")
    # label: FTQ
    # comment: Cubic Foot
    FTQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FTQ")
    # label: GLL
    # comment: Liquid Gallon (3.78541 DM3)
    GLL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#GLL")
    # label: INQ
    # comment: Cubic Inch
    INQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#INQ")
    # label: LTR
    # comment: Litre (1 DM3)
    LTR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#LTR")
    # label: MTQ
    # comment: Cubic Metre
    MTQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MTQ")
