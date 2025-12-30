from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Field


class BookingTimes(BaseModel):
    # label: earliestAcceptanceTime
    # comment: Earliest acceptance date time (requested or proposed)
    # iri: https://onerecord.iata.org/ns/cargo#earliestAcceptanceTime
    earliestAcceptanceTime: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#earliestAcceptanceTime",
    )
    # label: latestAcceptanceTime
    # comment: Latest Acceptance time as per CargoIQ definition (requested, proposed or actual)
    # iri: https://onerecord.iata.org/ns/cargo#latestAcceptanceTime
    latestAcceptanceTime: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#latestAcceptanceTime",
    )
    # label: latestArrivalTime
    # comment: Latest arrival time at destination
    # iri: https://onerecord.iata.org/ns/cargo#latestArrivalTime
    latestArrivalTime: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#latestArrivalTime",
    )
    # label: timeOfAvailability
    # comment: Time of availability of the shipment as per CargoIQ definition
    # iri: https://onerecord.iata.org/ns/cargo#timeOfAvailability
    timeOfAvailability: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#timeOfAvailability",
    )
    # label: totalTransitTime
    # comment: Total transit time as per CargoIQ definition, expressed as a duration
    # iri: https://onerecord.iata.org/ns/cargo#totalTransitTime
    totalTransitTime: Optional[timedelta] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalTransitTime",
    )
