from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Location import Location


class StationRemarks(BaseModel):
    # label: station
    # comment: Reference to the station (Airport), mandatory
    # iri: https://onerecord.iata.org/ns/cargo#station
    station: Optional[Location] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#station"
    )
    # label: remarksText
    # comment: Details of the remarks, mandatory
    # iri: https://onerecord.iata.org/ns/cargo#remarksText
    remarksText: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#remarksText",
    )
