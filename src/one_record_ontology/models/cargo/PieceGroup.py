from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class PieceGroup(BaseModel):
    # label: dryIceWeight
    # comment: Weight of dry ice
    # iri: https://onerecord.iata.org/ns/cargo#dryIceWeight
    dryIceWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#dryIceWeight")
    # label: pieceGroupGrossWeight
    # comment: Total gross weight of the piece group
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupGrossWeight
    pieceGroupGrossWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupGrossWeight")
    # label: pieceGroupCount
    # comment: Number of pieces in the piece group
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupCount
    pieceGroupCount: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupCount")
    # label: pieceGroupId
    # comment: Identifier of the piece group, increasing integers
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupId
    pieceGroupId: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupId")