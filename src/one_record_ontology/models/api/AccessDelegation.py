from one_record_ontology.models.cargo.Organization import Organization
from one_record_ontology.models.api.Permission import Permission
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
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