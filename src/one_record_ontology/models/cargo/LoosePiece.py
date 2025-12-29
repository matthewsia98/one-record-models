from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PieceGroup import PieceGroup
class LoosePiece(PieceGroup):
    # label: pieceHeight
    # comment: Height of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceHeight
    pieceHeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceHeight")
    # label: pieceLength
    # comment: Length of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceLength
    pieceLength: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceLength")
    # label: pieceWeight
    # comment: Weight of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceWeight
    pieceWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWeight")
    # label: pieceWidth
    # comment: Width of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceWidth
    pieceWidth: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWidth")
    # label: totalVolume
    # comment: Total volume fo the volume piece group
    # iri: https://onerecord.iata.org/ns/cargo#totalVolume
    totalVolume: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#totalVolume")
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#stackable")
    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#turnable
    turnable: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#turnable")