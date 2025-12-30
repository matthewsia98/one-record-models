from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Value import Value


class CO2Emissions(LogisticsObject):
    # label: calculatedEmissions
    # comment: CO2 emissions calculated
    # iri: https://onerecord.iata.org/ns/cargo#calculatedEmissions
    calculatedEmissions: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#calculatedEmissions",
    )
    # label: calculationFor
    # comment: Reference to the TransportMovement or TransportLegs the CO2Emissions have been calculated for
    # iri: https://onerecord.iata.org/ns/cargo#calculationFor
    calculationFor: Optional[LogisticsObject] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#calculationFor",
    )
    # label: methodName
    # comment: Name of the CO2 calculation method
    # iri: https://onerecord.iata.org/ns/cargo#methodName
    methodName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#methodName",
    )
    # label: methodVersion
    # comment: Version used for the calculation
    # iri: https://onerecord.iata.org/ns/cargo#methodVersion
    methodVersion: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#methodVersion",
    )
