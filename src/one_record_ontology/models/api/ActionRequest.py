from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.api.Error import Error
from one_record_ontology.models.api.RequestStatus import RequestStatus
from one_record_ontology.models.cargo.Organization import Organization


class ActionRequest(BaseModel):
    # label: has Error
    # comment: Error object(s) if the processing was not successful
    # iri: https://onerecord.iata.org/ns/api#hasError
    hasError: List[Error] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/api#hasError",
    )
    # label: has Request Status
    # iri: https://onerecord.iata.org/ns/api#hasRequestStatus
    hasRequestStatus: RequestStatus = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasRequestStatus"
    )
    # label: is Requested By
    # comment: Organization Identifier that represents the Organization that has requested the action
    # iri: https://onerecord.iata.org/ns/api#isRequestedBy
    isRequestedBy: Organization = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isRequestedBy"
    )
    # label: is revoked by
    # iri: https://onerecord.iata.org/ns/api#isRevokedBy
    isRevokedBy: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/api#isRevokedBy",
    )
    # label: Requested at
    # comment: Datetime when the request was created
    # iri: https://onerecord.iata.org/ns/api#isRequestedAt
    isRequestedAt: datetime = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isRequestedAt"
    )
    # label: Revoked at
    # comment: The datetime when the action request was revoked.
    # iri: https://onerecord.iata.org/ns/api#isRevokedAt
    isRevokedAt: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/api#isRevokedAt",
    )
