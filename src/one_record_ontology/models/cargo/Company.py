from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.Organization import Organization
class Company(Organization):
    # label: iataCargoAgentCode
    # comment: IATA accredited cargo agent 7 digit number
    # iri: https://onerecord.iata.org/ns/cargo#iataCargoAgentCode
    iataCargoAgentCode: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentCode")
    # label: iataCargoAgentLocationIdentifier
    # comment: IATA CASS cargo agent 4 digit branch number / location identifier
    # iri: https://onerecord.iata.org/ns/cargo#iataCargoAgentLocationIdentifier
    iataCargoAgentLocationIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentLocationIdentifier")