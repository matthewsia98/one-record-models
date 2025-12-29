from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class WaybillLineItem(BaseModel):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight")
    # label: lineItemPackages
    # comment: References to piece groupings for rating
    # iri: https://onerecord.iata.org/ns/cargo#lineItemPackages
    lineItemPackages: List[LineItemPackage] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemPackages")
    # label: rateCharge
    # comment: TACT Rate for rate description details
    # iri: https://onerecord.iata.org/ns/cargo#rateCharge
    rateCharge: List[CurrencyValue] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rateCharge")
    # label: rateClassCode
    # comment: Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCode
    rateClassCode: List[RateClassCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCode")
    # label: rateClassCodeBasic
    # comment: Rate Surcharge/Reduction - Basic Rate Class Code
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCodeBasic
    rateClassCodeBasic: List[BasicRateClassCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCodeBasic")
    # label: rateGrossWeight
    # comment: Information about the total gross weight considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateGrossWeight
    rateGrossWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rateGrossWeight")
    # label: ratePercentage
    # comment: Rate Surcharge/Reduction - Percentage of  red. / surcharge
    # iri: https://onerecord.iata.org/ns/cargo#ratePercentage
    ratePercentage: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ratePercentage")
    # label: rateVolume
    # comment: Information about the total volume considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateVolume
    rateVolume: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rateVolume")
    # label: rcp
    # comment: IATA 3-letter city code of the rate combination point as defined in TACT
    # iri: https://onerecord.iata.org/ns/cargo#rcp
    rcp: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rcp")
    # label: uldRateClassType
    # comment: ULD Rate information - ULD Rate Class Type
    # iri: https://onerecord.iata.org/ns/cargo#uldRateClassType
    uldRateClassType: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldRateClassType")
    # label: uldReferences
    # comment: References to ULDs for which the rate applies
    # iri: https://onerecord.iata.org/ns/cargo#uldReferences
    uldReferences: List[ULD] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldReferences")
    # label: conversionFactor
    # comment: Volume to weight conversion factor
    # iri: https://onerecord.iata.org/ns/cargo#conversionFactor
    conversionFactor: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor")
    # label: lineItemNumber
    # comment: Number of the line item
    # iri: https://onerecord.iata.org/ns/cargo#lineItemNumber
    lineItemNumber: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#lineItemNumber")
    # label: rateSlac
    # comment: Integer holding the total slac considered for a rate
    # iri: https://onerecord.iata.org/ns/cargo#rateSlac
    rateSlac: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rateSlac")