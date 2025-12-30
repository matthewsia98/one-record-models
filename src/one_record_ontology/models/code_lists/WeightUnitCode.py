from enum import Enum

from rdflib import URIRef


class WeightUnitCode(str, Enum):
    """
    label: WeightUnitCode
    comment: Restricted sub-code list of weight units from MeasurementUnitCode
    """

    # label: KGM
    # comment: Kilogram
    KGM = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KGM")
    # label: LBR
    # comment: Pound UK, US (0.45359237 KGM)
    LBR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#LBR")
    # label: ONZ
    # comment: Ounce UK, US (28.949523 GRM)
    ONZ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#ONZ")
