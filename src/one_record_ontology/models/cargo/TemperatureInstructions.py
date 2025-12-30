from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Value import Value


class TemperatureInstructions(BaseModel):
    # label: maxTemperature
    # comment: Maximum temperature of the range
    # iri: https://onerecord.iata.org/ns/cargo#maxTemperature
    maxTemperature: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#maxTemperature",
    )
    # label: minTemperature
    # comment: Minimum temperature of the range
    # iri: https://onerecord.iata.org/ns/cargo#minTemperature
    minTemperature: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#minTemperature",
    )
