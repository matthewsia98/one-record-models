from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class TransportLegs(LogisticsObject):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: co2Emissions
    # comment: References to CO2Emissions
    # iri: https://onerecord.iata.org/ns/cargo#co2Emissions
    co2Emissions: List[CO2Emissions] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#co2Emissions")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: operatingTransportMeans
    # comment: Reference to the TransportMeans operating the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#operatingTransportMeans
    operatingTransportMeans: List[TransportMeans] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans")
    # label: transportMeansServiceType
    # comment: Type of transport means service, e.g. Aircraftor Truck
    # iri: https://onerecord.iata.org/ns/cargo#transportMeansServiceType
    transportMeansServiceType: List[TransportMeansServiceType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansServiceType")
    # label: transportMeansType
    # comment: Type of transport means, e.g. 744, RFS
    # iri: https://onerecord.iata.org/ns/cargo#transportMeansType
    transportMeansType: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansType")
    # label: arrivalDate
    # comment: Arrival date and time of the leg
    # iri: https://onerecord.iata.org/ns/cargo#arrivalDate
    arrivalDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalDate")
    # label: departureDate
    # comment: Departure date and time of the leg
    # iri: https://onerecord.iata.org/ns/cargo#departureDate
    departureDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#departureDate")
    # label: TransportLegs
    # comment: Leg number
    # iri: https://onerecord.iata.org/ns/cargo#legNumber
    legNumber: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#legNumber")
    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    # iri: https://onerecord.iata.org/ns/cargo#transportIdentifier
    transportIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier")