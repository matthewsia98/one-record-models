"""
This file was automatically generated from the ONE Record API ontology.

Ontology source: https://onerecord.iata.org/ns/cargo/ontology.ttl
Ontology version: https://onerecord.iata.org/ns/cargo/3.2-rc2
Generated on: 2025-12-31T20:58:49.476919+00:00

DO NOT EDIT MANUALLY.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from enum import Enum
from typing import ClassVar, List, Union

from pydantic import Field
from pydantic.json_schema import SkipJsonSchema
from rdflib import URIRef

from one_record_ontology.models.base_model import OneRecordBaseModel
from one_record_ontology.models.generated.code_lists import (
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


class AccountType(str, Enum):
    # label: CONSIGNEE
    # comment: Consignee's Account
    CONSIGNEE = URIRef("https://onerecord.iata.org/ns/cargo#CONSIGNEE")

    # label: FF
    # comment: Freight Forwarder Account
    FF = URIRef("https://onerecord.iata.org/ns/cargo#FF")

    # label: CONSIGNOR
    # comment: Consignor
    CONSIGNOR = URIRef("https://onerecord.iata.org/ns/cargo#CONSIGNOR")


class ActionTimeType(str, Enum):
    # label: REQUESTED
    # comment: Used when a time is requested
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")

    # label: PLANNED
    # comment: Used when a time is planned
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")

    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")


class BookingOptionStatus(str, Enum):
    # label: NOT_BOOKABLE
    # comment: Used when a booking option proposal is not bookable
    NOT_BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NOT_BOOKABLE")

    # label: BOOKED
    # comment: Used when a booking option proposal is booked
    BOOKED = URIRef("https://onerecord.iata.org/ns/cargo#BOOKED")

    # label: QUEUED
    # comment: Used when a booking or booking option is queued or pending
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")

    # label: BOOKABLE
    # comment: Used when a booking option (or proposal) is bookable
    BOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#BOOKABLE")

    # label: EXPIRED
    # comment: Used when a booking option proposal is expired
    EXPIRED = URIRef("https://onerecord.iata.org/ns/cargo#EXPIRED")

    # label: ON_REQUEST
    # comment: Used when a booking option proposal is on request
    ON_REQUEST = URIRef("https://onerecord.iata.org/ns/cargo#ON_REQUEST")

    # label: NONBOOKABLE
    # comment: Used when a booking option is nonbookable
    NONBOOKABLE = URIRef("https://onerecord.iata.org/ns/cargo#NONBOOKABLE")


class BookingStatus(str, Enum):
    # label: DELETED
    # comment: Used when a booking is deleted
    DELETED = URIRef("https://onerecord.iata.org/ns/cargo#DELETED")

    # label: QUEUED
    # comment: Used when a booking or booking option is queued or pending
    QUEUED = URIRef("https://onerecord.iata.org/ns/cargo#QUEUED")

    # label: REJECTED
    # comment: Used when a booking is rejected
    REJECTED = URIRef("https://onerecord.iata.org/ns/cargo#REJECTED")

    # label: CONFIRMED
    # comment: Used when a booking is confirmed
    CONFIRMED = URIRef("https://onerecord.iata.org/ns/cargo#CONFIRMED")


class CompositionType(str, Enum):
    # label: COMPOSITION
    # comment: Describes a composition, for example the loading of a container or the build-up of an ULD
    COMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#COMPOSITION")

    # label: DECOMPOSITION
    # comment: Describes a decomposition, for example the unloading of a container or the break-down of an ULD
    DECOMPOSITION = URIRef("https://onerecord.iata.org/ns/cargo#DECOMPOSITION")


class ContactDetailType(str, Enum):
    # label: ALTERNATE_EMAIL_ADDRESS
    # comment: Indicates a contact detail as alternate email address
    ALTERNATE_EMAIL_ADDRESS = URIRef(
        "https://onerecord.iata.org/ns/cargo#ALTERNATE_EMAIL_ADDRESS"
    )

    # label: PHONE_NUMBER
    # comment: Indicates a contact detail as phone number
    PHONE_NUMBER = URIRef("https://onerecord.iata.org/ns/cargo#PHONE_NUMBER")

    # label: ALTERNATE_PHONE_NUMBER
    # comment: Indicates a contact detail as alternate phone number
    ALTERNATE_PHONE_NUMBER = URIRef(
        "https://onerecord.iata.org/ns/cargo#ALTERNATE_PHONE_NUMBER"
    )

    # label: WEBSITE
    # comment: Indicates a contact detail as website
    WEBSITE = URIRef("https://onerecord.iata.org/ns/cargo#WEBSITE")

    # label: EMAIL_ADDRESS
    # comment: Indicates a contact detail as email address
    EMAIL_ADDRESS = URIRef("https://onerecord.iata.org/ns/cargo#EMAIL_ADDRESS")

    # label: FAX_NUMBER
    # comment: Indicates a contact detail as fax number
    FAX_NUMBER = URIRef("https://onerecord.iata.org/ns/cargo#FAX_NUMBER")

    # label: TELEX
    # comment: Indicates a contact detail as telex
    TELEX = URIRef("https://onerecord.iata.org/ns/cargo#TELEX")


class ContactRole(str, Enum):
    # label: EMERGENCY_CONTACT
    # comment: Indicates a contact person as emergency contact
    EMERGENCY_CONTACT = URIRef("https://onerecord.iata.org/ns/cargo#EMERGENCY_CONTACT")

    # label: CUSTOMER_CONTACT
    # comment: Indicates a contact person as customer contact
    CUSTOMER_CONTACT = URIRef("https://onerecord.iata.org/ns/cargo#CUSTOMER_CONTACT")

    # label: CUSTOMS_CONTACT
    # comment: Indicates a contact person as customs contact
    CUSTOMS_CONTACT = URIRef("https://onerecord.iata.org/ns/cargo#CUSTOMS_CONTACT")


class DirectionType(str, Enum):
    # label: UNPLANNED_STOP
    # comment: Indicates the that the movement time describes an unplanned stop
    UNPLANNED_STOP = URIRef("https://onerecord.iata.org/ns/cargo#UNPLANNED_STOP")

    # label: INBOUND
    # comment: Indicates the described direction in a movement time as inbound
    INBOUND = URIRef("https://onerecord.iata.org/ns/cargo#INBOUND")

    # label: OUTBOUND
    # comment: Indicates the described direction in a movement time as outbound
    OUTBOUND = URIRef("https://onerecord.iata.org/ns/cargo#OUTBOUND")


class EventTimeType(str, Enum):
    # label: PLANNED
    # comment: Used when a time is planned
    PLANNED = URIRef("https://onerecord.iata.org/ns/cargo#PLANNED")

    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")

    # label: REQUESTED
    # comment: Used when a time is requested
    REQUESTED = URIRef("https://onerecord.iata.org/ns/cargo#REQUESTED")

    # label: ESTIMATED
    # comment: Used when a time is estimated
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")

    # label: EXPECTED
    # comment: Used when a time is expected
    EXPECTED = URIRef("https://onerecord.iata.org/ns/cargo#EXPECTED")


class ExecutionStatus(str, Enum):
    # label: ACTIVE
    # comment: Used when a LogisticsActivity is active
    ACTIVE = URIRef("https://onerecord.iata.org/ns/cargo#ACTIVE")

    # label: PENDING
    # comment: Used when a LogisticsActivity is pending
    PENDING = URIRef("https://onerecord.iata.org/ns/cargo#PENDING")

    # label: CANCELLED
    # comment: Used when a LogisticsActivity is cancelled
    CANCELLED = URIRef("https://onerecord.iata.org/ns/cargo#CANCELLED")

    # label: COMPLETE
    # comment: Used when a LogisticsActivity is complete
    COMPLETE = URIRef("https://onerecord.iata.org/ns/cargo#COMPLETE")


class LoadType(str, Enum):
    # label: PALLET
    # comment: Indicates the load type as pallet
    PALLET = URIRef("https://onerecord.iata.org/ns/cargo#PALLET")

    # label: UNIT_LOAD_DEVICE
    # comment: Indicates the load type as uld
    UNIT_LOAD_DEVICE = URIRef("https://onerecord.iata.org/ns/cargo#UNIT_LOAD_DEVICE")

    # label: BULK
    # comment: Indicates the load type as bulk
    BULK = URIRef("https://onerecord.iata.org/ns/cargo#BULK")

    # label: LOOSE
    # comment: Indicates the load type as loose
    LOOSE = URIRef("https://onerecord.iata.org/ns/cargo#LOOSE")


class LoadingType(str, Enum):
    # label: LOADING
    # comment: Describes a loading process, for example putting an ULD on an aircraft or a piece in a truck
    LOADING = URIRef("https://onerecord.iata.org/ns/cargo#LOADING")

    # label: UNLOADING
    # comment: Describes an unloading process, for example removing an ULD from an aircraft or a piece from a truck
    UNLOADING = URIRef("https://onerecord.iata.org/ns/cargo#UNLOADING")


class ModeQualifier(str, Enum):
    # label: ON_CARRIAGE
    # comment: Indicates the mode qualifier as on carriage
    ON_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#ON_CARRIAGE")

    # label: PRE_CARRIAGE
    # comment: Indicates the mode qualifier as pre carriage
    PRE_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#PRE_CARRIAGE")

    # label: MAIN_CARRIAGE
    # comment: Indicates the mode qualifier as main carriage
    MAIN_CARRIAGE = URIRef("https://onerecord.iata.org/ns/cargo#MAIN_CARRIAGE")


class MovementTimeType(str, Enum):
    # label: ESTIMATED
    # comment: Used when a time is estimated
    ESTIMATED = URIRef("https://onerecord.iata.org/ns/cargo#ESTIMATED")

    # label: SCHEDULED
    # comment: Used when a time is scheduled
    SCHEDULED = URIRef("https://onerecord.iata.org/ns/cargo#SCHEDULED")

    # label: ACTUAL
    # comment: Used when a time is actual
    ACTUAL = URIRef("https://onerecord.iata.org/ns/cargo#ACTUAL")


class SensorType(str, Enum):
    # label: VIBRATION
    # comment: Indicates the sensor type as vibration
    VIBRATION = URIRef("https://onerecord.iata.org/ns/cargo#VIBRATION")

    # label: GEOLOCATION
    # comment: Indicates the sensor type as geolocation
    GEOLOCATION = URIRef("https://onerecord.iata.org/ns/cargo#GEOLOCATION")

    # label: THERMOMETER
    # comment: Indicates the sensor type as thermometer
    THERMOMETER = URIRef("https://onerecord.iata.org/ns/cargo#THERMOMETER")

    # label: TILT
    # comment: Indicates the sensor type as tilt
    TILT = URIRef("https://onerecord.iata.org/ns/cargo#TILT")

    # label: PRESSURE
    # comment: Indicates the sensor type as pressure
    PRESSURE = URIRef("https://onerecord.iata.org/ns/cargo#PRESSURE")

    # label: HUMIDITY
    # comment: Indicates the sensor type as humidity
    HUMIDITY = URIRef("https://onerecord.iata.org/ns/cargo#HUMIDITY")

    # label: LIGHT
    # comment: Indicates the sensor type as light
    LIGHT = URIRef("https://onerecord.iata.org/ns/cargo#LIGHT")

    # label: ACCELEROMETER
    # comment: Indicates the sensor type as accelerometer
    ACCELEROMETER = URIRef("https://onerecord.iata.org/ns/cargo#ACCELEROMETER")


class StoringType(str, Enum):
    # label: STORE_OUT
    # comment: Describes a store-out process, where a physical object leaves a specific location
    STORE_OUT = URIRef("https://onerecord.iata.org/ns/cargo#STORE_OUT")

    # label: STORE_IN
    # comment: Describes a store-in process, where a physical object is assigned to a specific location
    STORE_IN = URIRef("https://onerecord.iata.org/ns/cargo#STORE_IN")


class WaybillType(str, Enum):
    # label: HOUSE
    # comment: Indicates a House Waybill
    HOUSE = URIRef("https://onerecord.iata.org/ns/cargo#HOUSE")

    # label: DIRECT
    # comment: Indicates a Direct waybill
    DIRECT = URIRef("https://onerecord.iata.org/ns/cargo#DIRECT")

    # label: MASTER
    # comment: Indicates a Master Waybill
    MASTER = URIRef("https://onerecord.iata.org/ns/cargo#MASTER")


class AccountNumber(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#AccountNumber"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#AccountNumber"),
    ]

    # label: accountNumberType
    # comment: Type of the account of the account number
    accountNumberType: Union[AccountType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountNumberType",
        default=None,
    )

    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    textualValue: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
        default=None,
    )


class AccountingNote(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#AccountingNote"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#AccountingNote"),
    ]

    # label: accountingNoteIdentifier
    # comment: String holding accounting information (AWB box 10)
    accountingNoteIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteIdentifier",
        default=None,
    )

    # label: accountingNoteText
    # comment: String holding the identifier in an accounting note (AWB box 10)
    accountingNoteText: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteText",
        default=None,
    )


class ActivitySequence(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#ActivitySequence"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ActivitySequence"),
    ]

    # label: activity
    # comment: Reference to the Activity that is performed as part of a Service
    activity: Union[LogisticsActivity, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#activity",
        default=None,
    )

    # label: sequenceNumber
    # comment: Short text to detail sequence number (alphanumeric)
    sequenceNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#sequenceNumber",
        default=None,
    )


class Address(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Address")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Address"),
    ]

    # label: addressCode
    # comment: Address identifier using special coding systems e.g. US CBP FIRMS code
    addressCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#addressCode",
        default=None,
    )

    # label: cityCode
    # comment: UN/LOCODE city code (5 letter) or IATA city code (3 letter)
    cityCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#cityCode",
        default=None,
    )

    # label: country
    # comment: Country details. Refer ISO 3166-2
    country: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#country",
        default=None,
    )

    # label: postalCode
    # comment: Postal / ZIP code
    postalCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#postalCode",
        default=None,
    )

    # label: regionCode
    # comment: Region/ State / Department. Refer ISO 3166-2
    regionCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#regionCode",
        default=None,
    )

    # label: cityName
    # comment: String holding a city name
    cityName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#cityName",
        default=None,
    )

    # label: postOfficeBox
    # comment: Post Office box number / code
    postOfficeBox: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#postOfficeBox",
        default=None,
    )

    # label: streetAddressLines
    # comment: Street address including street name, street number, building number, apartment etc
    streetAddressLines: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#streetAddressLines",
        default_factory=list,
    )

    # label: textualPostCode
    # comment: Postal / ZIP code
    textualPostCode: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualPostCode",
        default=None,
    )


class Adjustments(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Adjustments")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Adjustments"),
    ]

    # label: correctionNumber
    # comment: Number of the adjustment
    correctionNumber: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#correctionNumber",
        default=None,
    )

    # label: correctionSerialNumber
    # comment: Serial Number of the correction
    correctionSerialNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#correctionSerialNumber",
        default=None,
    )

    # label: reasonsForAdjustments
    # comment: A free text for user to include a reason for correction
    reasonsForAdjustments: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#reasonsForAdjustments",
        default=None,
    )


class BookingPreferences(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#BookingPreferences"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BookingPreferences"),
    ]

    # label: aircraftPossibilityCode
    # comment: Type of aircraft to be used if any specific requirements (e.g. Pure freighter, etc.)
    aircraftPossibilityCode: Union[AircraftPossibilityCode, SkipJsonSchema[None]] = (
        Field(
            serialization_alias="https://onerecord.iata.org/ns/cargo#aircraftPossibilityCode",
            default=None,
        )
    )

    # label: excludedViaPoints
    # comment: Locations of excluded Via Points
    excludedViaPoints: List[Location] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#excludedViaPoints",
        default_factory=list,
    )

    # label: includedViaPoints
    # comment: Locations or stations to included in the routing
    includedViaPoints: List[Location] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#includedViaPoints",
        default_factory=list,
    )

    # label: maxSegments
    # comment: Maximum number of segments for the transportation of the goods. 1 means direct flight
    maxSegments: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#maxSegments",
        default=None,
    )

    # label: preferredTransportId
    # comment: When part of the Request it refers to the preferred Transport ID from the customer. When part of the BookingOption (offer or actual booking) it refers to the expected Transport ID or flight
    preferredTransportId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#preferredTransportId",
        default=None,
    )

    # label: priceReferenceId
    # comment: Reference to a price reference if existing (e.g. Allotment number, contract reference, etc.)
    priceReferenceId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#priceReferenceId",
        default=None,
    )


class BookingSegment(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#BookingSegment"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BookingSegment"),
    ]

    # label: pieceGroups
    # comment: Reference to the Piece groups of the shipment
    pieceGroups: List[PieceGroup] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroups",
        default_factory=list,
    )

    # label: spaceAllocationCode
    # comment: Current status of the space allocation of the booking segment
    spaceAllocationCode: Union[SpaceAllocationCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#spaceAllocationCode",
        default=None,
    )

    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    transportLegs: Union[TransportLegs, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs",
        default=None,
    )

    # label: allotmentCode
    # comment: String holding an allotment code of a booking segment
    allotmentCode: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#allotmentCode",
        default=None,
    )


class BookingTimes(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#BookingTimes")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BookingTimes"),
    ]

    # label: earliestAcceptanceTime
    # comment: Earliest acceptance date time (requested or proposed)
    earliestAcceptanceTime: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#earliestAcceptanceTime",
        default=None,
    )

    # label: latestAcceptanceTime
    # comment: Latest Acceptance time as per CargoIQ definition (requested, proposed or actual)
    latestAcceptanceTime: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#latestAcceptanceTime",
        default=None,
    )

    # label: latestArrivalTime
    # comment: Latest arrival time at destination
    latestArrivalTime: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#latestArrivalTime",
        default=None,
    )

    # label: timeOfAvailability
    # comment: Time of availability of the shipment as per CargoIQ definition
    timeOfAvailability: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#timeOfAvailability",
        default=None,
    )

    # label: totalTransitTime
    # comment: Total transit time as per CargoIQ definition, expressed as a duration
    totalTransitTime: Union[timedelta, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalTransitTime",
        default=None,
    )


class CarrierProduct(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#CarrierProduct"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#CarrierProduct"),
    ]

    # label: productCode
    # comment: Carrier's product code
    productCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#productCode",
        default=None,
    )

    # label: serviceLevelCode
    # comment: Service level code
    serviceLevelCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceLevelCode",
        default=None,
    )

    # label: productDescription
    # comment: Carrier's product description
    productDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#productDescription",
        default=None,
    )


class Characteristic(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#Characteristic"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Characteristic"),
    ]

    # label: characteristicType
    # comment: Product characteristics code - e.g. CLR - Color. Not restricted to a list.
    characteristicType: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#characteristicType",
        default=None,
    )

    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    textualValue: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
        default=None,
    )


class CodeListElement(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#CodeListElement"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#CodeListElement"),
    ]

    # label: code
    # comment: Code or short version of a code, for example "CH" for Switzerland when referring to the UN/LOCODE code list
    code: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#code",
        default=None,
    )

    # label: codeDescription
    # comment: Description or long version of the code, for example "Switzerland" for Switzerland when referring to the UN/LOCODE code list
    codeDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeDescription",
        default=None,
    )

    # label: codeLevel
    # comment: Integer indicating the level of a code if a codelists is hierarchical, for example HS-Codes
    codeLevel: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeLevel",
        default=None,
    )

    # label: codeListName
    # comment: Official name of the code list without version number when direct reference is not possible, for example "UN/LOCODE" when referring to the UN/LOCODE code list
    codeListName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeListName",
        default=None,
    )

    # label: codeListReference
    # comment: URL to access the code list the code is taken from, for example "https://unece.org/trade/cefact/unlocode-code-list-country-and-territory" for UN/LOCODE.
    codeListReference: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeListReference",
        default=None,
    )

    # label: codeListVersion
    # comment: Version of the code list, for example "223-1" for UN/LOCODE. Used if the property codeListName is used or the version is not apparent from the resource referred to in property codeListReference.
    codeListVersion: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeListVersion",
        default=None,
    )


class ContactDetail(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#ContactDetail"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ContactDetail"),
    ]

    # label: contactDetailType
    # comment: Type of the contact details, e.g. Phone number, Mail address
    contactDetailType: Union[ContactDetailType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetailType",
        default=None,
    )

    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    textualValue: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
        default=None,
    )


class CurrencyValue(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#CurrencyValue"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#CurrencyValue"),
    ]

    # label: currencyUnit
    # comment: Information about the currency used in a CurrencyValue. Create an instance of CurrencyCode based on ISO 4217
    currencyUnit: Union[CurrencyCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#currencyUnit",
        default=None,
    )

    # label: numericalValue
    # comment: Numerical value
    numericalValue: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue",
        default=None,
    )


class Dimensions(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Dimensions")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Dimensions"),
    ]

    # label: height
    # comment: Height
    height: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#height",
        default=None,
    )

    # label: length
    # comment: Length
    length: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#length",
        default=None,
    )

    # label: volume
    # comment: Volume
    volume: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#volume",
        default=None,
    )

    # label: width
    # comment: Width
    width: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#width",
        default=None,
    )


class Geolocation(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Geolocation")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Geolocation"),
    ]

    # label: elevation
    # comment: Elevation from sea level - Change of data type to Value as of ontology v1.1
    elevation: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#elevation",
        default=None,
    )

    # label: latitude
    # comment: Location latitude decimal
    latitude: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#latitude",
        default=None,
    )

    # label: longitude
    # comment: Location longitude decimal
    longitude: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#longitude",
        default=None,
    )


class LineItemPackage(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LineItemPackage"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LineItemPackage"),
    ]

    # label: packageGrossWeight
    # comment: Information about the total weight of a grouping of pieces
    packageGrossWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageGrossWeight",
        default=None,
    )

    # label: packageVolume
    # comment: Information about the total volume of a grouping of pieces
    packageVolume: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageVolume",
        default=None,
    )

    # label: pieceReferences
    # comment: References to Pieces for which a rate applies
    pieceReferences: List[Piece] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceReferences",
        default_factory=list,
    )

    # label: packageSlac
    # comment: Integer holding the total slac of a grouping of pieces
    packageSlac: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageSlac",
        default=None,
    )


class LogisticsEvent(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LogisticsEvent"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsEvent"),
    ]

    # label: eventCode
    # comment: Movement or milestone code. Can hold a named individual of the StatusCode core code list (corresponding to cXML code list 1.18), but can also be referring to different code lists.
    eventCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventCode",
        default=None,
    )

    # label: eventFor
    # comment: Refers to the URI of the linked object(s)
    eventFor: Union[LogisticsObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventFor",
        default=None,
    )

    # label: eventLocation
    # comment: Location of event
    eventLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventLocation",
        default=None,
    )

    # label: eventTimeType
    # comment: Indicates type of event e.g.  Scheduled, Estimated, Actual
    eventTimeType: Union[EventTimeType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventTimeType",
        default=None,
    )

    # label: externalReferences
    # comment: References to all associated ExternalReferences
    externalReferences: List[ExternalReference] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#externalReferences",
        default_factory=list,
    )

    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    involvedParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
        default_factory=list,
    )

    # label: recordingActor
    # comment: Reference to the Actor recording the LogisticsEvent
    recordingActor: Union[Actor, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#recordingActor",
        default=None,
    )

    # label: recordingOrganization
    # comment: Organization recording the LogisticsEvent
    recordingOrganization: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#recordingOrganization",
        default=None,
    )

    # label: creationDate
    # comment: DateTime at which the LogisticsEvent was posted
    creationDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#creationDate",
        default=None,
    )

    # label: eventDate
    # comment: Date and time of the event
    eventDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventDate",
        default=None,
    )

    # label: eventName
    # comment: If no EventCode provided, event name - e.g. Security clearance
    eventName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#eventName",
        default=None,
    )

    # label: partialEventIndicator
    # comment: Boolean indicating that the LogisticsEvent is only applicable for parts of the LogisticObject it was recorded for, for example for some Pieces of a Shipment
    partialEventIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#partialEventIndicator",
        default=None,
    )


class LogisticsObject(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LogisticsObject"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: checks
    # comment: References to the CheckActions performed on the object
    checks: List[Check] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checks",
        default_factory=list,
    )

    # label: events
    # comment: Events object
    events: List[LogisticsEvent] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#events",
        default_factory=list,
    )

    # label: externalReferences
    # comment: References to all associated ExternalReferences
    externalReferences: List[ExternalReference] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#externalReferences",
        default_factory=list,
    )

    # label: skeletonIndicator
    # comment: Indicator whether a logistics object is a skeleton object
    skeletonIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#skeletonIndicator",
        default=None,
    )


class Measurement(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Measurement")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Measurement"),
    ]

    # label: measurementValue
    # comment: Information about all non-Geolocation values of the measurement
    measurementValue: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#measurementValue",
        default=None,
    )

    # label: recordedGeolocation
    # comment: Reference to the Geolocation recorded of the measurement
    recordedGeolocation: Union[Geolocation, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#recordedGeolocation",
        default=None,
    )

    # label: measurementTimestamp
    # comment: Timestamp for the measurement
    measurementTimestamp: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#measurementTimestamp",
        default=None,
    )


class MovementTime(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#MovementTime")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#MovementTime"),
    ]

    # label: direction
    # comment: Direction to indicate if it's Inbound or Outbound
    direction: Union[DirectionType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#direction",
        default=None,
    )

    # label: movementMilestone
    # comment: The milestone list still needs to be defined, it includes elements from CXML Code List 1.92 but is not limited to those values, e.g. block-on and block-off times might be added as a comparison to wheels off and touchdown.
    movementMilestone: Union[MovementIndicator, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementMilestone",
        default=None,
    )

    # label: movementTimeType
    # comment: The type of time can be Actual, Estimated ot Scheduled
    movementTimeType: Union[MovementTimeType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimeType",
        default=None,
    )

    # label: movementTimestamp
    # comment: Timestamp (date and time) of the movement time. If the movement time is recorded asynchronously, the timestamp should reflect the actual time, not when the data was created.
    movementTimestamp: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimestamp",
        default=None,
    )


class OtherCharge(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#OtherCharge")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#OtherCharge"),
    ]

    # label: chargePaymentType
    # comment: Indicates if charge is prepaid or collect (P, C)
    chargePaymentType: Union[PrepaidCollectIndicator, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargePaymentType",
        default=None,
    )

    # label: entitlement
    # comment: Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    entitlement: Union[EntitlementCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#entitlement",
        default=None,
    )

    # label: otherChargeAmount
    # comment: Other Charge amount
    otherChargeAmount: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeAmount",
        default=None,
    )

    # label: otherChargeCode
    # comment: Refer to CargoXML Code List 1.2 for Other Charges
    otherChargeCode: Union[OtherChargeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeCode",
        default=None,
    )

    # label: chargeQuantity
    # comment: Double describing the time or item basis quantity of a charge
    chargeQuantity: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeQuantity",
        default=None,
    )

    # label: locationIndicator
    # comment: String indicating if the Other Charge Location is Origin (O) or Transit (T) or Destination(D)
    locationIndicator: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationIndicator",
        default=None,
    )

    # label: reasonDescription
    # comment: String describing the reason for a charge
    reasonDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#reasonDescription",
        default=None,
    )


class OtherIdentifier(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#OtherIdentifier"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#OtherIdentifier"),
    ]

    # label: otherIdentifierType
    # comment: Identifier type or description
    otherIdentifierType: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifierType",
        default=None,
    )

    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    textualValue: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
        default=None,
    )


class Party(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Party")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Party"),
    ]

    # label: accountNumbers
    # comment: Information about account numbers
    accountNumbers: List[AccountNumber] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountNumbers",
        default_factory=list,
    )

    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    otherIdentifiers: List[OtherIdentifier] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
        default_factory=list,
    )

    # label: partyDetails
    # comment: Reference to the Agent described by the role of the Party
    partyDetails: Union[LogisticsAgent, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#partyDetails",
        default=None,
    )

    # label: partyRole
    # comment: Role fo the Company in the context. Can refer to Code List 1.36 in the CXML Toolkit
    partyRole: Union[ParticipantIdentifier, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#partyRole",
        default=None,
    )


class PieceGroup(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#PieceGroup")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#PieceGroup"),
    ]

    # label: dryIceWeight
    # comment: Weight of dry ice
    dryIceWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#dryIceWeight",
        default=None,
    )

    # label: pieceGroupGrossWeight
    # comment: Total gross weight of the piece group
    pieceGroupGrossWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupGrossWeight",
        default=None,
    )

    # label: pieceGroupCount
    # comment: Number of pieces in the piece group
    pieceGroupCount: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupCount",
        default=None,
    )

    # label: pieceGroupId
    # comment: Identifier of the piece group, increasing integers
    pieceGroupId: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroupId",
        default=None,
    )


class Ranges(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Ranges")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Ranges"),
    ]

    # label: rateClassCode
    # comment: Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    rateClassCode: Union[RateClassCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCode",
        default=None,
    )

    # label: uldRateClassType
    # comment: ULD Rate information - ULD Rate Class Type
    uldRateClassType: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldRateClassType",
        default=None,
    )

    # label: maximumQuantity
    # comment: Maximum quantity
    maximumQuantity: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#maximumQuantity",
        default=None,
    )

    # label: minimumQuantity
    # comment: Minimum quantity
    minimumQuantity: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#minimumQuantity",
        default=None,
    )

    # label: unitBasis
    # comment: Specific commodity code linked to commodity
    unitBasis: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#unitBasis",
        default=None,
    )


class RegulatedEntity(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#RegulatedEntity"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#RegulatedEntity"),
    ]

    # label: owningOrganization
    # comment: Reference to the Organization for which the RegulatedEntity information is valid
    owningOrganization: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#owningOrganization",
        default=None,
    )

    # label: regulatedEntityCategory
    # comment: Category code of the Regulated Entity
    regulatedEntityCategory: Union[
        RegulatedEntityCategoryCode, SkipJsonSchema[None]
    ] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityCategory",
        default=None,
    )

    # label: regulatedEntityExpiryDate
    # comment: Expiry date 4 digits month/year
    regulatedEntityExpiryDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityExpiryDate",
        default=None,
    )

    # label: regulatedEntityIdentifier
    # comment: Regulated entity identifier as per IATA e-CSD/CSD Resolution 65
    regulatedEntityIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityIdentifier",
        default=None,
    )


class StationRemarks(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#StationRemarks"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#StationRemarks"),
    ]

    # label: station
    # comment: Reference to the station (Airport), mandatory
    station: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#station",
        default=None,
    )

    # label: remarksText
    # comment: Details of the remarks, mandatory
    remarksText: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#remarksText",
        default=None,
    )


class TemperatureInstructions(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#TemperatureInstructions"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#TemperatureInstructions"),
    ]

    # label: maxTemperature
    # comment: Maximum temperature of the range
    maxTemperature: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#maxTemperature",
        default=None,
    )

    # label: minTemperature
    # comment: Minimum temperature of the range
    minTemperature: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#minTemperature",
        default=None,
    )


class UnitsPreference(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#UnitsPreference"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#UnitsPreference"),
    ]

    # label: currency
    # comment: Preferred unit for currency
    currency: Union[CurrencyCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#currency",
        default=None,
    )

    # label: dimensionsUnit
    # comment: Preferred unit for measurement and dimensions
    dimensionsUnit: Union[DimensionsUnitCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#dimensionsUnit",
        default=None,
    )

    # label: temperatureUnit
    # comment: Preferred unit for temperature
    temperatureUnit: Union[TemperatureUnitCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureUnit",
        default=None,
    )

    # label: volumeUnit
    # comment: Preferred unit for volume
    volumeUnit: Union[VolumeUnitCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#volumeUnit",
        default=None,
    )

    # label: weightUnit
    # comment: Preferred unit for weight
    weightUnit: Union[WeightUnitCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#weightUnit",
        default=None,
    )


class Value(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Value")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Value"),
    ]

    # label: unit
    # comment: Unit of measurement as per MeasurementUnitCode codelist. If the code is not present, create an instance of MeasurementUnitCode based on UNECE Rec. 20 Rev. 17e-2021
    unit: Union[MeasurementUnitCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#unit",
        default=None,
    )

    # label: numericalValue
    # comment: Numerical value
    numericalValue: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue",
        default=None,
    )


class VolumetricWeight(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#VolumetricWeight"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#VolumetricWeight"),
    ]

    # label: chargeableWeight
    # comment: Chargeable weight
    chargeableWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight",
        default=None,
    )

    # label: conversionFactor
    # comment: Volume to weight conversion factor
    conversionFactor: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor",
        default=None,
    )


class WaybillLineItem(OneRecordBaseModel):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#WaybillLineItem"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#WaybillLineItem"),
    ]

    # label: chargeableWeight
    # comment: Chargeable weight
    chargeableWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight",
        default=None,
    )

    # label: lineItemPackages
    # comment: References to piece groupings for rating
    lineItemPackages: List[LineItemPackage] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemPackages",
        default_factory=list,
    )

    # label: rateCharge
    # comment: TACT Rate for rate description details
    rateCharge: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateCharge",
        default=None,
    )

    # label: rateClassCode
    # comment: Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    rateClassCode: Union[RateClassCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCode",
        default=None,
    )

    # label: rateClassCodeBasic
    # comment: Rate Surcharge/Reduction - Basic Rate Class Code
    rateClassCodeBasic: Union[BasicRateClassCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCodeBasic",
        default=None,
    )

    # label: rateGrossWeight
    # comment: Information about the total gross weight considered for a rate
    rateGrossWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateGrossWeight",
        default=None,
    )

    # label: ratePercentage
    # comment: Rate Surcharge/Reduction - Percentage of  red. / surcharge
    ratePercentage: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ratePercentage",
        default=None,
    )

    # label: rateVolume
    # comment: Information about the total volume considered for a rate
    rateVolume: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateVolume",
        default=None,
    )

    # label: rcp
    # comment: IATA 3-letter city code of the rate combination point as defined in TACT
    rcp: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rcp",
        default=None,
    )

    # label: uldRateClassType
    # comment: ULD Rate information - ULD Rate Class Type
    uldRateClassType: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldRateClassType",
        default=None,
    )

    # label: uldReferences
    # comment: References to ULDs for which the rate applies
    uldReferences: List[ULD] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldReferences",
        default_factory=list,
    )

    # label: conversionFactor
    # comment: Volume to weight conversion factor
    conversionFactor: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor",
        default=None,
    )

    # label: lineItemNumber
    # comment: Number of the line item
    lineItemNumber: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemNumber",
        default=None,
    )

    # label: rateSlac
    # comment: Integer holding the total slac considered for a rate
    rateSlac: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateSlac",
        default=None,
    )


class Answer(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Answer")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Answer"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: answerActor
    # comment: Reference to the Actor giving the Answer
    answerActor: Union[Actor, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#answerActor",
        default=None,
    )

    # label: answerValue
    # comment: Information about an answer Value of any kind of the Answer
    answerValue: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#answerValue",
        default=None,
    )

    # label: givenAtLocation
    # comment: Reference to the Location from which the Question was answered, relevant for split checks with documentary and physical elements
    givenAtLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#givenAtLocation",
        default=None,
    )

    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    involvedParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
        default_factory=list,
    )

    # label: question
    # comment: Reference to the Question the Answer is for
    question: Union[Question, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#question",
        default=None,
    )

    # label: text
    # comment: Text for the Answer
    text: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#text",
        default=None,
    )


class BillingDetails(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#BillingDetails"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BillingDetails"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: adjustments
    # comment: Information about Adjustments performed on the BillingDetails
    adjustments: List[Adjustments] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#adjustments",
        default_factory=list,
    )

    # label: awbUseIndicator
    # comment: It must either contain the values of R for Revenue AWB, V for Void AWB or S for Service AWB.
    awbUseIndicator: Union[AWBUseIndicator, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbUseIndicator",
        default=None,
    )

    # label: detailedWaybill
    # comment: Reference to the Waybill
    detailedWaybill: Union[Waybill, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#detailedWaybill",
        default=None,
    )

    # label: taxDueAgent
    # comment: Tax due Agent (VAT/GST on Commission). Total VAT/TAX amount payable by airline to agent
    taxDueAgent: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAgent",
        default=None,
    )

    # label: taxDueAirline
    # comment: Tax due Airline (as per AWB, or VAT/GST as per invoice). Total VAT/TAX amount payable by agent to airline
    taxDueAirline: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAirline",
        default=None,
    )

    # label: awbAcceptanceDate
    # comment: The Date AWB Acceptance should be the same as the Date AWB Delivery. (beginning of the process)
    awbAcceptanceDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbAcceptanceDate",
        default=None,
    )

    # label: awbDeliveryDate
    # comment: The Date AWB Delivery is also used as the AWB Execution date which will determine which billing period it will be processed and billed in.
    awbDeliveryDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbDeliveryDate",
        default=None,
    )

    # label: awbExecutionDate
    # comment: The AWB execution date determines which billing period the document will be processed and billed in.
    awbExecutionDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbExecutionDate",
        default=None,
    )

    # label: commission
    # comment: The commission amount in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    commission: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#commission",
        default=None,
    )

    # label: commissionIndicator
    # comment: Indicates if commission is applied. Boolean
    commissionIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#commissionIndicator",
        default=None,
    )

    # label: commissionPercentage
    # comment: The commission percentage in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    commissionPercentage: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#commissionPercentage",
        default=None,
    )

    # label: discount
    # comment: This is used as a discount to the “official” transportation charge on AWB to arrive at actual selling price
    discount: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#discount",
        default=None,
    )

    # label: exchangeRate
    # comment: The Rate at which the Air Waybill Amount has been multiplied to arrive at the amount of settlement.
    exchangeRate: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#exchangeRate",
        default=None,
    )

    # label: nbCorrections
    # comment: Number of corrections to CASS records
    nbCorrections: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#nbCorrections",
        default=None,
    )

    # label: vatIndicator
    # comment: Indicate if subject to VAT (boolean)
    vatIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#vatIndicator",
        default=None,
    )


class BookingOption(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#BookingOption"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BookingOption"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    bookingTimes: Union[BookingTimes, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingTimes",
        default=None,
    )

    # label: carrier
    # comment: Reference to the operating carrier
    carrier: Union[Carrier, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrier",
        default=None,
    )

    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    carrierProduct: Union[CarrierProduct, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct",
        default=None,
    )

    # label: forBookingOptionRequest
    # comment: Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    forBookingOptionRequest: Union[BookingOptionRequest, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOptionRequest",
        default=None,
    )

    # label: forBookingRequest
    # comment: Reference to the Booking Request the of the Booking Option
    forBookingRequest: Union[BookingRequest, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingRequest",
        default=None,
    )

    # label: price
    # comment: Price of the Booking (if different from the offer)
    price: Union[Price, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#price",
        default=None,
    )

    # label: stationRemarks
    # comment: Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    stationRemarks: List[StationRemarks] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#stationRemarks",
        default_factory=list,
    )

    # label: statusBookingOption
    # comment: Status of the Booking Option
    statusBookingOption: Union[BookingOptionStatus, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#statusBookingOption",
        default=None,
    )

    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    transportLegs: List[TransportLegs] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs",
        default_factory=list,
    )

    # label: unitsPreference
    # comment: Reference to unit preferences of the request (e.g. kg or cm)
    unitsPreference: Union[UnitsPreference, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#unitsPreference",
        default=None,
    )

    # label: additionalInformation
    # comment: Additional information related to the Booking Option, e.g. sales details
    additionalInformation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#additionalInformation",
        default=None,
    )

    # label: alternatives
    # comment: Description of the alternatives proposed that do not match the Booking Option Request
    alternatives: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#alternatives",
        default_factory=list,
    )

    # label: offerValidFrom
    # comment: Date and time of beginning of offer validity
    offerValidFrom: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidFrom",
        default=None,
    )

    # label: offerValidTo
    # comment: Date and time of end of offer validity
    offerValidTo: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidTo",
        default=None,
    )

    # label: requestMatch
    # comment: Indicates if the Booking Option is a match to the Booking Option Request preferences
    requestMatch: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#requestMatch",
        default=None,
    )


class BookingOptionRequest(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#BookingOptionRequest"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BookingOptionRequest"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: bookingOptions
    # comment: Reference to all Booking Options
    bookingOptions: List[BookingOption] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingOptions",
        default_factory=list,
    )

    # label: bookingPreference
    # comment: Reference to the Booking preferences
    bookingPreference: Union[BookingPreferences, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingPreference",
        default=None,
    )

    # label: bookingShipmentDetails
    # comment: Reference to the BookingShipment if required
    bookingShipmentDetails: Union[BookingShipment, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingShipmentDetails",
        default=None,
    )

    # label: bookingToUpdate
    # comment: Reference to the Booking to update
    bookingToUpdate: Union[Booking, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingToUpdate",
        default=None,
    )

    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    carrierProduct: Union[CarrierProduct, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct",
        default=None,
    )

    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    involvedParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
        default_factory=list,
    )

    # label: timePreferences
    # comment: Schedule preferences of the request
    timePreferences: Union[BookingTimes, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#timePreferences",
        default=None,
    )

    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    transportLegs: List[TransportLegs] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs",
        default_factory=list,
    )

    # label: unitsPreference
    # comment: Reference to unit preferences of the request (e.g. kg or cm)
    unitsPreference: Union[UnitsPreference, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#unitsPreference",
        default=None,
    )

    # label: knownShipper
    # comment: Indication if shipper is a Known Shipper as per TSA grant
    knownShipper: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#knownShipper",
        default=None,
    )


class BookingRequest(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#BookingRequest"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BookingRequest"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: booking
    # comment: Reference to the Booking
    booking: Union[Booking, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#booking",
        default=None,
    )

    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    forBookingOption: Union[BookingOption, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption",
        default=None,
    )

    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    waybillNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber",
        default=None,
        pattern=r"[A-Z0-9]+",
    )

    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    waybillPrefix: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix",
        default=None,
        max_length=3,
    )


class BookingShipment(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#BookingShipment"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#BookingShipment"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: chargeableWeight
    # comment: Chargeable weight
    chargeableWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight",
        default=None,
    )

    # label: customsInformation
    # comment: Customs details
    customsInformation: List[CustomsInformation] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation",
        default_factory=list,
    )

    # label: densityGroupCode
    # comment: Density Group Code as defined in cXML code list 2
    densityGroupCode: Union[DensityGroupCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#densityGroupCode",
        default=None,
    )

    # label: expectedCommodity
    # comment: Expected commodity of the shipment as per Commodity Code list. Either this or expected HS code required
    expectedCommodity: Union[CommodityCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#expectedCommodity",
        default=None,
    )

    # label: expectedHScode
    # comment: Expected commodity of the shipment as per HS code (at least 6 digits). Either this or expectedCommodityCode required
    expectedHScode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#expectedHScode",
        default=None,
    )

    # label: forBookingOptionRequest
    # comment: Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    forBookingOptionRequest: Union[BookingOptionRequest, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOptionRequest",
        default=None,
    )

    # label: pieceGroups
    # comment: Reference to the Piece groups of the shipment
    pieceGroups: List[PieceGroup] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroups",
        default_factory=list,
    )

    # label: specialHandlingCodes
    # comment: Three-letter special handling code (SPH)
    specialHandlingCodes: List[SpecialHandlingCode] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialHandlingCodes",
        default_factory=list,
    )

    # label: temperatureInstructions
    # comment: Temperature instructions if a specific range
    temperatureInstructions: Union[TemperatureInstructions, SkipJsonSchema[None]] = (
        Field(
            serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureInstructions",
            default=None,
        )
    )

    # label: totalDimensions
    # comment: Dimensions of the whole shipment
    totalDimensions: Union[Dimensions, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalDimensions",
        default=None,
    )

    # label: totalGrossWeight
    # comment: Total gross weight of the whole shipment
    totalGrossWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalGrossWeight",
        default=None,
    )

    # label: consolidationIndicator
    # comment: Indication if the shipment is a consolidation
    consolidationIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#consolidationIndicator",
        default=None,
    )

    # label: specialServiceRequests
    # comment: Special service requests
    specialServiceRequests: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialServiceRequests",
        default_factory=list,
    )

    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    textualHandlingInstructions: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions",
        default_factory=list,
    )


class CO2Emissions(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#CO2Emissions")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#CO2Emissions"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: calculatedEmissions
    # comment: CO2 emissions calculated
    calculatedEmissions: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#calculatedEmissions",
        default=None,
    )

    # label: calculationFor
    # comment: Reference to the TransportMovement or TransportLegs the CO2Emissions have been calculated for
    calculationFor: Union[LogisticsObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#calculationFor",
        default=None,
    )

    # label: methodName
    # comment: Name of the CO2 calculation method
    methodName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#methodName",
        default=None,
    )

    # label: methodVersion
    # comment: Version used for the calculation
    methodVersion: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#methodVersion",
        default=None,
    )


class CheckTemplate(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#CheckTemplate"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#CheckTemplate"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    involvedParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
        default_factory=list,
    )

    # label: legacyTemplate
    # comment: Reference to an ExternalReference holding a legacy template outside of ONE Record, such as a photo or pdf of a checksheet
    legacyTemplate: Union[ExternalReference, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#legacyTemplate",
        default=None,
    )

    # label: questions
    # comment: References to all Questions that are part of this template
    questions: List[Question] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#questions",
        default_factory=list,
    )

    # label: usedInCheck
    # comment: Reference to the Check the template was used in
    usedInCheck: Union[Check, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#usedInCheck",
        default=None,
    )

    # label: date
    # comment: DateTime on which the CheckTemplate was released
    date: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#date",
        default=None,
    )

    # label: name
    # comment: Human-understandable name of object depending on the context
    name: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#name",
        default=None,
    )

    # label: templatePurpose
    # comment: Purpose of the template
    templatePurpose: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#templatePurpose",
        default=None,
    )

    # label: version
    # comment: Version of the template
    version: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#version",
        default=None,
    )


class CheckTotalResult(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#CheckTotalResult"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#CheckTotalResult"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: certifiedByActor
    # comment: Reference to the Actor certifying the result of the Check if required
    certifiedByActor: Union[Person, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#certifiedByActor",
        default=None,
    )

    # label: resultOfCheck
    resultOfCheck: Union[Check, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#resultOfCheck",
        default=None,
    )

    # label: resultValue
    # comment: Information about a result Value of any kind of the Check
    resultValue: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#resultValue",
        default=None,
    )

    # label: checkRemark
    # comment: Free text remarks to the check result
    checkRemark: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkRemark",
        default=None,
    )

    # label: passed
    # comment: Boolean indicating whether the Check was passed
    passed: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#passed",
        default=None,
    )


class CustomsInformation(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#CustomsInformation"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#CustomsInformation"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: contentCode
    # comment: Customs, Security and Regulatory Control Information Identifier. Coded indicator qualifying Customs related information: Item Number "I", Exemption Legend "L", System Downtime Reference "S", Unique Consignment Reference Number "U", Movement Reference Number "M" . Refers to Code List 1.1. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    contentCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contentCode",
        default=None,
    )

    # label: country
    # comment: Country details. Refer ISO 3166-2
    country: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#country",
        default=None,
    )

    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    issuedForPiece: Union[Piece, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece",
        default=None,
    )

    # label: issuedForShipment
    # comment: Reference to the shipment the document was issued for
    issuedForShipment: Union[Shipment, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForShipment",
        default=None,
    )

    # label: subjectCode
    # comment: Information Identifier. Code identifying a piece of information/entity e.g. "IMP" for import, "EXP" for export, "AGT" for Agent, "ISS" for The Regulated Agent Issuing the Security Status for a Consignment etc. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    subjectCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#subjectCode",
        default=None,
    )

    # label: note
    # comment: Free text for customs remarks, not used in OCI Composition Rules Table
    note: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#note",
        default=None,
    )

    # label: ociLineNumber
    # comment: Integer holding the oci line number when upcasting multi-line oci structures from CIMP/CXML
    ociLineNumber: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ociLineNumber",
        default=None,
    )

    # label: otherCustomsInformation
    # comment: Supplementary Customs, Security and Regulatory Control Information
    otherCustomsInformation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherCustomsInformation",
        default=None,
    )


class DgDeclaration(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#DgDeclaration"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#DgDeclaration"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: arrivalLocation
    # comment: Reference to the arrival Location
    arrivalLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
        default=None,
    )

    # label: declarationPlace
    # comment: Reference to the Location the DgDeclaration was declared at
    declarationPlace: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#declarationPlace",
        default=None,
    )

    # label: departureLocation
    # comment: Reference to the departure Location
    departureLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
        default=None,
    )

    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    issuedForPiece: Union[Piece, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece",
        default=None,
    )

    # label: aircraftLimitationInformation
    # comment: Contains the Special Handling Code related to the prescribed limitation. Hardcoded to PASSENGER AND CARGO AIRCRAFT or CARGO AIRCRAFT ONLY. This field is mandatory for air (Air)
    aircraftLimitationInformation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#aircraftLimitationInformation",
        default=None,
    )

    # label: complianceDeclarationText
    # comment: Contains the warning message complying with the regulations text note. This field is mandatory for air (Air)
    complianceDeclarationText: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#complianceDeclarationText",
        default=None,
    )

    # label: declarationDate
    # comment: Date and time at which the DgDeclaration was declared
    declarationDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#declarationDate",
        default=None,
    )

    # label: exclusiveUseIndicator
    # comment: Indicates an exclusive use shipment
    exclusiveUseIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#exclusiveUseIndicator",
        default=None,
    )

    # label: handlingInformation
    # comment: Free text. This may include items such as Control temperature for substances stabilized by temperature control, name and telephone number of a responsible person for infectious substances.
    handlingInformation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#handlingInformation",
        default=None,
    )

    # label: shipperDeclarationText
    # comment: Contains the shipper's declaration to comply with the regulations text note. Free text . This field is mandatory for air (Air)
    shipperDeclarationText: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shipperDeclarationText",
        default=None,
    )

    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    shippingRefNo: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo",
        default=None,
    )


class DgProductRadioactive(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#DgProductRadioactive"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#DgProductRadioactive"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: dgRaTypeCode
    # comment: The category of the package or all packed in one. Complete text to be transmitted: I-White, II-Yellow, III-Yellow instead of I, II, III
    dgRaTypeCode: Union[RaTypeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#dgRaTypeCode",
        default=None,
    )

    # label: forProductDg
    # comment: Reference to the ProductDg this DgProductRadioactive details
    forProductDg: Union[ProductDg, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forProductDg",
        default=None,
    )

    # label: isotopes
    # comment: DgRadioactiveIsotope.
    isotopes: List[DgRadioactiveIsotope] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#isotopes",
        default_factory=list,
    )

    # label: fissileExceptionIndicator
    # comment: Indicates if Fissile is excepted
    fissileExceptionIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#fissileExceptionIndicator",
        default=None,
    )

    # label: fissileExceptionReference
    # comment: Fissile exception reference, mandatory if Fissile Exception Indicator is true.
    fissileExceptionReference: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#fissileExceptionReference",
        default=None,
    )

    # label: transportIndexNumeric
    # comment: Radioactive Transport-Index value of the package or all packed in one. Conditionally mandatory and applies to categories II-Yellow and III-Yellow only; field only contains the value, if printed, TI must be added as a prefix to the value  to be printed in the Packing Instructions column
    transportIndexNumeric: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportIndexNumeric",
        default=None,
    )


class DgRadioactiveIsotope(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#DgRadioactiveIsotope"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#DgRadioactiveIsotope"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: contentOfDgProductRadioactive
    # comment: Reference to the DgProductRadioactive this Isotope is contained in
    contentOfDgProductRadioactive: Union[DgProductRadioactive, SkipJsonSchema[None]] = (
        Field(
            serialization_alias="https://onerecord.iata.org/ns/cargo#contentOfDgProductRadioactive",
            default=None,
        )
    )

    # label: physicalChemicalForm
    # comment: A description of the physical and chemical form of the material.
    physicalChemicalForm: Union[
        RadioactiveMaterialClassification, SkipJsonSchema[None]
    ] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#physicalChemicalForm",
        default=None,
    )

    # label: activityLevelMeasure
    # comment: Numeric expression of the activity of a radioactive Item
    activityLevelMeasure: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#activityLevelMeasure",
        default=None,
    )

    # label: criticalitySafetyIndexNumeric
    # comment: Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.
    criticalitySafetyIndexNumeric: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#criticalitySafetyIndexNumeric",
        default=None,
    )

    # label: isotopeId
    # comment: Id of each radionuclide or for mixtures of radionuclides.
    isotopeId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#isotopeId",
        default=None,
    )

    # label: isotopeName
    # comment: The name or symbol of each radionuclide or for mixtures of radionuclides, an appropriate general description, or a list of the most restrictive radionuclides.
    isotopeName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#isotopeName",
        default=None,
    )

    # label: lowDispersibleIndicator
    # comment: A notation that the material is low dispersible radioactive material.
    lowDispersibleIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#lowDispersibleIndicator",
        default=None,
    )

    # label: specialFormIndicator
    # comment: A notation that the material is special form
    specialFormIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialFormIndicator",
        default=None,
    )


class EpermitConsignment(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#EpermitConsignment"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#EpermitConsignment"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: consignmentItems
    # comment: Reference to te pieces (Live Animals) of the permit
    consignmentItems: Union[PieceLiveAnimals, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#consignmentItems",
        default=None,
    )

    # label: epermit
    # comment: Reference to the Epermit of the consignment
    epermit: Union[LiveAnimalsEpermit, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#epermit",
        default=None,
    )

    # label: examiningQuantity
    # comment: Quantity measured by the examining authority (box 14)
    examiningQuantity: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#examiningQuantity",
        default=None,
    )

    # label: usedToDateQuotaQuantity
    # comment: total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    usedToDateQuotaQuantity: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#usedToDateQuotaQuantity",
        default=None,
    )


class EpermitSignature(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#EpermitSignature"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#EpermitSignature"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: forEpermit
    # comment: Reference to the LiveAnimalsEpermit this Signature applies to
    forEpermit: Union[LiveAnimalsEpermit, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forEpermit",
        default=None,
    )

    # label: signatoryCompany
    # comment: Signatory company name
    signatoryCompany: Union[Company, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryCompany",
        default=None,
    )

    # label: signatoryRole
    # comment: Role of the signatory with regards to the ePermit: Applicant, Permit issuer, Issuing Authority or Examining authority
    signatoryRole: Union[SignatoryRole, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryRole",
        default=None,
    )

    # label: signatureTypeCode
    # comment: Code specifying a type of government action such as inspection, detention, fumigation, security.
    signatureTypeCode: Union[SignatureTypeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatureTypeCode",
        default=None,
    )

    # label: securityStampId
    # comment: Security Stamp ID
    securityStampId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#securityStampId",
        default=None,
    )

    # label: signatureDate
    # comment: Date and time of the signature
    signatureDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatureDate",
        default=None,
    )

    # label: signatureStatement
    # comment: Signatory signature authentication text
    signatureStatement: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatureStatement",
        default=None,
    )


class ExternalReference(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#ExternalReference"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ExternalReference"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: createdAtLocation
    # comment: Location of the document, e.g. location where the document was emitted
    createdAtLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#createdAtLocation",
        default=None,
    )

    # label: originator
    # comment: Document originator details and contacts
    originator: Union[Company, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#originator",
        default=None,
    )

    # label: referenceForObjects
    # comment: References to the LogisticsObjects referring to this external reference
    referenceForObjects: List[LogisticsObject] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#referenceForObjects",
        default_factory=list,
    )

    # label: checksum
    # comment: Checksum of the document to validate its integrity
    checksum: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checksum",
        default=None,
    )

    # label: documentIdentifier
    # comment: Unique document identifier
    documentIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentIdentifier",
        default=None,
    )

    # label: documentLink
    # comment: Link to the document, e.g. URL of the file where it is hosted
    documentLink: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentLink",
        default=None,
    )

    # label: documentName
    # comment: If no DocumentType provided, name of the referenced document
    documentName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentName",
        default=None,
    )

    # label: documentType
    # comment: Type of the referenced document . Can refer UNEDIFACT 11  e.g. 740 - Air Waybill, but not limited to
    documentType: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentType",
        default=None,
    )

    # label: documentVersion
    # comment: Document version number
    documentVersion: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentVersion",
        default=None,
    )

    # label: validFrom
    # comment: Validity start date based on usage context
    validFrom: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#validFrom",
        default=None,
    )

    # label: validUntil
    # comment: Validity end date (date of expiry) based on usage context
    validUntil: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#validUntil",
        default=None,
    )


class Insurance(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Insurance")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Insurance"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: coveringOrganization
    # comment: Party covering the insurance
    coveringOrganization: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#coveringOrganization",
        default=None,
    )

    # label: insuredAmount
    # comment: Insured amount - amount covered by the insurance policy
    insuredAmount: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#insuredAmount",
        default=None,
    )

    # label: insuredShipments
    # comment: Reference to the shipments insured
    insuredShipments: List[Shipment] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#insuredShipments",
        default_factory=list,
    )


class LiveAnimalsEpermit(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LiveAnimalsEpermit"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LiveAnimalsEpermit"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: consignee
    # comment: Reference to the Organization that fulfills the role of the consignee, for a LiveAnimalsEpermit it has to include complete name and address (box 3)
    consignee: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#consignee",
        default=None,
    )

    # label: consignments
    # comment: Reference to the pieces and properties linked to the Permit (box 7 to 12)
    consignments: List[EpermitConsignment] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#consignments",
        default_factory=list,
    )

    # label: permitTypeCode
    # comment: Code specifying the document name. (box 1)
    permitTypeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#permitTypeCode",
        default=None,
    )

    # label: signatures
    # comment: List of all the signatures of the Epermit (applicant box 4, issuing authority box 6, issuer box 13 and examining authority box 14)
    signatures: List[EpermitSignature] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatures",
        default_factory=list,
    )

    # label: transactionPurposeCode
    # comment: Code indicating the purpose of the transaction (box 5a)
    transactionPurposeCode: Union[TransactionPurposeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transactionPurposeCode",
        default=None,
    )

    # label: transportContractTypeCode
    # comment: Code specifying the transport document name (box 15)
    transportContractTypeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportContractTypeCode",
        default=None,
    )

    # label: copyIndicator
    # comment: Indicates if the permit is a copy (true) or an original (false) (box 1)
    copyIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#copyIndicator",
        default=None,
    )

    # label: epermitNumber
    # comment: The original number is a unique number allocated to each document by the relevant Management Authority. (box 1)
    epermitNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#epermitNumber",
        default=None,
    )

    # label: permitTypeOtherDescription
    # comment: Description if TypeCode is Other (box 1)
    permitTypeOtherDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#permitTypeOtherDescription",
        default=None,
    )

    # label: specialConditions
    # comment: Special conditions (box 5)
    specialConditions: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialConditions",
        default=None,
    )

    # label: transactionPurpose
    # comment: Purpose of the transaction in free text (box 5a)
    transactionPurpose: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transactionPurpose",
        default=None,
    )

    # label: transportContractId
    # comment: Reference to the Air Waybill or other transport contract document (box 15)
    transportContractId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportContractId",
        default=None,
    )

    # label: validFrom
    # comment: Validity start date based on usage context
    validFrom: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#validFrom",
        default=None,
    )

    # label: validUntil
    # comment: Validity end date (date of expiry) based on usage context
    validUntil: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#validUntil",
        default=None,
    )


class LogisticsAction(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LogisticsAction"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsAction"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: actionTimeType
    # comment: Enum stating the type of the Action
    actionTimeType: Union[ActionTimeType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#actionTimeType",
        default=None,
    )

    # label: contactDetails
    # comment: Information about contactDetails
    contactDetails: List[ContactDetail] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails",
        default_factory=list,
    )

    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    contactPersons: List[Actor] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons",
        default_factory=list,
    )

    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    otherIdentifiers: List[OtherIdentifier] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
        default_factory=list,
    )

    # label: performedAt
    # comment: Reference to the Location the Action was performed at
    performedAt: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#performedAt",
        default=None,
    )

    # label: servedActivity
    # comment: Reference to the Activity the Action was performed for
    servedActivity: Union[LogisticsActivity, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#servedActivity",
        default=None,
    )

    # label: actionEndTime
    # comment: DateTime holding the end time of the Action; Type is indicated through ActionType property
    actionEndTime: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#actionEndTime",
        default=None,
    )

    # label: actionStartTime
    # comment: DateTime holding the start time of the Action; Type is indicated through ActionType property
    actionStartTime: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#actionStartTime",
        default=None,
    )


class LogisticsActivity(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LogisticsActivity"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsActivity"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: checkActions
    # comment: References to CheckActions performed for the Activity
    checkActions: List[Check] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkActions",
        default_factory=list,
    )

    # label: contactDetails
    # comment: Information about contactDetails
    contactDetails: List[ContactDetail] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails",
        default_factory=list,
    )

    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    contactPersons: List[Actor] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons",
        default_factory=list,
    )

    # label: executionStatus
    # comment: Enum stating the status of the Activity
    executionStatus: Union[ExecutionStatus, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#executionStatus",
        default=None,
    )

    # label: servedServices
    # comment: Reference to Services this Activity is executed for
    servedServices: List[LogisticsService] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#servedServices",
        default_factory=list,
    )


class LogisticsAgent(LogisticsObject):
    pass


class LogisticsService(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LogisticsService"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsService"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: activitySequences
    # comment: Information about the Activities that are part of the Service and their sequence
    activitySequences: List[ActivitySequence] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#activitySequences",
        default_factory=list,
    )

    # label: contactDetails
    # comment: Information about contactDetails
    contactDetails: List[ContactDetail] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails",
        default_factory=list,
    )

    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    contactPersons: List[Actor] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons",
        default_factory=list,
    )


class PackagingType(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#PackagingType"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#PackagingType"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: appliedOnPieces
    # comment: Piece on which the Packaging type is applicable
    appliedOnPieces: List[Piece] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#appliedOnPieces",
        default_factory=list,
    )

    # label: typeCode
    # comment: Packaging type identifier as per UNECE Rec 21 Annex V and VI e.g. 1A - Drum, steel - Packaging material code. Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations
    typeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#typeCode",
        default=None,
    )

    # label: description
    # comment: Natural language description if required
    description: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
        default=None,
    )


class PhysicalLogisticsObject(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: attachedIotDevices
    # comment: References to all connected IotDevices
    attachedIotDevices: List[IotDevice] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#attachedIotDevices",
        default_factory=list,
    )

    # label: involvedInActions
    # comment: References to the Actions the object is involved in
    involvedInActions: List[LogisticsAction] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedInActions",
        default_factory=list,
    )


class Price(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Price")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Price"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: chargeCode
    # comment: Charge code, refer to CargoXML Code List 1.1
    chargeCode: Union[ChargeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeCode",
        default=None,
    )

    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    forBookingOption: Union[BookingOption, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption",
        default=None,
    )

    # label: ratings
    # comment: Rating used for pricing
    ratings: List[Ratings] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ratings",
        default_factory=list,
    )

    # label: grandTotal
    # comment: Total price
    grandTotal: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#grandTotal",
        default=None,
    )


class Product(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Product")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Product"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: describedObjects
    # comment: Reference to the Items or Pieces in which the product can be found.
    describedObjects: List[PhysicalLogisticsObject] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#describedObjects",
        default_factory=list,
    )

    # label: hsCode
    # comment: Harmonized Commodity code, refer to hsType used. 6 minimum digits are expected.
    hsCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#hsCode",
        default=None,
    )

    # label: manufacturer
    # comment: Manufacturing company details and contacts
    manufacturer: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer",
        default=None,
    )

    # label: otherCharacteristics
    # comment: Characteristics of the product
    otherCharacteristics: List[Characteristic] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherCharacteristics",
        default_factory=list,
    )

    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    otherIdentifiers: List[OtherIdentifier] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
        default_factory=list,
    )

    # label: commodityItemNumber
    # comment: Indicates the specific commodity on which the rate class code is applied
    commodityItemNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#commodityItemNumber",
        default=None,
    )

    # label: description
    # comment: Natural language description if required
    description: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
        default=None,
    )

    # label: hsCommodityDescription
    # comment: Commodity description
    hsCommodityDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityDescription",
        default=None,
    )

    # label: hsCommodityName
    # comment: If no Code provided, name of commodity
    hsCommodityName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityName",
        default=None,
    )

    # label: hsType
    # comment: Reference identifying the type of standard code to be used for the Commodity Classification (Brussels Tariff Nomenclature, EU Harmonized System Code, UN Standard International Trade Classification). Mandatory if the commodity code is more than 6 digits
    hsType: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#hsType",
        default=None,
    )

    # label: uniqueIdentifier
    # comment: Manufacturer's unique product identifier
    uniqueIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uniqueIdentifier",
        default=None,
    )


class Question(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Question")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Question"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: answer
    # comment: Reference to the Answer to the Question
    answer: Union[Answer, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#answer",
        default=None,
    )

    # label: checkTemplate
    # comment: Reference to the CheckTemplate the Question is from
    checkTemplate: Union[CheckTemplate, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkTemplate",
        default=None,
    )

    # label: answerOptionsText
    # comment: Text restrictions to the Answer
    answerOptionsText: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsText",
        default=None,
    )

    # label: answerOptionsValue
    # comment: Value restrictions to the answer
    answerOptionsValue: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsValue",
        default=None,
    )

    # label: longText
    # comment: Long text of the question
    longText: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#longText",
        default=None,
    )

    # label: questionNumber
    # comment: Number of the Question within the template (alphanumeric)
    questionNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#questionNumber",
        default=None,
    )

    # label: questionSection
    # comment: Section of the CheckTemplate this Question is part of
    questionSection: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#questionSection",
        default=None,
    )

    # label: shortText
    # comment: Short text of the Question
    shortText: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shortText",
        default=None,
    )


class Ratings(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Ratings")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Ratings"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: billingChargeIdentifier
    # comment: Billing charge identifiers to be used for CASS. Refer to CargoXML Code List 1.33
    billingChargeIdentifier: Union[ChargeIdentifier, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#billingChargeIdentifier",
        default=None,
    )

    # label: chargePaymentType
    # comment: Indicates if charge is prepaid or collect (P, C)
    chargePaymentType: Union[PrepaidCollectIndicator, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargePaymentType",
        default=None,
    )

    # label: chargeType
    # comment: Charge type related to amount total as per bullet points 2/21 - data elements 24A - 3B  from AWB
    chargeType: Union[ChargeIdentifier, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeType",
        default=None,
    )

    # label: entitlement
    # comment: Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    entitlement: Union[EntitlementCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#entitlement",
        default=None,
    )

    # label: forPrices
    # comment: Reference to the Prices based on this Ratings
    forPrices: List[Price] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#forPrices",
        default_factory=list,
    )

    # label: otherChargeCode
    # comment: Refer to CargoXML Code List 1.2 for Other Charges
    otherChargeCode: Union[OtherChargeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeCode",
        default=None,
    )

    # label: ranges
    # comment: Reference to the ranges
    ranges: List[Ranges] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ranges",
        default_factory=list,
    )

    # label: rcp
    # comment: IATA 3-letter city code of the rate combination point as defined in TACT
    rcp: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#rcp",
        default=None,
    )

    # label: chargeDescription
    # comment: Description of the charge e.g. Airfreight, fuel, etc.
    chargeDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeDescription",
        default=None,
    )

    # label: priceReferenceId
    # comment: Reference to a price reference if existing (e.g. Allotment number, contract reference, etc.)
    priceReferenceId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#priceReferenceId",
        default=None,
    )

    # label: priceSpecification
    # comment: Specification of the price e.g. Street, Group, Spot, etc.
    priceSpecification: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#priceSpecification",
        default=None,
    )

    # label: quantity
    # comment: Quantity for the charge if applicable
    quantity: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#quantity",
        default=None,
    )

    # label: subTotal
    # comment: Subtotal of the charge
    subTotal: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#subTotal",
        default=None,
    )


class SecurityDeclaration(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#SecurityDeclaration"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#SecurityDeclaration"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: groundsForExemption
    # comment: Exemption code - e.g. BIOM- Bio-Medical Samples SMUS - small undersized shipments MAIL - mail BIOM - bio-medical samples DIPL - diplomatic bags or diplomatic mail LFSM - life-saving materials NUCL - nuclear materials TRNS - transfer or transshipment
    groundsForExemption: List[ScreeningExemption] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#groundsForExemption",
        default_factory=list,
    )

    # label: issuedBy
    # comment: Name of person (or employee ID) who issued the security status
    issuedBy: Union[Person, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedBy",
        default=None,
    )

    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    issuedForPiece: List[Piece] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece",
        default_factory=list,
    )

    # label: otherRegulatedEntities
    # comment: Any other regulated entity that accepts custody of the cargo and accepts the security status originally issued
    otherRegulatedEntities: List[RegulatedEntity] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherRegulatedEntities",
        default_factory=list,
    )

    # label: receivedFrom
    # comment: Regulated entity that tendered the consignment
    receivedFrom: Union[RegulatedEntity, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#receivedFrom",
        default=None,
    )

    # label: regulatedEntityAcceptor
    # comment: Information about the accepting regulated entity of the Security Declaration
    regulatedEntityAcceptor: List[RegulatedEntity] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityAcceptor",
        default_factory=list,
    )

    # label: regulatedEntityIssuer
    # comment: Regulated entity issuing the Security Declaration
    regulatedEntityIssuer: Union[RegulatedEntity, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityIssuer",
        default=None,
    )

    # label: screeningMethods
    # comment: Screening methods which have been used to secure the cargo PHS – Physical Inspection and/or hand search VCK - Visual check XRY- X-ray equipment EDS - Explosive detection system EDD - Explosive detection dogsETD - Explosive trace detection equipment - particles or vapor CMD - Cargo metal detection AOM - Subjected to any other means: this entry should be followed by free text specifying what other mean was used to secure the cargo
    screeningMethods: List[ScreeningMethod] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#screeningMethods",
        default_factory=list,
    )

    # label: securityStatus
    # comment: Security status indicator (CXML 1.13) - e.g. SPX- Cargo Secure for Passenger and All-Cargo Aircraft
    securityStatus: Union[SecurityStatus, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#securityStatus",
        default=None,
    )

    # label: additionalSecurityInformation
    # comment: Any additional information that may be required by an ICAO Member State
    additionalSecurityInformation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#additionalSecurityInformation",
        default=None,
    )

    # label: issuedOn
    # comment: Date and time when the security status was issued
    issuedOn: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedOn",
        default=None,
    )

    # label: otherScreeningMethods
    # comment: Other methods used to secure the cargo
    otherScreeningMethods: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherScreeningMethods",
        default_factory=list,
    )


class Shipment(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Shipment")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Shipment"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: customsInformation
    # comment: Customs details
    customsInformation: List[CustomsInformation] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation",
        default_factory=list,
    )

    # label: incoterms
    # comment: Standard codes as defined by UNCEFACT and ICC that correspond to international rules for the interpretation of the most commonly used trade terms in different countries. UNECE recommendation n. 5 Incoterms 2.
    incoterms: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#incoterms",
        default=None,
    )

    # label: insurance
    # comment: Insurance details
    insurance: Union[Insurance, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#insurance",
        default=None,
    )

    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    involvedParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
        default_factory=list,
    )

    # label: pieces
    # comment: References to the Pieces that are part of this Shipment
    pieces: List[Piece] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieces",
        default_factory=list,
    )

    # label: totalDimensions
    # comment: Dimensions of the whole shipment
    totalDimensions: List[Dimensions] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalDimensions",
        default_factory=list,
    )

    # label: totalGrossWeight
    # comment: Total gross weight of the whole shipment
    totalGrossWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalGrossWeight",
        default=None,
    )

    # label: waybill
    # comment: Reference to the Waybill of the shipment
    waybill: Union[Waybill, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybill",
        default=None,
    )

    # label: goodsDescription
    # comment: Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    goodsDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#goodsDescription",
        default=None,
    )

    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    textualHandlingInstructions: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions",
        default_factory=list,
    )


class TransportLegs(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#TransportLegs"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#TransportLegs"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: arrivalLocation
    # comment: Reference to the arrival Location
    arrivalLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
        default=None,
    )

    # label: co2Emissions
    # comment: References to CO2Emissions
    co2Emissions: Union[CO2Emissions, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#co2Emissions",
        default=None,
    )

    # label: departureLocation
    # comment: Reference to the departure Location
    departureLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
        default=None,
    )

    # label: operatingTransportMeans
    # comment: Reference to the TransportMeans operating the TransportMovement
    operatingTransportMeans: Union[TransportMeans, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans",
        default=None,
    )

    # label: transportMeansServiceType
    # comment: Type of transport means service, e.g. Aircraftor Truck
    transportMeansServiceType: Union[
        TransportMeansServiceType, SkipJsonSchema[None]
    ] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansServiceType",
        default=None,
    )

    # label: transportMeansType
    # comment: Type of transport means, e.g. 744, RFS
    transportMeansType: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportMeansType",
        default=None,
    )

    # label: arrivalDate
    # comment: Arrival date and time of the leg
    arrivalDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalDate",
        default=None,
    )

    # label: departureDate
    # comment: Departure date and time of the leg
    departureDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureDate",
        default=None,
    )

    # label: TransportLegs
    # comment: Leg number
    legNumber: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#legNumber",
        default=None,
    )

    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    transportIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier",
        default=None,
    )


class Waybill(LogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Waybill")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Waybill"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsObject"),
    ]

    # label: accountingNotes
    # comment: Information about accounting notes (AWB box 10)
    accountingNotes: List[AccountingNote] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNotes",
        default_factory=list,
    )

    # label: arrivalLocation
    # comment: Reference to the arrival Location
    arrivalLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
        default=None,
    )

    # label: billingDetails
    # comment: Reference to the BillingDetails of the Waybill
    billingDetails: Union[BillingDetails, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#billingDetails",
        default=None,
    )

    # label: carrierChargeCode
    # comment: One letter charge code as per bullet point 12 - data element 13 from AWB
    carrierChargeCode: Union[ChargeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierChargeCode",
        default=None,
    )

    # label: carrierDeclarationPlace
    # comment: Location of individual or company involved in the movement of a consignment or Coded representation of a specific airport/city code
    carrierDeclarationPlace: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierDeclarationPlace",
        default=None,
    )

    # label: customsOriginCode
    # comment: Code indicating the origin of goods for Customs purposes (e.g. For goods in free circulation in the EU) List to be provided by local authorities
    customsOriginCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#customsOriginCode",
        default=None,
    )

    # label: declaredValueForCarriage
    # comment: The value of a shipment declared for carriage purposes
    declaredValueForCarriage: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#declaredValueForCarriage",
        default=None,
    )

    # label: declaredValueForCustoms
    # comment: The value of a shipment declared for customs purposes
    declaredValueForCustoms: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#declaredValueForCustoms",
        default=None,
    )

    # label: departureLocation
    # comment: Reference to the departure Location
    departureLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
        default=None,
    )

    # label: destinationCharges
    # comment: Charges levied at destination accruing to the last carrier, in destination currency
    destinationCharges: List[CurrencyValue] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#destinationCharges",
        default_factory=list,
    )

    # label: houseWaybills
    # comment: Refers to the Waybill(s) contained
    houseWaybills: List[Waybill] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#houseWaybills",
        default_factory=list,
    )

    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    involvedParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
        default_factory=list,
    )

    # label: masterWaybill
    # comment: Reference to the master Waybill if it is contained in one
    masterWaybill: Union[Waybill, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#masterWaybill",
        default=None,
    )

    # label: otherCharges
    # comment: Information about Other Charges applying to this Waybill
    otherCharges: List[OtherCharge] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherCharges",
        default_factory=list,
    )

    # label: otherChargesIndicator
    # comment: Indicator whether the payment of Other Charges is to be made at origin (prepaid) or at destination (collect) as per bullet point 13 - data element 15a/15b from AWB
    otherChargesIndicator: Union[PrepaidCollectIndicator, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargesIndicator",
        default=None,
    )

    # label: referredBookingOption
    # comment: Refers to the Booking
    referredBookingOption: Union[Booking, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#referredBookingOption",
        default=None,
    )

    # label: serviceCode
    # comment: One letter service code as per bullet point 18.4 - data element 22Z from AWB
    serviceCode: Union[ServiceCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceCode",
        default=None,
    )

    # label: shipment
    # comment: Reference to the Shipment
    shipment: Union[Shipment, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shipment",
        default=None,
    )

    # label: taxAmount
    # comment: Information about taxes
    taxAmount: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#taxAmount",
        default=None,
    )

    # label: waybillLineItems
    # comment: Information about rates applying to this Waybill handled as line item
    waybillLineItems: List[WaybillLineItem] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillLineItems",
        default_factory=list,
    )

    # label: waybillType
    # comment: Type of the Waybill: House, Direct or Master
    waybillType: Union[WaybillType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillType",
        default=None,
    )

    # label: weightValuationIndicator
    # comment: Indicator whether the payment for the Weight/Valuation is to be made at origin (prepaid) or at destination (collect) as per bullet point 13 - data element 14a/14b from AWB
    weightValuationIndicator: Union[PrepaidCollectIndicator, SkipJsonSchema[None]] = (
        Field(
            serialization_alias="https://onerecord.iata.org/ns/cargo#weightValuationIndicator",
            default=None,
        )
    )

    # label: accountingInformation
    # comment: Indicates the details of accounting information. Free text e.g. PAYMENT BY CERTIFIED CHEQUE etc.
    accountingInformation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountingInformation",
        default=None,
    )

    # label: carrierDeclarationDate
    # comment: Date upon which the certification is made by the carrier
    carrierDeclarationDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierDeclarationDate",
        default=None,
    )

    # label: carrierDeclarationSignature
    # comment: Contains the authentication of the Carrier
    carrierDeclarationSignature: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierDeclarationSignature",
        default=None,
    )

    # label: consignorDeclarationSignature
    # comment: Name of consignor signatory
    consignorDeclarationSignature: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#consignorDeclarationSignature",
        default=None,
    )

    # label: destinationCurrencyRate
    # comment: Conversion rate applied
    destinationCurrencyRate: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#destinationCurrencyRate",
        default=None,
    )

    # label: modularCheckNumber
    # comment: The check is a Modular 7 validation on the AWB number, recorded as a boolean.
    modularCheckNumber: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#modularCheckNumber",
        default=None,
    )

    # label: shippingInfo
    # comment: The shipper or its Agent may enter the appropriate optional shipping
    shippingInfo: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingInfo",
        default=None,
    )

    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    shippingRefNo: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo",
        default=None,
    )

    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    waybillNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber",
        default=None,
        pattern=r"[A-Z0-9]+",
    )

    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    waybillPrefix: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix",
        default=None,
        max_length=3,
    )


class LoosePiece(PieceGroup):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#LoosePiece")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LoosePiece"),
        URIRef("https://onerecord.iata.org/ns/cargo#PieceGroup"),
    ]

    # label: pieceHeight
    # comment: Height of a single piece
    pieceHeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceHeight",
        default=None,
    )

    # label: pieceLength
    # comment: Length of a single piece
    pieceLength: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceLength",
        default=None,
    )

    # label: pieceWeight
    # comment: Weight of a single piece
    pieceWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWeight",
        default=None,
    )

    # label: pieceWidth
    # comment: Width of a single piece
    pieceWidth: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceWidth",
        default=None,
    )

    # label: totalVolume
    # comment: Total volume fo the volume piece group
    totalVolume: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalVolume",
        default=None,
    )

    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    stackable: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#stackable",
        default=None,
    )

    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    turnable: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#turnable",
        default=None,
    )


class ULDBasicPiece(PieceGroup):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#ULDBasicPiece"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ULDBasicPiece"),
        URIRef("https://onerecord.iata.org/ns/cargo#PieceGroup"),
    ]

    # label: uldLoadingIndicator
    # comment: Indicator related to ULD loading (e.g. Main deck only)
    uldLoadingIndicator: Union[ULDLoadingIndicator, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldLoadingIndicator",
        default=None,
    )

    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    slac: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#slac",
        default=None,
    )


class ULDSpecificPiece(PieceGroup):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#ULDSpecificPiece"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ULDSpecificPiece"),
        URIRef("https://onerecord.iata.org/ns/cargo#PieceGroup"),
    ]

    # label: uldContourCode
    # comment: Contour code as per IATA ULD Regulation
    uldContourCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldContourCode",
        default=None,
    )

    # label: uldType
    # comment: Type of ULD as per IATA ULD Regulation
    uldType: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldType",
        default=None,
    )

    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    slac: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#slac",
        default=None,
    )

    # label: uldSerialNumber
    # comment: Serial number that allows to uniquely identify the ULD
    uldSerialNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldSerialNumber",
        default=None,
    )


class VolumePieceGroup(PieceGroup):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#VolumePieceGroup"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#VolumePieceGroup"),
        URIRef("https://onerecord.iata.org/ns/cargo#PieceGroup"),
    ]

    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    stackable: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#stackable",
        default=None,
    )


class Check(LogisticsAction):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Check")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Check"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsAction"),
    ]

    # label: checkTotalResult
    # comment: Reference to the result of the Check
    checkTotalResult: Union[CheckTotalResult, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkTotalResult",
        default=None,
    )

    # label: checkedObject
    # comment: Reference to the checked Object
    checkedObject: Union[LogisticsObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkedObject",
        default=None,
    )

    # label: checker
    # comment: Reference to the Actor performing the Check
    checker: Union[Actor, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#checker",
        default=None,
    )

    # label: usedTemplate
    # comment: Reference to the Template used in the Check
    usedTemplate: Union[CheckTemplate, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#usedTemplate",
        default=None,
    )


class Composing(LogisticsAction):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Composing")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Composing"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsAction"),
    ]

    # label: composedMaterials
    # comment: References to the Materials being built-up or broken-down
    composedMaterials: List[LoadingMaterial] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#composedMaterials",
        default_factory=list,
    )

    # label: composedPieces
    # comment: References to the Pieces being built-up or broken-down
    composedPieces: List[Piece] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#composedPieces",
        default_factory=list,
    )

    # label: compositionType
    # comment: Enum stating whether the CompositionAction describes build-up or break-down
    compositionType: Union[CompositionType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#compositionType",
        default=None,
    )

    # label: onLoadingUnit
    # comment: Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    loadingUnit: Union[LoadingUnit, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingUnit",
        default=None,
    )


class Loading(LogisticsAction):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Loading")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Loading"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsAction"),
    ]

    # label: loadedMaterials
    # comment: References to Materials onloaded or offloaded
    loadedMaterials: List[LoadingMaterial] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadedMaterials",
        default_factory=list,
    )

    # label: loadedPieces
    # comment: References to Pieces onloaded or offloaded
    loadedPieces: List[Piece] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadedPieces",
        default_factory=list,
    )

    # label: loadedUnits
    # comment: References to LoadingUnits onloaded or offloaded
    loadedUnits: List[LoadingUnit] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadedUnits",
        default_factory=list,
    )

    # label: loadingType
    # comment: Enum stating whether the LoadingAction describes onloading or offloading
    loadingType: Union[LoadingType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingType",
        default=None,
    )

    # label: onTransportMeans
    # comment: Reference to the TransportMeans that is being onloaded or offloaded
    onTransportMeans: Union[TransportMeans, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#onTransportMeans",
        default=None,
    )

    # label: loadingPositionIdentifier
    # comment: Short text stating the loading position in the TransportMeans
    loadingPositionIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingPositionIdentifier",
        default=None,
    )


class Storing(LogisticsAction):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Storing")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Storing"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsAction"),
    ]

    # label: storedObjects
    # comment: Reference to the Objects being stored in or stored out
    storedObjects: List[PhysicalLogisticsObject] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#storedObjects",
        default_factory=list,
    )

    # label: storingType
    # comment: Enum stating whether the StoringAction describes the store-in or the store-out
    storingType: Union[StoringType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#storingType",
        default=None,
    )

    # label: storagePlaceIdentifier
    # comment: Short text stating the exact place of storage
    storagePlaceIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#storagePlaceIdentifier",
        default=None,
    )


class Storage(LogisticsActivity):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Storage")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Storage"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsActivity"),
    ]

    # label: storingActions
    # comment: References to all StoringActions performed for the Storing Activity
    storingActions: List[Storing] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#storingActions",
        default_factory=list,
    )

    # label: storingIdentifier
    # comment: Short text holding the process number if necessary
    storingIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#storingIdentifier",
        default=None,
    )


class TransportMovement(LogisticsActivity):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#TransportMovement"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#TransportMovement"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsActivity"),
    ]

    # label: arrivalLocation
    # comment: Reference to the arrival Location
    arrivalLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
        default=None,
    )

    # label: co2Emissions
    # comment: References to CO2Emissions
    co2Emissions: List[CO2Emissions] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#co2Emissions",
        default_factory=list,
    )

    # label: departureLocation
    # comment: Reference to the departure Location
    departureLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
        default=None,
    )

    # label: distanceCalculated
    # comment: Information about the calculated distance
    distanceCalculated: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#distanceCalculated",
        default=None,
    )

    # label: distanceMeasured
    # comment: Information about the measured distance
    distanceMeasured: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#distanceMeasured",
        default=None,
    )

    # label: fuelAmountCalculated
    # comment: Information about the calculated fuel amount
    fuelAmountCalculated: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountCalculated",
        default=None,
    )

    # label: fuelAmountMeasured
    # comment: Information about the measured fuel amount
    fuelAmountMeasured: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#fuelAmountMeasured",
        default=None,
    )

    # label: loadingActions
    # comment: References to all actions of type Loading performed for the TransportMovement
    loadingActions: List[Loading] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingActions",
        default_factory=list,
    )

    # label: modeCode
    # comment: Mode of transport code, refer to UNECE Rec. 19 https://unece.org/fileadmin/DAM/cefact/recommendations/rec19/rec19_1cf19e.pdf
    modeCode: Union[ModeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#modeCode",
        default=None,
    )

    # label: modeQualifier
    # comment: Pre-Carriage, Main-Carriage or On-Carriage
    modeQualifier: Union[ModeQualifier, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#modeQualifier",
        default=None,
    )

    # label: movementTimes
    # comment: Information about times related to the movement (milestone list to be defined)
    movementTimes: List[MovementTime] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#movementTimes",
        default_factory=list,
    )

    # label: operatingParties
    # comment: Information about the parties operating this TransportMovement, for example pilot and co-pilot; can also refer to organizations through Party
    operatingParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatingParties",
        default_factory=list,
    )

    # label: operatingTransportMeans
    # comment: Reference to the TransportMeans operating the TransportMovement
    operatingTransportMeans: Union[TransportMeans, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatingTransportMeans",
        default=None,
    )

    # label: fuelType
    # comment: e.g. Kerosene, Diesel, SAF, Electricity [renewable], Electricity [non-renewable]
    fuelType: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#fuelType",
        default=None,
    )

    # label: seal
    # comment: Seal identifier
    seal: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#seal",
        default=None,
    )

    # label: transportIdentifier
    # comment: Airline flight number, or rail/truck/maritime line id
    transportIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportIdentifier",
        default=None,
    )


class UnitComposition(LogisticsActivity):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#UnitComposition"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#UnitComposition"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsActivity"),
    ]

    # label: compositionActions
    # comment: References to all CompositionActions performed for the UnitComposition
    compositionActions: List[Composing] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#compositionActions",
        default_factory=list,
    )

    # label: onLoadingUnit
    # comment: Reference to the LoadingUnit composed in the Unit Composition or referenced in Composing actions
    loadingUnit: Union[LoadingUnit, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingUnit",
        default=None,
    )

    # label: compositionIdentifier
    # comment: Short text holding the process number if necessary
    compositionIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#compositionIdentifier",
        default=None,
    )

    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    slac: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#slac",
        default=None,
    )


class Actor(LogisticsAgent):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Actor")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Actor"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsAgent"),
    ]

    # label: associatedOrganization
    # comment: Reference to the Organization the Actor is associated with
    associatedOrganization: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#associatedOrganization",
        default=None,
    )


class Organization(LogisticsAgent):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Organization")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Organization"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsAgent"),
    ]

    # label: basedAtLocation
    # comment: Reference to the Location where the Organization is based at or headquartered
    basedAtLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#basedAtLocation",
        default=None,
    )

    # label: contactPersons
    # comment: References to Actors (Person, NonHumanActor) acting as contacts
    contactPersons: List[Actor] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactPersons",
        default_factory=list,
    )

    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    otherIdentifiers: List[OtherIdentifier] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
        default_factory=list,
    )

    # label: parentOrganization
    # comment: Reference to the parent Organization
    parentOrganization: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#parentOrganization",
        default=None,
    )

    # label: subOrganization
    # comment: References to all sub-Organizations
    subOrganization: List[Organization] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#subOrganization",
        default_factory=list,
    )

    # label: name
    # comment: Human-understandable name of object depending on the context
    name: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#name",
        default=None,
    )

    # label: shortName
    # comment: Short name of the Organization if any
    shortName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shortName",
        default=None,
    )


class Booking(LogisticsService):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Booking")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Booking"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsService"),
    ]

    # label: arrivalLocation
    # comment: Reference to the arrival Location
    arrivalLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
        default=None,
    )

    # label: bookingRequest
    # comment: Reference to the Booking Request
    bookingRequest: Union[BookingRequest, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingRequest",
        default=None,
    )

    # label: bookingSegments
    # comment: Information about booking segments - physics allocated to a specific transport leg
    bookingSegments: List[BookingSegment] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingSegments",
        default_factory=list,
    )

    # label: bookingShipmentDetails
    # comment: Reference to the BookingShipment if required
    bookingShipmentDetails: Union[BookingShipment, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingShipmentDetails",
        default=None,
    )

    # label: bookingStatus
    # comment: Status of the Booking
    bookingStatus: Union[BookingStatus, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingStatus",
        default=None,
    )

    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    bookingTimes: List[BookingTimes] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#bookingTimes",
        default_factory=list,
    )

    # label: carrier
    # comment: Reference to the operating carrier
    carrier: Union[Carrier, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrier",
        default=None,
    )

    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    carrierProduct: Union[CarrierProduct, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct",
        default=None,
    )

    # label: departureLocation
    # comment: Reference to the departure Location
    departureLocation: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
        default=None,
    )

    # label: issuedForWaybill
    # comment: Reference to the Waybill object
    issuedForWaybill: Union[Waybill, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForWaybill",
        default=None,
    )

    # label: stationRemarks
    # comment: Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    stationRemarks: List[StationRemarks] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#stationRemarks",
        default_factory=list,
    )

    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    transportLegs: List[TransportLegs] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs",
        default_factory=list,
    )

    # label: updateBookingOptionRequests
    # comment: References to BookingOptionRequests that request to update the Booking
    updateBookingOptionRequests: List[BookingOptionRequest] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#updateBookingOptionRequests",
        default_factory=list,
    )

    # label: additionalInformation
    # comment: Additional information related to the Booking Option, e.g. sales details
    additionalInformation: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#additionalInformation",
        default_factory=list,
    )

    # label: shippingInfo
    # comment: The shipper or its Agent may enter the appropriate optional shipping
    shippingInfo: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingInfo",
        default=None,
    )

    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    shippingRefNo: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo",
        default=None,
    )

    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    waybillNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber",
        default=None,
        pattern=r"[A-Z0-9]+",
    )

    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    waybillPrefix: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix",
        default=None,
        max_length=3,
    )


class HandlingService(LogisticsService):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#HandlingService"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#HandlingService"),
        URIRef("https://onerecord.iata.org/ns/cargo#LogisticsService"),
    ]

    # label: handlingServiceFor
    handlingServiceFor: List[PhysicalLogisticsObject] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#handlingServiceFor",
        default_factory=list,
    )

    # label: serviceForWaybills
    # comment: Reference to the Waybills this service is to be performed for. To be used if a service is to be performed for a specific shipment or set of
    serviceForWaybills: List[Waybill] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceForWaybills",
        default_factory=list,
    )

    # label: serviceProvider
    # comment: Reference to the Party providing the service
    serviceProvider: Union[Party, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceProvider",
        default=None,
    )

    # label: serviceRequestor
    # comment: Reference to the Party requesting the service
    serviceRequestor: Union[Party, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceRequestor",
        default=None,
    )


class IotDevice(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#IotDevice")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#IotDevice"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: attachedToObject
    # comment: Reference to the PhysicalLogisticsObject the IotDevice is attached to
    attachedToObject: Union[PhysicalLogisticsObject, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#attachedToObject",
        default=None,
    )

    # label: connectedSensors
    # comment: Reference to the sensors linked to the device
    connectedSensors: List[Sensor] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#connectedSensors",
        default_factory=list,
    )

    # label: manufacturer
    # comment: Manufacturing company details and contacts
    manufacturer: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer",
        default=None,
    )

    # label: description
    # comment: Natural language description if required
    description: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
        default=None,
    )

    # label: deviceModel
    # comment: Commercial denomination of the device
    deviceModel: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#deviceModel",
        default=None,
    )

    # label: name
    # comment: Human-understandable name of object depending on the context
    name: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#name",
        default=None,
    )

    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    serialNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber",
        default=None,
    )


class Item(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Item")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Item"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: dimensions
    # comment: Dimensions details
    dimensions: Union[Dimensions, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#dimensions",
        default=None,
    )

    # label: inPiece
    # comment: Reference to the Piece this Item or Piece is contained in
    inPiece: Union[Piece, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#inPiece",
        default=None,
    )

    # label: itemQuantity
    # comment: Quantity of the item when applicable, with associated units of measure
    itemQuantity: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#itemQuantity",
        default=None,
    )

    # label: ofProduct
    # comment: Reference to the Product describing the Item
    ofProduct: Union[Product, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ofProduct",
        default=None,
    )

    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    otherIdentifiers: List[OtherIdentifier] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
        default_factory=list,
    )

    # label: productionCountry
    # comment: Production country details. Refer ISO 3166-2
    productionCountry: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#productionCountry",
        default=None,
    )

    # label: targetCountry
    # comment: Item target country. Refer ISO 3166-2
    targetCountry: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#targetCountry",
        default=None,
    )

    # label: unitPrice
    # comment: Product price per unit in the base
    unitPrice: Union[CurrencyValue, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#unitPrice",
        default=None,
    )

    # label: weight
    # comment: Weight of the item
    weight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#weight",
        default=None,
    )

    # label: batchNumber
    # comment: Production batch number / reference
    batchNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#batchNumber",
        default=None,
    )

    # label: expiryDate
    # comment: Product expiry date - e.g. for perishables goods or goods with programmed obsolescence
    expiryDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#expiryDate",
        default=None,
    )

    # label: lotNumber
    # comment: Production lot number / reference
    lotNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#lotNumber",
        default=None,
    )

    # label: productionDate
    # comment: Production date
    productionDate: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#productionDate",
        default=None,
    )

    # label: quantityForUnitPrice
    # comment: Product quantity for unit price - e.g. 12 (eggs for one USD 1)
    quantityForUnitPrice: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#quantityForUnitPrice",
        default=None,
    )


class LoadingMaterial(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#LoadingMaterial"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LoadingMaterial"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: manufacturer
    # comment: Manufacturing company details and contacts
    manufacturer: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer",
        default=None,
    )

    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    otherIdentifiers: List[OtherIdentifier] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
        default_factory=list,
    )

    # label: description
    # comment: Natural language description if required
    description: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
        default=None,
    )

    # label: materialModel
    # comment: Model of the LoadingMaterial if any
    materialModel: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#materialModel",
        default=None,
    )

    # label: materialType
    # comment: Type of the LoadingMaterial
    materialType: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#materialType",
        default=None,
    )

    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    serialNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber",
        default=None,
    )


class LoadingUnit(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#LoadingUnit")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#LoadingUnit"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: inUnitComposition
    inUnitComposition: Union[UnitComposition, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#inUnitComposition",
        default=None,
    )

    # label: tareWeight
    # comment: Tare weight of the empty ULD
    tareWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#tareWeight",
        default=None,
    )

    # label: remarks
    # comment: Remarks or Supplement Information
    remarks: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#remarks",
        default=None,
    )


class Location(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Location")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Location"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: address
    # comment: Address details
    address: Union[Address, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#address",
        default=None,
    )

    # label: geolocation
    # comment: Geolocation details
    geolocation: Union[Geolocation, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#geolocation",
        default=None,
    )

    # label: locationCodes
    # comment: Location code of airport, freight terminal, seaport, rail station. UN/LOCODE city code (5 letter) or IATA airport code (3 letter)
    locationCodes: List[CodeListElement] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationCodes",
        default_factory=list,
    )

    # label: onsiteActions
    # comment: References to the Actions happening at the Location
    onsiteActions: List[LogisticsAction] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#onsiteActions",
        default_factory=list,
    )

    # comment: Reference to the Location this is a Sublocation of
    subLocationOf: Union[Location, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#subLocationOf",
        default=None,
    )

    # comment: References to Sublocations that describe the Location in more detail
    subLocations: List[Location] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#subLocations",
        default_factory=list,
    )

    # label: locationName
    # comment: Full name of the location
    locationName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationName",
        default=None,
    )

    # label: locationType
    # comment: Location type - e.g. Airport, Freight terminal, Rail station, Seaport, etc
    locationType: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationType",
        default=None,
    )


class Piece(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Piece")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Piece"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: containedItems
    # comment: Reference to the item(s) contained in the piece
    containedItems: List[Item] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#containedItems",
        default_factory=list,
    )

    # label: containedPieces
    # comment: Details of contained piece(s)
    containedPieces: List[Piece] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#containedPieces",
        default_factory=list,
    )

    # label: contentProductionCountry
    # comment: Goods production country, mandatory when there are no Items. Refer ISO 3166-2
    contentProductionCountry: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contentProductionCountry",
        default=None,
    )

    # label: contentProducts
    # comment: Reference to the Products describing the content of the Piece, mandatory if no data on Item level is used
    contentProducts: List[Product] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contentProducts",
        default_factory=list,
    )

    # label: customsInformation
    # comment: Customs details
    customsInformation: List[CustomsInformation] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation",
        default_factory=list,
    )

    # label: dimensions
    # comment: Dimensions details
    dimensions: Union[Dimensions, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#dimensions",
        default=None,
    )

    # label: fulfillsUldTypeCode
    # comment: Text holding an ULD Type Code if the Piece fulfills it before UnitComposition
    fulfillsUldTypeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#fulfillsUldTypeCode",
        default=None,
    )

    # label: grossWeight
    # comment: Weight details
    grossWeight: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#grossWeight",
        default=None,
    )

    # label: inPiece
    # comment: Reference to the Piece this Item or Piece is contained in
    inPiece: Union[Piece, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#inPiece",
        default=None,
    )

    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    involvedParties: List[Party] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
        default_factory=list,
    )

    # label: loadType
    # comment: Load type of the shipment or piece (Bulk, ULD, Pallet, Loose)
    loadType: Union[LoadType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadType",
        default=None,
    )

    # label: ofShipment
    # comment: Reference to the Shipment the Piece is assigned to
    ofShipment: List[Shipment] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ofShipment",
        default_factory=list,
    )

    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    otherIdentifiers: List[OtherIdentifier] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
        default_factory=list,
    )

    # label: packageMarkCoded
    # comment: Reference identifying how the package is marked. Field is hardcode to "SSCC-18", "UPC" or "Other"
    packageMarkCoded: Union[PackageMarkCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageMarkCoded",
        default=None,
    )

    # label: packagingType
    # comment: Packaging details
    packagingType: Union[PackagingType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#packagingType",
        default=None,
    )

    # label: securityDeclarations
    # comment: Security details of the piece
    securityDeclarations: List[SecurityDeclaration] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#securityDeclarations",
        default_factory=list,
    )

    # label: specialHandlingCodes
    # comment: Three-letter special handling code (SPH)
    specialHandlingCodes: List[SpecialHandlingCode] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialHandlingCodes",
        default_factory=list,
    )

    # label: temperatureInstructions
    # comment: Temperature instructions if a specific range
    temperatureInstructions: Union[TemperatureInstructions, SkipJsonSchema[None]] = (
        Field(
            serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureInstructions",
            default=None,
        )
    )

    # label: coload
    # comment: Coload indicator for the pieces (boolean)
    coload: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#coload",
        default=None,
    )

    # label: goodsDescription
    # comment: Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    goodsDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#goodsDescription",
        default=None,
    )

    # label: nvdForCarriage
    # comment: When no value is declared for Carriage, this field may be completed with the value TRUE otherwise FALSE
    nvdForCarriage: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCarriage",
        default=None,
    )

    # label: nvdForCustoms
    # comment: When no value is declared for Customs, this field may be completed with the value TRUE otherwise FALSE
    nvdForCustoms: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCustoms",
        default=None,
    )

    # label: packagedeIdentifier
    # comment: SSCC-18 code for the value of the package mark, company or bar code, free text, pallet code, etc.
    packagedeIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#packagedeIdentifier",
        default=None,
    )

    # label: shippingMarks
    # comment: Shipping marks
    shippingMarks: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingMarks",
        default_factory=list,
    )

    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    slac: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#slac",
        default=None,
    )

    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    stackable: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#stackable",
        default=None,
    )

    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    textualHandlingInstructions: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions",
        default_factory=list,
    )

    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    turnable: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#turnable",
        default=None,
    )

    # label: upid
    # comment: Unique Piece Identifier (UPID) of the piece. Refer IATA Recommended Practice 1689
    upid: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#upid",
        default=None,
    )


class Sensor(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Sensor")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Sensor"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: measurements
    # comment: Reference to the Measurements recorded by the Sensor
    measurements: List[Measurement] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#measurements",
        default_factory=list,
    )

    # label: partOfIotDevice
    # comment: Reference to the IoT Device to which the sensor is linked
    partOfIotDevice: Union[IotDevice, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#partOfIotDevice",
        default=None,
    )

    # label: sensorType
    # comment: Type of sensor as described in Interactive Cargo Recommended Practice
    sensorType: Union[SensorType, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#sensorType",
        default=None,
    )

    # label: description
    # comment: Natural language description if required
    description: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
        default=None,
    )

    # label: name
    # comment: Human-understandable name of object depending on the context
    name: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#name",
        default=None,
    )

    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    serialNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber",
        default=None,
    )


class TransportMeans(PhysicalLogisticsObject):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#TransportMeans"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#TransportMeans"),
        URIRef("https://onerecord.iata.org/ns/cargo#PhysicalLogisticsObject"),
    ]

    # label: operatedTransportMovement
    # comment: Transport Movement on which the Transport Means is used
    operatedTransportMovement: Union[TransportMovement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#operatedTransportMovement",
        default=None,
    )

    # label: transportOrganization
    # comment: Company operating the transport means
    transportOrganization: Union[Organization, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportOrganization",
        default=None,
    )

    # label: typicalCo2Coefficient
    # comment: Required for some CO2 calculations
    typicalCo2Coefficient: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#typicalCo2Coefficient",
        default=None,
    )

    # label: typicalFuelConsumption
    # comment: Typical fuel consumption (e.g. 2 L / 1 nm)
    typicalFuelConsumption: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#typicalFuelConsumption",
        default=None,
    )

    # label: vehicleType
    # comment: Vehicle or container type. Refer UNECE28, e.g. 4.. - Aircraft, type unknown.For Air refer to IATA Standard Schedules Information Manual in section ATA/IATA Aircraft Types
    vehicleType: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleType",
        default=None,
    )

    # label: vehicleModel
    # comment: Model or make of the vehicle (e.g. A33-3)
    vehicleModel: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleModel",
        default=None,
    )

    # label: vehicleRegistration
    # comment: Vehicle identification - e.g. aircraft registration number
    vehicleRegistration: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleRegistration",
        default=None,
    )

    # label: vehicleSize
    # comment: Size of the vehicle - free text
    vehicleSize: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#vehicleSize",
        default=None,
    )


class ProductDg(Product):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#ProductDg")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ProductDg"),
        URIRef("https://onerecord.iata.org/ns/cargo#Product"),
    ]

    # label: dgRadioactiveMaterial
    # comment: Dg Radioactive Material
    dgRadioactiveMaterial: Union[DgProductRadioactive, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#dgRadioactiveMaterial",
        default=None,
    )

    # label: explosiveCompatibilityGroupCode
    # comment: Specifies the reference to the group which identifies the kind of substances and articles that are deemed to be compatible. Mandatory field in case of transport of explosive articles or substances
    explosiveCompatibilityGroupCode: Union[
        ExplosiveCompatibilityGroupCode, SkipJsonSchema[None]
    ] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#explosiveCompatibilityGroupCode",
        default=None,
    )

    # label: packagingDangerLevelCode
    # comment: Packing group, If used must reference I, II or III
    packagingDangerLevelCode: Union[PackagingDangerLevelCode, SkipJsonSchema[None]] = (
        Field(
            serialization_alias="https://onerecord.iata.org/ns/cargo#packagingDangerLevelCode",
            default=None,
        )
    )

    # label: additionalHazardClassificationId
    # comment: Identifies the subsidiary hazard class / division identification containing a numeric field separated by a decimal. There may be , 1 or 2 subsidiary risk classes or divisions. If there is more than one, each should be separated by a comma. The subsidiary risk must be shown in parentheses.
    additionalHazardClassificationId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#additionalHazardClassificationId",
        default=None,
    )

    # label: authorizationInformation
    # comment: Contains additional information relating to an approval, permission or other specific detail applicable to the commodity (e.g. Dangerous Goods in excepted quantities)
    authorizationInformation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#authorizationInformation",
        default=None,
    )

    # label: hazardClassificationId
    # comment: Identifies the hazard class / division identification containing a numeric field separated by a decimal
    hazardClassificationId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#hazardClassificationId",
        default=None,
    )

    # label: packingInstructionNumber
    # comment: The packing instruction number applicable to the UN number / proper shipping name entry. A three-numeric value which may be preceded by the letter Y.  Mandatory field for air transport (Air)
    packingInstructionNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#packingInstructionNumber",
        default=None,
    )

    # label: properShippingName
    # comment: The name used to describe the particular article or substance as shown in the UN Model Regulations Dangerous Goods List
    properShippingName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#properShippingName",
        default=None,
    )

    # label: specialProvisionId
    # comment: For Air Mode: Special Provision may show a single, double or triple digit number preceded by the letter A, against appropriate entries in the List of Dangerous Goods
    specialProvisionId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialProvisionId",
        default=None,
    )

    # label: technicalName
    # comment: This is additional chemical name(s) required for some proper shipping names. When added the technical must be shown in parentheses immediately following the proper shipping name.
    technicalName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#technicalName",
        default=None,
    )

    # label: unNumber
    # comment: Reference identifying the United Nations Dangerous Goods serial number assigned within the UN to substances and articles contained in a list of the dangerous goods most commonly carried. e.g. 1189 - Ethylene glycol monomethyl ether acetate
    unNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#unNumber",
        default=None,
    )


class NonHumanActor(Actor):
    pass


class Person(Actor):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Person")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Person"),
        URIRef("https://onerecord.iata.org/ns/cargo#Actor"),
    ]

    # label: contactDetails
    # comment: Information about contactDetails
    contactDetails: List[ContactDetail] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetails",
        default_factory=list,
    )

    # label: contactRole
    # comment: Contact type - e.g. Emergency contact, Customs contact, Customer contact
    contactRole: Union[ContactRole, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactRole",
        default=None,
    )

    # label: documents
    # comment: Linked documents to the person, e.g. driver's license, ID, etc.
    documents: List[ExternalReference] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#documents",
        default_factory=list,
    )

    # label: department
    # comment: Department / Division / Unit
    department: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#department",
        default=None,
    )

    # label: employeeId
    # comment: Employee ID
    employeeId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#employeeId",
        default=None,
    )

    # label: firstName
    # comment: First name / given name
    firstName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#firstName",
        default=None,
    )

    # label: jobTitle
    # comment: Job title / position
    jobTitle: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#jobTitle",
        default=None,
    )

    # label: lastName
    # comment: Last name / family name / surname
    lastName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#lastName",
        default=None,
    )

    # label: middleName
    # comment: Middle name/ other name
    middleName: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#middleName",
        default=None,
    )

    # label: salutation
    # comment: Salutation
    salutation: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#salutation",
        default=None,
    )


class Company(Organization):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Company")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Company"),
        URIRef("https://onerecord.iata.org/ns/cargo#Organization"),
    ]

    # label: iataCargoAgentCode
    # comment: IATA accredited cargo agent 7 digit number
    iataCargoAgentCode: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentCode",
        default=None,
        max_length=7,
    )

    # label: iataCargoAgentLocationIdentifier
    # comment: IATA CASS cargo agent 4 digit branch number / location identifier
    iataCargoAgentLocationIdentifier: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentLocationIdentifier",
        default=None,
        max_length=4,
    )


class PublicAuthority(Organization):
    pass


class ItemDg(Item):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#ItemDg")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ItemDg"),
        URIRef("https://onerecord.iata.org/ns/cargo#Item"),
    ]

    # label: emergencyContact
    # comment: Contains the Emergency contact name (e.g. the name of the agency) and phone number (min required)
    emergencyContact: Union[Person, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#emergencyContact",
        default=None,
    )

    # label: netWeightMeasure
    # comment: The total net weight of dangerous goods transported of this line item. For air transport the value must be the volume or mass in each package.
    netWeightMeasure: Union[Value, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#netWeightMeasure",
        default=None,
    )

    # label: reportableQuantity
    # comment: Reportable quantities, To and from the USA only
    reportableQuantity: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#reportableQuantity",
        default=None,
    )

    # label: supplementaryInfoPrefix
    # comment: Additional information that may be added in addition to the proper shipping name to more fully describe the goods or to identify a particular condition
    supplementaryInfoPrefix: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#supplementaryInfoPrefix",
        default=None,
    )

    # label: supplementaryInfoSuffix
    # comment: Additional information that may be added in addition to the proper shipping to more fully describe the goods or to identify a particular condition
    supplementaryInfoSuffix: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#supplementaryInfoSuffix",
        default=None,
    )


class ULD(LoadingUnit):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#ULD")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#ULD"),
        URIRef("https://onerecord.iata.org/ns/cargo#LoadingUnit"),
    ]

    # label: demurrageCode
    # comment: Contains three designator of demurrage code, refer to RP 1654 (BCC, HHH, XXX, ZZZ)
    demurrageCode: Union[DemurrageCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#demurrageCode",
        default=None,
    )

    # label: loadingIndicator
    # comment: ULD height or loading limitation code. Refer CXML Code List 1.47,  e.g. R - ULD Height above 244 centimetres
    loadingIndicator: Union[ULDLoadingIndicator, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingIndicator",
        default=None,
    )

    # label: odlnCode
    # comment: Contains two designator codes of ODLN or Operational Damage Limit Notices. ODLN code is used to define type of damage after visually check the serviceability of ULDs section 7, Standard Specifications 4/3 or 4/4 in ULD Regulations
    odlnCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#odlnCode",
        default=None,
    )

    # label: ownerCode
    # comment: Owner code of the ULD in aa, an or na format - owner can be an airline or leasing company
    ownerCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ownerCode",
        default=None,
    )

    # label: serviceabilityCode
    # comment: Designator of serviceability condition e.g. SER or DAM
    serviceabilityCode: Union[ULDConditionCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceabilityCode",
        default=None,
    )

    # label: uldTypeCode
    # comment: Standard Unit Load Device type code e.g. AKE - Certified Container - Contoured. Refer to IATA ULD Technical Manual
    uldTypeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldTypeCode",
        default=None,
    )

    # label: ataDesignator
    # comment: US / ATA Unit Load Device type code e.g. M2
    ataDesignator: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#ataDesignator",
        default=None,
    )

    # label: damageFlag
    # comment: Indicates if the ULD is Damaged
    damageFlag: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#damageFlag",
        default=None,
    )

    # label: numberOfDoors
    # comment: Number of doors
    numberOfDoors: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfDoors",
        default=None,
    )

    # label: numberOfFittings
    # comment: Number of fittings
    numberOfFittings: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfFittings",
        default=None,
    )

    # label: numberOfNets
    # comment: Number of nets
    numberOfNets: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfNets",
        default=None,
    )

    # label: numberOfStraps
    # comment: Number of straps
    numberOfStraps: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfStraps",
        default=None,
    )

    # label: sealNumber
    # comment: ULD seal number if applicable
    sealNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#sealNumber",
        default=None,
    )

    # label: uldSerialNumber
    # comment: Serial number that allows to uniquely identify the ULD
    uldSerialNumber: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldSerialNumber",
        default=None,
    )


class PieceDg(Piece):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#PieceDg")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#PieceDg"),
        URIRef("https://onerecord.iata.org/ns/cargo#Piece"),
    ]

    # label: dgDeclaration
    # comment: Reference to the Dangerous Goods declaration
    dgDeclaration: Union[DgDeclaration, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#dgDeclaration",
        default=None,
    )

    # label: overpackTypeCode
    # comment: Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations
    overpackTypeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#overpackTypeCode",
        default=None,
    )

    # label: allPackedInOneIndicator
    # comment: A statement identifying that the dangerous goods listed above are all contained in the same outer packaging. Takes the form All packed in one aaaa (description of packaging type) x nn (number of packages). Applies to air transport only. (Air)
    allPackedInOneIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#allPackedInOneIndicator",
        default=None,
    )

    # label: overpackCriticalitySafetyIndexNumeric
    # comment: Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.
    overpackCriticalitySafetyIndexNumeric: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#overpackCriticalitySafetyIndexNumeric",
        default=None,
    )

    # label: overpackIndicator
    # comment: Overpack indicator
    overpackIndicator: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#overpackIndicator",
        default=None,
    )

    # label: overpackT1
    # comment: A single number assigned to a package, overpack or freight container to provide control over radiation exposure.
    overpackT1: Union[bool, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#overpackT1",
        default=None,
    )

    # label: qValueNumeric
    # comment: Most instances of all packed in one will require the addition of the Q value which  1. Applies to air transport only. (Air)
    qValueNumeric: Union[float, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#qValueNumeric",
        default=None,
    )


class PieceLiveAnimals(Piece):
    _type: ClassVar[URIRef] = URIRef(
        "https://onerecord.iata.org/ns/cargo#PieceLiveAnimals"
    )
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#PieceLiveAnimals"),
        URIRef("https://onerecord.iata.org/ns/cargo#Piece"),
    ]

    # label: associatedEpermit
    # comment: Reference to the permits associated with the Live Animals
    associatedEpermit: Union[EpermitConsignment, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#associatedEpermit",
        default=None,
    )

    # label: exportTradeCountry
    # comment: Country of last re-export (box 12a). Refer ISO 3166-2
    exportTradeCountry: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#exportTradeCountry",
        default=None,
    )

    # label: goodsTypeCode
    # comment: Appendix number of the convention (I, II or III) (box 1)
    goodsTypeCode: Union[GoodsTypeCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#goodsTypeCode",
        default=None,
    )

    # label: goodsTypeExtensionCode
    # comment: Appendix number of the convention (I, II or III) (box 1)
    goodsTypeExtensionCode: Union[GoodsTypeExtensionCode, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#goodsTypeExtensionCode",
        default=None,
    )

    # label: originReferencePermitTypeCode
    # comment: Document type code of origin reference permit or re-export reference Certificate (box 12/12a)
    originReferencePermitTypeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitTypeCode",
        default=None,
    )

    # label: originTradeCountry
    # comment: country of origin (box 12). Refer ISO 3166-2
    originTradeCountry: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#originTradeCountry",
        default=None,
    )

    # label: specimenTypeCode
    # comment: Description of specimens, CITES type code (box 9)
    specimenTypeCode: Union[CodeListElement, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specimenTypeCode",
        default=None,
    )

    # label: acquisitionDateTime
    # comment: Defined in Resolution Conf. 13.6 and is required for pre-Convention specimens (box 12b)
    acquisitionDateTime: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#acquisitionDateTime",
        default=None,
    )

    # label: annualQuotaQuantity
    # comment: total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    annualQuotaQuantity: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#annualQuotaQuantity",
        default=None,
    )

    # label: categoryCode
    # comment: Operations code ID. Refers to the number of the registered captive-breeding or artificial propagation operation (box 12b)
    categoryCode: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#categoryCode",
        default_factory=list,
    )

    # label: originReferencePermitDateTime
    # comment: Issuing date for Origin reference permit or re-export reference Certificate (box 12)
    originReferencePermitDateTime: Union[datetime, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitDateTime",
        default=None,
    )

    # label: originReferencePermitId
    # comment: identifier of Origin reference permit or re-export reference Certificate (box 12/12a)
    originReferencePermitId: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitId",
        default=None,
    )

    # label: quantityAnimals
    # comment: Quantity including units (box 11)
    quantityAnimals: Union[int, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#quantityAnimals",
        default=None,
    )

    # label: speciesCommonName
    # comment: Species common name (box 8)
    speciesCommonName: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#speciesCommonName",
        default_factory=list,
    )

    # label: speciesScientificName
    # comment: Species scientific name (box 7)
    speciesScientificName: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#speciesScientificName",
        default_factory=list,
    )

    # label: specimenDescription
    # comment: Description of specimens, including age and sex if LA (box 9)
    specimenDescription: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#specimenDescription",
        default=None,
    )


class Carrier(Company):
    _type: ClassVar[URIRef] = URIRef("https://onerecord.iata.org/ns/cargo#Carrier")
    _types: ClassVar[List[URIRef]] = [
        URIRef("https://onerecord.iata.org/ns/cargo#Carrier"),
        URIRef("https://onerecord.iata.org/ns/cargo#Company"),
    ]

    # label: airlineCode
    # comment: IATA two-character airline code
    airlineCode: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#airlineCode",
        default=None,
        max_length=2,
    )

    # label: prefix
    # comment: IATA three-numeric airline prefix number
    prefix: Union[str, SkipJsonSchema[None]] = Field(
        serialization_alias="https://onerecord.iata.org/ns/cargo#prefix",
        default=None,
        max_length=3,
    )


for _cls in list(locals().values()):
    if isinstance(_cls, type) and issubclass(_cls, OneRecordBaseModel):
        result = _cls.model_rebuild()
        if result is False:
            raise RuntimeError(f"Failed to rebuild model for class {_cls.__name__}")
