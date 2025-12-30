from __future__ import annotations

from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field
from rdflib import URIRef

from one_record_ontology.models.code_lists import (
    AircraftPossibilityCode,
    AWBUseIndicator,
    BasicRateClassCode,
    ChargeCode,
    ChargeIdentifier,
    CommodityCode,
    CurrencyCode,
    DemurrageCode,
    DensityGroupCode,
    DimensionsUnitCode,
    EntitlementCode,
    ExplosiveCompatibilityGroupCode,
    GoodsTypeCode,
    GoodsTypeExtensionCode,
    MeasurementUnitCode,
    ModeCode,
    MovementIndicator,
    OtherChargeCode,
    PackageMarkCode,
    PackagingDangerLevelCode,
    ParticipantIdentifier,
    PrepaidCollectIndicator,
    RadioactiveMaterialClassification,
    RateClassCode,
    RaTypeCode,
    RegulatedEntityCategoryCode,
    ScreeningExemption,
    ScreeningMethod,
    SecurityStatus,
    ServiceCode,
    SignatoryRole,
    SignatureTypeCode,
    SpaceAllocationCode,
    SpecialHandlingCode,
    TemperatureUnitCode,
    TransactionPurposeCode,
    TransportMeansServiceType,
    ULDConditionCode,
    ULDLoadingIndicator,
    VolumeUnitCode,
    WeightUnitCode,
)


class AccountNumber(BaseModel):
    # label: accountNumberType
    # comment: Type of the account of the account number
    # iri: https://onerecord.iata.org/ns/cargo#accountNumberType
    accountNumberType: Optional[AccountType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#accountNumberType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")
class AccountType(CodeListElement):
    ...
class AccountingNote(BaseModel):
    # label: accountingNoteIdentifier
    # comment: String holding accounting information (AWB box 10)
    # iri: https://onerecord.iata.org/ns/cargo#accountingNoteIdentifier
    accountingNoteIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteIdentifier")
    # label: accountingNoteText
    # comment: String holding the identifier in an accounting note (AWB box 10)
    # iri: https://onerecord.iata.org/ns/cargo#accountingNoteText
    accountingNoteText: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteText")
class ActionTimeType(str, Enum):
    """
    label: ActionTimeType
    comment: Restricted code list for acceptable action times
    """
    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: PLANNED
    # comment: Used when a time is planned
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")
    # label: REQUESTED
    # comment: Used when a time is requested
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")
class ActivitySequence(BaseModel):
    # label: activity
    # comment: Reference to the Activity that is performed as part of a Service
    # iri: https://onerecord.iata.org/ns/cargo#activity
    activity: Optional[LogisticsActivity] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#activity")
    # label: sequenceNumber
    # comment: Short text to detail sequence number (alphanumeric)
    # iri: https://onerecord.iata.org/ns/cargo#sequenceNumber
    sequenceNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#sequenceNumber")
class Actor(LogisticsAgent):
    # label: associatedOrganization
    # comment: Reference to the Organization the Actor is associated with
    # iri: https://onerecord.iata.org/ns/cargo#associatedOrganization
    associatedOrganization: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#associatedOrganization")
class Address(BaseModel):
    # label: addressCode
    # comment: Address identifier using special coding systems e.g. US CBP FIRMS code
    # iri: https://onerecord.iata.org/ns/cargo#addressCode
    addressCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#addressCode")
    # label: cityCode
    # comment: UN/LOCODE city code (5 letter) or IATA city code (3 letter)
    # iri: https://onerecord.iata.org/ns/cargo#cityCode
    cityCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#cityCode")
    # label: country
    # comment: Country details. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#country
    country: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#country")
    # label: postalCode
    # comment: Postal / ZIP code
    # iri: https://onerecord.iata.org/ns/cargo#postalCode
    postalCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#postalCode")
    # label: regionCode
    # comment: Region/ State / Department. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#regionCode
    regionCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#regionCode")
    # label: cityName
    # comment: String holding a city name
    # iri: https://onerecord.iata.org/ns/cargo#cityName
    cityName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#cityName")
    # label: postOfficeBox
    # comment: Post Office box number / code
    # iri: https://onerecord.iata.org/ns/cargo#postOfficeBox
    postOfficeBox: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#postOfficeBox")
    # label: streetAddressLines
    # comment: Street address including street name, street number, building number, apartment etc
    # iri: https://onerecord.iata.org/ns/cargo#streetAddressLines
    streetAddressLines: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#streetAddressLines")
    # label: textualPostCode
    # comment: Postal / ZIP code
    # iri: https://onerecord.iata.org/ns/cargo#textualPostCode
    textualPostCode: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#textualPostCode")
class Adjustments(BaseModel):
    # label: correctionNumber
    # comment: Number of the adjustment
    # iri: https://onerecord.iata.org/ns/cargo#correctionNumber
    correctionNumber: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#correctionNumber")
    # label: correctionSerialNumber
    # comment: Serial Number of the correction
    # iri: https://onerecord.iata.org/ns/cargo#correctionSerialNumber
    correctionSerialNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#correctionSerialNumber")
    # label: reasonsForAdjustments
    # comment: A free text for user to include a reason for correction
    # iri: https://onerecord.iata.org/ns/cargo#reasonsForAdjustments
    reasonsForAdjustments: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#reasonsForAdjustments")
class Answer(LogisticsObject):
    # label: answerActor
    # comment: Reference to the Actor giving the Answer
    # iri: https://onerecord.iata.org/ns/cargo#answerActor
    answerActor: Optional[Actor] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#answerActor")
    # label: answerValue
    # comment: Information about an answer Value of any kind of the Answer
    # iri: https://onerecord.iata.org/ns/cargo#answerValue
    answerValue: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#answerValue")
    # label: givenAtLocation
    # comment: Reference to the Location from which the Question was answered, relevant for split checks with documentary and physical elements
    # iri: https://onerecord.iata.org/ns/cargo#givenAtLocation
    givenAtLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#givenAtLocation")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: question
    # comment: Reference to the Question the Answer is for
    # iri: https://onerecord.iata.org/ns/cargo#question
    question: Optional[Question] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#question")
    # label: text
    # comment: Text for the Answer
    # iri: https://onerecord.iata.org/ns/cargo#text
    text: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#text")
class BillingDetails(LogisticsObject):
    # label: adjustments
    # comment: Information about Adjustments performed on the BillingDetails
    # iri: https://onerecord.iata.org/ns/cargo#adjustments
    adjustments: List[Adjustments] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#adjustments")
    # label: awbUseIndicator
    # comment: It must either contain the values of R for Revenue AWB, V for Void AWB or S for Service AWB.
    # iri: https://onerecord.iata.org/ns/cargo#awbUseIndicator
    awbUseIndicator: Optional[AWBUseIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#awbUseIndicator")
    # label: detailedWaybill
    # comment: Reference to the Waybill
    # iri: https://onerecord.iata.org/ns/cargo#detailedWaybill
    detailedWaybill: Optional[Waybill] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#detailedWaybill")
    # label: taxDueAgent
    # comment: Tax due Agent (VAT/GST on Commission). Total VAT/TAX amount payable by airline to agent
    # iri: https://onerecord.iata.org/ns/cargo#taxDueAgent
    taxDueAgent: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAgent")
    # label: taxDueAirline
    # comment: Tax due Airline (as per AWB, or VAT/GST as per invoice). Total VAT/TAX amount payable by agent to airline
    # iri: https://onerecord.iata.org/ns/cargo#taxDueAirline
    taxDueAirline: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAirline")
    # label: awbAcceptanceDate
    # comment: The Date AWB Acceptance should be the same as the Date AWB Delivery. (beginning of the process)
    # iri: https://onerecord.iata.org/ns/cargo#awbAcceptanceDate
    awbAcceptanceDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#awbAcceptanceDate")
    # label: awbDeliveryDate
    # comment: The Date AWB Delivery is also used as the AWB Execution date which will determine which billing period it will be processed and billed in.
    # iri: https://onerecord.iata.org/ns/cargo#awbDeliveryDate
    awbDeliveryDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#awbDeliveryDate")
    # label: awbExecutionDate
    # comment: The AWB execution date determines which billing period the document will be processed and billed in.
    # iri: https://onerecord.iata.org/ns/cargo#awbExecutionDate
    awbExecutionDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#awbExecutionDate")
    # label: commission
    # comment: The commission amount in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    # iri: https://onerecord.iata.org/ns/cargo#commission
    commission: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#commission")
    # label: commissionIndicator
    # comment: Indicates if commission is applied. Boolean
    # iri: https://onerecord.iata.org/ns/cargo#commissionIndicator
    commissionIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#commissionIndicator")
    # label: commissionPercentage
    # comment: The commission percentage in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    # iri: https://onerecord.iata.org/ns/cargo#commissionPercentage
    commissionPercentage: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#commissionPercentage")
    # label: discount
    # comment: This is used as a discount to the “official” transportation charge on AWB to arrive at actual selling price
    # iri: https://onerecord.iata.org/ns/cargo#discount
    discount: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#discount")
    # label: exchangeRate
    # comment: The Rate at which the Air Waybill Amount has been multiplied to arrive at the amount of settlement.
    # iri: https://onerecord.iata.org/ns/cargo#exchangeRate
    exchangeRate: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#exchangeRate")
    # label: nbCorrections
    # comment: Number of corrections to CASS records
    # iri: https://onerecord.iata.org/ns/cargo#nbCorrections
    nbCorrections: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#nbCorrections")
    # label: vatIndicator
    # comment: Indicate if subject to VAT (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#vatIndicator
    vatIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#vatIndicator")
class Booking(LogisticsService):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: bookingRequest
    # comment: Reference to the Booking Request
    # iri: https://onerecord.iata.org/ns/cargo#bookingRequest
    bookingRequest: Optional[BookingRequest] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingRequest")
    # label: bookingSegments
    # comment: Information about booking segments - physics allocated to a specific transport leg
    # iri: https://onerecord.iata.org/ns/cargo#bookingSegments
    bookingSegments: List[BookingSegment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingSegments")
    # label: bookingShipmentDetails
    # comment: Reference to the BookingShipment if required
    # iri: https://onerecord.iata.org/ns/cargo#bookingShipmentDetails
    bookingShipmentDetails: Optional[BookingShipment] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingShipmentDetails")
    # label: bookingStatus
    # comment: Status of the Booking
    # iri: https://onerecord.iata.org/ns/cargo#bookingStatus
    bookingStatus: Optional[BookingStatus] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingStatus")
    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#bookingTimes
    bookingTimes: List[BookingTimes] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingTimes")
    # label: carrier
    # comment: Reference to the operating carrier
    # iri: https://onerecord.iata.org/ns/cargo#carrier
    carrier: Optional[Carrier] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrier")
    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    # iri: https://onerecord.iata.org/ns/cargo#carrierProduct
    carrierProduct: Optional[CarrierProduct] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: issuedForWaybill
    # comment: Reference to the Waybill object
    # iri: https://onerecord.iata.org/ns/cargo#issuedForWaybill
    issuedForWaybill: Optional[Waybill] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForWaybill")
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
    shippingInfo: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingInfo")
    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    # iri: https://onerecord.iata.org/ns/cargo#shippingRefNo
    shippingRefNo: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo")
    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    # iri: https://onerecord.iata.org/ns/cargo#waybillNumber
    waybillNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber")
    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    # iri: https://onerecord.iata.org/ns/cargo#waybillPrefix
    waybillPrefix: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix")
class BookingOption(LogisticsObject):
    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#bookingTimes
    bookingTimes: Optional[BookingTimes] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingTimes")
    # label: carrier
    # comment: Reference to the operating carrier
    # iri: https://onerecord.iata.org/ns/cargo#carrier
    carrier: Optional[Carrier] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrier")
    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    # iri: https://onerecord.iata.org/ns/cargo#carrierProduct
    carrierProduct: Optional[CarrierProduct] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct")
    # label: forBookingOptionRequest
    # comment: Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOptionRequest
    forBookingOptionRequest: Optional[BookingOptionRequest] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOptionRequest")
    # label: forBookingRequest
    # comment: Reference to the Booking Request the of the Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#forBookingRequest
    forBookingRequest: Optional[BookingRequest] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingRequest")
    # label: price
    # comment: Price of the Booking (if different from the offer)
    # iri: https://onerecord.iata.org/ns/cargo#price
    price: Optional[Price] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#price")
    # label: stationRemarks
    # comment: Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    # iri: https://onerecord.iata.org/ns/cargo#stationRemarks
    stationRemarks: List[StationRemarks] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#stationRemarks")
    # label: statusBookingOption
    # comment: Status of the Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#statusBookingOption
    statusBookingOption: Optional[BookingOptionStatus] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#statusBookingOption")
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs")
    # label: unitsPreference
    # comment: Reference to unit preferences of the request (e.g. kg or cm)
    # iri: https://onerecord.iata.org/ns/cargo#unitsPreference
    unitsPreference: Optional[UnitsPreference] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unitsPreference")
    # label: additionalInformation
    # comment: Additional information related to the Booking Option, e.g. sales details
    # iri: https://onerecord.iata.org/ns/cargo#additionalInformation
    additionalInformation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#additionalInformation")
    # label: alternatives
    # comment: Description of the alternatives proposed that do not match the Booking Option Request
    # iri: https://onerecord.iata.org/ns/cargo#alternatives
    alternatives: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#alternatives")
    # label: offerValidFrom
    # comment: Date and time of beginning of offer validity
    # iri: https://onerecord.iata.org/ns/cargo#offerValidFrom
    offerValidFrom: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidFrom")
    # label: offerValidTo
    # comment: Date and time of end of offer validity
    # iri: https://onerecord.iata.org/ns/cargo#offerValidTo
    offerValidTo: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidTo")
    # label: requestMatch
    # comment: Indicates if the Booking Option is a match to the Booking Option Request preferences
    # iri: https://onerecord.iata.org/ns/cargo#requestMatch
    requestMatch: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#requestMatch")
class BookingOptionRequest(LogisticsObject):
    # label: bookingOptions
    # comment: Reference to all Booking Options
    # iri: https://onerecord.iata.org/ns/cargo#bookingOptions
    bookingOptions: List[BookingOption] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingOptions")
    # label: bookingPreference
    # comment: Reference to the Booking preferences
    # iri: https://onerecord.iata.org/ns/cargo#bookingPreference
    bookingPreference: Optional[BookingPreferences] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingPreference")
    # label: bookingShipmentDetails
    # comment: Reference to the BookingShipment if required
    # iri: https://onerecord.iata.org/ns/cargo#bookingShipmentDetails
    bookingShipmentDetails: Optional[BookingShipment] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingShipmentDetails")
    # label: bookingToUpdate
    # comment: Reference to the Booking to update
    # iri: https://onerecord.iata.org/ns/cargo#bookingToUpdate
    bookingToUpdate: Optional[Booking] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingToUpdate")
    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    # iri: https://onerecord.iata.org/ns/cargo#carrierProduct
    carrierProduct: Optional[CarrierProduct] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: timePreferences
    # comment: Schedule preferences of the request
    # iri: https://onerecord.iata.org/ns/cargo#timePreferences
    timePreferences: Optional[BookingTimes] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#timePreferences")
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs")
    # label: unitsPreference
    # comment: Reference to unit preferences of the request (e.g. kg or cm)
    # iri: https://onerecord.iata.org/ns/cargo#unitsPreference
    unitsPreference: Optional[UnitsPreference] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unitsPreference")
    # label: knownShipper
    # comment: Indication if shipper is a Known Shipper as per TSA grant
    # iri: https://onerecord.iata.org/ns/cargo#knownShipper
    knownShipper: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#knownShipper")
class BookingOptionStatus(str, Enum):
    """
    label: BookingOptionStatus
    comment: Restricted code list containing the statuses of a booking option
    """
    # label: BOOKABLE
    # comment: Used when a booking option (or proposal) is bookable
    BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#BOOKABLE")
    # label: BOOKED
    # comment: Used when a booking option proposal is booked
    BOOKED = URIRef("https://onerecord.iata.org/ns/cargo#BOOKED")
    # label: EXPIRED
    # comment: Used when a booking option proposal is expired
    EXPIRED = URIRef("https://onerecord.iata.org/ns/cargo#EXPIRED")
    # label: NONBOOKABLE
    # comment: Used when a booking option is nonbookable
    NONBOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NONBOOKABLE")
    # label: NOT_BOOKABLE
    # comment: Used when a booking option proposal is not bookable
    NOT_BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NOT_BOOKABLE")
    # label: ON_REQUEST
    # comment: Used when a booking option proposal is on request
    ON_REQUEST = URIRef("https://onerecord.iata.org/ns/cargo#ON_REQUEST")
    # label: QUEUED
    # comment: Used when a booking or booking option is queued or pending
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")
class BookingPreferences(BaseModel):
    # label: aircraftPossibilityCode
    # comment: Type of aircraft to be used if any specific requirements (e.g. Pure freighter, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#aircraftPossibilityCode
    aircraftPossibilityCode: Optional[AircraftPossibilityCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#aircraftPossibilityCode")
    # label: excludedViaPoints
    # comment: Locations of excluded Via Points
    # iri: https://onerecord.iata.org/ns/cargo#excludedViaPoints
    excludedViaPoints: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#excludedViaPoints")
    # label: includedViaPoints
    # comment: Locations or stations to included in the routing
    # iri: https://onerecord.iata.org/ns/cargo#includedViaPoints
    includedViaPoints: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#includedViaPoints")
    # label: maxSegments
    # comment: Maximum number of segments for the transportation of the goods. 1 means direct flight
    # iri: https://onerecord.iata.org/ns/cargo#maxSegments
    maxSegments: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#maxSegments")
    # label: preferredTransportId
    # comment: When part of the Request it refers to the preferred Transport ID from the customer. When part of the BookingOption (offer or actual booking) it refers to the expected Transport ID or flight
    # iri: https://onerecord.iata.org/ns/cargo#preferredTransportId
    preferredTransportId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#preferredTransportId")
    # label: priceReferenceId
    # comment: Reference to a price reference if existing (e.g. Allotment number, contract reference, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#priceReferenceId
    priceReferenceId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#priceReferenceId")
class BookingRequest(LogisticsObject):
    # label: booking
    # comment: Reference to the Booking
    # iri: https://onerecord.iata.org/ns/cargo#booking
    booking: Optional[Booking] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#booking")
    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOption
    forBookingOption: Optional[BookingOption] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption")
    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    # iri: https://onerecord.iata.org/ns/cargo#waybillNumber
    waybillNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber")
    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    # iri: https://onerecord.iata.org/ns/cargo#waybillPrefix
    waybillPrefix: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix")
class BookingSegment(BaseModel):
    # label: pieceGroups
    # comment: Reference to the Piece groups of the shipment
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroups
    pieceGroups: List[PieceGroup] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroups")
    # label: spaceAllocationCode
    # comment: Current status of the space allocation of the booking segment
    # iri: https://onerecord.iata.org/ns/cargo#spaceAllocationCode
    spaceAllocationCode: Optional[SpaceAllocationCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#spaceAllocationCode")
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: Optional[TransportLegs] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs")
    # label: allotmentCode
    # comment: String holding an allotment code of a booking segment
    # iri: https://onerecord.iata.org/ns/cargo#allotmentCode
    allotmentCode: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#allotmentCode")
class BookingShipment(LogisticsObject):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight")
    # label: customsInformation
    # comment: Customs details
    # iri: https://onerecord.iata.org/ns/cargo#customsInformation
    customsInformation: List[CustomsInformation] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation")
    # label: densityGroupCode
    # comment: Density Group Code as defined in cXML code list 2
    # iri: https://onerecord.iata.org/ns/cargo#densityGroupCode
    densityGroupCode: Optional[DensityGroupCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#densityGroupCode")
    # label: expectedCommodity
    # comment: Expected commodity of the shipment as per Commodity Code list. Either this or expected HS code required
    # iri: https://onerecord.iata.org/ns/cargo#expectedCommodity
    expectedCommodity: Optional[CommodityCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#expectedCommodity")
    # label: expectedHScode
    # comment: Expected commodity of the shipment as per HS code (at least 6 digits). Either this or expectedCommodityCode required
    # iri: https://onerecord.iata.org/ns/cargo#expectedHScode
    expectedHScode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#expectedHScode")
    # label: forBookingOptionRequest
    # comment: Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOptionRequest
    forBookingOptionRequest: Optional[BookingOptionRequest] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOptionRequest")
    # label: pieceGroups
    # comment: Reference to the Piece groups of the shipment
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroups
    pieceGroups: List[PieceGroup] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroups")
    # label: specialHandlingCodes
    # comment: Three-letter special handling code (SPH)
    # iri: https://onerecord.iata.org/ns/cargo#specialHandlingCodes
    specialHandlingCodes: List[SpecialHandlingCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#specialHandlingCodes")
    # label: temperatureInstructions
    # comment: Temperature instructions if a specific range
    # iri: https://onerecord.iata.org/ns/cargo#temperatureInstructions
    temperatureInstructions: Optional[TemperatureInstructions] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureInstructions")
    # label: totalDimensions
    # comment: Dimensions of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalDimensions
    totalDimensions: Optional[Dimensions] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#totalDimensions")
    # label: totalGrossWeight
    # comment: Total gross weight of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalGrossWeight
    totalGrossWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#totalGrossWeight")
    # label: consolidationIndicator
    # comment: Indication if the shipment is a consolidation
    # iri: https://onerecord.iata.org/ns/cargo#consolidationIndicator
    consolidationIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#consolidationIndicator")
    # label: specialServiceRequests
    # comment: Special service requests
    # iri: https://onerecord.iata.org/ns/cargo#specialServiceRequests
    specialServiceRequests: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#specialServiceRequests")
    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    # iri: https://onerecord.iata.org/ns/cargo#textualHandlingInstructions
    textualHandlingInstructions: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions")
class BookingStatus(str, Enum):
    """
    label: BookingStatus
    comment: Restricted code list containing the possible statuses of a booking
    """
    # label: CONFIRMED
    # comment: Used when a booking is confirmed
    CONFIRMED = URIRef("https://onerecord.iata.org/ns/cargo#CONFIRMED")
    # label: DELETED
    # comment: Used when a booking is deleted
    DELETED = URIRef("https://onerecord.iata.org/ns/cargo#DELETED")
    # label: QUEUED
    # comment: Used when a booking or booking option is queued or pending
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")
    # label: REJECTED
    # comment: Used when a booking is rejected
    REJECTED = URIRef("https://onerecord.iata.org/ns/cargo#REJECTED")
class BookingTimes(BaseModel):
    # label: earliestAcceptanceTime
    # comment: Earliest acceptance date time (requested or proposed)
    # iri: https://onerecord.iata.org/ns/cargo#earliestAcceptanceTime
    earliestAcceptanceTime: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#earliestAcceptanceTime")
    # label: latestAcceptanceTime
    # comment: Latest Acceptance time as per CargoIQ definition (requested, proposed or actual)
    # iri: https://onerecord.iata.org/ns/cargo#latestAcceptanceTime
    latestAcceptanceTime: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#latestAcceptanceTime")
    # label: latestArrivalTime
    # comment: Latest arrival time at destination
    # iri: https://onerecord.iata.org/ns/cargo#latestArrivalTime
    latestArrivalTime: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#latestArrivalTime")
    # label: timeOfAvailability
    # comment: Time of availability of the shipment as per CargoIQ definition
    # iri: https://onerecord.iata.org/ns/cargo#timeOfAvailability
    timeOfAvailability: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#timeOfAvailability")
    # label: totalTransitTime
    # comment: Total transit time as per CargoIQ definition, expressed as a duration
    # iri: https://onerecord.iata.org/ns/cargo#totalTransitTime
    totalTransitTime: Optional[timedelta] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#totalTransitTime")
class CO2Emissions(LogisticsObject):
    # label: calculatedEmissions
    # comment: CO2 emissions calculated
    # iri: https://onerecord.iata.org/ns/cargo#calculatedEmissions
    calculatedEmissions: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#calculatedEmissions")
    # label: calculationFor
    # comment: Reference to the TransportMovement or TransportLegs the CO2Emissions have been calculated for
    # iri: https://onerecord.iata.org/ns/cargo#calculationFor
    calculationFor: Optional[LogisticsObject] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#calculationFor")
    # label: methodName
    # comment: Name of the CO2 calculation method
    # iri: https://onerecord.iata.org/ns/cargo#methodName
    methodName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#methodName")
    # label: methodVersion
    # comment: Version used for the calculation
    # iri: https://onerecord.iata.org/ns/cargo#methodVersion
    methodVersion: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#methodVersion")
class Carrier(Company):
    # label: airlineCode
    # comment: IATA two-character airline code
    # iri: https://onerecord.iata.org/ns/cargo#airlineCode
    airlineCode: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#airlineCode")
    # label: prefix
    # comment: IATA three-numeric airline prefix number
    # iri: https://onerecord.iata.org/ns/cargo#prefix
    prefix: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#prefix")
class CarrierProduct(BaseModel):
    # label: productCode
    # comment: Carrier's product code
    # iri: https://onerecord.iata.org/ns/cargo#productCode
    productCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#productCode")
    # label: serviceLevelCode
    # comment: Service level code
    # iri: https://onerecord.iata.org/ns/cargo#serviceLevelCode
    serviceLevelCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serviceLevelCode")
    # label: productDescription
    # comment: Carrier's product description
    # iri: https://onerecord.iata.org/ns/cargo#productDescription
    productDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#productDescription")
class Characteristic(BaseModel):
    # label: characteristicType
    # comment: Product characteristics code - e.g. CLR - Color. Not restricted to a list.
    # iri: https://onerecord.iata.org/ns/cargo#characteristicType
    characteristicType: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#characteristicType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")
class Check(LogisticsAction):
    # label: checkTotalResult
    # comment: Reference to the result of the Check
    # iri: https://onerecord.iata.org/ns/cargo#checkTotalResult
    checkTotalResult: Optional[CheckTotalResult] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checkTotalResult")
    # label: checkedObject
    # comment: Reference to the checked Object
    # iri: https://onerecord.iata.org/ns/cargo#checkedObject
    checkedObject: Optional[LogisticsObject] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checkedObject")
    # label: checker
    # comment: Reference to the Actor performing the Check
    # iri: https://onerecord.iata.org/ns/cargo#checker
    checker: Optional[Actor] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checker")
    # label: usedTemplate
    # comment: Reference to the Template used in the Check
    # iri: https://onerecord.iata.org/ns/cargo#usedTemplate
    usedTemplate: Optional[CheckTemplate] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#usedTemplate")
class CheckTemplate(LogisticsObject):
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: legacyTemplate
    # comment: Reference to an ExternalReference holding a legacy template outside of ONE Record, such as a photo or pdf of a checksheet
    # iri: https://onerecord.iata.org/ns/cargo#legacyTemplate
    legacyTemplate: Optional[ExternalReference] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#legacyTemplate")
    # label: questions
    # comment: References to all Questions that are part of this template
    # iri: https://onerecord.iata.org/ns/cargo#questions
    questions: List[Question] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#questions")
    # label: usedInCheck
    # comment: Reference to the Check the template was used in
    # iri: https://onerecord.iata.org/ns/cargo#usedInCheck
    usedInCheck: Optional[Check] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#usedInCheck")
    # label: date
    # comment: DateTime on which the CheckTemplate was released
    # iri: https://onerecord.iata.org/ns/cargo#date
    date: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#date")
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#name")
    # label: templatePurpose
    # comment: Purpose of the template
    # iri: https://onerecord.iata.org/ns/cargo#templatePurpose
    templatePurpose: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#templatePurpose")
    # label: version
    # comment: Version of the template
    # iri: https://onerecord.iata.org/ns/cargo#version
    version: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#version")
class CheckTotalResult(LogisticsObject):
    # label: certifiedByActor
    # comment: Reference to the Actor certifying the result of the Check if required
    # iri: https://onerecord.iata.org/ns/cargo#certifiedByActor
    certifiedByActor: Optional[Person] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#certifiedByActor")
    # label: resultOfCheck
    # iri: https://onerecord.iata.org/ns/cargo#resultOfCheck
    resultOfCheck: Optional[Check] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#resultOfCheck")
    # label: resultValue
    # comment: Information about a result Value of any kind of the Check
    # iri: https://onerecord.iata.org/ns/cargo#resultValue
    resultValue: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#resultValue")
    # label: checkRemark
    # comment: Free text remarks to the check result
    # iri: https://onerecord.iata.org/ns/cargo#checkRemark
    checkRemark: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checkRemark")
    # label: passed
    # comment: Boolean indicating whether the Check was passed
    # iri: https://onerecord.iata.org/ns/cargo#passed
    passed: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#passed")
class CodeListElement(BaseModel):
    # label: code
    # comment: Code or short version of a code, for example "CH" for Switzerland when referring to the UN/LOCODE code list
    # iri: https://onerecord.iata.org/ns/cargo#code
    code: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#code")
    # label: codeDescription
    # comment: Description or long version of the code, for example "Switzerland" for Switzerland when referring to the UN/LOCODE code list
    # iri: https://onerecord.iata.org/ns/cargo#codeDescription
    codeDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#codeDescription")
    # label: codeLevel
    # comment: Integer indicating the level of a code if a codelists is hierarchical, for example HS-Codes
    # iri: https://onerecord.iata.org/ns/cargo#codeLevel
    codeLevel: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#codeLevel")
    # label: codeListName
    # comment: Official name of the code list without version number when direct reference is not possible, for example "UN/LOCODE" when referring to the UN/LOCODE code list
    # iri: https://onerecord.iata.org/ns/cargo#codeListName
    codeListName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#codeListName")
    # label: codeListReference
    # comment: URL to access the code list the code is taken from, for example "https://unece.org/trade/cefact/unlocode-code-list-country-and-territory" for UN/LOCODE.
    # iri: https://onerecord.iata.org/ns/cargo#codeListReference
    codeListReference: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#codeListReference")
    # label: codeListVersion
    # comment: Version of the code list, for example "223-1" for UN/LOCODE. Used if the property codeListName is used or the version is not apparent from the resource referred to in property codeListReference.
    # iri: https://onerecord.iata.org/ns/cargo#codeListVersion
    codeListVersion: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#codeListVersion")
class Company(Organization):
    # label: iataCargoAgentCode
    # comment: IATA accredited cargo agent 7 digit number
    # iri: https://onerecord.iata.org/ns/cargo#iataCargoAgentCode
    iataCargoAgentCode: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentCode")
    # label: iataCargoAgentLocationIdentifier
    # comment: IATA CASS cargo agent 4 digit branch number / location identifier
    # iri: https://onerecord.iata.org/ns/cargo#iataCargoAgentLocationIdentifier
    iataCargoAgentLocationIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentLocationIdentifier")
class Composing(LogisticsAction):
    # label: composedMaterials
    # comment: References to the Materials being built-up or broken-down
    # iri: https://onerecord.iata.org/ns/cargo#composedMaterials
    composedMaterials: List[LoadingMaterial] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#composedMaterials")
    # label: composedPieces
    # comment: References to the Pieces being built-up or broken-down
    # iri: https://onerecord.iata.org/ns/cargo#composedPieces
    composedPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#composedPieces")
    # label: compositionType
    # comment: Enum stating whether the CompositionAction describes build-up or break-down
    # iri: https://onerecord.iata.org/ns/cargo#compositionType
    compositionType: Optional[CompositionType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#compositionType")
    # label: onLoadingUnit
    # comment: Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    # iri: https://onerecord.iata.org/ns/cargo#loadingUnit
    loadingUnit: Optional[LoadingUnit] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingUnit")
class CompositionType(str, Enum):
    """
    label: CompositionType
    comment: Restricted code list for Composing subtypes
    """
    # label: COMPOSITION
    # comment: Describes a composition, for example the loading of a container or the build-up of an ULD
    COMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#COMPOSITION")
    # label: DECOMPOSITION
    # comment: Describes a decomposition, for example the unloading of a container or the break-down of an ULD
    DECOMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#DECOMPOSITION")
class ContactDetail(BaseModel):
    # label: contactDetailType
    # comment: Type of the contact details, e.g. Phone number, Mail address
    # iri: https://onerecord.iata.org/ns/cargo#contactDetailType
    contactDetailType: Optional[ContactDetailType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetailType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")
class ContactDetailType(CodeListElement):
    ...
class ContactRole(CodeListElement):
    ...
class CurrencyValue(BaseModel):
    # label: currencyUnit
    # comment: Information about the currency used in a CurrencyValue. Create an instance of CurrencyCode based on ISO 4217
    # iri: https://onerecord.iata.org/ns/cargo#currencyUnit
    currencyUnit: Optional[CurrencyCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#currencyUnit")
    # label: numericalValue
    # comment: Numerical value
    # iri: https://onerecord.iata.org/ns/cargo#numericalValue
    numericalValue: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue")
class CustomsInformation(LogisticsObject):
    # label: contentCode
    # comment: Customs, Security and Regulatory Control Information Identifier. Coded indicator qualifying Customs related information: Item Number "I", Exemption Legend "L", System Downtime Reference "S", Unique Consignment Reference Number "U", Movement Reference Number "M" . Refers to Code List 1.1. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    # iri: https://onerecord.iata.org/ns/cargo#contentCode
    contentCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#contentCode")
    # label: country
    # comment: Country details. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#country
    country: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#country")
    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForPiece
    issuedForPiece: Optional[Piece] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece")
    # label: issuedForShipment
    # comment: Reference to the shipment the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForShipment
    issuedForShipment: Optional[Shipment] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForShipment")
    # label: subjectCode
    # comment: Information Identifier. Code identifying a piece of information/entity e.g. "IMP" for import, "EXP" for export, "AGT" for Agent, "ISS" for The Regulated Agent Issuing the Security Status for a Consignment etc. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    # iri: https://onerecord.iata.org/ns/cargo#subjectCode
    subjectCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#subjectCode")
    # label: note
    # comment: Free text for customs remarks, not used in OCI Composition Rules Table
    # iri: https://onerecord.iata.org/ns/cargo#note
    note: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#note")
    # label: ociLineNumber
    # comment: Integer holding the oci line number when upcasting multi-line oci structures from CIMP/CXML
    # iri: https://onerecord.iata.org/ns/cargo#ociLineNumber
    ociLineNumber: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#ociLineNumber")
    # label: otherCustomsInformation
    # comment: Supplementary Customs, Security and Regulatory Control Information
    # iri: https://onerecord.iata.org/ns/cargo#otherCustomsInformation
    otherCustomsInformation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#otherCustomsInformation")
class DgDeclaration(LogisticsObject):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: declarationPlace
    # comment: Reference to the Location the DgDeclaration was declared at
    # iri: https://onerecord.iata.org/ns/cargo#declarationPlace
    declarationPlace: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#declarationPlace")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForPiece
    issuedForPiece: Optional[Piece] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece")
    # label: aircraftLimitationInformation
    # comment: Contains the Special Handling Code related to the prescribed limitation. Hardcoded to PASSENGER AND CARGO AIRCRAFT or CARGO AIRCRAFT ONLY. This field is mandatory for air (Air) 
    # iri: https://onerecord.iata.org/ns/cargo#aircraftLimitationInformation
    aircraftLimitationInformation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#aircraftLimitationInformation")
    # label: complianceDeclarationText
    # comment: Contains the warning message complying with the regulations text note. This field is mandatory for air (Air) 
    # iri: https://onerecord.iata.org/ns/cargo#complianceDeclarationText
    complianceDeclarationText: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#complianceDeclarationText")
    # label: declarationDate
    # comment: Date and time at which the DgDeclaration was declared
    # iri: https://onerecord.iata.org/ns/cargo#declarationDate
    declarationDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#declarationDate")
    # label: exclusiveUseIndicator
    # comment: Indicates an exclusive use shipment
    # iri: https://onerecord.iata.org/ns/cargo#exclusiveUseIndicator
    exclusiveUseIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#exclusiveUseIndicator")
    # label: handlingInformation
    # comment: Free text. This may include items such as Control temperature for substances stabilized by temperature control, name and telephone number of a responsible person for infectious substances. 
    # iri: https://onerecord.iata.org/ns/cargo#handlingInformation
    handlingInformation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#handlingInformation")
    # label: shipperDeclarationText
    # comment: Contains the shipper's declaration to comply with the regulations text note. Free text . This field is mandatory for air (Air)
    # iri: https://onerecord.iata.org/ns/cargo#shipperDeclarationText
    shipperDeclarationText: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shipperDeclarationText")
    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    # iri: https://onerecord.iata.org/ns/cargo#shippingRefNo
    shippingRefNo: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo")
class DgProductRadioactive(LogisticsObject):
    # label: dgRaTypeCode
    # comment: The category of the package or all packed in one. Complete text to be transmitted: I-White, II-Yellow, III-Yellow instead of I, II, III
    # iri: https://onerecord.iata.org/ns/cargo#dgRaTypeCode
    dgRaTypeCode: Optional[RaTypeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#dgRaTypeCode")
    # label: forProductDg
    # comment: Reference to the ProductDg this DgProductRadioactive details
    # iri: https://onerecord.iata.org/ns/cargo#forProductDg
    forProductDg: Optional[ProductDg] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#forProductDg")
    # label: isotopes
    # comment: DgRadioactiveIsotope.
    # iri: https://onerecord.iata.org/ns/cargo#isotopes
    isotopes: List[DgRadioactiveIsotope] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#isotopes")
    # label: fissileExceptionIndicator
    # comment: Indicates if Fissile is excepted
    # iri: https://onerecord.iata.org/ns/cargo#fissileExceptionIndicator
    fissileExceptionIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#fissileExceptionIndicator")
    # label: fissileExceptionReference
    # comment: Fissile exception reference, mandatory if Fissile Exception Indicator is true.
    # iri: https://onerecord.iata.org/ns/cargo#fissileExceptionReference
    fissileExceptionReference: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#fissileExceptionReference")
    # label: transportIndexNumeric
    # comment: Radioactive Transport-Index value of the package or all packed in one. Conditionally mandatory and applies to categories II-Yellow and III-Yellow only; field only contains the value, if printed, TI must be added as a prefix to the value  to be printed in the Packing Instructions column
    # iri: https://onerecord.iata.org/ns/cargo#transportIndexNumeric
    transportIndexNumeric: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportIndexNumeric")
class DgRadioactiveIsotope(LogisticsObject):
    # label: contentOfDgProductRadioactive
    # comment: Reference to the DgProductRadioactive this Isotope is contained in
    # iri: https://onerecord.iata.org/ns/cargo#contentOfDgProductRadioactive
    contentOfDgProductRadioactive: Optional[DgProductRadioactive] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#contentOfDgProductRadioactive")
    # label: physicalChemicalForm
    # comment: A description of the physical and chemical form of the material.
    # iri: https://onerecord.iata.org/ns/cargo#physicalChemicalForm
    physicalChemicalForm: Optional[RadioactiveMaterialClassification] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#physicalChemicalForm")
    # label: activityLevelMeasure
    # comment: Numeric expression of the activity of a radioactive Item
    # iri: https://onerecord.iata.org/ns/cargo#activityLevelMeasure
    activityLevelMeasure: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#activityLevelMeasure")
    # label: criticalitySafetyIndexNumeric
    # comment: Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.
    # iri: https://onerecord.iata.org/ns/cargo#criticalitySafetyIndexNumeric
    criticalitySafetyIndexNumeric: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#criticalitySafetyIndexNumeric")
    # label: isotopeId
    # comment: Id of each radionuclide or for mixtures of radionuclides.
    # iri: https://onerecord.iata.org/ns/cargo#isotopeId
    isotopeId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#isotopeId")
    # label: isotopeName
    # comment: The name or symbol of each radionuclide or for mixtures of radionuclides, an appropriate general description, or a list of the most restrictive radionuclides. 
    # iri: https://onerecord.iata.org/ns/cargo#isotopeName
    isotopeName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#isotopeName")
    # label: lowDispersibleIndicator
    # comment: A notation that the material is low dispersible radioactive material.
    # iri: https://onerecord.iata.org/ns/cargo#lowDispersibleIndicator
    lowDispersibleIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#lowDispersibleIndicator")
    # label: specialFormIndicator
    # comment: A notation that the material is special form
    # iri: https://onerecord.iata.org/ns/cargo#specialFormIndicator
    specialFormIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#specialFormIndicator")
class Dimensions(BaseModel):
    # label: height
    # comment: Height
    # iri: https://onerecord.iata.org/ns/cargo#height
    height: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#height")
    # label: length
    # comment: Length
    # iri: https://onerecord.iata.org/ns/cargo#length
    length: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#length")
    # label: volume
    # comment: Volume
    # iri: https://onerecord.iata.org/ns/cargo#volume
    volume: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#volume")
    # label: width
    # comment: Width
    # iri: https://onerecord.iata.org/ns/cargo#width
    width: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#width")
class DirectionType(str, Enum):
    """
    label: DirectionType
    comment: Restricted code list for the direction of a MovementTime
    """
    # label: INBOUND
    # comment: Indicates the described direction in a movement time as inbound
    INBOUND = URIRef("https://onerecord.iata.org/ns/cargo#INBOUND")
    # label: OUTBOUND
    # comment: Indicates the described direction in a movement time as outbound
    OUTBOUND = URIRef("https://onerecord.iata.org/ns/cargo#OUTBOUND")
    # label: UNPLANNED_STOP
    # comment: Indicates the that the movement time describes an unplanned stop
    UNPLANNED_STOP = URIRef("https://onerecord.iata.org/ns/cargo#UNPLANNED_STOP")
class EpermitConsignment(LogisticsObject):
    # label: consignmentItems
    # comment: Reference to te pieces (Live Animals) of the permit
    # iri: https://onerecord.iata.org/ns/cargo#consignmentItems
    consignmentItems: Optional[PieceLiveAnimals] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#consignmentItems")
    # label: epermit
    # comment: Reference to the Epermit of the consignment
    # iri: https://onerecord.iata.org/ns/cargo#epermit
    epermit: Optional[LiveAnimalsEpermit] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#epermit")
    # label: examiningQuantity
    # comment: Quantity measured by the examining authority (box 14)
    # iri: https://onerecord.iata.org/ns/cargo#examiningQuantity
    examiningQuantity: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#examiningQuantity")
    # label: usedToDateQuotaQuantity
    # comment: total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    # iri: https://onerecord.iata.org/ns/cargo#usedToDateQuotaQuantity
    usedToDateQuotaQuantity: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#usedToDateQuotaQuantity")
class EpermitSignature(LogisticsObject):
    # label: forEpermit
    # comment: Reference to the LiveAnimalsEpermit this Signature applies to
    # iri: https://onerecord.iata.org/ns/cargo#forEpermit
    forEpermit: Optional[LiveAnimalsEpermit] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#forEpermit")
    # label: signatoryCompany
    # comment: Signatory company name
    # iri: https://onerecord.iata.org/ns/cargo#signatoryCompany
    signatoryCompany: Optional[Company] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryCompany")
    # label: signatoryRole
    # comment: Role of the signatory with regards to the ePermit: Applicant, Permit issuer, Issuing Authority or Examining authority
    # iri: https://onerecord.iata.org/ns/cargo#signatoryRole
    signatoryRole: Optional[SignatoryRole] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryRole")
    # label: signatureTypeCode
    # comment: Code specifying a type of government action such as inspection, detention, fumigation, security.
    # iri: https://onerecord.iata.org/ns/cargo#signatureTypeCode
    signatureTypeCode: Optional[SignatureTypeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#signatureTypeCode")
    # label: securityStampId
    # comment: Security Stamp ID
    # iri: https://onerecord.iata.org/ns/cargo#securityStampId
    securityStampId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#securityStampId")
    # label: signatureDate
    # comment: Date and time of the signature
    # iri: https://onerecord.iata.org/ns/cargo#signatureDate
    signatureDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#signatureDate")
    # label: signatureStatement
    # comment: Signatory signature authentication text
    # iri: https://onerecord.iata.org/ns/cargo#signatureStatement
    signatureStatement: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#signatureStatement")
class EventTimeType(str, Enum):
    """
    label: EventTimeType
    comment: Restricted code list for acceptable event times
    """
    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: ESTIMATED
    # comment: Used when a time is estimated
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")
    # label: EXPECTED
    # comment: Used when a time is expected
    EXPECTED = URIRef("https://onerecord.iata.org/ns/cargo#EXPECTED")
    # label: PLANNED
    # comment: Used when a time is planned
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")
    # label: REQUESTED
    # comment: Used when a time is requested
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")
class ExecutionStatus(str, Enum):
    """
    label: ExecutionStatus
    comment: Restricted code list for the execution status of activities
    """
    # label: ACTIVE
    # comment: Used when a LogisticsActivity is active
    ACTIVE = URIRef("https://onerecord.iata.org/ns/cargo#ACTIVE")
    # label: CANCELLED
    # comment: Used when a LogisticsActivity is cancelled
    CANCELLED = URIRef("https://onerecord.iata.org/ns/cargo#CANCELLED")
    # label: COMPLETE
    # comment: Used when a LogisticsActivity is complete
    COMPLETE = URIRef("https://onerecord.iata.org/ns/cargo#COMPLETE")
    # label: PENDING
    # comment: Used when a LogisticsActivity is pending
    PENDING = URIRef("https://onerecord.iata.org/ns/cargo#PENDING")
class ExternalReference(LogisticsObject):
    # label: createdAtLocation
    # comment: Location of the document, e.g. location where the document was emitted
    # iri: https://onerecord.iata.org/ns/cargo#createdAtLocation
    createdAtLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#createdAtLocation")
    # label: originator
    # comment: Document originator details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#originator
    originator: Optional[Company] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#originator")
    # label: referenceForObjects
    # comment: References to the LogisticsObjects referring to this external reference
    # iri: https://onerecord.iata.org/ns/cargo#referenceForObjects
    referenceForObjects: List[LogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#referenceForObjects")
    # label: checksum
    # comment: Checksum of the document to validate its integrity
    # iri: https://onerecord.iata.org/ns/cargo#checksum
    checksum: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checksum")
    # label: documentIdentifier
    # comment: Unique document identifier
    # iri: https://onerecord.iata.org/ns/cargo#documentIdentifier
    documentIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#documentIdentifier")
    # label: documentLink
    # comment: Link to the document, e.g. URL of the file where it is hosted
    # iri: https://onerecord.iata.org/ns/cargo#documentLink
    documentLink: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#documentLink")
    # label: documentName
    # comment: If no DocumentType provided, name of the referenced document 
    # iri: https://onerecord.iata.org/ns/cargo#documentName
    documentName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#documentName")
    # label: documentType
    # comment: Type of the referenced document . Can refer UNEDIFACT 11  e.g. 740 - Air Waybill, but not limited to
    # iri: https://onerecord.iata.org/ns/cargo#documentType
    documentType: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#documentType")
    # label: documentVersion
    # comment: Document version number
    # iri: https://onerecord.iata.org/ns/cargo#documentVersion
    documentVersion: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#documentVersion")
    # label: validFrom
    # comment: Validity start date based on usage context
    # iri: https://onerecord.iata.org/ns/cargo#validFrom
    validFrom: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#validFrom")
    # label: validUntil
    # comment: Validity end date (date of expiry) based on usage context
    # iri: https://onerecord.iata.org/ns/cargo#validUntil
    validUntil: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#validUntil")
class Geolocation(BaseModel):
    # label: elevation
    # comment: Elevation from sea level - Change of data type to Value as of ontology v1.1
    # iri: https://onerecord.iata.org/ns/cargo#elevation
    elevation: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#elevation")
    # label: latitude
    # comment: Location latitude decimal
    # iri: https://onerecord.iata.org/ns/cargo#latitude
    latitude: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#latitude")
    # label: longitude
    # comment: Location longitude decimal
    # iri: https://onerecord.iata.org/ns/cargo#longitude
    longitude: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#longitude")
class HandlingService(LogisticsService):
    # label: handlingServiceFor
    # iri: https://onerecord.iata.org/ns/cargo#handlingServiceFor
    handlingServiceFor: List[PhysicalLogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#handlingServiceFor")
    # label: serviceForWaybills
    # comment: Reference to the Waybills this service is to be performed for. To be used if a service is to be performed for a specific shipment or set of
    # iri: https://onerecord.iata.org/ns/cargo#serviceForWaybills
    serviceForWaybills: List[Waybill] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#serviceForWaybills")
    # label: serviceProvider
    # comment: Reference to the Party providing the service
    # iri: https://onerecord.iata.org/ns/cargo#serviceProvider
    serviceProvider: Optional[Party] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serviceProvider")
    # label: serviceRequestor
    # comment: Reference to the Party requesting the service
    # iri: https://onerecord.iata.org/ns/cargo#serviceRequestor
    serviceRequestor: Optional[Party] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serviceRequestor")
class Insurance(LogisticsObject):
    # label: coveringOrganization
    # comment: Party covering the insurance 
    # iri: https://onerecord.iata.org/ns/cargo#coveringOrganization
    coveringOrganization: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#coveringOrganization")
    # label: insuredAmount
    # comment: Insured amount - amount covered by the insurance policy
    # iri: https://onerecord.iata.org/ns/cargo#insuredAmount
    insuredAmount: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#insuredAmount")
    # label: insuredShipments
    # comment: Reference to the shipments insured
    # iri: https://onerecord.iata.org/ns/cargo#insuredShipments
    insuredShipments: List[Shipment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#insuredShipments")
class IotDevice(PhysicalLogisticsObject):
    # label: attachedToObject
    # comment: Reference to the PhysicalLogisticsObject the IotDevice is attached to
    # iri: https://onerecord.iata.org/ns/cargo#attachedToObject
    attachedToObject: Optional[PhysicalLogisticsObject] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#attachedToObject")
    # label: connectedSensors
    # comment: Reference to the sensors linked to the device
    # iri: https://onerecord.iata.org/ns/cargo#connectedSensors
    connectedSensors: List[Sensor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#connectedSensors")
    # label: manufacturer
    # comment: Manufacturing company details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#manufacturer
    manufacturer: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
    # label: deviceModel
    # comment: Commercial denomination of the device
    # iri: https://onerecord.iata.org/ns/cargo#deviceModel
    deviceModel: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#deviceModel")
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#name")
    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    # iri: https://onerecord.iata.org/ns/cargo#serialNumber
    serialNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber")
class Item(PhysicalLogisticsObject):
    # label: dimensions
    # comment: Dimensions details
    # iri: https://onerecord.iata.org/ns/cargo#dimensions
    dimensions: Optional[Dimensions] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#dimensions")
    # label: inPiece
    # comment: Reference to the Piece this Item or Piece is contained in
    # iri: https://onerecord.iata.org/ns/cargo#inPiece
    inPiece: Optional[Piece] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#inPiece")
    # label: itemQuantity
    # comment: Quantity of the item when applicable, with associated units of measure
    # iri: https://onerecord.iata.org/ns/cargo#itemQuantity
    itemQuantity: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#itemQuantity")
    # label: ofProduct
    # comment: Reference to the Product describing the Item
    # iri: https://onerecord.iata.org/ns/cargo#ofProduct
    ofProduct: Optional[Product] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#ofProduct")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: productionCountry
    # comment: Production country details. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#productionCountry
    productionCountry: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#productionCountry")
    # label: targetCountry
    # comment: Item target country. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#targetCountry
    targetCountry: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#targetCountry")
    # label: unitPrice
    # comment: Product price per unit in the base
    # iri: https://onerecord.iata.org/ns/cargo#unitPrice
    unitPrice: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unitPrice")
    # label: weight
    # comment: Weight of the item
    # iri: https://onerecord.iata.org/ns/cargo#weight
    weight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#weight")
    # label: batchNumber
    # comment: Production batch number / reference
    # iri: https://onerecord.iata.org/ns/cargo#batchNumber
    batchNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#batchNumber")
    # label: expiryDate
    # comment: Product expiry date - e.g. for perishables goods or goods with programmed obsolescence
    # iri: https://onerecord.iata.org/ns/cargo#expiryDate
    expiryDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#expiryDate")
    # label: lotNumber
    # comment: Production lot number / reference
    # iri: https://onerecord.iata.org/ns/cargo#lotNumber
    lotNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#lotNumber")
    # label: productionDate
    # comment: Production date
    # iri: https://onerecord.iata.org/ns/cargo#productionDate
    productionDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#productionDate")
    # label: quantityForUnitPrice
    # comment: Product quantity for unit price - e.g. 12 (eggs for one USD 1)
    # iri: https://onerecord.iata.org/ns/cargo#quantityForUnitPrice
    quantityForUnitPrice: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#quantityForUnitPrice")
class ItemDg(Item):
    # label: emergencyContact
    # comment: Contains the Emergency contact name (e.g. the name of the agency) and phone number (min required)
    # iri: https://onerecord.iata.org/ns/cargo#emergencyContact
    emergencyContact: Optional[Person] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#emergencyContact")
    # label: netWeightMeasure
    # comment: The total net weight of dangerous goods transported of this line item. For air transport the value must be the volume or mass in each package.
    # iri: https://onerecord.iata.org/ns/cargo#netWeightMeasure
    netWeightMeasure: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#netWeightMeasure")
    # label: reportableQuantity
    # comment: Reportable quantities, To and from the USA only
    # iri: https://onerecord.iata.org/ns/cargo#reportableQuantity
    reportableQuantity: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#reportableQuantity")
    # label: supplementaryInfoPrefix
    # comment: Additional information that may be added in addition to the proper shipping name to more fully describe the goods or to identify a particular condition
    # iri: https://onerecord.iata.org/ns/cargo#supplementaryInfoPrefix
    supplementaryInfoPrefix: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#supplementaryInfoPrefix")
    # label: supplementaryInfoSuffix
    # comment: Additional information that may be added in addition to the proper shipping to more fully describe the goods or to identify a particular condition
    # iri: https://onerecord.iata.org/ns/cargo#supplementaryInfoSuffix
    supplementaryInfoSuffix: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#supplementaryInfoSuffix")
class LineItemPackage(BaseModel):
    # label: packageGrossWeight
    # comment: Information about the total weight of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageGrossWeight
    packageGrossWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packageGrossWeight")
    # label: packageVolume
    # comment: Information about the total volume of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageVolume
    packageVolume: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packageVolume")
    # label: pieceReferences
    # comment: References to Pieces for which a rate applies
    # iri: https://onerecord.iata.org/ns/cargo#pieceReferences
    pieceReferences: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceReferences")
    # label: packageSlac
    # comment: Integer holding the total slac of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageSlac
    packageSlac: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packageSlac")
class LiveAnimalsEpermit(LogisticsObject):
    # label: consignee
    # comment: Reference to the Organization that fulfills the role of the consignee, for a LiveAnimalsEpermit it has to include complete name and address (box 3)
    # iri: https://onerecord.iata.org/ns/cargo#consignee
    consignee: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#consignee")
    # label: consignments
    # comment: Reference to the pieces and properties linked to the Permit (box 7 to 12)
    # iri: https://onerecord.iata.org/ns/cargo#consignments
    consignments: List[EpermitConsignment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#consignments")
    # label: permitTypeCode
    # comment: Code specifying the document name. (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#permitTypeCode
    permitTypeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#permitTypeCode")
    # label: signatures
    # comment: List of all the signatures of the Epermit (applicant box 4, issuing authority box 6, issuer box 13 and examining authority box 14)
    # iri: https://onerecord.iata.org/ns/cargo#signatures
    signatures: List[EpermitSignature] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#signatures")
    # label: transactionPurposeCode
    # comment: Code indicating the purpose of the transaction (box 5a)
    # iri: https://onerecord.iata.org/ns/cargo#transactionPurposeCode
    transactionPurposeCode: Optional[TransactionPurposeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transactionPurposeCode")
    # label: transportContractTypeCode
    # comment: Code specifying the transport document name (box 15)
    # iri: https://onerecord.iata.org/ns/cargo#transportContractTypeCode
    transportContractTypeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportContractTypeCode")
    # label: copyIndicator
    # comment: Indicates if the permit is a copy (true) or an original (false) (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#copyIndicator
    copyIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#copyIndicator")
    # label: epermitNumber
    # comment: The original number is a unique number allocated to each document by the relevant Management Authority. (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#epermitNumber
    epermitNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#epermitNumber")
    # label: permitTypeOtherDescription
    # comment: Description if TypeCode is Other (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#permitTypeOtherDescription
    permitTypeOtherDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#permitTypeOtherDescription")
    # label: specialConditions
    # comment: Special conditions (box 5)
    # iri: https://onerecord.iata.org/ns/cargo#specialConditions
    specialConditions: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#specialConditions")
    # label: transactionPurpose
    # comment: Purpose of the transaction in free text (box 5a)
    # iri: https://onerecord.iata.org/ns/cargo#transactionPurpose
    transactionPurpose: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transactionPurpose")
    # label: transportContractId
    # comment: Reference to the Air Waybill or other transport contract document (box 15)
    # iri: https://onerecord.iata.org/ns/cargo#transportContractId
    transportContractId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportContractId")
    # label: validFrom
    # comment: Validity start date based on usage context
    # iri: https://onerecord.iata.org/ns/cargo#validFrom
    validFrom: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#validFrom")
    # label: validUntil
    # comment: Validity end date (date of expiry) based on usage context
    # iri: https://onerecord.iata.org/ns/cargo#validUntil
    validUntil: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#validUntil")
class LoadType(str, Enum):
    """
    label: LoadType
    comment: Restricted code list for the Load Type of a piece or shipment
    """
    # label: BULK
    # comment: Indicates the load type as bulk
    BULK = URIRef("https://onerecord.iata.org/ns/cargo#BULK")
    # label: LOOSE
    # comment: Indicates the load type as loose
    LOOSE = URIRef("https://onerecord.iata.org/ns/cargo#LOOSE")
    # label: PALLET
    # comment: Indicates the load type as pallet
    PALLET = URIRef("https://onerecord.iata.org/ns/cargo#PALLET")
    # label: UNIT_LOAD_DEVICE
    # comment: Indicates the load type as uld
    UNIT_LOAD_DEVICE = URIRef("https://onerecord.iata.org/ns/cargo#UNIT_LOAD_DEVICE")
class Loading(LogisticsAction):
    # label: loadedMaterials
    # comment: References to Materials onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#loadedMaterials
    loadedMaterials: List[LoadingMaterial] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadedMaterials")
    # label: loadedPieces
    # comment: References to Pieces onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#loadedPieces
    loadedPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadedPieces")
    # label: loadedUnits
    # comment: References to LoadingUnits onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#loadedUnits
    loadedUnits: List[LoadingUnit] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadedUnits")
    # label: loadingType
    # comment: Enum stating whether the LoadingAction describes onloading or offloading
    # iri: https://onerecord.iata.org/ns/cargo#loadingType
    loadingType: Optional[LoadingType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingType")
    # label: onTransportMeans
    # comment: Reference to the TransportMeans that is being onloaded or offloaded
    # iri: https://onerecord.iata.org/ns/cargo#onTransportMeans
    onTransportMeans: Optional[TransportMeans] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#onTransportMeans")
    # label: loadingPositionIdentifier
    # comment: Short text stating the loading position in the TransportMeans
    # iri: https://onerecord.iata.org/ns/cargo#loadingPositionIdentifier
    loadingPositionIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingPositionIdentifier")
class LoadingMaterial(PhysicalLogisticsObject):
    # label: manufacturer
    # comment: Manufacturing company details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#manufacturer
    manufacturer: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
    # label: materialModel
    # comment: Model of the LoadingMaterial if any
    # iri: https://onerecord.iata.org/ns/cargo#materialModel
    materialModel: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#materialModel")
    # label: materialType
    # comment: Type of the LoadingMaterial
    # iri: https://onerecord.iata.org/ns/cargo#materialType
    materialType: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#materialType")
    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    # iri: https://onerecord.iata.org/ns/cargo#serialNumber
    serialNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber")
class LoadingType(str, Enum):
    """
    label: LoadingType
    comment: Restricted code list for Loading subtypes
    """
    # label: LOADING
    # comment: Describes a loading process, for example putting an ULD on an aircraft or a piece in a truck
    LOADING = URIRef("https://onerecord.iata.org/ns/cargo#LOADING")
    # label: UNLOADING
    # comment: Describes an unloading process, for example removing an ULD from an aircraft or a piece from a truck
    UNLOADING = URIRef("https://onerecord.iata.org/ns/cargo#UNLOADING")
class LoadingUnit(PhysicalLogisticsObject):
    # label: inUnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#inUnitComposition
    inUnitComposition: Optional[UnitComposition] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#inUnitComposition")
    # label: tareWeight
    # comment: Tare weight of the empty ULD
    # iri: https://onerecord.iata.org/ns/cargo#tareWeight
    tareWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#tareWeight")
    # label: remarks
    # comment: Remarks or Supplement Information
    # iri: https://onerecord.iata.org/ns/cargo#remarks
    remarks: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#remarks")
class Location(PhysicalLogisticsObject):
    # label: address
    # comment: Address details
    # iri: https://onerecord.iata.org/ns/cargo#address
    address: Optional[Address] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#address")
    # label: geolocation
    # comment: Geolocation details
    # iri: https://onerecord.iata.org/ns/cargo#geolocation
    geolocation: Optional[Geolocation] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#geolocation")
    # label: locationCodes
    # comment: Location code of airport, freight terminal, seaport, rail station. UN/LOCODE city code (5 letter) or IATA airport code (3 letter)
    # iri: https://onerecord.iata.org/ns/cargo#locationCodes
    locationCodes: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#locationCodes")
    # label: onsiteActions
    # comment: References to the Actions happening at the Location
    # iri: https://onerecord.iata.org/ns/cargo#onsiteActions
    onsiteActions: List[LogisticsAction] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#onsiteActions")
    # comment: Reference to the Location this is a Sublocation of
    # iri: https://onerecord.iata.org/ns/cargo#subLocationOf
    subLocationOf: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#subLocationOf")
    # comment: References to Sublocations that describe the Location in more detail
    # iri: https://onerecord.iata.org/ns/cargo#subLocations
    subLocations: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#subLocations")
    # label: locationName
    # comment: Full name of the location
    # iri: https://onerecord.iata.org/ns/cargo#locationName
    locationName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#locationName")
    # label: locationType
    # comment: Location type - e.g. Airport, Freight terminal, Rail station, Seaport, etc
    # iri: https://onerecord.iata.org/ns/cargo#locationType
    locationType: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#locationType")
class LogisticsAction(LogisticsObject):
    # label: actionTimeType
    # comment: Enum stating the type of the Action
    # iri: https://onerecord.iata.org/ns/cargo#actionTimeType
    actionTimeType: Optional[ActionTimeType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#actionTimeType")
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails")
    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    # iri: https://onerecord.iata.org/ns/cargo#contactPersons
    contactPersons: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: performedAt
    # comment: Reference to the Location the Action was performed at
    # iri: https://onerecord.iata.org/ns/cargo#performedAt
    performedAt: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#performedAt")
    # label: servedActivity
    # comment: Reference to the Activity the Action was performed for
    # iri: https://onerecord.iata.org/ns/cargo#servedActivity
    servedActivity: Optional[LogisticsActivity] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#servedActivity")
    # label: actionEndTime
    # comment: DateTime holding the end time of the Action; Type is indicated through ActionType property
    # iri: https://onerecord.iata.org/ns/cargo#actionEndTime
    actionEndTime: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#actionEndTime")
    # label: actionStartTime
    # comment: DateTime holding the start time of the Action; Type is indicated through ActionType property
    # iri: https://onerecord.iata.org/ns/cargo#actionStartTime
    actionStartTime: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#actionStartTime")
class LogisticsActivity(LogisticsObject):
    # label: checkActions
    # comment: References to CheckActions performed for the Activity
    # iri: https://onerecord.iata.org/ns/cargo#checkActions
    checkActions: List[Check] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checkActions")
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails")
    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    # iri: https://onerecord.iata.org/ns/cargo#contactPersons
    contactPersons: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons")
    # label: executionStatus
    # comment: Enum stating the status of the Activity
    # iri: https://onerecord.iata.org/ns/cargo#executionStatus
    executionStatus: Optional[ExecutionStatus] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#executionStatus")
    # label: servedServices
    # comment: Reference to Services this Activity is executed for
    # iri: https://onerecord.iata.org/ns/cargo#servedServices
    servedServices: List[LogisticsService] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#servedServices")
class LogisticsAgent(LogisticsObject):
    ...
class LogisticsEvent(BaseModel):
    # label: eventCode
    # comment: Movement or milestone code. Can hold a named individual of the StatusCode core code list (corresponding to cXML code list 1.18), but can also be referring to different code lists.
    # iri: https://onerecord.iata.org/ns/cargo#eventCode
    eventCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#eventCode")
    # label: eventFor
    # comment: Refers to the URI of the linked object(s)
    # iri: https://onerecord.iata.org/ns/cargo#eventFor
    eventFor: Optional[LogisticsObject] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#eventFor")
    # label: eventLocation
    # comment: Location of event
    # iri: https://onerecord.iata.org/ns/cargo#eventLocation
    eventLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#eventLocation")
    # label: eventTimeType
    # comment: Indicates type of event e.g.  Scheduled, Estimated, Actual
    # iri: https://onerecord.iata.org/ns/cargo#eventTimeType
    eventTimeType: Optional[EventTimeType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#eventTimeType")
    # label: externalReferences
    # comment: References to all associated ExternalReferences
    # iri: https://onerecord.iata.org/ns/cargo#externalReferences
    externalReferences: List[ExternalReference] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#externalReferences")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: recordingActor
    # comment: Reference to the Actor recording the LogisticsEvent
    # iri: https://onerecord.iata.org/ns/cargo#recordingActor
    recordingActor: Optional[Actor] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#recordingActor")
    # label: recordingOrganization
    # comment: Organization recording the LogisticsEvent
    # iri: https://onerecord.iata.org/ns/cargo#recordingOrganization
    recordingOrganization: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#recordingOrganization")
    # label: creationDate
    # comment: DateTime at which the LogisticsEvent was posted
    # iri: https://onerecord.iata.org/ns/cargo#creationDate
    creationDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#creationDate")
    # label: eventDate
    # comment: Date and time of the event
    # iri: https://onerecord.iata.org/ns/cargo#eventDate
    eventDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#eventDate")
    # label: eventName
    # comment: If no EventCode provided, event name - e.g. Security clearance
    # iri: https://onerecord.iata.org/ns/cargo#eventName
    eventName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#eventName")
    # label: partialEventIndicator
    # comment: Boolean indicating that the LogisticsEvent is only applicable for parts of the LogisticObject it was recorded for, for example for some Pieces of a Shipment
    # iri: https://onerecord.iata.org/ns/cargo#partialEventIndicator
    partialEventIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#partialEventIndicator")
class LogisticsObject(BaseModel):
    # label: checks
    # comment: References to the CheckActions performed on the object
    # iri: https://onerecord.iata.org/ns/cargo#checks
    checks: List[Check] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checks")
    # label: events
    # comment: Events object
    # iri: https://onerecord.iata.org/ns/cargo#events
    events: List[LogisticsEvent] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#events")
    # label: externalReferences
    # comment: References to all associated ExternalReferences
    # iri: https://onerecord.iata.org/ns/cargo#externalReferences
    externalReferences: List[ExternalReference] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#externalReferences")
    # label: skeletonIndicator
    # comment: Indicator whether a logistics object is a skeleton object
    # iri: https://onerecord.iata.org/ns/cargo#skeletonIndicator
    skeletonIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#skeletonIndicator")
class LogisticsService(LogisticsObject):
    # label: activitySequences
    # comment: Information about the Activities that are part of the Service and their sequence
    # iri: https://onerecord.iata.org/ns/cargo#activitySequences
    activitySequences: List[ActivitySequence] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#activitySequences")
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails")
    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    # iri: https://onerecord.iata.org/ns/cargo#contactPersons
    contactPersons: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons")
class LoosePiece(PieceGroup):
    # label: pieceHeight
    # comment: Height of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceHeight
    pieceHeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceHeight")
    # label: pieceLength
    # comment: Length of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceLength
    pieceLength: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceLength")
    # label: pieceWeight
    # comment: Weight of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceWeight
    pieceWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWeight")
    # label: pieceWidth
    # comment: Width of a single piece
    # iri: https://onerecord.iata.org/ns/cargo#pieceWidth
    pieceWidth: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWidth")
    # label: totalVolume
    # comment: Total volume fo the volume piece group
    # iri: https://onerecord.iata.org/ns/cargo#totalVolume
    totalVolume: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#totalVolume")
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#stackable")
    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#turnable
    turnable: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#turnable")
class Measurement(BaseModel):
    # label: measurementValue
    # comment: Information about all non-Geolocation values of the measurement
    # iri: https://onerecord.iata.org/ns/cargo#measurementValue
    measurementValue: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#measurementValue")
    # label: recordedGeolocation
    # comment: Reference to the Geolocation recorded of the measurement
    # iri: https://onerecord.iata.org/ns/cargo#recordedGeolocation
    recordedGeolocation: Optional[Geolocation] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#recordedGeolocation")
    # label: measurementTimestamp
    # comment: Timestamp for the measurement
    # iri: https://onerecord.iata.org/ns/cargo#measurementTimestamp
    measurementTimestamp: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#measurementTimestamp")
class ModeQualifier(str, Enum):
    """
    label: ModeQualifier
    comment: Open code list for transport modes
    """
    # label: MAIN_CARRIAGE
    # comment: Indicates the mode qualifier as main carriage
    MAIN_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#MAIN_CARRIAGE")
    # label: ON_CARRIAGE
    # comment: Indicates the mode qualifier as on carriage
    ON_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#ON_CARRIAGE")
    # label: PRE_CARRIAGE
    # comment: Indicates the mode qualifier as pre carriage
    PRE_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#PRE_CARRIAGE")
class MovementTime(BaseModel):
    # label: direction
    # comment: Direction to indicate if it's Inbound or Outbound
    # iri: https://onerecord.iata.org/ns/cargo#direction
    direction: Optional[DirectionType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#direction")
    # label: movementMilestone
    # comment: The milestone list still needs to be defined, it includes elements from CXML Code List 1.92 but is not limited to those values, e.g. block-on and block-off times might be added as a comparison to wheels off and touchdown.
    # iri: https://onerecord.iata.org/ns/cargo#movementMilestone
    movementMilestone: Optional[MovementIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#movementMilestone")
    # label: movementTimeType
    # comment: The type of time can be Actual, Estimated ot Scheduled
    # iri: https://onerecord.iata.org/ns/cargo#movementTimeType
    movementTimeType: Optional[MovementTimeType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimeType")
    # label: movementTimestamp
    # comment: Timestamp (date and time) of the movement time. If the movement time is recorded asynchronously, the timestamp should reflect the actual time, not when the data was created.
    # iri: https://onerecord.iata.org/ns/cargo#movementTimestamp
    movementTimestamp: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimestamp")
class MovementTimeType(str, Enum):
    """
    label: MovementTimeType
    comment: Restricted code list for MovementTime subtypes
    """
    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")
    # label: ESTIMATED
    # comment: Used when a time is estimated
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")
    # label: SCHEDULED
    # comment: Used when a time is scheduled
    SCHEDULED = URIRef("https://onerecord.iata.org/ns/cargo#SCHEDULED")
class NonHumanActor(Actor):
    ...
class Organization(LogisticsAgent):
    # label: basedAtLocation
    # comment: Reference to the Location where the Organization is based at or headquartered
    # iri: https://onerecord.iata.org/ns/cargo#basedAtLocation
    basedAtLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#basedAtLocation")
    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    # iri: https://onerecord.iata.org/ns/cargo#contactPersons
    contactPersons: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: parentOrganization
    # comment: Reference to the parent Organization
    # iri: https://onerecord.iata.org/ns/cargo#parentOrganization
    parentOrganization: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#parentOrganization")
    # label: subOrganization
    # comment: References to all sub-Organizations
    # iri: https://onerecord.iata.org/ns/cargo#subOrganization
    subOrganization: List[Organization] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#subOrganization")
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#name")
    # label: shortName
    # comment: Short name of the Organization if any
    # iri: https://onerecord.iata.org/ns/cargo#shortName
    shortName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shortName")
class OtherCharge(BaseModel):
    # label: chargePaymentType
    # comment: Indicates if charge is prepaid or collect (P, C)
    # iri: https://onerecord.iata.org/ns/cargo#chargePaymentType
    chargePaymentType: Optional[PrepaidCollectIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargePaymentType")
    # label: entitlement
    # comment: Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    # iri: https://onerecord.iata.org/ns/cargo#entitlement
    entitlement: Optional[EntitlementCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#entitlement")
    # label: otherChargeAmount
    # comment: Other Charge amount
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeAmount
    otherChargeAmount: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeAmount")
    # label: otherChargeCode
    # comment: Refer to CargoXML Code List 1.2 for Other Charges
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeCode
    otherChargeCode: Optional[OtherChargeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeCode")
    # label: chargeQuantity
    # comment: Double describing the time or item basis quantity of a charge
    # iri: https://onerecord.iata.org/ns/cargo#chargeQuantity
    chargeQuantity: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeQuantity")
    # label: locationIndicator
    # comment: String indicating if the Other Charge Location is Origin (O) or Transit (T) or Destination(D)
    # iri: https://onerecord.iata.org/ns/cargo#locationIndicator
    locationIndicator: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#locationIndicator")
    # label: reasonDescription
    # comment: String describing the reason for a charge
    # iri: https://onerecord.iata.org/ns/cargo#reasonDescription
    reasonDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#reasonDescription")
class OtherIdentifier(BaseModel):
    # label: otherIdentifierType
    # comment: Identifier type or description
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifierType
    otherIdentifierType: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifierType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")
class PackagingType(LogisticsObject):
    # label: appliedOnPieces
    # comment: Piece on which the Packaging type is applicable
    # iri: https://onerecord.iata.org/ns/cargo#appliedOnPieces
    appliedOnPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#appliedOnPieces")
    # label: typeCode
    # comment: Packaging type identifier as per UNECE Rec 21 Annex V and VI e.g. 1A - Drum, steel - Packaging material code. Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations 
    # iri: https://onerecord.iata.org/ns/cargo#typeCode
    typeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#typeCode")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
class Party(BaseModel):
    # label: accountNumbers
    # comment: Information about account numbers
    # iri: https://onerecord.iata.org/ns/cargo#accountNumbers
    accountNumbers: List[AccountNumber] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#accountNumbers")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: partyDetails
    # comment: Reference to the Agent described by the role of the Party
    # iri: https://onerecord.iata.org/ns/cargo#partyDetails
    partyDetails: Optional[LogisticsAgent] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#partyDetails")
    # label: partyRole
    # comment: Role fo the Company in the context. Can refer to Code List 1.36 in the CXML Toolkit
    # iri: https://onerecord.iata.org/ns/cargo#partyRole
    partyRole: Optional[ParticipantIdentifier] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#partyRole")
class Person(Actor):
    # label: contactDetails
    # comment: Information about contactDetails
    # iri: https://onerecord.iata.org/ns/cargo#contactDetails
    contactDetails: List[ContactDetail] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails")
    # label: contactRole
    # comment: Contact type - e.g. Emergency contact, Customs contact, Customer contact
    # iri: https://onerecord.iata.org/ns/cargo#contactRole
    contactRole: Optional[ContactRole] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#contactRole")
    # label: documents
    # comment: Linked documents to the person, e.g. driver's license, ID, etc.
    # iri: https://onerecord.iata.org/ns/cargo#documents
    documents: List[ExternalReference] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#documents")
    # label: department
    # comment: Department / Division / Unit
    # iri: https://onerecord.iata.org/ns/cargo#department
    department: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#department")
    # label: employeeId
    # comment: Employee ID
    # iri: https://onerecord.iata.org/ns/cargo#employeeId
    employeeId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#employeeId")
    # label: firstName
    # comment: First name / given name
    # iri: https://onerecord.iata.org/ns/cargo#firstName
    firstName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#firstName")
    # label: jobTitle
    # comment: Job title / position
    # iri: https://onerecord.iata.org/ns/cargo#jobTitle
    jobTitle: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#jobTitle")
    # label: lastName
    # comment: Last name / family name / surname
    # iri: https://onerecord.iata.org/ns/cargo#lastName
    lastName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#lastName")
    # label: middleName
    # comment: Middle name/ other name
    # iri: https://onerecord.iata.org/ns/cargo#middleName
    middleName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#middleName")
    # label: salutation
    # comment: Salutation 
    # iri: https://onerecord.iata.org/ns/cargo#salutation
    salutation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#salutation")
class PhysicalLogisticsObject(LogisticsObject):
    # label: attachedIotDevices
    # comment: References to all connected IotDevices
    # iri: https://onerecord.iata.org/ns/cargo#attachedIotDevices
    attachedIotDevices: List[IotDevice] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#attachedIotDevices")
    # label: involvedInActions
    # comment: References to the Actions the object is involved in
    # iri: https://onerecord.iata.org/ns/cargo#involvedInActions
    involvedInActions: List[LogisticsAction] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedInActions")
class Piece(PhysicalLogisticsObject):
    # label: containedItems
    # comment: Reference to the item(s) contained in the piece
    # iri: https://onerecord.iata.org/ns/cargo#containedItems
    containedItems: List[Item] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#containedItems")
    # label: containedPieces
    # comment: Details of contained piece(s)
    # iri: https://onerecord.iata.org/ns/cargo#containedPieces
    containedPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#containedPieces")
    # label: contentProductionCountry
    # comment: Goods production country, mandatory when there are no Items. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#contentProductionCountry
    contentProductionCountry: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#contentProductionCountry")
    # label: contentProducts
    # comment: Reference to the Products describing the content of the Piece, mandatory if no data on Item level is used
    # iri: https://onerecord.iata.org/ns/cargo#contentProducts
    contentProducts: List[Product] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contentProducts")
    # label: customsInformation
    # comment: Customs details
    # iri: https://onerecord.iata.org/ns/cargo#customsInformation
    customsInformation: List[CustomsInformation] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation")
    # label: dimensions
    # comment: Dimensions details
    # iri: https://onerecord.iata.org/ns/cargo#dimensions
    dimensions: Optional[Dimensions] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#dimensions")
    # label: fulfillsUldTypeCode
    # comment: Text holding an ULD Type Code if the Piece fulfills it before UnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#fulfillsUldTypeCode
    fulfillsUldTypeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#fulfillsUldTypeCode")
    # label: grossWeight
    # comment: Weight details
    # iri: https://onerecord.iata.org/ns/cargo#grossWeight
    grossWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#grossWeight")
    # label: inPiece
    # comment: Reference to the Piece this Item or Piece is contained in
    # iri: https://onerecord.iata.org/ns/cargo#inPiece
    inPiece: Optional[Piece] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#inPiece")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: loadType
    # comment: Load type of the shipment or piece (Bulk, ULD, Pallet, Loose)
    # iri: https://onerecord.iata.org/ns/cargo#loadType
    loadType: Optional[LoadType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#loadType")
    # label: ofShipment
    # comment: Reference to the Shipment the Piece is assigned to
    # iri: https://onerecord.iata.org/ns/cargo#ofShipment
    ofShipment: List[Shipment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ofShipment")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: packageMarkCoded
    # comment: Reference identifying how the package is marked. Field is hardcode to "SSCC-18", "UPC" or "Other"
    # iri: https://onerecord.iata.org/ns/cargo#packageMarkCoded
    packageMarkCoded: Optional[PackageMarkCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packageMarkCoded")
    # label: packagingType
    # comment: Packaging details 
    # iri: https://onerecord.iata.org/ns/cargo#packagingType
    packagingType: Optional[PackagingType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packagingType")
    # label: securityDeclarations
    # comment: Security details of the piece
    # iri: https://onerecord.iata.org/ns/cargo#securityDeclarations
    securityDeclarations: List[SecurityDeclaration] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#securityDeclarations")
    # label: specialHandlingCodes
    # comment: Three-letter special handling code (SPH)
    # iri: https://onerecord.iata.org/ns/cargo#specialHandlingCodes
    specialHandlingCodes: List[SpecialHandlingCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#specialHandlingCodes")
    # label: temperatureInstructions
    # comment: Temperature instructions if a specific range
    # iri: https://onerecord.iata.org/ns/cargo#temperatureInstructions
    temperatureInstructions: Optional[TemperatureInstructions] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureInstructions")
    # label: coload
    # comment: Coload indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#coload
    coload: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#coload")
    # label: goodsDescription
    # comment: Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    # iri: https://onerecord.iata.org/ns/cargo#goodsDescription
    goodsDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsDescription")
    # label: nvdForCarriage
    # comment: When no value is declared for Carriage, this field may be completed with the value TRUE otherwise FALSE
    # iri: https://onerecord.iata.org/ns/cargo#nvdForCarriage
    nvdForCarriage: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCarriage")
    # label: nvdForCustoms
    # comment: When no value is declared for Customs, this field may be completed with the value TRUE otherwise FALSE
    # iri: https://onerecord.iata.org/ns/cargo#nvdForCustoms
    nvdForCustoms: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCustoms")
    # label: packagedeIdentifier
    # comment: SSCC-18 code for the value of the package mark, company or bar code, free text, pallet code, etc.
    # iri: https://onerecord.iata.org/ns/cargo#packagedeIdentifier
    packagedeIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packagedeIdentifier")
    # label: shippingMarks
    # comment: Shipping marks
    # iri: https://onerecord.iata.org/ns/cargo#shippingMarks
    shippingMarks: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingMarks")
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac")
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#stackable")
    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    # iri: https://onerecord.iata.org/ns/cargo#textualHandlingInstructions
    textualHandlingInstructions: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions")
    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#turnable
    turnable: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#turnable")
    # label: upid
    # comment: Unique Piece Identifier (UPID) of the piece. Refer IATA Recommended Practice 1689
    # iri: https://onerecord.iata.org/ns/cargo#upid
    upid: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#upid")
class PieceDg(Piece):
    # label: dgDeclaration
    # comment: Reference to the Dangerous Goods declaration
    # iri: https://onerecord.iata.org/ns/cargo#dgDeclaration
    dgDeclaration: Optional[DgDeclaration] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#dgDeclaration")
    # label: overpackTypeCode
    # comment: Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations 
    # iri: https://onerecord.iata.org/ns/cargo#overpackTypeCode
    overpackTypeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackTypeCode")
    # label: allPackedInOneIndicator
    # comment: A statement identifying that the dangerous goods listed above are all contained in the same outer packaging. Takes the form All packed in one aaaa (description of packaging type) x nn (number of packages). Applies to air transport only. (Air) 
    # iri: https://onerecord.iata.org/ns/cargo#allPackedInOneIndicator
    allPackedInOneIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#allPackedInOneIndicator")
    # label: overpackCriticalitySafetyIndexNumeric
    # comment: Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI. 
    # iri: https://onerecord.iata.org/ns/cargo#overpackCriticalitySafetyIndexNumeric
    overpackCriticalitySafetyIndexNumeric: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackCriticalitySafetyIndexNumeric")
    # label: overpackIndicator
    # comment: Overpack indicator 
    # iri: https://onerecord.iata.org/ns/cargo#overpackIndicator
    overpackIndicator: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackIndicator")
    # label: overpackT1
    # comment: A single number assigned to a package, overpack or freight container to provide control over radiation exposure. 
    # iri: https://onerecord.iata.org/ns/cargo#overpackT1
    overpackT1: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackT1")
    # label: qValueNumeric
    # comment: Most instances of all packed in one will require the addition of the Q value which  1. Applies to air transport only. (Air)  
    # iri: https://onerecord.iata.org/ns/cargo#qValueNumeric
    qValueNumeric: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#qValueNumeric")
class PieceGroup(BaseModel):
    # label: dryIceWeight
    # comment: Weight of dry ice
    # iri: https://onerecord.iata.org/ns/cargo#dryIceWeight
    dryIceWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#dryIceWeight")
    # label: pieceGroupGrossWeight
    # comment: Total gross weight of the piece group
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupGrossWeight
    pieceGroupGrossWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupGrossWeight")
    # label: pieceGroupCount
    # comment: Number of pieces in the piece group
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupCount
    pieceGroupCount: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupCount")
    # label: pieceGroupId
    # comment: Identifier of the piece group, increasing integers
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroupId
    pieceGroupId: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupId")
class PieceLiveAnimals(Piece):
    # label: associatedEpermit
    # comment: Reference to the permits associated with the Live Animals
    # iri: https://onerecord.iata.org/ns/cargo#associatedEpermit
    associatedEpermit: Optional[EpermitConsignment] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#associatedEpermit")
    # label: exportTradeCountry
    # comment: Country of last re-export (box 12a). Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#exportTradeCountry
    exportTradeCountry: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#exportTradeCountry")
    # label: goodsTypeCode
    # comment: Appendix number of the convention (I, II or III) (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#goodsTypeCode
    goodsTypeCode: Optional[GoodsTypeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsTypeCode")
    # label: goodsTypeExtensionCode
    # comment: Appendix number of the convention (I, II or III) (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#goodsTypeExtensionCode
    goodsTypeExtensionCode: Optional[GoodsTypeExtensionCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsTypeExtensionCode")
    # label: originReferencePermitTypeCode
    # comment: Document type code of origin reference permit or re-export reference Certificate (box 12/12a)
    # iri: https://onerecord.iata.org/ns/cargo#originReferencePermitTypeCode
    originReferencePermitTypeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitTypeCode")
    # label: originTradeCountry
    # comment: country of origin (box 12). Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#originTradeCountry
    originTradeCountry: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#originTradeCountry")
    # label: specimenTypeCode
    # comment: Description of specimens, CITES type code (box 9)
    # iri: https://onerecord.iata.org/ns/cargo#specimenTypeCode
    specimenTypeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#specimenTypeCode")
    # label: acquisitionDateTime
    # comment: Defined in Resolution Conf. 13.6 and is required for pre-Convention specimens (box 12b)
    # iri: https://onerecord.iata.org/ns/cargo#acquisitionDateTime
    acquisitionDateTime: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#acquisitionDateTime")
    # label: annualQuotaQuantity
    # comment: total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    # iri: https://onerecord.iata.org/ns/cargo#annualQuotaQuantity
    annualQuotaQuantity: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#annualQuotaQuantity")
    # label: categoryCode
    # comment: Operations code ID. Refers to the number of the registered captive-breeding or artificial propagation operation (box 12b)
    # iri: https://onerecord.iata.org/ns/cargo#categoryCode
    categoryCode: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#categoryCode")
    # label: originReferencePermitDateTime
    # comment: Issuing date for Origin reference permit or re-export reference Certificate (box 12)
    # iri: https://onerecord.iata.org/ns/cargo#originReferencePermitDateTime
    originReferencePermitDateTime: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitDateTime")
    # label: originReferencePermitId
    # comment: identifier of Origin reference permit or re-export reference Certificate (box 12/12a)
    # iri: https://onerecord.iata.org/ns/cargo#originReferencePermitId
    originReferencePermitId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitId")
    # label: quantityAnimals
    # comment: Quantity including units (box 11)
    # iri: https://onerecord.iata.org/ns/cargo#quantityAnimals
    quantityAnimals: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#quantityAnimals")
    # label: speciesCommonName
    # comment: Species common name (box 8)
    # iri: https://onerecord.iata.org/ns/cargo#speciesCommonName
    speciesCommonName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#speciesCommonName")
    # label: speciesScientificName
    # comment: Species scientific name (box 7)
    # iri: https://onerecord.iata.org/ns/cargo#speciesScientificName
    speciesScientificName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#speciesScientificName")
    # label: specimenDescription
    # comment: Description of specimens, including age and sex if LA (box 9)
    # iri: https://onerecord.iata.org/ns/cargo#specimenDescription
    specimenDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#specimenDescription")
class Price(LogisticsObject):
    # label: chargeCode
    # comment: Charge code, refer to CargoXML Code List 1.1
    # iri: https://onerecord.iata.org/ns/cargo#chargeCode
    chargeCode: Optional[ChargeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeCode")
    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOption
    forBookingOption: Optional[BookingOption] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption")
    # label: ratings
    # comment: Rating used for pricing
    # iri: https://onerecord.iata.org/ns/cargo#ratings
    ratings: List[Ratings] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ratings")
    # label: grandTotal
    # comment: Total price
    # iri: https://onerecord.iata.org/ns/cargo#grandTotal
    grandTotal: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#grandTotal")
class Product(LogisticsObject):
    # label: describedObjects
    # comment: Reference to the Items or Pieces in which the product can be found.
    # iri: https://onerecord.iata.org/ns/cargo#describedObjects
    describedObjects: List[PhysicalLogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#describedObjects")
    # label: hsCode
    # comment: Harmonized Commodity code, refer to hsType used. 6 minimum digits are expected.
    # iri: https://onerecord.iata.org/ns/cargo#hsCode
    hsCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#hsCode")
    # label: manufacturer
    # comment: Manufacturing company details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#manufacturer
    manufacturer: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer")
    # label: otherCharacteristics
    # comment: Characteristics of the product
    # iri: https://onerecord.iata.org/ns/cargo#otherCharacteristics
    otherCharacteristics: List[Characteristic] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherCharacteristics")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: commodityItemNumber
    # comment: Indicates the specific commodity on which the rate class code is applied
    # iri: https://onerecord.iata.org/ns/cargo#commodityItemNumber
    commodityItemNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#commodityItemNumber")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
    # label: hsCommodityDescription
    # comment: Commodity description
    # iri: https://onerecord.iata.org/ns/cargo#hsCommodityDescription
    hsCommodityDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityDescription")
    # label: hsCommodityName
    # comment: If no Code provided, name of commodity
    # iri: https://onerecord.iata.org/ns/cargo#hsCommodityName
    hsCommodityName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityName")
    # label: hsType
    # comment: Reference identifying the type of standard code to be used for the Commodity Classification (Brussels Tariff Nomenclature, EU Harmonized System Code, UN Standard International Trade Classification). Mandatory if the commodity code is more than 6 digits
    # iri: https://onerecord.iata.org/ns/cargo#hsType
    hsType: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#hsType")
    # label: uniqueIdentifier
    # comment: Manufacturer's unique product identifier
    # iri: https://onerecord.iata.org/ns/cargo#uniqueIdentifier
    uniqueIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uniqueIdentifier")
class ProductDg(Product):
    # label: dgRadioactiveMaterial
    # comment: Dg Radioactive Material
    # iri: https://onerecord.iata.org/ns/cargo#dgRadioactiveMaterial
    dgRadioactiveMaterial: Optional[DgProductRadioactive] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#dgRadioactiveMaterial")
    # label: explosiveCompatibilityGroupCode
    # comment: Specifies the reference to the group which identifies the kind of substances and articles that are deemed to be compatible. Mandatory field in case of transport of explosive articles or substances
    # iri: https://onerecord.iata.org/ns/cargo#explosiveCompatibilityGroupCode
    explosiveCompatibilityGroupCode: Optional[ExplosiveCompatibilityGroupCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#explosiveCompatibilityGroupCode")
    # label: packagingDangerLevelCode
    # comment: Packing group, If used must reference I, II or III
    # iri: https://onerecord.iata.org/ns/cargo#packagingDangerLevelCode
    packagingDangerLevelCode: Optional[PackagingDangerLevelCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packagingDangerLevelCode")
    # label: additionalHazardClassificationId
    # comment: Identifies the subsidiary hazard class / division identification containing a numeric field separated by a decimal. There may be , 1 or 2 subsidiary risk classes or divisions. If there is more than one, each should be separated by a comma. The subsidiary risk must be shown in parentheses. 
    # iri: https://onerecord.iata.org/ns/cargo#additionalHazardClassificationId
    additionalHazardClassificationId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#additionalHazardClassificationId")
    # label: authorizationInformation
    # comment: Contains additional information relating to an approval, permission or other specific detail applicable to the commodity (e.g. Dangerous Goods in excepted quantities) 
    # iri: https://onerecord.iata.org/ns/cargo#authorizationInformation
    authorizationInformation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#authorizationInformation")
    # label: hazardClassificationId
    # comment: Identifies the hazard class / division identification containing a numeric field separated by a decimal
    # iri: https://onerecord.iata.org/ns/cargo#hazardClassificationId
    hazardClassificationId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#hazardClassificationId")
    # label: packingInstructionNumber
    # comment: The packing instruction number applicable to the UN number / proper shipping name entry. A three-numeric value which may be preceded by the letter Y.  Mandatory field for air transport (Air) 
    # iri: https://onerecord.iata.org/ns/cargo#packingInstructionNumber
    packingInstructionNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#packingInstructionNumber")
    # label: properShippingName
    # comment: The name used to describe the particular article or substance as shown in the UN Model Regulations Dangerous Goods List
    # iri: https://onerecord.iata.org/ns/cargo#properShippingName
    properShippingName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#properShippingName")
    # label: specialProvisionId
    # comment: For Air Mode: Special Provision may show a single, double or triple digit number preceded by the letter A, against appropriate entries in the List of Dangerous Goods
    # iri: https://onerecord.iata.org/ns/cargo#specialProvisionId
    specialProvisionId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#specialProvisionId")
    # label: technicalName
    # comment: This is additional chemical name(s) required for some proper shipping names. When added the technical must be shown in parentheses immediately following the proper shipping name. 
    # iri: https://onerecord.iata.org/ns/cargo#technicalName
    technicalName: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#technicalName")
    # label: unNumber
    # comment: Reference identifying the United Nations Dangerous Goods serial number assigned within the UN to substances and articles contained in a list of the dangerous goods most commonly carried. e.g. 1189 - Ethylene glycol monomethyl ether acetate
    # iri: https://onerecord.iata.org/ns/cargo#unNumber
    unNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unNumber")
class PublicAuthority(Organization):
    ...
class Question(LogisticsObject):
    # label: answer
    # comment: Reference to the Answer to the Question
    # iri: https://onerecord.iata.org/ns/cargo#answer
    answer: Optional[Answer] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#answer")
    # label: checkTemplate
    # comment: Reference to the CheckTemplate the Question is from
    # iri: https://onerecord.iata.org/ns/cargo#checkTemplate
    checkTemplate: Optional[CheckTemplate] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checkTemplate")
    # label: answerOptionsText
    # comment: Text restrictions to the Answer
    # iri: https://onerecord.iata.org/ns/cargo#answerOptionsText
    answerOptionsText: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsText")
    # label: answerOptionsValue
    # comment: Value restrictions to the answer
    # iri: https://onerecord.iata.org/ns/cargo#answerOptionsValue
    answerOptionsValue: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsValue")
    # label: longText
    # comment: Long text of the question
    # iri: https://onerecord.iata.org/ns/cargo#longText
    longText: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#longText")
    # label: questionNumber
    # comment: Number of the Question within the template (alphanumeric)
    # iri: https://onerecord.iata.org/ns/cargo#questionNumber
    questionNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#questionNumber")
    # label: questionSection
    # comment: Section of the CheckTemplate this Question is part of
    # iri: https://onerecord.iata.org/ns/cargo#questionSection
    questionSection: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#questionSection")
    # label: shortText
    # comment: Short text of the Question
    # iri: https://onerecord.iata.org/ns/cargo#shortText
    shortText: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shortText")
class Ranges(BaseModel):
    # label: rateClassCode
    # comment: Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCode
    rateClassCode: Optional[RateClassCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCode")
    # label: uldRateClassType
    # comment: ULD Rate information - ULD Rate Class Type
    # iri: https://onerecord.iata.org/ns/cargo#uldRateClassType
    uldRateClassType: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldRateClassType")
    # label: maximumQuantity
    # comment: Maximum quantity
    # iri: https://onerecord.iata.org/ns/cargo#maximumQuantity
    maximumQuantity: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#maximumQuantity")
    # label: minimumQuantity
    # comment: Minimum quantity
    # iri: https://onerecord.iata.org/ns/cargo#minimumQuantity
    minimumQuantity: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#minimumQuantity")
    # label: unitBasis
    # comment: Specific commodity code linked to commodity
    # iri: https://onerecord.iata.org/ns/cargo#unitBasis
    unitBasis: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unitBasis")
class Ratings(LogisticsObject):
    # label: billingChargeIdentifier
    # comment: Billing charge identifiers to be used for CASS. Refer to CargoXML Code List 1.33
    # iri: https://onerecord.iata.org/ns/cargo#billingChargeIdentifier
    billingChargeIdentifier: Optional[ChargeIdentifier] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#billingChargeIdentifier")
    # label: chargePaymentType
    # comment: Indicates if charge is prepaid or collect (P, C)
    # iri: https://onerecord.iata.org/ns/cargo#chargePaymentType
    chargePaymentType: Optional[PrepaidCollectIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargePaymentType")
    # label: chargeType
    # comment: Charge type related to amount total as per bullet points 2/21 - data elements 24A - 3B  from AWB
    # iri: https://onerecord.iata.org/ns/cargo#chargeType
    chargeType: Optional[ChargeIdentifier] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeType")
    # label: entitlement
    # comment: Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    # iri: https://onerecord.iata.org/ns/cargo#entitlement
    entitlement: Optional[EntitlementCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#entitlement")
    # label: forPrices
    # comment: Reference to the Prices based on this Ratings
    # iri: https://onerecord.iata.org/ns/cargo#forPrices
    forPrices: List[Price] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forPrices")
    # label: otherChargeCode
    # comment: Refer to CargoXML Code List 1.2 for Other Charges
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeCode
    otherChargeCode: Optional[OtherChargeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeCode")
    # label: ranges
    # comment: Reference to the ranges
    # iri: https://onerecord.iata.org/ns/cargo#ranges
    ranges: List[Ranges] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ranges")
    # label: rcp
    # comment: IATA 3-letter city code of the rate combination point as defined in TACT
    # iri: https://onerecord.iata.org/ns/cargo#rcp
    rcp: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rcp")
    # label: chargeDescription
    # comment: Description of the charge e.g. Airfreight, fuel, etc.
    # iri: https://onerecord.iata.org/ns/cargo#chargeDescription
    chargeDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeDescription")
    # label: priceReferenceId
    # comment: Reference to a price reference if existing (e.g. Allotment number, contract reference, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#priceReferenceId
    priceReferenceId: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#priceReferenceId")
    # label: priceSpecification
    # comment: Specification of the price e.g. Street, Group, Spot, etc.
    # iri: https://onerecord.iata.org/ns/cargo#priceSpecification
    priceSpecification: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#priceSpecification")
    # label: quantity
    # comment: Quantity for the charge if applicable
    # iri: https://onerecord.iata.org/ns/cargo#quantity
    quantity: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#quantity")
    # label: subTotal
    # comment: Subtotal of the charge
    # iri: https://onerecord.iata.org/ns/cargo#subTotal
    subTotal: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#subTotal")
class RegulatedEntity(BaseModel):
    # label: owningOrganization
    # comment: Reference to the Organization for which the RegulatedEntity information is valid
    # iri: https://onerecord.iata.org/ns/cargo#owningOrganization
    owningOrganization: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#owningOrganization")
    # label: regulatedEntityCategory
    # comment: Category code of the Regulated Entity
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityCategory
    regulatedEntityCategory: Optional[RegulatedEntityCategoryCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityCategory")
    # label: regulatedEntityExpiryDate
    # comment: Expiry date 4 digits month/year
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityExpiryDate
    regulatedEntityExpiryDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityExpiryDate")
    # label: regulatedEntityIdentifier
    # comment: Regulated entity identifier as per IATA e-CSD/CSD Resolution 65
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityIdentifier
    regulatedEntityIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityIdentifier")
class SecurityDeclaration(LogisticsObject):
    # label: groundsForExemption
    # comment: Exemption code - e.g. BIOM- Bio-Medical Samples SMUS - small undersized shipments MAIL - mail BIOM - bio-medical samples DIPL - diplomatic bags or diplomatic mail LFSM - life-saving materials NUCL - nuclear materials TRNS - transfer or transshipment
    # iri: https://onerecord.iata.org/ns/cargo#groundsForExemption
    groundsForExemption: List[ScreeningExemption] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#groundsForExemption")
    # label: issuedBy
    # comment: Name of person (or employee ID) who issued the security status
    # iri: https://onerecord.iata.org/ns/cargo#issuedBy
    issuedBy: Optional[Person] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedBy")
    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForPiece
    issuedForPiece: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece")
    # label: otherRegulatedEntities
    # comment: Any other regulated entity that accepts custody of the cargo and accepts the security status originally issued
    # iri: https://onerecord.iata.org/ns/cargo#otherRegulatedEntities
    otherRegulatedEntities: List[RegulatedEntity] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherRegulatedEntities")
    # label: receivedFrom
    # comment: Regulated entity that tendered the consignment
    # iri: https://onerecord.iata.org/ns/cargo#receivedFrom
    receivedFrom: Optional[RegulatedEntity] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#receivedFrom")
    # label: regulatedEntityAcceptor
    # comment: Information about the accepting regulated entity of the Security Declaration
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityAcceptor
    regulatedEntityAcceptor: List[RegulatedEntity] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityAcceptor")
    # label: regulatedEntityIssuer
    # comment: Regulated entity issuing the Security Declaration
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityIssuer
    regulatedEntityIssuer: Optional[RegulatedEntity] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityIssuer")
    # label: screeningMethods
    # comment: Screening methods which have been used to secure the cargo PHS – Physical Inspection and/or hand search VCK - Visual check XRY- X-ray equipment EDS - Explosive detection system EDD - Explosive detection dogsETD - Explosive trace detection equipment - particles or vapor CMD - Cargo metal detection AOM - Subjected to any other means: this entry should be followed by free text specifying what other mean was used to secure the cargo
    # iri: https://onerecord.iata.org/ns/cargo#screeningMethods
    screeningMethods: List[ScreeningMethod] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#screeningMethods")
    # label: securityStatus
    # comment: Security status indicator (CXML 1.13) - e.g. SPX- Cargo Secure for Passenger and All-Cargo Aircraft 
    # iri: https://onerecord.iata.org/ns/cargo#securityStatus
    securityStatus: Optional[SecurityStatus] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#securityStatus")
    # label: additionalSecurityInformation
    # comment: Any additional information that may be required by an ICAO Member State
    # iri: https://onerecord.iata.org/ns/cargo#additionalSecurityInformation
    additionalSecurityInformation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#additionalSecurityInformation")
    # label: issuedOn
    # comment: Date and time when the security status was issued
    # iri: https://onerecord.iata.org/ns/cargo#issuedOn
    issuedOn: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedOn")
    # label: otherScreeningMethods
    # comment: Other methods used to secure the cargo
    # iri: https://onerecord.iata.org/ns/cargo#otherScreeningMethods
    otherScreeningMethods: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherScreeningMethods")
class Sensor(PhysicalLogisticsObject):
    # label: measurements
    # comment: Reference to the Measurements recorded by the Sensor
    # iri: https://onerecord.iata.org/ns/cargo#measurements
    measurements: List[Measurement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#measurements")
    # label: partOfIotDevice
    # comment: Reference to the IoT Device to which the sensor is linked
    # iri: https://onerecord.iata.org/ns/cargo#partOfIotDevice
    partOfIotDevice: Optional[IotDevice] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#partOfIotDevice")
    # label: sensorType
    # comment: Type of sensor as described in Interactive Cargo Recommended Practice
    # iri: https://onerecord.iata.org/ns/cargo#sensorType
    sensorType: Optional[SensorType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#sensorType")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
    # label: name
    # comment: Human-understandable name of object depending on the context
    # iri: https://onerecord.iata.org/ns/cargo#name
    name: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#name")
    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    # iri: https://onerecord.iata.org/ns/cargo#serialNumber
    serialNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber")
class SensorType(CodeListElement):
    ...
class Shipment(LogisticsObject):
    # label: customsInformation
    # comment: Customs details
    # iri: https://onerecord.iata.org/ns/cargo#customsInformation
    customsInformation: List[CustomsInformation] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation")
    # label: incoterms
    # comment: Standard codes as defined by UNCEFACT and ICC that correspond to international rules for the interpretation of the most commonly used trade terms in different countries. UNECE recommendation n. 5 Incoterms 2.
    # iri: https://onerecord.iata.org/ns/cargo#incoterms
    incoterms: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#incoterms")
    # label: insurance
    # comment: Insurance details
    # iri: https://onerecord.iata.org/ns/cargo#insurance
    insurance: Optional[Insurance] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#insurance")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: pieces
    # comment: References to the Pieces that are part of this Shipment
    # iri: https://onerecord.iata.org/ns/cargo#pieces
    pieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieces")
    # label: totalDimensions
    # comment: Dimensions of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalDimensions
    totalDimensions: List[Dimensions] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#totalDimensions")
    # label: totalGrossWeight
    # comment: Total gross weight of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalGrossWeight
    totalGrossWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#totalGrossWeight")
    # label: waybill
    # comment: Reference to the Waybill of the shipment
    # iri: https://onerecord.iata.org/ns/cargo#waybill
    waybill: Optional[Waybill] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybill")
    # label: goodsDescription
    # comment: Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    # iri: https://onerecord.iata.org/ns/cargo#goodsDescription
    goodsDescription: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsDescription")
    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    # iri: https://onerecord.iata.org/ns/cargo#textualHandlingInstructions
    textualHandlingInstructions: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions")
class StationRemarks(BaseModel):
    # label: station
    # comment: Reference to the station (Airport), mandatory 
    # iri: https://onerecord.iata.org/ns/cargo#station
    station: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#station")
    # label: remarksText
    # comment: Details of the remarks, mandatory
    # iri: https://onerecord.iata.org/ns/cargo#remarksText
    remarksText: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#remarksText")
class Storage(LogisticsActivity):
    # label: storingActions
    # comment: References to all StoringActions performed for the Storing Activity
    # iri: https://onerecord.iata.org/ns/cargo#storingActions
    storingActions: List[Storing] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#storingActions")
    # label: storingIdentifier
    # comment: Short text holding the process number if necessary
    # iri: https://onerecord.iata.org/ns/cargo#storingIdentifier
    storingIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#storingIdentifier")
class Storing(LogisticsAction):
    # label: storedObjects
    # comment: Reference to the Objects being stored in or stored out
    # iri: https://onerecord.iata.org/ns/cargo#storedObjects
    storedObjects: List[PhysicalLogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#storedObjects")
    # label: storingType
    # comment: Enum stating whether the StoringAction describes the store-in or the store-out
    # iri: https://onerecord.iata.org/ns/cargo#storingType
    storingType: Optional[StoringType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#storingType")
    # label: storagePlaceIdentifier
    # comment: Short text stating the exact place of storage
    # iri: https://onerecord.iata.org/ns/cargo#storagePlaceIdentifier
    storagePlaceIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#storagePlaceIdentifier")
class StoringType(str, Enum):
    """
    label: StoringType
    comment: Restricted code list for Storing subtypes
    """
    # label: STORE_IN
    # comment: Describes a store-in process, where a physical object is assigned to a specific location
    STORE_IN = URIRef("https://onerecord.iata.org/ns/cargo#STORE_IN")
    # label: STORE_OUT
    # comment: Describes a store-out process, where a physical object leaves a specific location
    STORE_OUT = URIRef("https://onerecord.iata.org/ns/cargo#STORE_OUT")
class TemperatureInstructions(BaseModel):
    # label: maxTemperature
    # comment: Maximum temperature of the range
    # iri: https://onerecord.iata.org/ns/cargo#maxTemperature
    maxTemperature: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#maxTemperature")
    # label: minTemperature
    # comment: Minimum temperature of the range
    # iri: https://onerecord.iata.org/ns/cargo#minTemperature
    minTemperature: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#minTemperature")
class TransportLegs(LogisticsObject):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: co2Emissions
    # comment: References to CO2Emissions
    # iri: https://onerecord.iata.org/ns/cargo#co2Emissions
    co2Emissions: Optional[CO2Emissions] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#co2Emissions")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: operatingTransportMeans
    # comment: Reference to the TransportMeans operating the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#operatingTransportMeans
    operatingTransportMeans: Optional[TransportMeans] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans")
    # label: transportMeansServiceType
    # comment: Type of transport means service, e.g. Aircraftor Truck
    # iri: https://onerecord.iata.org/ns/cargo#transportMeansServiceType
    transportMeansServiceType: Optional[TransportMeansServiceType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansServiceType")
    # label: transportMeansType
    # comment: Type of transport means, e.g. 744, RFS
    # iri: https://onerecord.iata.org/ns/cargo#transportMeansType
    transportMeansType: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansType")
    # label: arrivalDate
    # comment: Arrival date and time of the leg
    # iri: https://onerecord.iata.org/ns/cargo#arrivalDate
    arrivalDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalDate")
    # label: departureDate
    # comment: Departure date and time of the leg
    # iri: https://onerecord.iata.org/ns/cargo#departureDate
    departureDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#departureDate")
    # label: TransportLegs
    # comment: Leg number
    # iri: https://onerecord.iata.org/ns/cargo#legNumber
    legNumber: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#legNumber")
    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    # iri: https://onerecord.iata.org/ns/cargo#transportIdentifier
    transportIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier")
class TransportMeans(PhysicalLogisticsObject):
    # label: operatedTransportMovement
    # comment: Transport Movement on which the Transport Means is used
    # iri: https://onerecord.iata.org/ns/cargo#operatedTransportMovement
    operatedTransportMovement: Optional[TransportMovement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#operatedTransportMovement")
    # label: transportOrganization
    # comment: Company operating the transport means
    # iri: https://onerecord.iata.org/ns/cargo#transportOrganization
    transportOrganization: Optional[Organization] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportOrganization")
    # label: typicalCo2Coefficient
    # comment: Required for some CO2 calculations
    # iri: https://onerecord.iata.org/ns/cargo#typicalCo2Coefficient
    typicalCo2Coefficient: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#typicalCo2Coefficient")
    # label: typicalFuelConsumption
    # comment: Typical fuel consumption (e.g. 2 L / 1 nm)
    # iri: https://onerecord.iata.org/ns/cargo#typicalFuelConsumption
    typicalFuelConsumption: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#typicalFuelConsumption")
    # label: vehicleType
    # comment: Vehicle or container type. Refer UNECE28, e.g. 4.. - Aircraft, type unknown.For Air refer to IATA Standard Schedules Information Manual in section ATA/IATA Aircraft Types
    # iri: https://onerecord.iata.org/ns/cargo#vehicleType
    vehicleType: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleType")
    # label: vehicleModel
    # comment: Model or make of the vehicle (e.g. A33-3)
    # iri: https://onerecord.iata.org/ns/cargo#vehicleModel
    vehicleModel: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleModel")
    # label: vehicleRegistration
    # comment: Vehicle identification - e.g. aircraft registration number
    # iri: https://onerecord.iata.org/ns/cargo#vehicleRegistration
    vehicleRegistration: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleRegistration")
    # label: vehicleSize
    # comment: Size of the vehicle - free text
    # iri: https://onerecord.iata.org/ns/cargo#vehicleSize
    vehicleSize: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleSize")
class TransportMovement(LogisticsActivity):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: co2Emissions
    # comment: References to CO2Emissions
    # iri: https://onerecord.iata.org/ns/cargo#co2Emissions
    co2Emissions: List[CO2Emissions] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#co2Emissions")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: distanceCalculated
    # comment: Information about the calculated distance
    # iri: https://onerecord.iata.org/ns/cargo#distanceCalculated
    distanceCalculated: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#distanceCalculated")
    # label: distanceMeasured
    # comment: Information about the measured distance
    # iri: https://onerecord.iata.org/ns/cargo#distanceMeasured
    distanceMeasured: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#distanceMeasured")
    # label: fuelAmountCalculated
    # comment: Information about the calculated fuel amount
    # iri: https://onerecord.iata.org/ns/cargo#fuelAmountCalculated
    fuelAmountCalculated: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountCalculated")
    # label: fuelAmountMeasured
    # comment: Information about the measured fuel amount
    # iri: https://onerecord.iata.org/ns/cargo#fuelAmountMeasured
    fuelAmountMeasured: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountMeasured")
    # label: loadingActions
    # comment: References to all actions of type Loading performed for the TransportMovement
    # iri: https://onerecord.iata.org/ns/cargo#loadingActions
    loadingActions: List[Loading] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingActions")
    # label: modeCode
    # comment: Mode of transport code, refer to UNECE Rec. 19 https://unece.org/fileadmin/DAM/cefact/recommendations/rec19/rec19_1cf19e.pdf
    # iri: https://onerecord.iata.org/ns/cargo#modeCode
    modeCode: Optional[ModeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#modeCode")
    # label: modeQualifier
    # comment: Pre-Carriage, Main-Carriage or On-Carriage
    # iri: https://onerecord.iata.org/ns/cargo#modeQualifier
    modeQualifier: Optional[ModeQualifier] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#modeQualifier")
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
    operatingTransportMeans: Optional[TransportMeans] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans")
    # label: fuelType
    # comment: e.g. Kerosene, Diesel, SAF, Electricity [renewable], Electricity [non-renewable]
    # iri: https://onerecord.iata.org/ns/cargo#fuelType
    fuelType: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#fuelType")
    # label: seal
    # comment: Seal identifier
    # iri: https://onerecord.iata.org/ns/cargo#seal
    seal: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#seal")
    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    # iri: https://onerecord.iata.org/ns/cargo#transportIdentifier
    transportIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier")
class ULD(LoadingUnit):
    # label: demurrageCode
    # comment: Contains three designator of demurrage code, refer to RP 1654 (BCC, HHH, XXX, ZZZ)
    # iri: https://onerecord.iata.org/ns/cargo#demurrageCode
    demurrageCode: Optional[DemurrageCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#demurrageCode")
    # label: loadingIndicator
    # comment: ULD height or loading limitation code. Refer CXML Code List 1.47,  e.g. R - ULD Height above 244 centimetres
    # iri: https://onerecord.iata.org/ns/cargo#loadingIndicator
    loadingIndicator: Optional[ULDLoadingIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingIndicator")
    # label: odlnCode
    # comment: Contains two designator codes of ODLN or Operational Damage Limit Notices. ODLN code is used to define type of damage after visually check the serviceability of ULDs section 7, Standard Specifications 4/3 or 4/4 in ULD Regulations
    # iri: https://onerecord.iata.org/ns/cargo#odlnCode
    odlnCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#odlnCode")
    # label: ownerCode
    # comment: Owner code of the ULD in aa, an or na format - owner can be an airline or leasing company
    # iri: https://onerecord.iata.org/ns/cargo#ownerCode
    ownerCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#ownerCode")
    # label: serviceabilityCode
    # comment: Designator of serviceability condition e.g. SER or DAM 
    # iri: https://onerecord.iata.org/ns/cargo#serviceabilityCode
    serviceabilityCode: Optional[ULDConditionCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serviceabilityCode")
    # label: uldTypeCode
    # comment: Standard Unit Load Device type code e.g. AKE - Certified Container - Contoured. Refer to IATA ULD Technical Manual
    # iri: https://onerecord.iata.org/ns/cargo#uldTypeCode
    uldTypeCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldTypeCode")
    # label: ataDesignator
    # comment: US / ATA Unit Load Device type code e.g. M2
    # iri: https://onerecord.iata.org/ns/cargo#ataDesignator
    ataDesignator: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#ataDesignator")
    # label: damageFlag
    # comment: Indicates if the ULD is Damaged
    # iri: https://onerecord.iata.org/ns/cargo#damageFlag
    damageFlag: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#damageFlag")
    # label: numberOfDoors
    # comment: Number of doors
    # iri: https://onerecord.iata.org/ns/cargo#numberOfDoors
    numberOfDoors: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfDoors")
    # label: numberOfFittings
    # comment: Number of fittings
    # iri: https://onerecord.iata.org/ns/cargo#numberOfFittings
    numberOfFittings: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfFittings")
    # label: numberOfNets
    # comment: Number of nets
    # iri: https://onerecord.iata.org/ns/cargo#numberOfNets
    numberOfNets: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfNets")
    # label: numberOfStraps
    # comment: Number of straps
    # iri: https://onerecord.iata.org/ns/cargo#numberOfStraps
    numberOfStraps: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfStraps")
    # label: sealNumber
    # comment: ULD seal number if applicable
    # iri: https://onerecord.iata.org/ns/cargo#sealNumber
    sealNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#sealNumber")
    # label: uldSerialNumber
    # comment: Serial number that allows to uniquely identify the ULD
    # iri: https://onerecord.iata.org/ns/cargo#uldSerialNumber
    uldSerialNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldSerialNumber")
class ULDBasicPiece(PieceGroup):
    # label: uldLoadingIndicator
    # comment: Indicator related to ULD loading (e.g. Main deck only)
    # iri: https://onerecord.iata.org/ns/cargo#uldLoadingIndicator
    uldLoadingIndicator: Optional[ULDLoadingIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldLoadingIndicator")
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac")
class ULDSpecificPiece(PieceGroup):
    # label: uldContourCode
    # comment: Contour code as per IATA ULD Regulation
    # iri: https://onerecord.iata.org/ns/cargo#uldContourCode
    uldContourCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldContourCode")
    # label: uldType
    # comment: Type of ULD as per IATA ULD Regulation
    # iri: https://onerecord.iata.org/ns/cargo#uldType
    uldType: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldType")
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac")
    # label: uldSerialNumber
    # comment: Serial number that allows to uniquely identify the ULD
    # iri: https://onerecord.iata.org/ns/cargo#uldSerialNumber
    uldSerialNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldSerialNumber")
class UnitComposition(LogisticsActivity):
    # label: compositionActions
    # comment: References to all CompositionActions performed for the UnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#compositionActions
    compositionActions: List[Composing] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#compositionActions")
    # label: onLoadingUnit
    # comment: Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    # iri: https://onerecord.iata.org/ns/cargo#loadingUnit
    loadingUnit: Optional[LoadingUnit] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#loadingUnit")
    # label: compositionIdentifier
    # comment: Short text holding the process number if necessary
    # iri: https://onerecord.iata.org/ns/cargo#compositionIdentifier
    compositionIdentifier: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#compositionIdentifier")
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac")
class UnitsPreference(BaseModel):
    # label: currency
    # comment: Preferred unit for currency
    # iri: https://onerecord.iata.org/ns/cargo#currency
    currency: Optional[CurrencyCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#currency")
    # label: dimensionsUnit
    # comment: Preferred unit for measurement and dimensions
    # iri: https://onerecord.iata.org/ns/cargo#dimensionsUnit
    dimensionsUnit: Optional[DimensionsUnitCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#dimensionsUnit")
    # label: temperatureUnit
    # comment: Preferred unit for temperature
    # iri: https://onerecord.iata.org/ns/cargo#temperatureUnit
    temperatureUnit: Optional[TemperatureUnitCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureUnit")
    # label: volumeUnit
    # comment: Preferred unit for volume
    # iri: https://onerecord.iata.org/ns/cargo#volumeUnit
    volumeUnit: Optional[VolumeUnitCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#volumeUnit")
    # label: weightUnit
    # comment: Preferred unit for weight
    # iri: https://onerecord.iata.org/ns/cargo#weightUnit
    weightUnit: Optional[WeightUnitCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#weightUnit")
class Value(BaseModel):
    # label: unit
    # comment: Unit of measurement as per MeasurementUnitCode codelist. If the code is not present, create an instance of MeasurementUnitCode based on UNECE Rec. 20 Rev. 17e-2021
    # iri: https://onerecord.iata.org/ns/cargo#unit
    unit: Optional[MeasurementUnitCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unit")
    # label: numericalValue
    # comment: Numerical value
    # iri: https://onerecord.iata.org/ns/cargo#numericalValue
    numericalValue: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue")
class VolumePieceGroup(PieceGroup):
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#stackable")
class VolumetricWeight(BaseModel):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight")
    # label: conversionFactor
    # comment: Volume to weight conversion factor
    # iri: https://onerecord.iata.org/ns/cargo#conversionFactor
    conversionFactor: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor")
class Waybill(LogisticsObject):
    # label: accountingNotes
    # comment: Information about accounting notes (AWB box 10)
    # iri: https://onerecord.iata.org/ns/cargo#accountingNotes
    accountingNotes: List[AccountingNote] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNotes")
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: billingDetails
    # comment: Reference to the BillingDetails of the Waybill
    # iri: https://onerecord.iata.org/ns/cargo#billingDetails
    billingDetails: Optional[BillingDetails] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#billingDetails")
    # label: carrierChargeCode
    # comment: One letter charge code as per bullet point 12 - data element 13 from AWB
    # iri: https://onerecord.iata.org/ns/cargo#carrierChargeCode
    carrierChargeCode: Optional[ChargeCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierChargeCode")
    # label: carrierDeclarationPlace
    # comment: Location of individual or company involved in the movement of a consignment or Coded representation of a specific airport/city code
    # iri: https://onerecord.iata.org/ns/cargo#carrierDeclarationPlace
    carrierDeclarationPlace: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierDeclarationPlace")
    # label: customsOriginCode
    # comment: Code indicating the origin of goods for Customs purposes (e.g. For goods in free circulation in the EU) List to be provided by local authorities
    # iri: https://onerecord.iata.org/ns/cargo#customsOriginCode
    customsOriginCode: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#customsOriginCode")
    # label: declaredValueForCarriage
    # comment: The value of a shipment declared for carriage purposes
    # iri: https://onerecord.iata.org/ns/cargo#declaredValueForCarriage
    declaredValueForCarriage: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#declaredValueForCarriage")
    # label: declaredValueForCustoms
    # comment: The value of a shipment declared for customs purposes
    # iri: https://onerecord.iata.org/ns/cargo#declaredValueForCustoms
    declaredValueForCustoms: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#declaredValueForCustoms")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: destinationCharges
    # comment: Charges levied at destination accruing to the last carrier, in destination currency
    # iri: https://onerecord.iata.org/ns/cargo#destinationCharges
    destinationCharges: List[CurrencyValue] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#destinationCharges")
    # label: houseWaybills
    # comment: Refers to the Waybill(s) contained
    # iri: https://onerecord.iata.org/ns/cargo#houseWaybills
    houseWaybills: List[Waybill] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#houseWaybills")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: masterWaybill
    # comment: Reference to the master Waybill if it is contained in one
    # iri: https://onerecord.iata.org/ns/cargo#masterWaybill
    masterWaybill: Optional[Waybill] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#masterWaybill")
    # label: otherCharges
    # comment: Information about Other Charges applying to this Waybill
    # iri: https://onerecord.iata.org/ns/cargo#otherCharges
    otherCharges: List[OtherCharge] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherCharges")
    # label: otherChargesIndicator
    # comment: Indicator whether the payment of Other Charges is to be made at origin (prepaid) or at destination (collect) as per bullet point 13 - data element 15a/15b from AWB
    # iri: https://onerecord.iata.org/ns/cargo#otherChargesIndicator
    otherChargesIndicator: Optional[PrepaidCollectIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargesIndicator")
    # label: referredBookingOption
    # comment: Refers to the Booking
    # iri: https://onerecord.iata.org/ns/cargo#referredBookingOption
    referredBookingOption: Optional[Booking] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#referredBookingOption")
    # label: serviceCode
    # comment: One letter service code as per bullet point 18.4 - data element 22Z from AWB
    # iri: https://onerecord.iata.org/ns/cargo#serviceCode
    serviceCode: Optional[ServiceCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#serviceCode")
    # label: shipment
    # comment: Reference to the Shipment
    # iri: https://onerecord.iata.org/ns/cargo#shipment
    shipment: Optional[Shipment] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shipment")
    # label: taxAmount
    # comment: Information about taxes
    # iri: https://onerecord.iata.org/ns/cargo#taxAmount
    taxAmount: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#taxAmount")
    # label: waybillLineItems
    # comment: Information about rates applying to this Waybill handled as line item
    # iri: https://onerecord.iata.org/ns/cargo#waybillLineItems
    waybillLineItems: List[WaybillLineItem] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillLineItems")
    # label: waybillType
    # comment: Type of the Waybill: House, Direct or Master
    # iri: https://onerecord.iata.org/ns/cargo#waybillType
    waybillType: Optional[WaybillType] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillType")
    # label: weightValuationIndicator
    # comment: Indicator whether the payment for the Weight/Valuation is to be made at origin (prepaid) or at destination (collect) as per bullet point 13 - data element 14a/14b from AWB
    # iri: https://onerecord.iata.org/ns/cargo#weightValuationIndicator
    weightValuationIndicator: Optional[PrepaidCollectIndicator] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#weightValuationIndicator")
    # label: accountingInformation
    # comment: Indicates the details of accounting information. Free text e.g. PAYMENT BY CERTIFIED CHEQUE etc.
    # iri: https://onerecord.iata.org/ns/cargo#accountingInformation
    accountingInformation: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#accountingInformation")
    # label: carrierDeclarationDate
    # comment: Date upon which the certification is made by the carrier
    # iri: https://onerecord.iata.org/ns/cargo#carrierDeclarationDate
    carrierDeclarationDate: Optional[datetime] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierDeclarationDate")
    # label: carrierDeclarationSignature
    # comment: Contains the authentication of the Carrier
    # iri: https://onerecord.iata.org/ns/cargo#carrierDeclarationSignature
    carrierDeclarationSignature: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierDeclarationSignature")
    # label: consignorDeclarationSignature
    # comment: Name of consignor signatory
    # iri: https://onerecord.iata.org/ns/cargo#consignorDeclarationSignature
    consignorDeclarationSignature: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#consignorDeclarationSignature")
    # label: destinationCurrencyRate
    # comment: Conversion rate applied
    # iri: https://onerecord.iata.org/ns/cargo#destinationCurrencyRate
    destinationCurrencyRate: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#destinationCurrencyRate")
    # label: modularCheckNumber
    # comment: The check is a Modular 7 validation on the AWB number, recorded as a boolean.
    # iri: https://onerecord.iata.org/ns/cargo#modularCheckNumber
    modularCheckNumber: Optional[bool] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#modularCheckNumber")
    # label: shippingInfo
    # comment: The shipper or its Agent may enter the appropriate optional shipping
    # iri: https://onerecord.iata.org/ns/cargo#shippingInfo
    shippingInfo: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingInfo")
    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    # iri: https://onerecord.iata.org/ns/cargo#shippingRefNo
    shippingRefNo: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo")
    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    # iri: https://onerecord.iata.org/ns/cargo#waybillNumber
    waybillNumber: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber")
    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    # iri: https://onerecord.iata.org/ns/cargo#waybillPrefix
    waybillPrefix: Optional[str] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix")
class WaybillLineItem(BaseModel):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight")
    # label: lineItemPackages
    # comment: References to piece groupings for rating
    # iri: https://onerecord.iata.org/ns/cargo#lineItemPackages
    lineItemPackages: List[LineItemPackage] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemPackages")
    # label: rateCharge
    # comment: TACT Rate for rate description details
    # iri: https://onerecord.iata.org/ns/cargo#rateCharge
    rateCharge: Optional[CurrencyValue] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateCharge")
    # label: rateClassCode
    # comment: Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCode
    rateClassCode: Optional[RateClassCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCode")
    # label: rateClassCodeBasic
    # comment: Rate Surcharge/Reduction - Basic Rate Class Code
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCodeBasic
    rateClassCodeBasic: Optional[BasicRateClassCode] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCodeBasic")
    # label: rateGrossWeight
    # comment: Information about the total gross weight considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateGrossWeight
    rateGrossWeight: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateGrossWeight")
    # label: ratePercentage
    # comment: Rate Surcharge/Reduction - Percentage of  red. / surcharge
    # iri: https://onerecord.iata.org/ns/cargo#ratePercentage
    ratePercentage: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#ratePercentage")
    # label: rateVolume
    # comment: Information about the total volume considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateVolume
    rateVolume: Optional[Value] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateVolume")
    # label: rcp
    # comment: IATA 3-letter city code of the rate combination point as defined in TACT
    # iri: https://onerecord.iata.org/ns/cargo#rcp
    rcp: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rcp")
    # label: uldRateClassType
    # comment: ULD Rate information - ULD Rate Class Type
    # iri: https://onerecord.iata.org/ns/cargo#uldRateClassType
    uldRateClassType: Optional[CodeListElement] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldRateClassType")
    # label: uldReferences
    # comment: References to ULDs for which the rate applies
    # iri: https://onerecord.iata.org/ns/cargo#uldReferences
    uldReferences: List[ULD] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldReferences")
    # label: conversionFactor
    # comment: Volume to weight conversion factor
    # iri: https://onerecord.iata.org/ns/cargo#conversionFactor
    conversionFactor: Optional[float] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor")
    # label: lineItemNumber
    # comment: Number of the line item
    # iri: https://onerecord.iata.org/ns/cargo#lineItemNumber
    lineItemNumber: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemNumber")
    # label: rateSlac
    # comment: Integer holding the total slac considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateSlac
    rateSlac: Optional[int] = Field(default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateSlac")
class WaybillType(str, Enum):
    """
    label: WaybillType
    comment: Restricted code list for Waybill types
    """
    # label: DIRECT
    # comment: Indicates a Direct waybill
    DIRECT = URIRef("https://onerecord.iata.org/ns/cargo#DIRECT")
    # label: HOUSE
    # comment: Indicates a House Waybill
    HOUSE = URIRef("https://onerecord.iata.org/ns/cargo#HOUSE")
    # label: MASTER
    # comment: Indicates a Master Waybill
    MASTER = URIRef("https://onerecord.iata.org/ns/cargo#MASTER")