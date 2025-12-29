from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class Ratings(LogisticsObject):
    # label: billingChargeIdentifier
    # comment: Billing charge identifiers to be used for CASS. Refer to CargoXML Code List 1.33
    # iri: https://onerecord.iata.org/ns/cargo#billingChargeIdentifier
    billingChargeIdentifier: List[ChargeIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#billingChargeIdentifier")
    # label: chargePaymentType
    # comment: Indicates if charge is prepaid or collect (P, C)
    # iri: https://onerecord.iata.org/ns/cargo#chargePaymentType
    chargePaymentType: List[PrepaidCollectIndicator] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargePaymentType")
    # label: chargeType
    # comment: Charge type related to amount total as per bullet points 2/21 - data elements 24A - 3B  from AWB
    # iri: https://onerecord.iata.org/ns/cargo#chargeType
    chargeType: List[ChargeIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeType")
    # label: entitlement
    # comment: Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    # iri: https://onerecord.iata.org/ns/cargo#entitlement
    entitlement: List[EntitlementCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#entitlement")
    # label: forPrices
    # comment: Reference to the Prices based on this Ratings
    # iri: https://onerecord.iata.org/ns/cargo#forPrices
    forPrices: List[Price] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forPrices")
    # label: otherChargeCode
    # comment: Refer to CargoXML Code List 1.2 for Other Charges
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeCode
    otherChargeCode: List[OtherChargeCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeCode")
    # label: ranges
    # comment: Reference to the ranges
    # iri: https://onerecord.iata.org/ns/cargo#ranges
    ranges: List[Ranges] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ranges")
    # label: rcp
    # comment: IATA 3-letter city code of the rate combination point as defined in TACT
    # iri: https://onerecord.iata.org/ns/cargo#rcp
    rcp: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rcp")
    # label: chargeDescription
    # comment: Description of the charge e.g. Airfreight, fuel, etc.
    # iri: https://onerecord.iata.org/ns/cargo#chargeDescription
    chargeDescription: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeDescription")
    # label: priceReferenceId
    # comment: Reference to a price reference if existing (e.g. Allotment number, contract reference, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#priceReferenceId
    priceReferenceId: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#priceReferenceId")
    # label: priceSpecification
    # comment: Specification of the price e.g. Street, Group, Spot, etc.
    # iri: https://onerecord.iata.org/ns/cargo#priceSpecification
    priceSpecification: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#priceSpecification")
    # label: quantity
    # comment: Quantity for the charge if applicable
    # iri: https://onerecord.iata.org/ns/cargo#quantity
    quantity: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#quantity")
    # label: subTotal
    # comment: Subtotal of the charge
    # iri: https://onerecord.iata.org/ns/cargo#subTotal
    subTotal: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#subTotal")