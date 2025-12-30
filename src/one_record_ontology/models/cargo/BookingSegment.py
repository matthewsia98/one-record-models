from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.PieceGroup import PieceGroup
from one_record_ontology.models.cargo.TransportLegs import TransportLegs
from one_record_ontology.models.code_lists.SpaceAllocationCode import (
    SpaceAllocationCode,
)


class BookingSegment(BaseModel):
    # label: pieceGroups
    # comment: Reference to the Piece groups of the shipment
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroups
    pieceGroups: List[PieceGroup] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroups",
    )
    # label: spaceAllocationCode
    # comment: Current status of the space allocation of the booking segment
    # iri: https://onerecord.iata.org/ns/cargo#spaceAllocationCode
    spaceAllocationCode: Optional[SpaceAllocationCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#spaceAllocationCode",
    )
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: Optional[TransportLegs] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs",
    )
    # label: allotmentCode
    # comment: String holding an allotment code of a booking segment
    # iri: https://onerecord.iata.org/ns/cargo#allotmentCode
    allotmentCode: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#allotmentCode",
    )
