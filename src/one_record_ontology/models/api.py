from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import AnyUrl, BaseModel, Field
from rdflib import URIRef

from one_record_ontology.models.cargo import (
    LogisticsEvent,
    LogisticsObject,
    Organization,
)


class AccessDelegation(BaseModel):
    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsObject
    hasLogisticsObject: List[LogisticsObject] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject")
    # label: has Permission
    # iri: https://onerecord.iata.org/ns/api#hasPermission
    hasPermission: List[Permission] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasPermission")
    # label: is requested for
    # iri: https://onerecord.iata.org/ns/api#isRequestedFor
    isRequestedFor: List[Organization] = Field(serialization_alias="https://onerecord.iata.org/ns/api#isRequestedFor")
    # label: Description
    # comment: Reason for the request (optional)
    # iri: https://onerecord.iata.org/ns/api#hasDescription
    hasDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasDescription")
    # label: notify RequestStatus Change
    # comment: Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    # iri: https://onerecord.iata.org/ns/api#notifyRequestStatusChange
    notifyRequestStatusChange: bool = Field(serialization_alias="https://onerecord.iata.org/ns/api#notifyRequestStatusChange")
class AccessDelegationRequest(ActionRequest):
    # label: has Access Delegation
    # iri: https://onerecord.iata.org/ns/api#hasAccessDelegation
    hasAccessDelegation: AccessDelegation = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasAccessDelegation")
class ActionRequest(BaseModel):
    # label: has Error
    # comment: Error object(s) if the processing was not successful
    # iri: https://onerecord.iata.org/ns/api#hasError
    hasError: List[Error] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasError")
    # label: has Request Status
    # iri: https://onerecord.iata.org/ns/api#hasRequestStatus
    hasRequestStatus: RequestStatus = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasRequestStatus")
    # label: is Requested By
    # comment: Organization Identifier that represents the Organization that has requested the action
    # iri: https://onerecord.iata.org/ns/api#isRequestedBy
    isRequestedBy: Organization = Field(serialization_alias="https://onerecord.iata.org/ns/api#isRequestedBy")
    # label: is revoked by
    # iri: https://onerecord.iata.org/ns/api#isRevokedBy
    isRevokedBy: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#isRevokedBy")
    # label: Requested at
    # comment: Datetime when the request was created
    # iri: https://onerecord.iata.org/ns/api#isRequestedAt
    isRequestedAt: datetime = Field(serialization_alias="https://onerecord.iata.org/ns/api#isRequestedAt")
    # label: Revoked at
    # comment: The datetime when the action request was revoked.
    # iri: https://onerecord.iata.org/ns/api#isRevokedAt
    isRevokedAt: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#isRevokedAt")
class AuditTrail(BaseModel):
    # label: has Action Request
    # comment: Link any type of Action Request
    # iri: https://onerecord.iata.org/ns/api#hasActionRequest
    hasActionRequest: List[ActionRequest] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasActionRequest")
    # label: Latest revision
    # comment: Latest revision of the Logistics Object. Starting with revision 0
    # iri: https://onerecord.iata.org/ns/api#hasLatestRevision
    hasLatestRevision: int = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasLatestRevision")
class Change(BaseModel):
    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsObject
    hasLogisticsObject: LogisticsObject = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject")
    # label: has Operation
    # comment: Operation(s) to apply as PATCH on a Logistics Object
    # iri: https://onerecord.iata.org/ns/api#hasOperation
    hasOperation: List[Operation] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasOperation")
    # label: has Verification Request
    # comment: Link to the Verification Request
    # iri: https://onerecord.iata.org/ns/api#hasVerificationRequest
    hasVerificationRequest: List[VerificationRequest] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasVerificationRequest")
    # label: Description
    # comment: Reason for the request (optional)
    # iri: https://onerecord.iata.org/ns/api#hasDescription
    hasDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasDescription")
    # label: Revision
    # comment: Revision number of the Logistics Object, starting with 0 for changing the initial revision of a Logistics Object
    # iri: https://onerecord.iata.org/ns/api#hasRevision
    hasRevision: int = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasRevision")
    # label: notify RequestStatus Change
    # comment: Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    # iri: https://onerecord.iata.org/ns/api#notifyRequestStatusChange
    notifyRequestStatusChange: bool = Field(serialization_alias="https://onerecord.iata.org/ns/api#notifyRequestStatusChange")
class ChangeRequest(ActionRequest):
    # label: has Change
    # comment: Contains submitted Change object
    # iri: https://onerecord.iata.org/ns/api#hasChange
    hasChange: Any = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasChange")
class Collection(BaseModel):
    # label: has Item
    # comment: Item that is contained in a collection
    # iri: https://onerecord.iata.org/ns/api#hasItem
    hasItem: List[Any] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasItem")
    # label: Total items
    # comment: The number of total items contained in a collection
    # iri: https://onerecord.iata.org/ns/api#hasTotalItems
    hasTotalItems: int = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasTotalItems")
class Error(BaseModel):
    # label: has Error Detail
    # comment: Error details
    # iri: https://onerecord.iata.org/ns/api#hasErrorDetail
    hasErrorDetail: List[ErrorDetail] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasErrorDetail")
    # label: Title
    # comment: Short summary of the error
    # iri: https://onerecord.iata.org/ns/api#hasTitle
    hasTitle: str = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasTitle")
class ErrorDetail(BaseModel):
    # label: Code
    # comment: Error code is a numeric or alphanumeric code that can be used to determine the source of the error and why it occured.
    # iri: https://onerecord.iata.org/ns/api#hasCode
    hasCode: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasCode")
    # label: Message
    # comment: Message that describes the error
    # iri: https://onerecord.iata.org/ns/api#hasMessage
    hasMessage: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasMessage")
    # label: Property
    # comment: Property of the object for which the error applies in IRI format, i.e. https://onerecord.iata.org/ns/cargo#hasVolumetricWeight
    # iri: https://onerecord.iata.org/ns/api#hasProperty
    hasProperty: Optional[AnyUrl] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasProperty")
    # label: Resource
    # comment: URI of the object where the error occurred
    # iri: https://onerecord.iata.org/ns/api#hasResource
    hasResource: Optional[AnyUrl] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasResource")
class Notification(BaseModel):
    # label: has Event Type
    # iri: https://onerecord.iata.org/ns/api#hasEventType
    hasEventType: NotificationEventType = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasEventType")
    # label: has Logistics Event
    # comment: A reference to a cargo LogisticsEvent
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsEvent
    hasLogisticsEvent: List[LogisticsEvent] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsEvent")
    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsObject
    hasLogisticsObject: Optional[LogisticsObject] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject")
    # label: is triggered by
    # comment: Optional URI to the ChangeRequest that triggered a Notification if the eventType is one of CHANGE_REQUEST_ACCEPTED, CHANGE_REQUEST_REJECT, or CHANGE_REQUEST_FAILED
    # iri: https://onerecord.iata.org/ns/api#isTriggeredBy
    isTriggeredBy: Optional[ActionRequest] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#isTriggeredBy")
    # label: Changed property
    # comment: List of all changed properties as IRIs after a ChangeRequest was successfully applied, e.g. [https://onerecord.iata.org/ns/cargo#hasVolumetricWeight, https://onerecord.iata.org/ns/cargo/#hasGoodsDescription]
    # iri: https://onerecord.iata.org/ns/api#hasChangedProperty
    hasChangedProperty: List[AnyUrl] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasChangedProperty")
    # label: has Logistics Object Type
    # comment: The type of cargo:LogisticsObject in the notification e.g. https://onerecord.iata.org/ns/cargo#Piece
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsObjectType
    hasLogisticsObjectType: Optional[AnyUrl] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObjectType")
class NotificationEventType(str, Enum):
    """
    label: Notification Event Type
    """
    # label: ACCESS_DELEGATION_REQUEST_ACCEPTED
    ACCESS_DELEGATION_REQUEST_ACCEPTED = URIRef("https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_ACCEPTED")
    # label: ACCESS_DELEGATION_REQUEST_FAILED
    ACCESS_DELEGATION_REQUEST_FAILED = URIRef("https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_FAILED")
    # label: ACCESS_DELEGATION_REQUEST_PENDING
    ACCESS_DELEGATION_REQUEST_PENDING = URIRef("https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_PENDING")
    # label: ACCESS_DELEGATION_REQUEST_REJECTED
    ACCESS_DELEGATION_REQUEST_REJECTED = URIRef("https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_REJECTED")
    # label: ACCESS_DELEGATION_REQUEST_REVOKED
    ACCESS_DELEGATION_REQUEST_REVOKED = URIRef("https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_REVOKED")
    # label: CHANGE_REQUEST_ACCEPTED
    # comment: :EventType for accepted :ChangeRequests
    CHANGE_REQUEST_ACCEPTED = URIRef("https://onerecord.iata.org/ns/api#CHANGE_REQUEST_ACCEPTED")
    # label: CHANGE_REQUEST_FAILED
    # comment: :EventType for failed :ChangeRequests.
    CHANGE_REQUEST_FAILED = URIRef("https://onerecord.iata.org/ns/api#CHANGE_REQUEST_FAILED")
    # label: CHANGE_REQUEST_PENDING
    # comment: :EventType for pending :ChangeRequests.
    CHANGE_REQUEST_PENDING = URIRef("https://onerecord.iata.org/ns/api#CHANGE_REQUEST_PENDING")
    # label: CHANGE_REQUEST_PENDING
    CHANGE_REQUEST_REJECTED = URIRef("https://onerecord.iata.org/ns/api#CHANGE_REQUEST_REJECTED")
    # label: CHANGE_REQUEST_REVOKED
    CHANGE_REQUEST_REVOKED = URIRef("https://onerecord.iata.org/ns/api#CHANGE_REQUEST_REVOKED")
    # label: LOGISTICS_EVENT_RECEIVED
    LOGISTICS_EVENT_RECEIVED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_EVENT_RECEIVED")
    # label: LOGISTICS_OBJECT_CREATED
    LOGISTICS_OBJECT_CREATED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_CREATED")
    # label: LOGISTICS_OBJECT_UPDATED
    LOGISTICS_OBJECT_UPDATED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_UPDATED")
    # label: SUBSCRIPTION_REQUEST_ACCEPTED
    SUBSCRIPTION_REQUEST_ACCEPTED = URIRef("https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_ACCEPTED")
    # label: SUBSCRIPTION_REQUEST_FAILED
    SUBSCRIPTION_REQUEST_FAILED = URIRef("https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_FAILED")
    # label: SUBSCRIPTION_REQUEST_PENDING
    SUBSCRIPTION_REQUEST_PENDING = URIRef("https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_PENDING")
    # label: SUBSCRIPTION_REQUEST_REJECTED
    SUBSCRIPTION_REQUEST_REJECTED = URIRef("https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_REJECTED")
    # label: SUBSCRIPTION_REQUEST_REVOKED
    SUBSCRIPTION_REQUEST_REVOKED = URIRef("https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_REVOKED")
class Operation(BaseModel):
    # iri: https://onerecord.iata.org/ns/api#o
    o: OperationObject = Field(serialization_alias="https://onerecord.iata.org/ns/api#o")
    # iri: https://onerecord.iata.org/ns/api#op
    op: PatchOperation = Field(serialization_alias="https://onerecord.iata.org/ns/api#op")
    # label: p
    # comment: Operations objects must have exactly one p, predicate, member. The value of this member must be an URI, e.g. https://onerecord.iata.org/ns/cargo#hasGoodsDescription
    # iri: https://onerecord.iata.org/ns/api#p
    p: AnyUrl = Field(serialization_alias="https://onerecord.iata.org/ns/api#p")
    # label: s
    # comment: Operation objects MUST have exactly one "s", subject, member. The value of this member MUST be one of IRI or blank node.
    # iri: https://onerecord.iata.org/ns/api#s
    s: str = Field(serialization_alias="https://onerecord.iata.org/ns/api#s")
class OperationObject(BaseModel):
    # label: Datatype
    # comment: Data type of the field to update, must be a valid URI, e.g. http://www.w3.org/2001/XMLSchema#int
    # iri: https://onerecord.iata.org/ns/api#hasDatatype
    hasDatatype: AnyUrl = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasDatatype")
    # label: Value
    # comment: Updated value for the field
    # iri: https://onerecord.iata.org/ns/api#hasValue
    hasValue: str = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasValue")
class PatchOperation(str, Enum):
    """
    label: Patch Operation
    """
    # label: ADD
    # comment: Defines a :PatchOperation to be an operation that adds new triples.
    ADD = URIRef("https://onerecord.iata.org/ns/api#ADD")
    # label: DELETE
    DELETE = URIRef("https://onerecord.iata.org/ns/api#DELETE")
class Permission(str, Enum):
    """
    label: Permission
    """
    # label: GET_LOGISTICS_EVENT
    # comment: :Permission to get a :LogisticsEvent
    GET_LOGISTICS_EVENT = URIRef("https://onerecord.iata.org/ns/api#GET_LOGISTICS_EVENT")
    # label: GET_LOGISTICS_OBJECT
    # comment: :Permission to get a :LogisticsObject
    GET_LOGISTICS_OBJECT = URIRef("https://onerecord.iata.org/ns/api#GET_LOGISTICS_OBJECT")
    # label: PATCH_LOGISTICS_OBJECT
    PATCH_LOGISTICS_OBJECT = URIRef("https://onerecord.iata.org/ns/api#PATCH_LOGISTICS_OBJECT")
    # label: POST_LOGISTICS_EVENT
    # comment: :Permission to add a logistics event.
    POST_LOGISTICS_EVENT = URIRef("https://onerecord.iata.org/ns/api#POST_LOGISTICS_EVENT")
class RequestStatus(str, Enum):
    """
    label: RequestStatus
    """
    # label: REQUEST_ACCEPTED
    REQUEST_ACCEPTED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_ACCEPTED")
    # label: REQUEST_FAILED
    REQUEST_FAILED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_FAILED")
    # label: REQUEST_PENDING
    REQUEST_PENDING = URIRef("https://onerecord.iata.org/ns/api#REQUEST_PENDING")
    # label: REQUEST_REJECTED
    REQUEST_REJECTED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_REJECTED")
    # label: REQUEST_REVOKED
    REQUEST_REVOKED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_REVOKED")
class ServerInformation(BaseModel):
    # label: has Data Holder
    # comment: The data holder of the servers data.
    # iri: https://onerecord.iata.org/ns/api#hasDataHolder
    hasDataHolder: Organization = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasDataHolder")
    # label: Supported encoding
    # comment: Optional list of supported encodings of the ONE Record server, e.g. gzip
    # iri: https://onerecord.iata.org/ns/api#hasSupportedEncoding
    hasSupportedEncoding: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedEncoding")
    # label: Supported API version
    # comment: Supported ONE Record API versions by the server, MUST include at least one supported version.
    # iri: https://onerecord.iata.org/ns/api#hasSupportedApiVersion
    hasSupportedApiVersion: List[str] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedApiVersion")
    # label: Supported content type
    # comment: Supported content types of the server, MUST contain at least application/ld+json
    # iri: https://onerecord.iata.org/ns/api#hasSupportedContentType
    hasSupportedContentType: List[str] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedContentType")
    # label: Supported language
    # comment: Supported languages of the ONE Record API, minimum is en-US (American English)
    # iri: https://onerecord.iata.org/ns/api#hasSupportedLanguage
    hasSupportedLanguage: List[str] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedLanguage")
    # label: Supported ontology
    # comment: Supported ontologies on the server, MUST be non-versioned IRIs
    # iri: https://onerecord.iata.org/ns/api#hasSupportedOntology
    hasSupportedOntology: List[AnyUrl] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedOntology")
    # label: Supported ontology version
    # comment: Supported ontology versions on the server, MUST be versioned IRIs
    # iri: https://onerecord.iata.org/ns/api#hasSupportedOntologyVersion
    hasSupportedOntologyVersion: List[AnyUrl] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedOntologyVersion")
    # label: Server endpoint
    # comment: ONE Record API endpoint
    # iri: https://onerecord.iata.org/ns/api#hasServerEndpoint
    hasServerEndpoint: AnyUrl = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasServerEndpoint")
class Subscription(BaseModel):
    # label: has Subscriber
    # iri: https://onerecord.iata.org/ns/api#hasSubscriber
    hasSubscriber: Organization = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSubscriber")
    # iri: https://onerecord.iata.org/ns/api#hasTopicType
    hasTopicType: TopicType = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasTopicType")
    # label: Include Subscription Event Type
    # comment: An array used to indicate the specific types of notifications that the subscriber desires to receive from the publisher. The subscriber is required to specify their preferences on a per-type basis
    # iri: https://onerecord.iata.org/ns/api#includeSubscriptionEventType
    includeSubscriptionEventType: List[SubscriptionEventType] = Field(serialization_alias="https://onerecord.iata.org/ns/api#includeSubscriptionEventType")
    # label: Content type
    # comment: Content types that the subscriber wants to receive in the notifications, e.g. application/ld+json
    # iri: https://onerecord.iata.org/ns/api#hasContentType
    hasContentType: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/api#hasContentType")
    # label: notify RequestStatus Change
    # comment: Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    # iri: https://onerecord.iata.org/ns/api#notifyRequestStatusChange
    notifyRequestStatusChange: bool = Field(serialization_alias="https://onerecord.iata.org/ns/api#notifyRequestStatusChange")
    # label: Topic
    # comment: The Logistics Object type or specific Logistics Object to which the subscription belongs to e.g. https://onerecord.iata.org/Piece or https://1r.example.com/7f01363f-0c6a-4414-be48-d3692e219b91
    # iri: https://onerecord.iata.org/ns/api#hasTopic
    hasTopic: AnyUrl = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasTopic")
    # label: Expires at
    # comment: Expiry date as date time of the subscription information that supports caching but does not require the ONE Record client to store the datetime when the Subscription object was received; if not given: the information does not expire
    # iri: https://onerecord.iata.org/ns/api#expiresAt
    expiresAt: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#expiresAt")
    # label: Description
    # comment: Reason for the request (optional)
    # iri: https://onerecord.iata.org/ns/api#hasDescription
    hasDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#hasDescription")
    # label: Send LogisticsObject body
    # comment: Flag specifying if the publisher should send the whole logistics object or not in the notification object
    # iri: https://onerecord.iata.org/ns/api#sendLogisticsObjectBody
    sendLogisticsObjectBody: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/api#sendLogisticsObjectBody")
class SubscriptionEventType(str, Enum):
    """
    label: Subscription Event Type
    """
    # label: LOGISTICS_EVENT_RECEIVED
    LOGISTICS_EVENT_RECEIVED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_EVENT_RECEIVED")
    # label: LOGISTICS_OBJECT_CREATED
    LOGISTICS_OBJECT_CREATED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_CREATED")
    # label: LOGISTICS_OBJECT_UPDATED
    LOGISTICS_OBJECT_UPDATED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_UPDATED")
class SubscriptionRequest(ActionRequest):
    # label: has Subscription
    # comment: Link to the requestors Subscription object with all subscription information
    # iri: https://onerecord.iata.org/ns/api#hasSubscription
    hasSubscription: Subscription = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSubscription")
class TopicType(str, Enum):
    # label: LOGISTICS_OBJECT_IDENTIFIER
    LOGISTICS_OBJECT_IDENTIFIER = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_IDENTIFIER")
    # label: LOGISTICS_OBJECT_TYPE
    LOGISTICS_OBJECT_TYPE = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_TYPE")
class Verification(BaseModel):
    # label: has Error
    # comment: Error object(s) if the processing was not successful
    # iri: https://onerecord.iata.org/ns/api#hasError
    hasError: List[Error] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasError")
    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsObject
    hasLogisticsObject: LogisticsObject = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject")
    # label: Revision
    # comment: Revision number of the Logistics Object, starting with 0 for changing the initial revision of a Logistics Object
    # iri: https://onerecord.iata.org/ns/api#hasRevision
    hasRevision: int = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasRevision")
class VerificationRequest(ActionRequest):
    # label: has Verification
    # comment: Links to the Verification class
    # iri: https://onerecord.iata.org/ns/api#hasVerification
    hasVerification: Verification = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasVerification")