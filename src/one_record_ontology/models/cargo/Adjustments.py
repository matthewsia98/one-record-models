from typing import Optional

from pydantic import BaseModel, Field


class Adjustments(BaseModel):
    # label: correctionNumber
    # comment: Number of the adjustment
    # iri: https://onerecord.iata.org/ns/cargo#correctionNumber
    correctionNumber: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#correctionNumber",
    )
    # label: correctionSerialNumber
    # comment: Serial Number of the correction
    # iri: https://onerecord.iata.org/ns/cargo#correctionSerialNumber
    correctionSerialNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#correctionSerialNumber",
    )
    # label: reasonsForAdjustments
    # comment: A free text for user to include a reason for correction
    # iri: https://onerecord.iata.org/ns/cargo#reasonsForAdjustments
    reasonsForAdjustments: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#reasonsForAdjustments",
    )
