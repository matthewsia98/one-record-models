from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsService import LogisticsService
class Booking(LogisticsService):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: bookingRequest
    # comment: Reference to the Booking Request
    # iri: https://onerecord.iata.org/ns/cargo#bookingRequest
    bookingRequest: List[BookingRequest] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingRequest")
    # label: bookingSegments
    # comment: Information about booking segments - physics allocated to a specific transport leg
    # iri: https://onerecord.iata.org/ns/cargo#bookingSegments
    bookingSegments: List[BookingSegment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingSegments")
    # label: bookingShipmentDetails
    # comment: Reference to the BookingShipment if required
    # iri: https://onerecord.iata.org/ns/cargo#bookingShipmentDetails
    bookingShipmentDetails: List[BookingShipment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingShipmentDetails")
    # label: bookingStatus
    # comment: Status of the Booking
    # iri: https://onerecord.iata.org/ns/cargo#bookingStatus
    bookingStatus: List[BookingStatus] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingStatus")
    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#bookingTimes
    bookingTimes: List[BookingTimes] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingTimes")
    # label: carrier
    # comment: Reference to the operating carrier
    # iri: https://onerecord.iata.org/ns/cargo#carrier
    carrier: List[Carrier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#carrier")
    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    # iri: https://onerecord.iata.org/ns/cargo#carrierProduct
    carrierProduct: List[CarrierProduct] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: issuedForWaybill
    # comment: Reference to the Waybill object
    # iri: https://onerecord.iata.org/ns/cargo#issuedForWaybill
    issuedForWaybill: List[Waybill] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForWaybill")
    # label: stationRemarks
    # comment: Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    # iri: https://onerecord.iata.org/ns/cargo#stationRemarks
    stationRemarks: List[StationRemarks] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#stationRemarks")
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs")
    # label: updateBookingOptionRequests
    # comment: References to BookingOptionRequests that request to update the Booking
    # iri: https://onerecord.iata.org/ns/cargo#updateBookingOptionRequests
    updateBookingOptionRequests: List[BookingOptionRequest] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#updateBookingOptionRequests")
    # label: additionalInformation
    # comment: Additional information related to the Booking Option, e.g. sales details
    # iri: https://onerecord.iata.org/ns/cargo#additionalInformation
    additionalInformation: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#additionalInformation")
    # label: shippingInfo
    # comment: The shipper or its Agent may enter the appropriate optional shipping
    # iri: https://onerecord.iata.org/ns/cargo#shippingInfo
    shippingInfo: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingInfo")
    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    # iri: https://onerecord.iata.org/ns/cargo#shippingRefNo
    shippingRefNo: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo")
    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    # iri: https://onerecord.iata.org/ns/cargo#waybillNumber
    waybillNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber")
    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    # iri: https://onerecord.iata.org/ns/cargo#waybillPrefix
    waybillPrefix: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix")