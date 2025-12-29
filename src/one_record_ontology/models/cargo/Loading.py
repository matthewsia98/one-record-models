from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
class Loading(LogisticsAction):
    # label: loadedMaterials
    # comment: References to Materials onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#loadedMaterials
    loadedMaterials: List[LoadingMaterial] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadedMaterials")
    # label: loadedPieces
    # comment: References to Pieces onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#loadedPieces
    loadedPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadedPieces")
    # label: loadedUnits
    # comment: References to LoadingUnits onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#loadedUnits
    loadedUnits: List[LoadingUnit] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadedUnits")
    # label: loadingType
    # comment: Enum stating whether the LoadingAction describes onloading or offloading
    # iri: https://onerecord.iata.org/ns/cargo#loadingType
    loadingType: List[LoadingType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingType")
    # label: onTransportMeans
    # comment: Reference to the TransportMeans that is being onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#onTransportMeans
    onTransportMeans: List[TransportMeans] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#onTransportMeans")
    # label: loadingPositionIdentifier
    # comment: Short text stating the loading position in the TransportMeans
    # iri: https://onerecord.iata.org/ns/cargo#loadingPositionIdentifier
    loadingPositionIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingPositionIdentifier")