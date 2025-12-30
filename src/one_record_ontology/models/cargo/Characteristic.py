from typing import Optional

from pydantic import BaseModel, Field


class Characteristic(BaseModel):
    # label: characteristicType
    # comment: Product characteristics code - e.g. CLR - Color. Not restricted to a list.
    # iri: https://onerecord.iata.org/ns/cargo#characteristicType
    characteristicType: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#characteristicType",
    )
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
    )
