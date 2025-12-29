from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
class Composing(LogisticsAction):
    # label: composedMaterials
    # comment: References to the Materials being built-up or broken-down
    # iri: https://onerecord.iata.org/ns/cargo#composedMaterials
    composedMaterials: List[LoadingMaterial] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#composedMaterials")
    # label: composedPieces
    # comment: References to the Pieces being built-up or broken-down
    # iri: https://onerecord.iata.org/ns/cargo#composedPieces
    composedPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#composedPieces")
    # label: compositionType
    # comment: Enum stating whether the CompositionAction describes build-up or break-down
    # iri: https://onerecord.iata.org/ns/cargo#compositionType
    compositionType: List[CompositionType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#compositionType")
    # label: onLoadingUnit
    # comment: Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    # iri: https://onerecord.iata.org/ns/cargo#loadingUnit
    loadingUnit: List[LoadingUnit] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingUnit")