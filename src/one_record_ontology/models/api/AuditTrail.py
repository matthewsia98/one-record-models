from one_record_ontology.models.api.ActionRequest import ActionRequest
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class AuditTrail(BaseModel):
    # label: has Action Request
    # comment: Link any type of Action Request
    # iri: https://onerecord.iata.org/ns/api#hasActionRequest
    hasActionRequest: List[ActionRequest] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasActionRequest")
    # label: Latest revision
    # comment: Latest revision of the Logistics Object. Starting with revision 0
    # iri: https://onerecord.iata.org/ns/api#hasLatestRevision
    hasLatestRevision: int = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasLatestRevision")