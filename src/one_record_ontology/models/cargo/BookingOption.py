from datetime import datetime
from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.BookingOptionRequest import BookingOptionRequest
from one_record_ontology.models.cargo.BookingOptionStatus import BookingOptionStatus
from one_record_ontology.models.cargo.BookingRequest import BookingRequest
from one_record_ontology.models.cargo.BookingTimes import BookingTimes
from one_record_ontology.models.cargo.Carrier import Carrier
from one_record_ontology.models.cargo.CarrierProduct import CarrierProduct
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Price import Price
from one_record_ontology.models.cargo.StationRemarks import StationRemarks
from one_record_ontology.models.cargo.TransportLegs import TransportLegs
from one_record_ontology.models.cargo.UnitsPreference import UnitsPreference


class BookingOption(LogisticsObject):
    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#bookingTimes
    bookingTimes: Optional[BookingTimes] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingTimes",
    )
    # label: carrier
    # comment: Reference to the operating carrier
    # iri: https://onerecord.iata.org/ns/cargo#carrier
    carrier: Optional[Carrier] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrier"
    )
    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    # iri: https://onerecord.iata.org/ns/cargo#carrierProduct
    carrierProduct: Optional[CarrierProduct] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct",
    )
    # label: forBookingOptionRequest
    # comment: Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOptionRequest
    forBookingOptionRequest: Optional[BookingOptionRequest] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOptionRequest",
    )
    # label: forBookingRequest
    # comment: Reference to the Booking Request the of the Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#forBookingRequest
    forBookingRequest: Optional[BookingRequest] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingRequest",
    )
    # label: price
    # comment: Price of the Booking (if different from the offer)
    # iri: https://onerecord.iata.org/ns/cargo#price
    price: Optional[Price] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#price"
    )
    # label: stationRemarks
    # comment: Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    # iri: https://onerecord.iata.org/ns/cargo#stationRemarks
    stationRemarks: List[StationRemarks] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#stationRemarks",
    )
    # label: statusBookingOption
    # comment: Status of the Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#statusBookingOption
    statusBookingOption: Optional[BookingOptionStatus] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#statusBookingOption",
    )
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs",
    )
    # label: unitsPreference
    # comment: Reference to unit preferences of the request (e.g. kg or cm)
    # iri: https://onerecord.iata.org/ns/cargo#unitsPreference
    unitsPreference: Optional[UnitsPreference] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#unitsPreference",
    )
    # label: additionalInformation
    # comment: Additional information related to the Booking Option, e.g. sales details
    # iri: https://onerecord.iata.org/ns/cargo#additionalInformation
    additionalInformation: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#additionalInformation",
    )
    # label: alternatives
    # comment: Description of the alternatives proposed that do not match the Booking Option Request
    # iri: https://onerecord.iata.org/ns/cargo#alternatives
    alternatives: List[str] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#alternatives",
    )
    # label: offerValidFrom
    # comment: Date and time of beginning of offer validity
    # iri: https://onerecord.iata.org/ns/cargo#offerValidFrom
    offerValidFrom: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidFrom",
    )
    # label: offerValidTo
    # comment: Date and time of end of offer validity
    # iri: https://onerecord.iata.org/ns/cargo#offerValidTo
    offerValidTo: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidTo",
    )
    # label: requestMatch
    # comment: Indicates if the Booking Option is a match to the Booking Option Request preferences
    # iri: https://onerecord.iata.org/ns/cargo#requestMatch
    requestMatch: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#requestMatch",
    )
