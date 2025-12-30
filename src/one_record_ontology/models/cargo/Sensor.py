from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.IotDevice import IotDevice
from one_record_ontology.models.cargo.Measurement import Measurement
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)
from one_record_ontology.models.cargo.SensorType import SensorType


class Sensor(PhysicalLogisticsObject):
    # label: measurements
    # comment: Reference to the Measurements recorded by the Sensor
    # iri: https://onerecord.iata.org/ns/cargo#measurements
    measurements: List[Measurement] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#measurements",
    )
    # label: partOfIotDevice
    # comment: Reference to the IoT Device to which the sensor is linked
    # iri: https://onerecord.iata.org/ns/cargo#partOfIotDevice
    partOfIotDevice: Optional[IotDevice] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#partOfIotDevice",
    )
    # label: sensorType
    # comment: Type of sensor as described in Interactive Cargo Recommended Practice
    # iri: https://onerecord.iata.org/ns/cargo#sensorType
    sensorType: Optional[SensorType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#sensorType",
    )
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
    )
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#name"
    )
    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    # iri: https://onerecord.iata.org/ns/cargo#serialNumber
    serialNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber",
    )
