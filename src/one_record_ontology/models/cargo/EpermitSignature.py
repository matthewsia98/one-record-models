from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class EpermitSignature(LogisticsObject):
    # label: forEpermit
    # comment: Reference to the LiveAnimalsEpermit this Signature applies to
    # iri: https://onerecord.iata.org/ns/cargo#forEpermit
    forEpermit: List[LiveAnimalsEpermit] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forEpermit")
    # label: signatoryCompany
    # comment: Signatory company name
    # iri: https://onerecord.iata.org/ns/cargo#signatoryCompany
    signatoryCompany: List[Company] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryCompany")
    # label: signatoryRole
    # comment: Role of the signatory with regards to the ePermit: Applicant, Permit issuer, Issuing Authority or Examining authority
    # iri: https://onerecord.iata.org/ns/cargo#signatoryRole
    signatoryRole: List[SignatoryRole] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#signatoryRole")
    # label: signatureTypeCode
    # comment: Code specifying a type of government action such as inspection, detention, fumigation, security.
    # iri: https://onerecord.iata.org/ns/cargo#signatureTypeCode
    signatureTypeCode: List[SignatureTypeCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#signatureTypeCode")
    # label: securityStampId
    # comment: Security Stamp ID
    # iri: https://onerecord.iata.org/ns/cargo#securityStampId
    securityStampId: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#securityStampId")
    # label: signatureDate
    # comment: Date and time of the signature
    # iri: https://onerecord.iata.org/ns/cargo#signatureDate
    signatureDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#signatureDate")
    # label: signatureStatement
    # comment: Signatory signature authentication text
    # iri: https://onerecord.iata.org/ns/cargo#signatureStatement
    signatureStatement: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#signatureStatement")