from one_record_ontology.models.api.Any import Any
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.api.ActionRequest import ActionRequest
class ChangeRequest(ActionRequest):
    # label: has Change
    # comment: Contains submitted Change object
    # iri: https://onerecord.iata.org/ns/api#hasChange
    hasChange: Any = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasChange")