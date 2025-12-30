from datetime import datetime
from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Company import Company
from one_record_ontology.models.cargo.LiveAnimalsEpermit import LiveAnimalsEpermit
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.code_lists.SignatoryRole import SignatoryRole
from one_record_ontology.models.code_lists.SignatureTypeCode import SignatureTypeCode


class EpermitSignature(LogisticsObject):
    # label: forEpermit
    # comment: Reference to the LiveAnimalsEpermit this Signature applies to
    # iri: https://onerecord.iata.org/ns/cargo#forEpermit
    forEpermit: Optional[LiveAnimalsEpermit] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#forEpermit",
    )
    # label: signatoryCompany
    # comment: Signatory company name
    # iri: https://onerecord.iata.org/ns/cargo#signatoryCompany
    signatoryCompany: Optional[Company] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryCompany",
    )
    # label: signatoryRole
    # comment: Role of the signatory with regards to the ePermit: Applicant, Permit issuer, Issuing Authority or Examining authority
    # iri: https://onerecord.iata.org/ns/cargo#signatoryRole
    signatoryRole: Optional[SignatoryRole] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryRole",
    )
    # label: signatureTypeCode
    # comment: Code specifying a type of government action such as inspection, detention, fumigation, security.
    # iri: https://onerecord.iata.org/ns/cargo#signatureTypeCode
    signatureTypeCode: Optional[SignatureTypeCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatureTypeCode",
    )
    # label: securityStampId
    # comment: Security Stamp ID
    # iri: https://onerecord.iata.org/ns/cargo#securityStampId
    securityStampId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#securityStampId",
    )
    # label: signatureDate
    # comment: Date and time of the signature
    # iri: https://onerecord.iata.org/ns/cargo#signatureDate
    signatureDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatureDate",
    )
    # label: signatureStatement
    # comment: Signatory signature authentication text
    # iri: https://onerecord.iata.org/ns/cargo#signatureStatement
    signatureStatement: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#signatureStatement",
    )
