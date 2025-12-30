from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.code_lists.MeasurementUnitCode import (
    MeasurementUnitCode,
)


class Value(BaseModel):
    # label: unit
    # comment: Unit of measurement as per MeasurementUnitCode codelist. If the code is not present, create an instance of MeasurementUnitCode based on UNECE Rec. 20 Rev. 17e-2021
    # iri: https://onerecord.iata.org/ns/cargo#unit
    unit: Optional[MeasurementUnitCode] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unit"
    )
    # label: numericalValue
    # comment: Numerical value
    # iri: https://onerecord.iata.org/ns/cargo#numericalValue
    numericalValue: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue",
    )
