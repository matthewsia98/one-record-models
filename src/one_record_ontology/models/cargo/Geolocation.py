from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Value import Value


class Geolocation(BaseModel):
    # label: elevation
    # comment: Elevation from sea level - Change of data type to Value as of ontology v1.1
    # iri: https://onerecord.iata.org/ns/cargo#elevation
    elevation: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#elevation",
    )
    # label: latitude
    # comment: Location latitude decimal
    # iri: https://onerecord.iata.org/ns/cargo#latitude
    latitude: Optional[float] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#latitude"
    )
    # label: longitude
    # comment: Location longitude decimal
    # iri: https://onerecord.iata.org/ns/cargo#longitude
    longitude: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#longitude",
    )
