from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class CustomsInformation(LogisticsObject):
    # label: contentCode
    # comment: Customs, Security and Regulatory Control Information Identifier. Coded indicator qualifying Customs related information: Item Number "I", Exemption Legend "L", System Downtime Reference "S", Unique Consignment Reference Number "U", Movement Reference Number "M" . Refers to Code List 1.1. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    # iri: https://onerecord.iata.org/ns/cargo#contentCode
    contentCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contentCode")
    # label: country
    # comment: Country details. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#country
    country: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#country")
    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForPiece
    issuedForPiece: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece")
    # label: issuedForShipment
    # comment: Reference to the shipment the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForShipment
    issuedForShipment: List[Shipment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForShipment")
    # label: subjectCode
    # comment: Information Identifier. Code identifying a piece of information/entity e.g. "IMP" for import, "EXP" for export, "AGT" for Agent, "ISS" for The Regulated Agent Issuing the Security Status for a Consignment etc. Condition: At least one of the three elements (Country Code, Information Identifier or Customs, Security and Regulatory Control Information Identifier) must be completed
    # iri: https://onerecord.iata.org/ns/cargo#subjectCode
    subjectCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#subjectCode")
    # label: note
    # comment: Free text for customs remarks, not used in OCI Composition Rules Table
    # iri: https://onerecord.iata.org/ns/cargo#note
    note: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#note")
    # label: ociLineNumber
    # comment: Integer holding the oci line number when upcasting multi-line oci structures from CIMP/CXML
    # iri: https://onerecord.iata.org/ns/cargo#ociLineNumber
    ociLineNumber: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ociLineNumber")
    # label: otherCustomsInformation
    # comment: Supplementary Customs, Security and Regulatory Control Information
    # iri: https://onerecord.iata.org/ns/cargo#otherCustomsInformation
    otherCustomsInformation: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherCustomsInformation")