from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Value import Value


class PieceGroup(BaseModel):
    # label: dryIceWeight
    # comment: Weight of dry ice
    # iri: https://onerecord.iata.org/ns/cargo#dryIceWeight
    dryIceWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#dryIceWeight",
    )
    # label: pieceGroupGrossWeight
    # comment: Total gross weight of the piece group
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupGrossWeight
    pieceGroupGrossWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupGrossWeight",
    )
    # label: pieceGroupCount
    # comment: Number of pieces in the piece group
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupCount
    pieceGroupCount: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupCount",
    )
    # label: pieceGroupId
    # comment: Identifier of the piece group, increasing integers
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupId
    pieceGroupId: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupId",
    )
