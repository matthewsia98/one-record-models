from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class CheckTemplate(LogisticsObject):
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: legacyTemplate
    # comment: Reference to an ExternalReference holding a legacy template outside of ONE Record, such as a photo or pdf of a checksheet
    # iri: https://onerecord.iata.org/ns/cargo#legacyTemplate
    legacyTemplate: List[ExternalReference] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#legacyTemplate")
    # label: questions
    # comment: References to all Questions that are part of this template
    # iri: https://onerecord.iata.org/ns/cargo#questions
    questions: List[Question] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#questions")
    # label: usedInCheck
    # comment: Reference to the Check the template was used in
    # iri: https://onerecord.iata.org/ns/cargo#usedInCheck
    usedInCheck: List[Check] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#usedInCheck")
    # label: date
    # comment: DateTime on which the CheckTemplate was released
    # iri: https://onerecord.iata.org/ns/cargo#date
    date: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#date")
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#name")
    # label: templatePurpose
    # comment: Purpose of the template
    # iri: https://onerecord.iata.org/ns/cargo#templatePurpose
    templatePurpose: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#templatePurpose")
    # label: version
    # comment: Version of the template
    # iri: https://onerecord.iata.org/ns/cargo#version
    version: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#version")