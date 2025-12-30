from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.DirectionType import DirectionType
from one_record_ontology.models.cargo.MovementTimeType import MovementTimeType
from one_record_ontology.models.code_lists.MovementIndicator import MovementIndicator


class MovementTime(BaseModel):
    # label: direction
    # comment: Direction to indicate if it's Inbound or Outbound
    # iri: https://onerecord.iata.org/ns/cargo#direction
    direction: Optional[DirectionType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#direction",
    )
    # label: movementMilestone
    # comment: The milestone list still needs to be defined, it includes elements from CXML Code List 1.92 but is not limited to those values, e.g. block-on and block-off times might be added as a comparison to wheels off and touchdown.
    # iri: https://onerecord.iata.org/ns/cargo#movementMilestone
    movementMilestone: Optional[MovementIndicator] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementMilestone",
    )
    # label: movementTimeType
    # comment: The type of time can be Actual, Estimated ot Scheduled
    # iri: https://onerecord.iata.org/ns/cargo#movementTimeType
    movementTimeType: Optional[MovementTimeType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimeType",
    )
    # label: movementTimestamp
    # comment: Timestamp (date and time) of the movement time. If the movement time is recorded asynchronously, the timestamp should reflect the actual time, not when the data was created.
    # iri: https://onerecord.iata.org/ns/cargo#movementTimestamp
    movementTimestamp: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimestamp",
    )
