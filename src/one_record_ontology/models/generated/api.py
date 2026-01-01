"""
This file was automatically generated from the ONE Record API ontology.

Ontology source: https://onerecord.iata.org/ns/api/ontology.ttl
Ontology version: https://onerecord.iata.org/ns/api/2.2.0
Generated on: 2026-01-01T00:21:35.928985+00:00

DO NOT EDIT MANUALLY.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, ClassVar, List, Union

from pydantic import AnyUrl, Field
from pydantic.json_schema import SkipJsonSchema
from rdflib import URIRef

from one_record_ontology.models.base_model import OneRecordBaseModel
from one_record_ontology.models.generated.cargo import (
    LogisticsEvent,
    LogisticsObject,
    Organization,
)


class NotificationEventType(str, Enum):
    # label: SUBSCRIPTION_REQUEST_PENDING
    SUBSCRIPTION_REQUEST_PENDING = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_PENDING"
    )

    # label: LOGISTICS_OBJECT_UPDATED
    LOGISTICS_OBJECT_UPDATED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_UPDATED"
    )

    # label: SUBSCRIPTION_REQUEST_FAILED
    SUBSCRIPTION_REQUEST_FAILED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_FAILED"
    )

    # label: CHANGE_REQUEST_PENDING
    CHANGE_REQUEST_REJECTED = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_REJECTED"
    )

    # label: CHANGE_REQUEST_REVOKED
    CHANGE_REQUEST_REVOKED = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_REVOKED"
    )

    # label: SUBSCRIPTION_REQUEST_REVOKED
    SUBSCRIPTION_REQUEST_REVOKED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_REVOKED"
    )

    # label: CHANGE_REQUEST_ACCEPTED
    # comment: :EventType for accepted :ChangeRequests
    CHANGE_REQUEST_ACCEPTED = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_ACCEPTED"
    )

    # label: CHANGE_REQUEST_FAILED
    # comment: :EventType for failed :ChangeRequests.
    CHANGE_REQUEST_FAILED = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_FAILED"
    )

    # label: LOGISTICS_EVENT_RECEIVED
    LOGISTICS_EVENT_RECEIVED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_EVENT_RECEIVED"
    )

    # label: CHANGE_REQUEST_PENDING
    # comment: :EventType for pending :ChangeRequests.
    CHANGE_REQUEST_PENDING = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_PENDING"
    )

    # label: ACCESS_DELEGATION_REQUEST_PENDING
    ACCESS_DELEGATION_REQUEST_PENDING = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_PENDING"
    )

    # label: VERIFICATION_REQUEST_REVOKED
    VERIFICATION_REQUEST_REVOKED = URIRef(
        "https://onerecord.iata.org/ns/api#VERIFICATION_REQUEST_REVOKED"
    )

    # label: VERIFICATION_REQUEST_FAILED
    VERIFICATION_REQUEST_FAILED = URIRef(
        "https://onerecord.iata.org/ns/api#VERIFICATION_REQUEST_FAILED"
    )

    # label: LOGISTICS_OBJECT_CREATED
    LOGISTICS_OBJECT_CREATED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_CREATED"
    )

    # label: VERIFICATION_REQUEST_REJECTED
    VERIFICATION_REQUEST_REJECTED = URIRef(
        "https://onerecord.iata.org/ns/api#VERIFICATION_REQUEST_REJECTED"
    )

    # label: SUBSCRIPTION_REQUEST_ACCEPTED
    SUBSCRIPTION_REQUEST_ACCEPTED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_ACCEPTED"
    )

    # label: LOGISTICS_OBJECT_ACCESS_GRANTED
    LOGISTICS_OBJECT_ACCESS_GRANTED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_ACCESS_GRANTED"
    )

    # label: VERIFICATION_REQUEST_PENDING
    VERIFICATION_REQUEST_PENDING = URIRef(
        "https://onerecord.iata.org/ns/api#VERIFICATION_REQUEST_PENDING"
    )

    # label: SUBSCRIPTION_REQUEST_REJECTED
    SUBSCRIPTION_REQUEST_REJECTED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_REJECTED"
    )

    # label: ACCESS_DELEGATION_REQUEST_ACCEPTED
    ACCESS_DELEGATION_REQUEST_ACCEPTED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_ACCEPTED"
    )

    # label: VERIFICATION_REQUEST_ACKNOWLEDGED
    VERIFICATION_REQUEST_ACKNOWLEDGED = URIRef(
        "https://onerecord.iata.org/ns/api#VERIFICATION_REQUEST_ACKNOWLEDGED"
    )

    # label: ACCESS_DELEGATION_REQUEST_REJECTED
    ACCESS_DELEGATION_REQUEST_REJECTED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_REJECTED"
    )

    # label: LOGISTICS_OBJECT_AVAILABLE
    LOGISTICS_OBJECT_AVAILABLE = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_AVAILABLE"
    )

    # label: ACCESS_DELEGATION_REQUEST_FAILED
    ACCESS_DELEGATION_REQUEST_FAILED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_FAILED"
    )

    # label: ACCESS_DELEGATION_REQUEST_REVOKED
    ACCESS_DELEGATION_REQUEST_REVOKED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_REVOKED"
    )


class PatchOperation(str, Enum):
    # label: DELETE
    DELETE = URIRef("https://onerecord.iata.org/ns/api#DELETE")

    # label: ADD
    # comment: Defines a :PatchOperation to be an operation that adds new triples.
    ADD = URIRef("https://onerecord.iata.org/ns/api#ADD")


class Permission(str, Enum):
    # label: GET_LOGISTICS_EVENT
    # comment: :Permission to get a :LogisticsEvent
    GET_LOGISTICS_EVENT = URIRef(
        "https://onerecord.iata.org/ns/api#GET_LOGISTICS_EVENT"
    )

    # label: GET_LOGISTICS_OBJECT
    # comment: :Permission to get a :LogisticsObject
    GET_LOGISTICS_OBJECT = URIRef(
        "https://onerecord.iata.org/ns/api#GET_LOGISTICS_OBJECT"
    )

    # label: POST_LOGISTICS_EVENT
    # comment: :Permission to add a logistics event.
    POST_LOGISTICS_EVENT = URIRef(
        "https://onerecord.iata.org/ns/api#POST_LOGISTICS_EVENT"
    )

    # label: PATCH_LOGISTICS_OBJECT
    PATCH_LOGISTICS_OBJECT = URIRef(
        "https://onerecord.iata.org/ns/api#PATCH_LOGISTICS_OBJECT"
    )


class RequestStatus(str, Enum):
    # label: REQUEST_REVOKED
    REQUEST_REVOKED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_REVOKED")

    # label: REQUEST_ACCEPTED
    REQUEST_ACCEPTED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_ACCEPTED")

    # label: REQUEST_ACKNOWLEDGED
    REQUEST_ACKNOWLEDGED = URIRef(
        "https://onerecord.iata.org/ns/api#REQUEST_ACKNOWLEDGED"
    )

    # label: REQUEST_FAILED
    REQUEST_FAILED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_FAILED")

    # label: REQUEST_PENDING
    REQUEST_PENDING = URIRef("https://onerecord.iata.org/ns/api#REQUEST_PENDING")

    # label: REQUEST_REJECTED
    REQUEST_REJECTED = URIRef("https://onerecord.iata.org/ns/api#REQUEST_REJECTED")


class SubscriptionEventType(str, Enum):
    # label: LOGISTICS_OBJECT_UPDATED
    LOGISTICS_OBJECT_UPDATED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_UPDATED"
    )

    # label: LOGISTICS_EVENT_RECEIVED
    LOGISTICS_EVENT_RECEIVED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_EVENT_RECEIVED"
    )

    # label: LOGISTICS_OBJECT_CREATED
    LOGISTICS_OBJECT_CREATED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_CREATED"
    )


class TopicType(str, Enum):
    # label: LOGISTICS_OBJECT_IDENTIFIER
    LOGISTICS_OBJECT_IDENTIFIER = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_IDENTIFIER"
    )

    # label: LOGISTICS_OBJECT_TYPE
    LOGISTICS_OBJECT_TYPE = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_TYPE"
    )


class AccessDelegation(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/api#AccessDelegation"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#AccessDelegation"),
    ]

    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    hasLogisticsObject: List[LogisticsObject] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject",
        default_factory=list,
    )

    # label: has Permission
    hasPermission: List[Permission] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasPermission",
        default_factory=list,
    )

    # label: is requested for
    isRequestedFor: List[Organization] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isRequestedFor",
        default_factory=list,
    )

    # label: Description
    # comment: Reason for the request (optional)
    hasDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasDescription",
        default=None,
    )

    # label: notify RequestStatus Change
    # comment: Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    notifyRequestStatusChange: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#notifyRequestStatusChange",
        default=None,
    )


class ActionRequest(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#ActionRequest")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#ActionRequest"),
    ]

    # label: has Error
    # comment: Error object(s) if the processing was not successful
    hasError: List[Error] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasError",
        default_factory=list,
    )

    # label: has Request Status
    hasRequestStatus: Union[RequestStatus, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasRequestStatus",
        default=None,
    )

    # label: is Requested By
    # comment: Organization Identifier that represents the Organization that has requested the action
    isRequestedBy: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isRequestedBy",
        default=None,
    )

    # label: is revoked by
    isRevokedBy: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isRevokedBy",
        default=None,
    )

    # label: Requested at
    # comment: Datetime when the request was created
    isRequestedAt: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isRequestedAt",
        default=None,
    )

    # label: Revoked at
    # comment: The datetime when the action request was revoked.
    isRevokedAt: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isRevokedAt",
        default=None,
    )


class AuditTrail(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#AuditTrail")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#AuditTrail"),
    ]

    # label: has Action Request
    # comment: Link any type of Action Request
    hasActionRequest: List[ActionRequest] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasActionRequest",
        default_factory=list,
    )

    # label: Latest revision
    # comment: Latest revision of the Logistics Object. Starting with revision 0
    hasLatestRevision: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLatestRevision",
        default=None,
    )


class Change(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#Change")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#Change"),
    ]

    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    hasLogisticsObject: Union[LogisticsObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject",
        default=None,
    )

    # label: has Operation
    # comment: Operation(s) to apply as PATCH on a Logistics Object
    hasOperation: List[Operation] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasOperation",
        default_factory=list,
    )

    # label: has Verification Request
    # comment: Link to the Verification Request
    hasVerificationRequest: List[VerificationRequest] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasVerificationRequest",
        default_factory=list,
    )

    # label: Description
    # comment: Reason for the request (optional)
    hasDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasDescription",
        default=None,
    )

    # label: Revision
    # comment: Revision number of the Logistics Object, starting with 0 for changing the initial revision of a Logistics Object
    hasRevision: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasRevision",
        default=None,
    )

    # label: notify RequestStatus Change
    # comment: Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    notifyRequestStatusChange: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#notifyRequestStatusChange",
        default=None,
    )


class Collection(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#Collection")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#Collection"),
    ]

    # label: has Item
    # comment: Item that is contained in a collection
    hasItem: List[Any] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasItem",
        default_factory=list,
    )

    # label: Total items
    # comment: The number of total items contained in a collection
    hasTotalItems: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasTotalItems",
        default=None,
    )


class Error(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#Error")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#Error"),
    ]

    # label: has Error Detail
    # comment: Error details
    hasErrorDetail: List[ErrorDetail] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasErrorDetail",
        default_factory=list,
    )

    # label: Title
    # comment: Short summary of the error
    hasTitle: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasTitle",
        default=None,
    )


class ErrorDetail(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#ErrorDetail")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#ErrorDetail"),
    ]

    # label: Code
    # comment: Error code is a numeric or alphanumeric code that can be used to determine the source of the error and why it occured.
    hasCode: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasCode",
        default=None,
    )

    # label: Message
    # comment: Message that describes the error
    hasMessage: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasMessage",
        default=None,
    )

    # label: Property
    # comment: Property of the object for which the error applies in IRI format, i.e. https://onerecord.iata.org/ns/cargo#hasVolumetricWeight
    hasProperty: Union[AnyUrl, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasProperty",
        default=None,
    )

    # label: Resource
    # comment: URI of the object where the error occurred
    hasResource: Union[AnyUrl, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasResource",
        default=None,
    )


class Notification(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#Notification")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#Notification"),
    ]

    # label: has Event Type
    hasEventType: Union[NotificationEventType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasEventType",
        default=None,
    )

    # label: has Logistics Event
    # comment: A reference to a cargo LogisticsEvent
    hasLogisticsEvent: List[LogisticsEvent] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsEvent",
        default_factory=list,
    )

    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    hasLogisticsObject: Union[LogisticsObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject",
        default=None,
    )

    # label: is triggered by
    # comment: Optional URI to the ChangeRequest that triggered a Notification if the eventType is one of CHANGE_REQUEST_ACCEPTED, CHANGE_REQUEST_REJECT, or CHANGE_REQUEST_FAILED
    isTriggeredBy: Union[ActionRequest, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#isTriggeredBy",
        default=None,
    )

    # label: Changed property
    # comment: List of all changed properties as IRIs after a ChangeRequest was successfully applied, e.g. [https://onerecord.iata.org/ns/cargo#hasVolumetricWeight, https://onerecord.iata.org/ns/cargo/#hasGoodsDescription]
    hasChangedProperty: List[AnyUrl] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasChangedProperty",
        default_factory=list,
    )

    # label: has Logistics Object Type
    # comment: The type of cargo:LogisticsObject in the notification e.g. https://onerecord.iata.org/ns/cargo#Piece
    hasLogisticsObjectType: Union[AnyUrl, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObjectType",
        default=None,
    )


class Operation(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#Operation")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#Operation"),
    ]

    o: Union[OperationObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#o",
        default=None,
    )

    op: Union[PatchOperation, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#op",
        default=None,
    )

    # label: p
    # comment: Operations objects must have exactly one p, predicate, member. The value of this member must be an URI, e.g. https://onerecord.iata.org/ns/cargo#hasGoodsDescription
    p: Union[AnyUrl, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#p",
        default=None,
    )

    # label: s
    # comment: Operation objects MUST have exactly one "s", subject, member. The value of this member MUST be one of IRI or blank node.
    s: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#s",
        default=None,
    )


class OperationObject(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/api#OperationObject"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#OperationObject"),
    ]

    # label: Datatype
    # comment: Data type of the field to update, must be a valid URI, e.g. http://www.w3.org/2001/XMLSchema#int
    hasDatatype: Union[AnyUrl, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasDatatype",
        default=None,
    )

    # label: Value
    # comment: Updated value for the field
    hasValue: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasValue",
        default=None,
    )


class ServerInformation(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/api#ServerInformation"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#ServerInformation"),
    ]

    # label: has Data Holder
    # comment: The data holder of the servers data.
    hasDataHolder: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasDataHolder",
        default=None,
    )

    # label: Supported encoding
    # comment: Optional list of supported encodings of the ONE Record server, e.g. gzip
    hasSupportedEncoding: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedEncoding",
        default_factory=list,
    )

    # label: Supported API version
    # comment: Supported ONE Record API versions by the server, MUST include at least one supported version.
    hasSupportedApiVersion: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedApiVersion",
        default_factory=list,
    )

    # label: Supported content type
    # comment: Supported content types of the server, MUST contain at least application/ld+json
    hasSupportedContentType: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedContentType",
        default_factory=list,
    )

    # label: Supported language
    # comment: Supported languages of the ONE Record API, minimum is en-US (American English)
    hasSupportedLanguage: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedLanguage",
        default_factory=list,
    )

    # label: Supported ontology
    # comment: Supported ontologies on the server, MUST be non-versioned IRIs
    hasSupportedOntology: List[AnyUrl] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedOntology",
        default_factory=list,
    )

    # label: Supported ontology version
    # comment: Supported ontology versions on the server, MUST be versioned IRIs
    hasSupportedOntologyVersion: List[AnyUrl] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedOntologyVersion",
        default_factory=list,
    )

    # label: Server endpoint
    # comment: ONE Record API endpoint
    hasServerEndpoint: Union[AnyUrl, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasServerEndpoint",
        default=None,
    )


class Subscription(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#Subscription")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#Subscription"),
    ]

    # label: has Subscriber
    hasSubscriber: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSubscriber",
        default=None,
    )

    hasTopicType: Union[TopicType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasTopicType",
        default=None,
    )

    # label: Include Subscription Event Type
    # comment: An array used to indicate the specific types of notifications that the subscriber desires to receive from the publisher. The subscriber is required to specify their preferences on a per-type basis
    includeSubscriptionEventType: List[SubscriptionEventType] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#includeSubscriptionEventType",
        default_factory=list,
    )

    # label: Content type
    # comment: Content types that the subscriber wants to receive in the notifications, e.g. application/ld+json
    hasContentType: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasContentType",
        default_factory=list,
    )

    # label: notify RequestStatus Change
    # comment: Flag specifying if the requestor wants to receive Notification from the publisher when the status of an action request changed, default=FALSE
    notifyRequestStatusChange: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#notifyRequestStatusChange",
        default=None,
    )

    # label: Topic
    # comment: The Logistics Object type or specific Logistics Object to which the subscription belongs to e.g. https://onerecord.iata.org/Piece or https://1r.example.com/7f01363f-0c6a-4414-be48-d3692e219b91
    hasTopic: Union[AnyUrl, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasTopic",
        default=None,
    )

    # label: Expires at
    # comment: Expiry date as date time of the subscription information that supports caching but does not require the ONE Record client to store the datetime when the Subscription object was received; if not given: the information does not expire
    expiresAt: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#expiresAt",
        default=None,
    )

    # label: Description
    # comment: Reason for the request (optional)
    hasDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasDescription",
        default=None,
    )

    # label: Send LogisticsObject body
    # comment: Flag specifying if the publisher should send the whole logistics object or not in the notification object
    sendLogisticsObjectBody: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#sendLogisticsObjectBody",
        default=None,
    )


class Verification(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#Verification")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#Verification"),
    ]

    # label: has Error
    # comment: Error object(s) if the processing was not successful
    hasError: List[Error] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasError",
        default_factory=list,
    )

    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    hasLogisticsObject: Union[LogisticsObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject",
        default=None,
    )

    # label: Revision
    # comment: Revision number of the Logistics Object, starting with 0 for changing the initial revision of a Logistics Object
    hasRevision: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasRevision",
        default=None,
    )


class AccessDelegationRequest(ActionRequest):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/api#AccessDelegationRequest"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#AccessDelegationRequest"),
        URIRef("https://onerecord.iata.org/ns/api#ActionRequest"),
    ]

    # label: has Access Delegation
    hasAccessDelegation: Union[AccessDelegation, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasAccessDelegation",
        default=None,
    )


class ChangeRequest(ActionRequest):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/api#ChangeRequest")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#ChangeRequest"),
        URIRef("https://onerecord.iata.org/ns/api#ActionRequest"),
    ]

    # label: has Change
    # comment: Contains submitted Change object
    hasChange: Union[Change, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasChange",
        default=None,
    )


class SubscriptionRequest(ActionRequest):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/api#SubscriptionRequest"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#SubscriptionRequest"),
        URIRef("https://onerecord.iata.org/ns/api#ActionRequest"),
    ]

    # label: has Subscription
    # comment: Link to the requestors Subscription object with all subscription information
    hasSubscription: Union[Subscription, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSubscription",
        default=None,
    )


class VerificationRequest(ActionRequest):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/api#VerificationRequest"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/api#VerificationRequest"),
        URIRef("https://onerecord.iata.org/ns/api#ActionRequest"),
    ]

    # label: has Verification
    # comment: Links to the Verification class
    hasVerification: Union[Verification, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasVerification",
        default=None,
    )


for _cls in list(locals().values()):
    if isinstance(_cls, type) and issubclass(_cls, OneRecordBaseModel):
        result = _cls.model_rebuild()
        if result is False:
            raise RuntimeError(f"Failed to rebuild model for class {_cls.__name__}")
