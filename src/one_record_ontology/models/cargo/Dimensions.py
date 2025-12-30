from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Value import Value


class Dimensions(BaseModel):
    # label: height
    # comment: Height
    # iri: https://onerecord.iata.org/ns/cargo#height
    height: Optional[Value] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#height"
    )
    # label: length
    # comment: Length
    # iri: https://onerecord.iata.org/ns/cargo#length
    length: Optional[Value] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#length"
    )
    # label: volume
    # comment: Volume
    # iri: https://onerecord.iata.org/ns/cargo#volume
    volume: Optional[Value] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#volume"
    )
    # label: width
    # comment: Width
    # iri: https://onerecord.iata.org/ns/cargo#width
    width: Optional[Value] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#width"
    )
