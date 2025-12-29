from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Measurement(BaseModel):
    # label: measurementValue
    # comment: Information about all non-Geolocation values of the measurement
    # iri: https://onerecord.iata.org/ns/cargo#measurementValue
    measurementValue: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#measurementValue")
    # label: recordedGeolocation
    # comment: Reference to the Geolocation recorded of the measurement
    # iri: https://onerecord.iata.org/ns/cargo#recordedGeolocation
    recordedGeolocation: List[Geolocation] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#recordedGeolocation")
    # label: measurementTimestamp
    # comment: Timestamp for the measurement
    # iri: https://onerecord.iata.org/ns/cargo#measurementTimestamp
    measurementTimestamp: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#measurementTimestamp")