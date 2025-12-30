from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Actor import Actor
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsAgent import LogisticsAgent
from one_record_ontology.models.cargo.OtherIdentifier import OtherIdentifier


class Organization(LogisticsAgent):
    # label: basedAtLocation
    # comment: Reference to the Location where the Organization is based at or headquartered
    # iri: https://onerecord.iata.org/ns/cargo#basedAtLocation
    basedAtLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#basedAtLocation",
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
    # label: parentOrganization
    # comment: Reference to the parent Organization
    # iri: https://onerecord.iata.org/ns/cargo#parentOrganization
    parentOrganization: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#parentOrganization",
    )
    # label: subOrganization
    # comment: References to all sub-Organizations
    # iri: https://onerecord.iata.org/ns/cargo#subOrganization
    subOrganization: List[Organization] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#subOrganization",
    )
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#name"
    )
    # label: shortName
    # comment: Short name of the Organization if any
    # iri: https://onerecord.iata.org/ns/cargo#shortName
    shortName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#shortName",
    )
