from datetime import datetime
from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.CO2Emissions import CO2Emissions
from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.TransportMeans import TransportMeans
from one_record_ontology.models.code_lists.TransportMeansServiceType import (
    TransportMeansServiceType,
)


class TransportLegs(LogisticsObject):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
    )
    # label: co2Emissions
    # comment: References to CO2Emissions
    # iri: https://onerecord.iata.org/ns/cargo#co2Emissions
    co2Emissions: Optional[CO2Emissions] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#co2Emissions",
    )
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
    )
    # label: operatingTransportMeans
    # comment: Reference to the TransportMeans operating the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#operatingTransportMeans
    operatingTransportMeans: Optional[TransportMeans] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans",
    )
    # label: transportMeansServiceType
    # comment: Type of transport means service, e.g. Aircraftor Truck
    # iri: https://onerecord.iata.org/ns/cargo#transportMeansServiceType
    transportMeansServiceType: Optional[TransportMeansServiceType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansServiceType",
    )
    # label: transportMeansType
    # comment: Type of transport means, e.g. 744, RFS
    # iri: https://onerecord.iata.org/ns/cargo#transportMeansType
    transportMeansType: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansType",
    )
    # label: arrivalDate
    # comment: Arrival date and time of the leg
    # iri: https://onerecord.iata.org/ns/cargo#arrivalDate
    arrivalDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalDate",
    )
    # label: departureDate
    # comment: Departure date and time of the leg
    # iri: https://onerecord.iata.org/ns/cargo#departureDate
    departureDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureDate",
    )
    # label: TransportLegs
    # comment: Leg number
    # iri: https://onerecord.iata.org/ns/cargo#legNumber
    legNumber: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#legNumber",
    )
    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    # iri: https://onerecord.iata.org/ns/cargo#transportIdentifier
    transportIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier",
    )
