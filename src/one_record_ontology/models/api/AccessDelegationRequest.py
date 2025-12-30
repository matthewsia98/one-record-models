from pydantic import Field

from one_record_ontology.models.api.AccessDelegation import AccessDelegation
from one_record_ontology.models.api.ActionRequest import ActionRequest


class AccessDelegationRequest(ActionRequest):
    # label: has Access Delegation
    # iri: https://onerecord.iata.org/ns/api#hasAccessDelegation
    hasAccessDelegation: AccessDelegation = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasAccessDelegation"
    )
