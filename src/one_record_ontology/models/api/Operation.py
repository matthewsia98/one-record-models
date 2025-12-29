from one_record_ontology.models.api.PatchOperation import PatchOperation
from one_record_ontology.models.api.OperationObject import OperationObject
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Operation(BaseModel):
    # iri: https://onerecord.iata.org/ns/api#o
    o: OperationObject = Field(serialization_alias="https://onerecord.iata.org/ns/api#o")
    # iri: https://onerecord.iata.org/ns/api#op
    op: PatchOperation = Field(serialization_alias="https://onerecord.iata.org/ns/api#op")
    # label: p
    # comment: Operations objects must have exactly one p, predicate, member. The value of this member must be an URI, e.g. https://onerecord.iata.org/ns/cargo#hasGoodsDescription
    # iri: https://onerecord.iata.org/ns/api#p
    p: AnyUrl = Field(serialization_alias="https://onerecord.iata.org/ns/api#p")
    # label: s
    # comment: Operation objects MUST have exactly one "s", subject, member. The value of this member MUST be one of IRI or blank node.
    # iri: https://onerecord.iata.org/ns/api#s
    s: str = Field(serialization_alias="https://onerecord.iata.org/ns/api#s")