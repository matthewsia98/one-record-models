from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.LogisticsActivity import LogisticsActivity


class ActivitySequence(BaseModel):
    # label: activity
    # comment: Reference to the Activity that is performed as part of a Service
    # iri: https://onerecord.iata.org/ns/cargo#activity
    activity: Optional[LogisticsActivity] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#activity"
    )
    # label: sequenceNumber
    # comment: Short text to detail sequence number (alphanumeric)
    # iri: https://onerecord.iata.org/ns/cargo#sequenceNumber
    sequenceNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#sequenceNumber",
    )
