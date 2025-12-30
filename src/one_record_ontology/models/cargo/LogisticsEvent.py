from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Actor import Actor
from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.EventTimeType import EventTimeType
from one_record_ontology.models.cargo.ExternalReference import ExternalReference
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Organization import Organization
from one_record_ontology.models.cargo.Party import Party


class LogisticsEvent(BaseModel):
    # label: eventCode
    # comment: Movement or milestone code. Can hold a named individual of the StatusCode core code list (corresponding to cXML code list 1.18), but can also be referring to different code lists.
    # iri: https://onerecord.iata.org/ns/cargo#eventCode
    eventCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventCode",
    )
    # label: eventFor
    # comment: Refers to the URI of the linked object(s)
    # iri: https://onerecord.iata.org/ns/cargo#eventFor
    eventFor: Optional[LogisticsObject] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#eventFor"
    )
    # label: eventLocation
    # comment: Location of event
    # iri: https://onerecord.iata.org/ns/cargo#eventLocation
    eventLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventLocation",
    )
    # label: eventTimeType
    # comment: Indicates type of event e.g.  Scheduled, Estimated, Actual
    # iri: https://onerecord.iata.org/ns/cargo#eventTimeType
    eventTimeType: Optional[EventTimeType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventTimeType",
    )
    # label: externalReferences
    # comment: References to all associated ExternalReferences
    # iri: https://onerecord.iata.org/ns/cargo#externalReferences
    externalReferences: List[ExternalReference] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#externalReferences",
    )
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
    )
    # label: recordingActor
    # comment: Reference to the Actor recording the LogisticsEvent
    # iri: https://onerecord.iata.org/ns/cargo#recordingActor
    recordingActor: Optional[Actor] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#recordingActor",
    )
    # label: recordingOrganization
    # comment: Organization recording the LogisticsEvent
    # iri: https://onerecord.iata.org/ns/cargo#recordingOrganization
    recordingOrganization: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#recordingOrganization",
    )
    # label: creationDate
    # comment: DateTime at which the LogisticsEvent was posted
    # iri: https://onerecord.iata.org/ns/cargo#creationDate
    creationDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#creationDate",
    )
    # label: eventDate
    # comment: Date and time of the event
    # iri: https://onerecord.iata.org/ns/cargo#eventDate
    eventDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventDate",
    )
    # label: eventName
    # comment: If no EventCode provided, event name - e.g. Security clearance
    # iri: https://onerecord.iata.org/ns/cargo#eventName
    eventName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventName",
    )
    # label: partialEventIndicator
    # comment: Boolean indicating that the LogisticsEvent is only applicable for parts of the LogisticObject it was recorded for, for example for some Pieces of a Shipment
    # iri: https://onerecord.iata.org/ns/cargo#partialEventIndicator
    partialEventIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#partialEventIndicator",
    )
