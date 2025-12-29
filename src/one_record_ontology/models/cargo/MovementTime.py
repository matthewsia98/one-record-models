from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class MovementTime(BaseModel):
    # label: direction
    # comment: Direction to indicate if it's Inbound or Outbound
    # iri: https://onerecord.iata.org/ns/cargo#direction
    direction: List[DirectionType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#direction")
    # label: movementMilestone
    # comment: The milestone list still needs to be defined, it includes elements from CXML Code List 1.92 but is not limited to those values, e.g. block-on and block-off times might be added as a comparison to wheels off and touchdown.
    # iri: https://onerecord.iata.org/ns/cargo#movementMilestone
    movementMilestone: List[MovementIndicator] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#movementMilestone")
    # label: movementTimeType
    # comment: The type of time can be Actual, Estimated ot Scheduled
    # iri: https://onerecord.iata.org/ns/cargo#movementTimeType
    movementTimeType: List[MovementTimeType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimeType")
    # label: movementTimestamp
    # comment: Timestamp (date and time) of the movement time. If the movement time is recorded asynchronously, the timestamp should reflect the actual time, not when the data was created.
    # iri: https://onerecord.iata.org/ns/cargo#movementTimestamp
    movementTimestamp: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimestamp")