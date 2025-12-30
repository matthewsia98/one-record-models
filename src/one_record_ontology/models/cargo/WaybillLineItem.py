from typing import List, Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.cargo.LineItemPackage import LineItemPackage
from one_record_ontology.models.cargo.ULD import ULD
from one_record_ontology.models.cargo.Value import Value
from one_record_ontology.models.code_lists.BasicRateClassCode import BasicRateClassCode
from one_record_ontology.models.code_lists.RateClassCode import RateClassCode


class WaybillLineItem(BaseModel):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight",
    )
    # label: lineItemPackages
    # comment: References to piece groupings for rating
    # iri: https://onerecord.iata.org/ns/cargo#lineItemPackages
    lineItemPackages: List[LineItemPackage] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemPackages",
    )
    # label: rateCharge
    # comment: TACT Rate for rate description details
    # iri: https://onerecord.iata.org/ns/cargo#rateCharge
    rateCharge: Optional[CurrencyValue] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateCharge",
    )
    # label: rateClassCode
    # comment: Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCode
    rateClassCode: Optional[RateClassCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCode",
    )
    # label: rateClassCodeBasic
    # comment: Rate Surcharge/Reduction - Basic Rate Class Code
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCodeBasic
    rateClassCodeBasic: Optional[BasicRateClassCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCodeBasic",
    )
    # label: rateGrossWeight
    # comment: Information about the total gross weight considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateGrossWeight
    rateGrossWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateGrossWeight",
    )
    # label: ratePercentage
    # comment: Rate Surcharge/Reduction - Percentage of  red. / surcharge
    # iri: https://onerecord.iata.org/ns/cargo#ratePercentage
    ratePercentage: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#ratePercentage",
    )
    # label: rateVolume
    # comment: Information about the total volume considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateVolume
    rateVolume: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#rateVolume",
    )
    # label: rcp
    # comment: IATA 3-letter city code of the rate combination point as defined in TACT
    # iri: https://onerecord.iata.org/ns/cargo#rcp
    rcp: Optional[CodeListElement] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rcp"
    )
    # label: uldRateClassType
    # comment: ULD Rate information - ULD Rate Class Type
    # iri: https://onerecord.iata.org/ns/cargo#uldRateClassType
    uldRateClassType: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldRateClassType",
    )
    # label: uldReferences
    # comment: References to ULDs for which the rate applies
    # iri: https://onerecord.iata.org/ns/cargo#uldReferences
    uldReferences: List[ULD] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldReferences",
    )
    # label: conversionFactor
    # comment: Volume to weight conversion factor
    # iri: https://onerecord.iata.org/ns/cargo#conversionFactor
    conversionFactor: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor",
    )
    # label: lineItemNumber
    # comment: Number of the line item
    # iri: https://onerecord.iata.org/ns/cargo#lineItemNumber
    lineItemNumber: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemNumber",
    )
    # label: rateSlac
    # comment: Integer holding the total slac considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateSlac
    rateSlac: Optional[int] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#rateSlac"
    )
