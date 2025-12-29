from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class OtherCharge(BaseModel):
    # label: chargePaymentType
    # comment: Indicates if charge is prepaid or collect (P, C)
    # iri: https://onerecord.iata.org/ns/cargo#chargePaymentType
    chargePaymentType: List[PrepaidCollectIndicator] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargePaymentType")
    # label: entitlement
    # comment: Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    # iri: https://onerecord.iata.org/ns/cargo#entitlement
    entitlement: List[EntitlementCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#entitlement")
    # label: otherChargeAmount
    # comment: Other Charge amount
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeAmount
    otherChargeAmount: List[CurrencyValue] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeAmount")
    # label: otherChargeCode
    # comment: Refer to CargoXML Code List 1.2 for Other Charges
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeCode
    otherChargeCode: List[OtherChargeCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeCode")
    # label: chargeQuantity
    # comment: Double describing the time or item basis quantity of a charge
    # iri: https://onerecord.iata.org/ns/cargo#chargeQuantity
    chargeQuantity: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeQuantity")
    # label: locationIndicator
    # comment: String indicating if the Other Charge Location is Origin (O) or Transit (T) or Destination(D)
    # iri: https://onerecord.iata.org/ns/cargo#locationIndicator
    locationIndicator: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#locationIndicator")
    # label: reasonDescription
    # comment: String describing the reason for a charge
    # iri: https://onerecord.iata.org/ns/cargo#reasonDescription
    reasonDescription: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#reasonDescription")