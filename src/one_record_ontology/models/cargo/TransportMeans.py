from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.Organization import Organization
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)
from one_record_ontology.models.cargo.TransportMovement import TransportMovement
from one_record_ontology.models.cargo.Value import Value


class TransportMeans(PhysicalLogisticsObject):
    # label: operatedTransportMovement
    # comment: Transport Movement on which the Transport Means is used
    # iri: https://onerecord.iata.org/ns/cargo#operatedTransportMovement
    operatedTransportMovement: Optional[TransportMovement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatedTransportMovement",
    )
    # label: transportOrganization
    # comment: Company operating the transport means
    # iri: https://onerecord.iata.org/ns/cargo#transportOrganization
    transportOrganization: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportOrganization",
    )
    # label: typicalCo2Coefficient
    # comment: Required for some CO2 calculations
    # iri: https://onerecord.iata.org/ns/cargo#typicalCo2Coefficient
    typicalCo2Coefficient: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#typicalCo2Coefficient",
    )
    # label: typicalFuelConsumption
    # comment: Typical fuel consumption (e.g. 2 L / 1 nm)
    # iri: https://onerecord.iata.org/ns/cargo#typicalFuelConsumption
    typicalFuelConsumption: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#typicalFuelConsumption",
    )
    # label: vehicleType
    # comment: Vehicle or container type. Refer UNECE28, e.g. 4.. - Aircraft, type unknown.For Air refer to IATA Standard Schedules Information Manual in section ATA/IATA Aircraft Types
    # iri: https://onerecord.iata.org/ns/cargo#vehicleType
    vehicleType: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleType",
    )
    # label: vehicleModel
    # comment: Model or make of the vehicle (e.g. A33-3)
    # iri: https://onerecord.iata.org/ns/cargo#vehicleModel
    vehicleModel: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleModel",
    )
    # label: vehicleRegistration
    # comment: Vehicle identification - e.g. aircraft registration number
    # iri: https://onerecord.iata.org/ns/cargo#vehicleRegistration
    vehicleRegistration: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleRegistration",
    )
    # label: vehicleSize
    # comment: Size of the vehicle - free text
    # iri: https://onerecord.iata.org/ns/cargo#vehicleSize
    vehicleSize: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleSize",
    )
