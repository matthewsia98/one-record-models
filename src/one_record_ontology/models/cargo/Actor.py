from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsAgent import LogisticsAgent
class Actor(LogisticsAgent):
    # label: associatedOrganization
    # comment: Reference to the Organization the Actor is associated with
    # iri: https://onerecord.iata.org/ns/cargo#associatedOrganization
    associatedOrganization: List[Organization] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#associatedOrganization")