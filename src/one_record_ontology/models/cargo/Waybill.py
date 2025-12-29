from one_record_ontology.models..PrepaidCollectIndicator import PrepaidCollectIndicator
from one_record_ontology.models.cargo.WaybillType import WaybillType
from one_record_ontology.models.cargo.WaybillLineItem import WaybillLineItem
from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.cargo.Shipment import Shipment
from one_record_ontology.models..ServiceCode import ServiceCode
from one_record_ontology.models.cargo.Booking import Booking
from one_record_ontology.models..PrepaidCollectIndicator import PrepaidCollectIndicator
from one_record_ontology.models.cargo.OtherCharge import OtherCharge
from one_record_ontology.models.cargo.Waybill import Waybill
from one_record_ontology.models.cargo.Party import Party
from one_record_ontology.models.cargo.Waybill import Waybill
from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models..ChargeCode import ChargeCode
from one_record_ontology.models.cargo.BillingDetails import BillingDetails
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.AccountingNote import AccountingNote
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
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