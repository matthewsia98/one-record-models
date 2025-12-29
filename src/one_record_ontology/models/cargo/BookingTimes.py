from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class BookingTimes(BaseModel):
    # label: earliestAcceptanceTime
    # comment: Earliest acceptance date time (requested or proposed)
    # iri: https://onerecord.iata.org/ns/cargo#earliestAcceptanceTime
    earliestAcceptanceTime: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#earliestAcceptanceTime")
    # label: latestAcceptanceTime
    # comment: Latest Acceptance time as per CargoIQ definition (requested, proposed or actual)
    # iri: https://onerecord.iata.org/ns/cargo#latestAcceptanceTime
    latestAcceptanceTime: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#latestAcceptanceTime")
    # label: latestArrivalTime
    # comment: Latest arrival time at destination
    # iri: https://onerecord.iata.org/ns/cargo#latestArrivalTime
    latestArrivalTime: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#latestArrivalTime")
    # label: timeOfAvailability
    # comment: Time of availability of the shipment as per CargoIQ definition
    # iri: https://onerecord.iata.org/ns/cargo#timeOfAvailability
    timeOfAvailability: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#timeOfAvailability")
    # label: totalTransitTime
    # comment: Total transit time as per CargoIQ definition, expressed as a duration
    # iri: https://onerecord.iata.org/ns/cargo#totalTransitTime
    totalTransitTime: List[timedelta] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#totalTransitTime")