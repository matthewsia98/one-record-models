from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.code_lists.EntitlementCode import EntitlementCode
from one_record_ontology.models.code_lists.OtherChargeCode import OtherChargeCode
from one_record_ontology.models.code_lists.PrepaidCollectIndicator import (
    PrepaidCollectIndicator,
)


class OtherCharge(BaseModel):
    # label: chargePaymentType
    # comment: Indicates if charge is prepaid or collect (P, C)
    # iri: https://onerecord.iata.org/ns/cargo#chargePaymentType
    chargePaymentType: Optional[PrepaidCollectIndicator] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargePaymentType",
    )
    # label: entitlement
    # comment: Entitlement code to define if charges are Due carrier (C) or Due agent (A). Refer to CXML Code List 1.3
    # iri: https://onerecord.iata.org/ns/cargo#entitlement
    entitlement: Optional[EntitlementCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#entitlement",
    )
    # label: otherChargeAmount
    # comment: Other Charge amount
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeAmount
    otherChargeAmount: Optional[CurrencyValue] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeAmount",
    )
    # label: otherChargeCode
    # comment: Refer to CargoXML Code List 1.2 for Other Charges
    # iri: https://onerecord.iata.org/ns/cargo#otherChargeCode
    otherChargeCode: Optional[OtherChargeCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherChargeCode",
    )
    # label: chargeQuantity
    # comment: Double describing the time or item basis quantity of a charge
    # iri: https://onerecord.iata.org/ns/cargo#chargeQuantity
    chargeQuantity: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeQuantity",
    )
    # label: locationIndicator
    # comment: String indicating if the Other Charge Location is Origin (O) or Transit (T) or Destination(D)
    # iri: https://onerecord.iata.org/ns/cargo#locationIndicator
    locationIndicator: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationIndicator",
    )
    # label: reasonDescription
    # comment: String describing the reason for a charge
    # iri: https://onerecord.iata.org/ns/cargo#reasonDescription
    reasonDescription: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#reasonDescription",
    )
