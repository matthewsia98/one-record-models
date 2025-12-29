from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PhysicalLogisticsObject import PhysicalLogisticsObject
class TransportMeans(PhysicalLogisticsObject):
    # label: operatedTransportMovement
    # comment: Transport Movement on which the Transport Means is used
    # iri: https://onerecord.iata.org/ns/cargo#operatedTransportMovement
    operatedTransportMovement: List[TransportMovement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#operatedTransportMovement")
    # label: transportOrganization
    # comment: Company operating the transport means
    # iri: https://onerecord.iata.org/ns/cargo#transportOrganization
    transportOrganization: List[Organization] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportOrganization")
    # label: typicalCo2Coefficient
    # comment: Required for some CO2 calculations
    # iri: https://onerecord.iata.org/ns/cargo#typicalCo2Coefficient
    typicalCo2Coefficient: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#typicalCo2Coefficient")
    # label: typicalFuelConsumption
    # comment: Typical fuel consumption (e.g. 2 L / 1 nm)
    # iri: https://onerecord.iata.org/ns/cargo#typicalFuelConsumption
    typicalFuelConsumption: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#typicalFuelConsumption")
    # label: vehicleType
    # comment: Vehicle or container type. Refer UNECE28, e.g. 4.. - Aircraft, type unknown.For Air refer to IATA Standard Schedules Information Manual in section ATA/IATA Aircraft Types
    # iri: https://onerecord.iata.org/ns/cargo#vehicleType
    vehicleType: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleType")
    # label: vehicleModel
    # comment: Model or make of the vehicle (e.g. A33-3)
    # iri: https://onerecord.iata.org/ns/cargo#vehicleModel
    vehicleModel: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleModel")
    # label: vehicleRegistration
    # comment: Vehicle identification - e.g. aircraft registration number
    # iri: https://onerecord.iata.org/ns/cargo#vehicleRegistration
    vehicleRegistration: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleRegistration")
    # label: vehicleSize
    # comment: Size of the vehicle - free text
    # iri: https://onerecord.iata.org/ns/cargo#vehicleSize
    vehicleSize: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleSize")