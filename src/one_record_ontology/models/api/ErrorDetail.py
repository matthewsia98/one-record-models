from typing import Optional

from pydantic import AnyUrl, BaseModel, Field


class ErrorDetail(BaseModel):
    # label: Code
    # comment: Error code is a numeric or alphanumeric code that can be used to determine the source of the error and why it occured.
    # iri: https://onerecord.iata.org/ns/api#hasCode
    hasCode: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasCode"
    )
    # label: Message
    # comment: Message that describes the error
    # iri: https://onerecord.iata.org/ns/api#hasMessage
    hasMessage: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasMessage"
    )
    # label: Property
    # comment: Property of the object for which the error applies in IRI format, i.e. https://onerecord.iata.org/ns/cargo#hasVolumetricWeight
    # iri: https://onerecord.iata.org/ns/api#hasProperty
    hasProperty: Optional[AnyUrl] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/api#hasProperty",
    )
    # label: Resource
    # comment: URI of the object where the error occurred
    # iri: https://onerecord.iata.org/ns/api#hasResource
    hasResource: Optional[AnyUrl] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/api#hasResource",
    )
