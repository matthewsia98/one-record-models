from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PhysicalLogisticsObject import PhysicalLogisticsObject
class Sensor(PhysicalLogisticsObject):
    # label: measurements
    # comment: Reference to the Measurements recorded by the Sensor
    # iri: https://onerecord.iata.org/ns/cargo#measurements
    measurements: List[Measurement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#measurements")
    # label: partOfIotDevice
    # comment: Reference to the IoT Device to which the sensor is linked
    # iri: https://onerecord.iata.org/ns/cargo#partOfIotDevice
    partOfIotDevice: List[IotDevice] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#partOfIotDevice")
    # label: sensorType
    # comment: Type of sensor as described in Interactive Cargo Recommended Practice
    # iri: https://onerecord.iata.org/ns/cargo#sensorType
    sensorType: List[SensorType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#sensorType")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#name")
    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    # iri: https://onerecord.iata.org/ns/cargo#serialNumber
    serialNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber")