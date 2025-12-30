from datetime import datetime
from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Check import Check
from one_record_ontology.models.cargo.ExternalReference import ExternalReference
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Party import Party
from one_record_ontology.models.cargo.Question import Question


class CheckTemplate(LogisticsObject):
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
    )
    # label: legacyTemplate
    # comment: Reference to an ExternalReference holding a legacy template outside of ONE Record, such as a photo or pdf of a checksheet
    # iri: https://onerecord.iata.org/ns/cargo#legacyTemplate
    legacyTemplate: Optional[ExternalReference] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#legacyTemplate",
    )
    # label: questions
    # comment: References to all Questions that are part of this template
    # iri: https://onerecord.iata.org/ns/cargo#questions
    questions: List[Question] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#questions",
    )
    # label: usedInCheck
    # comment: Reference to the Check the template was used in
    # iri: https://onerecord.iata.org/ns/cargo#usedInCheck
    usedInCheck: Optional[Check] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#usedInCheck",
    )
    # label: date
    # comment: DateTime on which the CheckTemplate was released
    # iri: https://onerecord.iata.org/ns/cargo#date
    date: Optional[datetime] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#date"
    )
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#name"
    )
    # label: templatePurpose
    # comment: Purpose of the template
    # iri: https://onerecord.iata.org/ns/cargo#templatePurpose
    templatePurpose: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#templatePurpose",
    )
    # label: version
    # comment: Version of the template
    # iri: https://onerecord.iata.org/ns/cargo#version
    version: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#version"
    )
