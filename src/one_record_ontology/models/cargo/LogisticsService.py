from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class LogisticsService(LogisticsObject):
    # label: activitySequences
    # comment: Information about the Activities that are part of the Service and their sequence
    # iri: https://onerecord.iata.org/ns/cargo#activitySequences
    activitySequences: List[ActivitySequence] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#activitySequences")
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails")
    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    # iri: https://onerecord.iata.org/ns/cargo#contactPersons
    contactPersons: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons")