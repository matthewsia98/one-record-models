from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.BookingOptionRequest import BookingOptionRequest
from one_record_ontology.models.cargo.BookingRequest import BookingRequest
from one_record_ontology.models.cargo.BookingSegment import BookingSegment
from one_record_ontology.models.cargo.BookingShipment import BookingShipment
from one_record_ontology.models.cargo.BookingStatus import BookingStatus
from one_record_ontology.models.cargo.BookingTimes import BookingTimes
from one_record_ontology.models.cargo.Carrier import Carrier
from one_record_ontology.models.cargo.CarrierProduct import CarrierProduct
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsService import LogisticsService
from one_record_ontology.models.cargo.StationRemarks import StationRemarks
from one_record_ontology.models.cargo.TransportLegs import TransportLegs
from one_record_ontology.models.cargo.Waybill import Waybill


class Booking(LogisticsService):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
    )
    # label: bookingRequest
    # comment: Reference to the Booking Request
    # iri: https://onerecord.iata.org/ns/cargo#bookingRequest
    bookingRequest: Optional[BookingRequest] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingRequest",
    )
    # label: bookingSegments
    # comment: Information about booking segments - physics allocated to a specific transport leg
    # iri: https://onerecord.iata.org/ns/cargo#bookingSegments
    bookingSegments: List[BookingSegment] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingSegments",
    )
    # label: bookingShipmentDetails
    # comment: Reference to the BookingShipment if required
    # iri: https://onerecord.iata.org/ns/cargo#bookingShipmentDetails
    bookingShipmentDetails: Optional[BookingShipment] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingShipmentDetails",
    )
    # label: bookingStatus
    # comment: Status of the Booking
    # iri: https://onerecord.iata.org/ns/cargo#bookingStatus
    bookingStatus: Optional[BookingStatus] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingStatus",
    )
    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#bookingTimes
    bookingTimes: List[BookingTimes] = Field(
        default_factory=list,
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
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
    )
    # label: issuedForWaybill
    # comment: Reference to the Waybill object
    # iri: https://onerecord.iata.org/ns/cargo#issuedForWaybill
    issuedForWaybill: Optional[Waybill] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForWaybill",
    )
    # label: stationRemarks
    # comment: Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    # iri: https://onerecord.iata.org/ns/cargo#stationRemarks
    stationRemarks: List[StationRemarks] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#stationRemarks",
    )
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs",
    )
    # label: updateBookingOptionRequests
    # comment: References to BookingOptionRequests that request to update the Booking
    # iri: https://onerecord.iata.org/ns/cargo#updateBookingOptionRequests
    updateBookingOptionRequests: List[BookingOptionRequest] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#updateBookingOptionRequests",
    )
    # label: additionalInformation
    # comment: Additional information related to the Booking Option, e.g. sales details
    # iri: https://onerecord.iata.org/ns/cargo#additionalInformation
    additionalInformation: List[str] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#additionalInformation",
    )
    # label: shippingInfo
    # comment: The shipper or its Agent may enter the appropriate optional shipping
    # iri: https://onerecord.iata.org/ns/cargo#shippingInfo
    shippingInfo: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingInfo",
    )
    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    # iri: https://onerecord.iata.org/ns/cargo#shippingRefNo
    shippingRefNo: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo",
    )
    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    # iri: https://onerecord.iata.org/ns/cargo#waybillNumber
    waybillNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber",
    )
    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    # iri: https://onerecord.iata.org/ns/cargo#waybillPrefix
    waybillPrefix: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix",
    )
