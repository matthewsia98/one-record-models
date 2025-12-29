from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class BillingDetails(LogisticsObject):
    # label: adjustments
    # comment: Information about Adjustments performed on the BillingDetails
    # iri: https://onerecord.iata.org/ns/cargo#adjustments
    adjustments: List[Adjustments] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#adjustments")
    # label: awbUseIndicator
    # comment: It must either contain the values of R for Revenue AWB, V for Void AWB or S for Service AWB.
    # iri: https://onerecord.iata.org/ns/cargo#awbUseIndicator
    awbUseIndicator: List[AWBUseIndicator] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#awbUseIndicator")
    # label: detailedWaybill
    # comment: Reference to the Waybill
    # iri: https://onerecord.iata.org/ns/cargo#detailedWaybill
    detailedWaybill: List[Waybill] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#detailedWaybill")
    # label: taxDueAgent
    # comment: Tax due Agent (VAT/GST on Commission). Total VAT/TAX amount payable by airline to agent
    # iri: https://onerecord.iata.org/ns/cargo#taxDueAgent
    taxDueAgent: List[CurrencyValue] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAgent")
    # label: taxDueAirline
    # comment: Tax due Airline (as per AWB, or VAT/GST as per invoice). Total VAT/TAX amount payable by agent to airline
    # iri: https://onerecord.iata.org/ns/cargo#taxDueAirline
    taxDueAirline: List[CurrencyValue] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAirline")
    # label: awbAcceptanceDate
    # comment: The Date AWB Acceptance should be the same as the Date AWB Delivery. (beginning of the process)
    # iri: https://onerecord.iata.org/ns/cargo#awbAcceptanceDate
    awbAcceptanceDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#awbAcceptanceDate")
    # label: awbDeliveryDate
    # comment: The Date AWB Delivery is also used as the AWB Execution date which will determine which billing period it will be processed and billed in.
    # iri: https://onerecord.iata.org/ns/cargo#awbDeliveryDate
    awbDeliveryDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#awbDeliveryDate")
    # label: awbExecutionDate
    # comment: The AWB execution date determines which billing period the document will be processed and billed in.
    # iri: https://onerecord.iata.org/ns/cargo#awbExecutionDate
    awbExecutionDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#awbExecutionDate")
    # label: commission
    # comment: The commission amount in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    # iri: https://onerecord.iata.org/ns/cargo#commission
    commission: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#commission")
    # label: commissionIndicator
    # comment: Indicates if commission is applied. Boolean
    # iri: https://onerecord.iata.org/ns/cargo#commissionIndicator
    commissionIndicator: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#commissionIndicator")
    # label: commissionPercentage
    # comment: The commission percentage in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    # iri: https://onerecord.iata.org/ns/cargo#commissionPercentage
    commissionPercentage: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#commissionPercentage")
    # label: discount
    # comment: This is used as a discount to the “official” transportation charge on AWB to arrive at actual selling price
    # iri: https://onerecord.iata.org/ns/cargo#discount
    discount: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#discount")
    # label: exchangeRate
    # comment: The Rate at which the Air Waybill Amount has been multiplied to arrive at the amount of settlement.
    # iri: https://onerecord.iata.org/ns/cargo#exchangeRate
    exchangeRate: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#exchangeRate")
    # label: nbCorrections
    # comment: Number of corrections to CASS records
    # iri: https://onerecord.iata.org/ns/cargo#nbCorrections
    nbCorrections: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#nbCorrections")
    # label: vatIndicator
    # comment: Indicate if subject to VAT (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#vatIndicator
    vatIndicator: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#vatIndicator")