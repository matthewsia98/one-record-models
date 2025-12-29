from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class PackagingType(LogisticsObject):
    # label: appliedOnPieces
    # comment: Piece on which the Packaging type is applicable
    # iri: https://onerecord.iata.org/ns/cargo#appliedOnPieces
    appliedOnPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#appliedOnPieces")
    # label: typeCode
    # comment: Packaging type identifier as per UNECE Rec 21 Annex V and VI e.g. 1A - Drum, steel - Packaging material code. Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations 
    # iri: https://onerecord.iata.org/ns/cargo#typeCode
    typeCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#typeCode")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#description")