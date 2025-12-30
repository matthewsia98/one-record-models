from enum import Enum

from rdflib import URIRef


class DimensionsUnitCode(str, Enum):
    """
    label: DimensionsUnitCode
    comment: Restricted sub-code list of length units from MeasurementUnitCode
    """

    # label: CMT
    # comment: Centimetre
    CMT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CMT")
    # label: FOT
    # comment: Foot
    FOT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FOT")
    # label: INH
    # comment: Inch
    INH = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#INH")
    # label: MTR
    # comment: Metre
    MTR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MTR")
