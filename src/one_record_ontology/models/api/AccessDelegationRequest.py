from one_record_ontology.models.api.AccessDelegation import AccessDelegation
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.api.ActionRequest import ActionRequest
class AccessDelegationRequest(ActionRequest):
    # label: has Access Delegation
    # iri: https://onerecord.iata.org/ns/api#hasAccessDelegation
    hasAccessDelegation: AccessDelegation = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasAccessDelegation")