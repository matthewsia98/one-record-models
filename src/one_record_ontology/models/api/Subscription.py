from one_record_ontology.models.api.SubscriptionEventType import SubscriptionEventType
from one_record_ontology.models.api.TopicType import TopicType
from one_record_ontology.models.cargo.Organization import Organization
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
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