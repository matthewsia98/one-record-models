from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.PieceGroup import PieceGroup
from one_record_ontology.models.code_lists.ULDLoadingIndicator import (
    ULDLoadingIndicator,
)


class ULDBasicPiece(PieceGroup):
    # label: uldLoadingIndicator
    # comment: Indicator related to ULD loading (e.g. Main deck only)
    # iri: https://onerecord.iata.org/ns/cargo#uldLoadingIndicator
    uldLoadingIndicator: Optional[ULDLoadingIndicator] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldLoadingIndicator",
    )
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac"
    )
