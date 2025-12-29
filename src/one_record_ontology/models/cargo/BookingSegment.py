from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class BookingSegment(BaseModel):
    # label: pieceGroups
    # comment: Reference to the Piece groups of the shipment
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroups
    pieceGroups: List[PieceGroup] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroups")
    # label: spaceAllocationCode
    # comment: Current status of the space allocation of the booking segment
    # iri: https://onerecord.iata.org/ns/cargo#spaceAllocationCode
    spaceAllocationCode: List[SpaceAllocationCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#spaceAllocationCode")
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs")
    # label: allotmentCode
    # comment: String holding an allotment code of a booking segment
    # iri: https://onerecord.iata.org/ns/cargo#allotmentCode
    allotmentCode: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#allotmentCode")