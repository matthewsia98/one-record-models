from enum import Enum

from rdflib import URIRef


class TemperatureUnitCode(str, Enum):
    """
    label: TemperatureUnitCode
    comment: Restricted sub-code list of temperature units from MeasurementUnitCode
    """

    # label: CEL
    # comment: Degree Celsius
    CEL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CEL")
    # label: FAH
    # comment: Degree Fahrenheit
    FAH = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FAH")
    # label: KEL
    # comment: Kelvin
    KEL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KEL")
