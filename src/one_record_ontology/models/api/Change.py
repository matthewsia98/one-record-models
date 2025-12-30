from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.api.Operation import Operation
from one_record_ontology.models.api.VerificationRequest import VerificationRequest
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject


class Change(BaseModel):
    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsObject
    hasLogisticsObject: LogisticsObject = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject"
    )
    # label: has Operation
    # comment: Operation(s) to apply as PATCH on a Logistics Object
    # iri: https://onerecord.iata.org/ns/api#hasOperation
    hasOperation: List[Operation] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasOperation"
    )
    # label: has Verification Request
    # comment: Link to the Verification Request
    # iri: https://onerecord.iata.org/ns/api#hasVerificationRequest
    hasVerificationRequest: List[VerificationRequest] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/api#hasVerificationRequest",
    )
    # label: Description
    # comment: Reason for the request (optional)
    # iri: https://onerecord.iata.org/ns/api#hasDescription
    hasDescription: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/api#hasDescription",
    )
    # label: Revision
    # comment: Revision number of the Logistics Object, starting with 0 for changing the initial revision of a Logistics Object
    # iri: https://onerecord.iata.org/ns/api#hasRevision
    hasRevision: int = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasRevision"
    )
    # label: notify RequestStatus Change
    # comment: Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    # iri: https://onerecord.iata.org/ns/api#notifyRequestStatusChange
    notifyRequestStatusChange: bool = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#notifyRequestStatusChange"
    )
