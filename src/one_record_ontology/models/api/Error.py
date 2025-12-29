from one_record_ontology.models.api.ErrorDetail import ErrorDetail
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Error(BaseModel):
    # label: has Error Detail
    # comment: Error details
    # iri: https://onerecord.iata.org/ns/api#hasErrorDetail
    hasErrorDetail: List[ErrorDetail] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasErrorDetail")
    # label: Title
    # comment: Short summary of the error
    # iri: https://onerecord.iata.org/ns/api#hasTitle
    hasTitle: str = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasTitle")