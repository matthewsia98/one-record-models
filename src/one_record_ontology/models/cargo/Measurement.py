from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Geolocation import Geolocation
from one_record_ontology.models.cargo.Value import Value


class Measurement(BaseModel):
    # label: measurementValue
    # comment: Information about all non-Geolocation values of the measurement
    # iri: https://onerecord.iata.org/ns/cargo#measurementValue
    measurementValue: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#measurementValue",
    )
    # label: recordedGeolocation
    # comment: Reference to the Geolocation recorded of the measurement
    # iri: https://onerecord.iata.org/ns/cargo#recordedGeolocation
    recordedGeolocation: Optional[Geolocation] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#recordedGeolocation",
    )
    # label: measurementTimestamp
    # comment: Timestamp for the measurement
    # iri: https://onerecord.iata.org/ns/cargo#measurementTimestamp
    measurementTimestamp: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#measurementTimestamp",
    )
