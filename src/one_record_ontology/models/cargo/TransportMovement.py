from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsActivity import LogisticsActivity
class TransportMovement(LogisticsActivity):
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
    # label: distanceCalculated
    # comment: Information about the calculated distance
    # iri: https://onerecord.iata.org/ns/cargo#distanceCalculated
    distanceCalculated: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#distanceCalculated")
    # label: distanceMeasured
    # comment: Information about the measured distance
    # iri: https://onerecord.iata.org/ns/cargo#distanceMeasured
    distanceMeasured: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#distanceMeasured")
    # label: fuelAmountCalculated
    # comment: Information about the calculated fuel amount
    # iri: https://onerecord.iata.org/ns/cargo#fuelAmountCalculated
    fuelAmountCalculated: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountCalculated")
    # label: fuelAmountMeasured
    # comment: Information about the measured fuel amount
    # iri: https://onerecord.iata.org/ns/cargo#fuelAmountMeasured
    fuelAmountMeasured: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountMeasured")
    # label: loadingActions
    # comment: References to all actions of type Loading performed for the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#loadingActions
    loadingActions: List[Loading] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingActions")
    # label: modeCode
    # comment: Mode of transport code, refer to UNECE Rec. 19 https://unece.org/fileadmin/DAM/cefact/recommendations/rec19/rec19_1cf19e.pdf
    # iri: https://onerecord.iata.org/ns/cargo#modeCode
    modeCode: List[ModeCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#modeCode")
    # label: modeQualifier
    # comment: Pre-Carriage, Main-Carriage or On-Carriage
    # iri: https://onerecord.iata.org/ns/cargo#modeQualifier
    modeQualifier: List[ModeQualifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#modeQualifier")
    # label: movementTimes
    # comment: Information about times related to the movement (milestone list to be defined)
    # iri: https://onerecord.iata.org/ns/cargo#movementTimes
    movementTimes: List[MovementTime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimes")
    # label: operatingParties
    # comment: Information about the parties operating this TransportMovement, for example pilot and co-pilot; can also refer to organizations through Party
    # iri: https://onerecord.iata.org/ns/cargo#operatingParties
    operatingParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#operatingParties")
    # label: operatingTransportMeans
    # comment: Reference to the TransportMeans operating the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#operatingTransportMeans
    operatingTransportMeans: List[TransportMeans] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans")
    # label: fuelType
    # comment: e.g. Kerosene, Diesel, SAF, Electricity [renewable], Electricity [non-renewable]
    # iri: https://onerecord.iata.org/ns/cargo#fuelType
    fuelType: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#fuelType")
    # label: seal
    # comment: Seal identifier
    # iri: https://onerecord.iata.org/ns/cargo#seal
    seal: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#seal")
    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    # iri: https://onerecord.iata.org/ns/cargo#transportIdentifier
    transportIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier")