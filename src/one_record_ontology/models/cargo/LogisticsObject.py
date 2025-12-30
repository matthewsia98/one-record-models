from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Check import Check
from one_record_ontology.models.cargo.ExternalReference import ExternalReference
from one_record_ontology.models.cargo.LogisticsEvent import LogisticsEvent


class LogisticsObject(BaseModel):
    # label: checks
    # comment: References to the CheckActions performed on the object
    # iri: https://onerecord.iata.org/ns/cargo#checks
    checks: List[Check] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#checks",
    )
    # label: events
    # comment: Events object
    # iri: https://onerecord.iata.org/ns/cargo#events
    events: List[LogisticsEvent] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#events",
    )
    # label: externalReferences
    # comment: References to all associated ExternalReferences
    # iri: https://onerecord.iata.org/ns/cargo#externalReferences
    externalReferences: List[ExternalReference] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#externalReferences",
    )
    # label: skeletonIndicator
    # comment: Indicator whether a logistics object is a skeleton object
    # iri: https://onerecord.iata.org/ns/cargo#skeletonIndicator
    skeletonIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#skeletonIndicator",
    )
