from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class ActivitySequence(BaseModel):
    # label: activity
    # comment: Reference to the Activity that is performed as part of a Service
    # iri: https://onerecord.iata.org/ns/cargo#activity
    activity: List[LogisticsActivity] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#activity")
    # label: sequenceNumber
    # comment: Short text to detail sequence number (alphanumeric)
    # iri: https://onerecord.iata.org/ns/cargo#sequenceNumber
    sequenceNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#sequenceNumber")