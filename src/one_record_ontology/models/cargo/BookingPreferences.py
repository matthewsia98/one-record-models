from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.code_lists.AircraftPossibilityCode import (
    AircraftPossibilityCode,
)


class BookingPreferences(BaseModel):
    # label: aircraftPossibilityCode
    # comment: Type of aircraft to be used if any specific requirements (e.g. Pure freighter, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#aircraftPossibilityCode
    aircraftPossibilityCode: Optional[AircraftPossibilityCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#aircraftPossibilityCode",
    )
    # label: excludedViaPoints
    # comment: Locations of excluded Via Points
    # iri: https://onerecord.iata.org/ns/cargo#excludedViaPoints
    excludedViaPoints: List[Location] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#excludedViaPoints",
    )
    # label: includedViaPoints
    # comment: Locations or stations to included in the routing
    # iri: https://onerecord.iata.org/ns/cargo#includedViaPoints
    includedViaPoints: List[Location] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#includedViaPoints",
    )
    # label: maxSegments
    # comment: Maximum number of segments for the transportation of the goods. 1 means direct flight
    # iri: https://onerecord.iata.org/ns/cargo#maxSegments
    maxSegments: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#maxSegments",
    )
    # label: preferredTransportId
    # comment: When part of the Request it refers to the preferred Transport ID from the customer. When part of the BookingOption (offer or actual booking) it refers to the expected Transport ID or flight
    # iri: https://onerecord.iata.org/ns/cargo#preferredTransportId
    preferredTransportId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#preferredTransportId",
    )
    # label: priceReferenceId
    # comment: Reference to a price reference if existing (e.g. Allotment number, contract reference, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#priceReferenceId
    priceReferenceId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#priceReferenceId",
    )
