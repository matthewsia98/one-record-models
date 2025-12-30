from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.CO2Emissions import CO2Emissions
from one_record_ontology.models.cargo.Loading import Loading
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsActivity import LogisticsActivity
from one_record_ontology.models.cargo.ModeQualifier import ModeQualifier
from one_record_ontology.models.cargo.MovementTime import MovementTime
from one_record_ontology.models.cargo.Party import Party
from one_record_ontology.models.cargo.TransportMeans import TransportMeans
from one_record_ontology.models.cargo.Value import Value
from one_record_ontology.models.code_lists.ModeCode import ModeCode


class TransportMovement(LogisticsActivity):
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
    co2Emissions: List[CO2Emissions] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#co2Emissions",
    )
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
    )
    # label: distanceCalculated
    # comment: Information about the calculated distance
    # iri: https://onerecord.iata.org/ns/cargo#distanceCalculated
    distanceCalculated: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#distanceCalculated",
    )
    # label: distanceMeasured
    # comment: Information about the measured distance
    # iri: https://onerecord.iata.org/ns/cargo#distanceMeasured
    distanceMeasured: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#distanceMeasured",
    )
    # label: fuelAmountCalculated
    # comment: Information about the calculated fuel amount
    # iri: https://onerecord.iata.org/ns/cargo#fuelAmountCalculated
    fuelAmountCalculated: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountCalculated",
    )
    # label: fuelAmountMeasured
    # comment: Information about the measured fuel amount
    # iri: https://onerecord.iata.org/ns/cargo#fuelAmountMeasured
    fuelAmountMeasured: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountMeasured",
    )
    # label: loadingActions
    # comment: References to all actions of type Loading performed for the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#loadingActions
    loadingActions: List[Loading] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingActions",
    )
    # label: modeCode
    # comment: Mode of transport code, refer to UNECE Rec. 19 https://unece.org/fileadmin/DAM/cefact/recommendations/rec19/rec19_1cf19e.pdf
    # iri: https://onerecord.iata.org/ns/cargo#modeCode
    modeCode: Optional[ModeCode] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#modeCode"
    )
    # label: modeQualifier
    # comment: Pre-Carriage, Main-Carriage or On-Carriage
    # iri: https://onerecord.iata.org/ns/cargo#modeQualifier
    modeQualifier: Optional[ModeQualifier] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#modeQualifier",
    )
    # label: movementTimes
    # comment: Information about times related to the movement (milestone list to be defined)
    # iri: https://onerecord.iata.org/ns/cargo#movementTimes
    movementTimes: List[MovementTime] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimes",
    )
    # label: operatingParties
    # comment: Information about the parties operating this TransportMovement, for example pilot and co-pilot; can also refer to organizations through Party
    # iri: https://onerecord.iata.org/ns/cargo#operatingParties
    operatingParties: List[Party] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatingParties",
    )
    # label: operatingTransportMeans
    # comment: Reference to the TransportMeans operating the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#operatingTransportMeans
    operatingTransportMeans: Optional[TransportMeans] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans",
    )
    # label: fuelType
    # comment: e.g. Kerosene, Diesel, SAF, Electricity [renewable], Electricity [non-renewable]
    # iri: https://onerecord.iata.org/ns/cargo#fuelType
    fuelType: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#fuelType"
    )
    # label: seal
    # comment: Seal identifier
    # iri: https://onerecord.iata.org/ns/cargo#seal
    seal: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#seal"
    )
    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    # iri: https://onerecord.iata.org/ns/cargo#transportIdentifier
    transportIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier",
    )
