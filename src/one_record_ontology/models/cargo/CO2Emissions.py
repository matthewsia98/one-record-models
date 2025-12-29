from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class CO2Emissions(LogisticsObject):
    # label: calculatedEmissions
    # comment: CO2 emissions calculated
    # iri: https://onerecord.iata.org/ns/cargo#calculatedEmissions
    calculatedEmissions: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#calculatedEmissions")
    # label: calculationFor
    # comment: Reference to the TransportMovement or TransportLegs the CO2Emissions have been calculated for
    # iri: https://onerecord.iata.org/ns/cargo#calculationFor
    calculationFor: List[LogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#calculationFor")
    # label: methodName
    # comment: Name of the CO2 calculation method
    # iri: https://onerecord.iata.org/ns/cargo#methodName
    methodName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#methodName")
    # label: methodVersion
    # comment: Version used for the calculation
    # iri: https://onerecord.iata.org/ns/cargo#methodVersion
    methodVersion: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#methodVersion")