from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Actor import Actor
from one_record_ontology.models.cargo.ContactDetail import ContactDetail
from one_record_ontology.models.cargo.ContactRole import ContactRole
from one_record_ontology.models.cargo.ExternalReference import ExternalReference


class Person(Actor):
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails",
    )
    # label: contactRole
    # comment: Contact type - e.g. Emergency contact, Customs contact, Customer contact
    # iri: https://onerecord.iata.org/ns/cargo#contactRole
    contactRole: Optional[ContactRole] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactRole",
    )
    # label: documents
    # comment: Linked documents to the person, e.g. driver's license, ID, etc.
    # iri: https://onerecord.iata.org/ns/cargo#documents
    documents: List[ExternalReference] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#documents",
    )
    # label: department
    # comment: Department / Division / Unit
    # iri: https://onerecord.iata.org/ns/cargo#department
    department: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#department",
    )
    # label: employeeId
    # comment: Employee ID
    # iri: https://onerecord.iata.org/ns/cargo#employeeId
    employeeId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#employeeId",
    )
    # label: firstName
    # comment: First name / given name
    # iri: https://onerecord.iata.org/ns/cargo#firstName
    firstName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#firstName",
    )
    # label: jobTitle
    # comment: Job title / position
    # iri: https://onerecord.iata.org/ns/cargo#jobTitle
    jobTitle: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#jobTitle"
    )
    # label: lastName
    # comment: Last name / family name / surname
    # iri: https://onerecord.iata.org/ns/cargo#lastName
    lastName: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#lastName"
    )
    # label: middleName
    # comment: Middle name/ other name
    # iri: https://onerecord.iata.org/ns/cargo#middleName
    middleName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#middleName",
    )
    # label: salutation
    # comment: Salutation
    # iri: https://onerecord.iata.org/ns/cargo#salutation
    salutation: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#salutation",
    )
