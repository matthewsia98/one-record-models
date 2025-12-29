from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.Company import Company
class Carrier(Company):
    # label: airlineCode
    # comment: IATA two-character airline code
    # iri: https://onerecord.iata.org/ns/cargo#airlineCode
    airlineCode: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#airlineCode")
    # label: prefix
    # comment: IATA three-numeric airline prefix number
    # iri: https://onerecord.iata.org/ns/cargo#prefix
    prefix: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#prefix")