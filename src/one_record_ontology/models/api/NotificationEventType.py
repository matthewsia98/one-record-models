from enum import Enum

from rdflib import URIRef


class NotificationEventType(str, Enum):
    """
    label: Notification Event Type
    """

    # label: ACCESS_DELEGATION_REQUEST_ACCEPTED
    ACCESS_DELEGATION_REQUEST_ACCEPTED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_ACCEPTED"
    )
    # label: ACCESS_DELEGATION_REQUEST_FAILED
    ACCESS_DELEGATION_REQUEST_FAILED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_FAILED"
    )
    # label: ACCESS_DELEGATION_REQUEST_PENDING
    ACCESS_DELEGATION_REQUEST_PENDING = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_PENDING"
    )
    # label: ACCESS_DELEGATION_REQUEST_REJECTED
    ACCESS_DELEGATION_REQUEST_REJECTED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_REJECTED"
    )
    # label: ACCESS_DELEGATION_REQUEST_REVOKED
    ACCESS_DELEGATION_REQUEST_REVOKED = URIRef(
        "https://onerecord.iata.org/ns/api#ACCESS_DELEGATION_REQUEST_REVOKED"
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
    # label: CHANGE_REQUEST_PENDING
    # comment: :EventType for pending :ChangeRequests.
    CHANGE_REQUEST_PENDING = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_PENDING"
    )
    # label: CHANGE_REQUEST_PENDING
    CHANGE_REQUEST_REJECTED = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_REJECTED"
    )
    # label: CHANGE_REQUEST_REVOKED
    CHANGE_REQUEST_REVOKED = URIRef(
        "https://onerecord.iata.org/ns/api#CHANGE_REQUEST_REVOKED"
    )
    # label: LOGISTICS_EVENT_RECEIVED
    LOGISTICS_EVENT_RECEIVED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_EVENT_RECEIVED"
    )
    # label: LOGISTICS_OBJECT_CREATED
    LOGISTICS_OBJECT_CREATED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_CREATED"
    )
    # label: LOGISTICS_OBJECT_UPDATED
    LOGISTICS_OBJECT_UPDATED = URIRef(
        "https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_UPDATED"
    )
    # label: SUBSCRIPTION_REQUEST_ACCEPTED
    SUBSCRIPTION_REQUEST_ACCEPTED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_ACCEPTED"
    )
    # label: SUBSCRIPTION_REQUEST_FAILED
    SUBSCRIPTION_REQUEST_FAILED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_FAILED"
    )
    # label: SUBSCRIPTION_REQUEST_PENDING
    SUBSCRIPTION_REQUEST_PENDING = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_PENDING"
    )
    # label: SUBSCRIPTION_REQUEST_REJECTED
    SUBSCRIPTION_REQUEST_REJECTED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_REJECTED"
    )
    # label: SUBSCRIPTION_REQUEST_REVOKED
    SUBSCRIPTION_REQUEST_REVOKED = URIRef(
        "https://onerecord.iata.org/ns/api#SUBSCRIPTION_REQUEST_REVOKED"
    )
