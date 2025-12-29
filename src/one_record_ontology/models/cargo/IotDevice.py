from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PhysicalLogisticsObject import PhysicalLogisticsObject
class IotDevice(PhysicalLogisticsObject):
    # label: attachedToObject
    # comment: Reference to the PhysicalLogisticsObject the IotDevice is attached to
    # iri: https://onerecord.iata.org/ns/cargo#attachedToObject
    attachedToObject: List[PhysicalLogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#attachedToObject")
    # label: connectedSensors
    # comment: Reference to the sensors linked to the device
    # iri: https://onerecord.iata.org/ns/cargo#connectedSensors
    connectedSensors: List[Sensor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#connectedSensors")
    # label: manufacturer
    # comment: Manufacturing company details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#manufacturer
    manufacturer: List[Organization] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
    # label: deviceModel
    # comment: Commercial denomination of the device
    # iri: https://onerecord.iata.org/ns/cargo#deviceModel
    deviceModel: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#deviceModel")
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#name")
    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    # iri: https://onerecord.iata.org/ns/cargo#serialNumber
    serialNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber")