from typing import List

from pydantic import BaseModel, Field

from one_record_ontology.models.api.ErrorDetail import ErrorDetail


class Error(BaseModel):
    # label: has Error Detail
    # comment: Error details
    # iri: https://onerecord.iata.org/ns/api#hasErrorDetail
    hasErrorDetail: List[ErrorDetail] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasErrorDetail"
    )
    # label: Title
    # comment: Short summary of the error
    # iri: https://onerecord.iata.org/ns/api#hasTitle
    hasTitle: str = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasTitle"
    )
