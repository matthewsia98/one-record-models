from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PieceGroup import PieceGroup
class ULDBasicPiece(PieceGroup):
    # label: uldLoadingIndicator
    # comment: Indicator related to ULD loading (e.g. Main deck only)
    # iri: https://onerecord.iata.org/ns/cargo#uldLoadingIndicator
    uldLoadingIndicator: List[ULDLoadingIndicator] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldLoadingIndicator")
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#slac")