from datetime import datetime
from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Adjustments import Adjustments
from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Waybill import Waybill
from one_record_ontology.models.code_lists.AWBUseIndicator import AWBUseIndicator


class BillingDetails(LogisticsObject):
    # label: adjustments
    # comment: Information about Adjustments performed on the BillingDetails
    # iri: https://onerecord.iata.org/ns/cargo#adjustments
    adjustments: List[Adjustments] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#adjustments",
    )
    # label: awbUseIndicator
    # comment: It must either contain the values of R for Revenue AWB, V for Void AWB or S for Service AWB.
    # iri: https://onerecord.iata.org/ns/cargo#awbUseIndicator
    awbUseIndicator: Optional[AWBUseIndicator] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbUseIndicator",
    )
    # label: detailedWaybill
    # comment: Reference to the Waybill
    # iri: https://onerecord.iata.org/ns/cargo#detailedWaybill
    detailedWaybill: Optional[Waybill] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#detailedWaybill",
    )
    # label: taxDueAgent
    # comment: Tax due Agent (VAT/GST on Commission). Total VAT/TAX amount payable by airline to agent
    # iri: https://onerecord.iata.org/ns/cargo#taxDueAgent
    taxDueAgent: Optional[CurrencyValue] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAgent",
    )
    # label: taxDueAirline
    # comment: Tax due Airline (as per AWB, or VAT/GST as per invoice). Total VAT/TAX amount payable by agent to airline
    # iri: https://onerecord.iata.org/ns/cargo#taxDueAirline
    taxDueAirline: Optional[CurrencyValue] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#taxDueAirline",
    )
    # label: awbAcceptanceDate
    # comment: The Date AWB Acceptance should be the same as the Date AWB Delivery. (beginning of the process)
    # iri: https://onerecord.iata.org/ns/cargo#awbAcceptanceDate
    awbAcceptanceDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbAcceptanceDate",
    )
    # label: awbDeliveryDate
    # comment: The Date AWB Delivery is also used as the AWB Execution date which will determine which billing period it will be processed and billed in.
    # iri: https://onerecord.iata.org/ns/cargo#awbDeliveryDate
    awbDeliveryDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbDeliveryDate",
    )
    # label: awbExecutionDate
    # comment: The AWB execution date determines which billing period the document will be processed and billed in.
    # iri: https://onerecord.iata.org/ns/cargo#awbExecutionDate
    awbExecutionDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#awbExecutionDate",
    )
    # label: commission
    # comment: The commission amount in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    # iri: https://onerecord.iata.org/ns/cargo#commission
    commission: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#commission",
    )
    # label: commissionIndicator
    # comment: Indicates if commission is applied. Boolean
    # iri: https://onerecord.iata.org/ns/cargo#commissionIndicator
    commissionIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#commissionIndicator",
    )
    # label: commissionPercentage
    # comment: The commission percentage in favour of the Cargo Agent/Associate, applicable for the shipment concerned
    # iri: https://onerecord.iata.org/ns/cargo#commissionPercentage
    commissionPercentage: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#commissionPercentage",
    )
    # label: discount
    # comment: This is used as a discount to the “official” transportation charge on AWB to arrive at actual selling price
    # iri: https://onerecord.iata.org/ns/cargo#discount
    discount: Optional[float] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#discount"
    )
    # label: exchangeRate
    # comment: The Rate at which the Air Waybill Amount has been multiplied to arrive at the amount of settlement.
    # iri: https://onerecord.iata.org/ns/cargo#exchangeRate
    exchangeRate: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#exchangeRate",
    )
    # label: nbCorrections
    # comment: Number of corrections to CASS records
    # iri: https://onerecord.iata.org/ns/cargo#nbCorrections
    nbCorrections: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#nbCorrections",
    )
    # label: vatIndicator
    # comment: Indicate if subject to VAT (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#vatIndicator
    vatIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#vatIndicator",
    )
