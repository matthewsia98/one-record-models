from datetime import datetime
from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.ActionTimeType import ActionTimeType
from one_record_ontology.models.cargo.Actor import Actor
from one_record_ontology.models.cargo.ContactDetail import ContactDetail
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsActivity import LogisticsActivity
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.OtherIdentifier import OtherIdentifier


class LogisticsAction(LogisticsObject):
    # label: actionTimeType
    # comment: Enum stating the type of the Action
    # iri: https://onerecord.iata.org/ns/cargo#actionTimeType
    actionTimeType: Optional[ActionTimeType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#actionTimeType",
    )
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails",
    )
    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    # iri: https://onerecord.iata.org/ns/cargo#contactPersons
    contactPersons: List[Actor] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons",
    )
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
    )
    # label: performedAt
    # comment: Reference to the Location the Action was performed at
    # iri: https://onerecord.iata.org/ns/cargo#performedAt
    performedAt: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#performedAt",
    )
    # label: servedActivity
    # comment: Reference to the Activity the Action was performed for
    # iri: https://onerecord.iata.org/ns/cargo#servedActivity
    servedActivity: Optional[LogisticsActivity] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#servedActivity",
    )
    # label: actionEndTime
    # comment: DateTime holding the end time of the Action; Type is indicated through ActionType property
    # iri: https://onerecord.iata.org/ns/cargo#actionEndTime
    actionEndTime: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#actionEndTime",
    )
    # label: actionStartTime
    # comment: DateTime holding the start time of the Action; Type is indicated through ActionType property
    # iri: https://onerecord.iata.org/ns/cargo#actionStartTime
    actionStartTime: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#actionStartTime",
    )
