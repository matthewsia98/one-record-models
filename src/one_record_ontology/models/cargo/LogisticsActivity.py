from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class LogisticsActivity(LogisticsObject):
    # label: checkActions
    # comment: References to CheckActions performed for the Activity
    # iri: https://onerecord.iata.org/ns/cargo#checkActions
    checkActions: List[Check] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checkActions")
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails")
    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    # iri: https://onerecord.iata.org/ns/cargo#contactPersons
    contactPersons: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons")
    # label: executionStatus
    # comment: Enum stating the status of the Activity
    # iri: https://onerecord.iata.org/ns/cargo#executionStatus
    executionStatus: List[ExecutionStatus] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#executionStatus")
    # label: servedServices
    # comment: Reference to Services this Activity is executed for
    # iri: https://onerecord.iata.org/ns/cargo#servedServices
    servedServices: List[LogisticsService] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#servedServices")