from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Piece import Piece
from one_record_ontology.models.cargo.Value import Value


class LineItemPackage(BaseModel):
    # label: packageGrossWeight
    # comment: Information about the total weight of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageGrossWeight
    packageGrossWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageGrossWeight",
    )
    # label: packageVolume
    # comment: Information about the total volume of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageVolume
    packageVolume: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageVolume",
    )
    # label: pieceReferences
    # comment: References to Pieces for which a rate applies
    # iri: https://onerecord.iata.org/ns/cargo#pieceReferences
    pieceReferences: List[Piece] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceReferences",
    )
    # label: packageSlac
    # comment: Integer holding the total slac of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageSlac
    packageSlac: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageSlac",
    )
