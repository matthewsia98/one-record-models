from datetime import datetime
from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.EpermitConsignment import EpermitConsignment
from one_record_ontology.models.cargo.EpermitSignature import EpermitSignature
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Organization import Organization
from one_record_ontology.models.code_lists.TransactionPurposeCode import (
    TransactionPurposeCode,
)


class LiveAnimalsEpermit(LogisticsObject):
    # label: consignee
    # comment: Reference to the Organization that fulfills the role of the consignee, for a LiveAnimalsEpermit it has to include complete name and address (box 3)
    # iri: https://onerecord.iata.org/ns/cargo#consignee
    consignee: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#consignee",
    )
    # label: consignments
    # comment: Reference to the pieces and properties linked to the Permit (box 7 to 12)
    # iri: https://onerecord.iata.org/ns/cargo#consignments
    consignments: List[EpermitConsignment] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#consignments",
    )
    # label: permitTypeCode
    # comment: Code specifying the document name. (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#permitTypeCode
    permitTypeCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#permitTypeCode",
    )
    # label: signatures
    # comment: List of all the signatures of the Epermit (applicant box 4, issuing authority box 6, issuer box 13 and examining authority box 14)
    # iri: https://onerecord.iata.org/ns/cargo#signatures
    signatures: List[EpermitSignature] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatures",
    )
    # label: transactionPurposeCode
    # comment: Code indicating the purpose of the transaction (box 5a)
    # iri: https://onerecord.iata.org/ns/cargo#transactionPurposeCode
    transactionPurposeCode: Optional[TransactionPurposeCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transactionPurposeCode",
    )
    # label: transportContractTypeCode
    # comment: Code specifying the transport document name (box 15)
    # iri: https://onerecord.iata.org/ns/cargo#transportContractTypeCode
    transportContractTypeCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportContractTypeCode",
    )
    # label: copyIndicator
    # comment: Indicates if the permit is a copy (true) or an original (false) (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#copyIndicator
    copyIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#copyIndicator",
    )
    # label: epermitNumber
    # comment: The original number is a unique number allocated to each document by the relevant Management Authority. (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#epermitNumber
    epermitNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#epermitNumber",
    )
    # label: permitTypeOtherDescription
    # comment: Description if TypeCode is Other (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#permitTypeOtherDescription
    permitTypeOtherDescription: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#permitTypeOtherDescription",
    )
    # label: specialConditions
    # comment: Special conditions (box 5)
    # iri: https://onerecord.iata.org/ns/cargo#specialConditions
    specialConditions: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialConditions",
    )
    # label: transactionPurpose
    # comment: Purpose of the transaction in free text (box 5a)
    # iri: https://onerecord.iata.org/ns/cargo#transactionPurpose
    transactionPurpose: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transactionPurpose",
    )
    # label: transportContractId
    # comment: Reference to the Air Waybill or other transport contract document (box 15)
    # iri: https://onerecord.iata.org/ns/cargo#transportContractId
    transportContractId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#transportContractId",
    )
    # label: validFrom
    # comment: Validity start date based on usage context
    # iri: https://onerecord.iata.org/ns/cargo#validFrom
    validFrom: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#validFrom",
    )
    # label: validUntil
    # comment: Validity end date (date of expiry) based on usage context
    # iri: https://onerecord.iata.org/ns/cargo#validUntil
    validUntil: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#validUntil",
    )
