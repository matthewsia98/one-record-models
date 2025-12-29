from one_record_ontology.models.api.ActionRequest import ActionRequest
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.LogisticsEvent import LogisticsEvent
from one_record_ontology.models.api.NotificationEventType import NotificationEventType
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
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