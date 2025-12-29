from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PieceGroup import PieceGroup
class VolumePieceGroup(PieceGroup):
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#stackable")