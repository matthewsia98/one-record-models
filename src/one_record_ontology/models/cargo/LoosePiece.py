from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.PieceGroup import PieceGroup
from one_record_ontology.models.cargo.Value import Value


class LoosePiece(PieceGroup):
    # label: pieceHeight
    # comment: Height of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceHeight
    pieceHeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceHeight",
    )
    # label: pieceLength
    # comment: Length of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceLength
    pieceLength: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceLength",
    )
    # label: pieceWeight
    # comment: Weight of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceWeight
    pieceWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWeight",
    )
    # label: pieceWidth
    # comment: Width of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceWidth
    pieceWidth: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWidth",
    )
    # label: totalVolume
    # comment: Total volume fo the volume piece group
    # iri: https://onerecord.iata.org/ns/cargo#totalVolume
    totalVolume: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalVolume",
    )
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#stackable",
    )
    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#turnable
    turnable: Optional[bool] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#turnable"
    )
