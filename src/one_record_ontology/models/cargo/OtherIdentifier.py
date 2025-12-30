from typing import Optional

from pydantic import BaseModel, Field


class OtherIdentifier(BaseModel):
    # label: otherIdentifierType
    # comment: Identifier type or description
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifierType
    otherIdentifierType: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifierType",
    )
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
    )
