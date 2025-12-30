from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.CompositionType import CompositionType
from one_record_ontology.models.cargo.LoadingMaterial import LoadingMaterial
from one_record_ontology.models.cargo.LoadingUnit import LoadingUnit
from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
from one_record_ontology.models.cargo.Piece import Piece


class Composing(LogisticsAction):
    # label: composedMaterials
    # comment: References to the Materials being built-up or broken-down
    # iri: https://onerecord.iata.org/ns/cargo#composedMaterials
    composedMaterials: List[LoadingMaterial] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#composedMaterials",
    )
    # label: composedPieces
    # comment: References to the Pieces being built-up or broken-down
    # iri: https://onerecord.iata.org/ns/cargo#composedPieces
    composedPieces: List[Piece] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#composedPieces",
    )
    # label: compositionType
    # comment: Enum stating whether the CompositionAction describes build-up or break-down
    # iri: https://onerecord.iata.org/ns/cargo#compositionType
    compositionType: Optional[CompositionType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#compositionType",
    )
    # label: onLoadingUnit
    # comment: Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    # iri: https://onerecord.iata.org/ns/cargo#loadingUnit
    loadingUnit: Optional[LoadingUnit] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingUnit",
    )
