from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Composing import Composing
from one_record_ontology.models.cargo.LoadingUnit import LoadingUnit
from one_record_ontology.models.cargo.LogisticsActivity import LogisticsActivity


class UnitComposition(LogisticsActivity):
    # label: compositionActions
    # comment: References to all CompositionActions performed for the UnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#compositionActions
    compositionActions: List[Composing] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#compositionActions",
    )
    # label: onLoadingUnit
    # comment: Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    # iri: https://onerecord.iata.org/ns/cargo#loadingUnit
    loadingUnit: Optional[LoadingUnit] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingUnit",
    )
    # label: compositionIdentifier
    # comment: Short text holding the process number if necessary
    # iri: https://onerecord.iata.org/ns/cargo#compositionIdentifier
    compositionIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#compositionIdentifier",
    )
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac"
    )
