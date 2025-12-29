from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class OperationObject(BaseModel):
    # label: Datatype
    # comment: Data type of the field to update, must be a valid URI, e.g. http://www.w3.org/2001/XMLSchema#int
    # iri: https://onerecord.iata.org/ns/api#hasDatatype
    hasDatatype: AnyUrl = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasDatatype")
    # label: Value
    # comment: Updated value for the field
    # iri: https://onerecord.iata.org/ns/api#hasValue
    hasValue: str = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasValue")