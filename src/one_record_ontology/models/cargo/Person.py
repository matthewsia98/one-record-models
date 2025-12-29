from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.Actor import Actor
class Person(Actor):
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails")
    # label: contactRole
    # comment: Contact type - e.g. Emergency contact, Customs contact, Customer contact
    # iri: https://onerecord.iata.org/ns/cargo#contactRole
    contactRole: List[ContactRole] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactRole")
    # label: documents
    # comment: Linked documents to the person, e.g. driver's license, ID, etc.
    # iri: https://onerecord.iata.org/ns/cargo#documents
    documents: List[ExternalReference] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#documents")
    # label: department
    # comment: Department / Division / Unit
    # iri: https://onerecord.iata.org/ns/cargo#department
    department: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#department")
    # label: employeeId
    # comment: Employee ID
    # iri: https://onerecord.iata.org/ns/cargo#employeeId
    employeeId: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#employeeId")
    # label: firstName
    # comment: First name / given name
    # iri: https://onerecord.iata.org/ns/cargo#firstName
    firstName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#firstName")
    # label: jobTitle
    # comment: Job title / position
    # iri: https://onerecord.iata.org/ns/cargo#jobTitle
    jobTitle: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#jobTitle")
    # label: lastName
    # comment: Last name / family name / surname
    # iri: https://onerecord.iata.org/ns/cargo#lastName
    lastName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#lastName")
    # label: middleName
    # comment: Middle name/ other name
    # iri: https://onerecord.iata.org/ns/cargo#middleName
    middleName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#middleName")
    # label: salutation
    # comment: Salutation 
    # iri: https://onerecord.iata.org/ns/cargo#salutation
    salutation: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#salutation")