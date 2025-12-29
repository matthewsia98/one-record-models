from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class SecurityDeclaration(LogisticsObject):
    # label: groundsForExemption
    # comment: Exemption code - e.g. BIOM- Bio-Medical Samples SMUS - small undersized shipments MAIL - mail BIOM - bio-medical samples DIPL - diplomatic bags or diplomatic mail LFSM - life-saving materials NUCL - nuclear materials TRNS - transfer or transshipment
    # iri: https://onerecord.iata.org/ns/cargo#groundsForExemption
    groundsForExemption: List[ScreeningExemption] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#groundsForExemption")
    # label: issuedBy
    # comment: Name of person (or employee ID) who issued the security status
    # iri: https://onerecord.iata.org/ns/cargo#issuedBy
    issuedBy: List[Person] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedBy")
    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForPiece
    issuedForPiece: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece")
    # label: otherRegulatedEntities
    # comment: Any other regulated entity that accepts custody of the cargo and accepts the security status originally issued
    # iri: https://onerecord.iata.org/ns/cargo#otherRegulatedEntities
    otherRegulatedEntities: List[RegulatedEntity] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherRegulatedEntities")
    # label: receivedFrom
    # comment: Regulated entity that tendered the consignment
    # iri: https://onerecord.iata.org/ns/cargo#receivedFrom
    receivedFrom: List[RegulatedEntity] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#receivedFrom")
    # label: regulatedEntityAcceptor
    # comment: Information about the accepting regulated entity of the Security Declaration
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityAcceptor
    regulatedEntityAcceptor: List[RegulatedEntity] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityAcceptor")
    # label: regulatedEntityIssuer
    # comment: Regulated entity issuing the Security Declaration
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityIssuer
    regulatedEntityIssuer: List[RegulatedEntity] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityIssuer")
    # label: screeningMethods
    # comment: Screening methods which have been used to secure the cargo PHS – Physical Inspection and/or hand search VCK - Visual check XRY- X-ray equipment EDS - Explosive detection system EDD - Explosive detection dogsETD - Explosive trace detection equipment - particles or vapor CMD - Cargo metal detection AOM - Subjected to any other means: this entry should be followed by free text specifying what other mean was used to secure the cargo
    # iri: https://onerecord.iata.org/ns/cargo#screeningMethods
    screeningMethods: List[ScreeningMethod] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#screeningMethods")
    # label: securityStatus
    # comment: Security status indicator (CXML 1.13) - e.g. SPX- Cargo Secure for Passenger and All-Cargo Aircraft 
    # iri: https://onerecord.iata.org/ns/cargo#securityStatus
    securityStatus: List[SecurityStatus] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#securityStatus")
    # label: additionalSecurityInformation
    # comment: Any additional information that may be required by an ICAO Member State
    # iri: https://onerecord.iata.org/ns/cargo#additionalSecurityInformation
    additionalSecurityInformation: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#additionalSecurityInformation")
    # label: issuedOn
    # comment: Date and time when the security status was issued
    # iri: https://onerecord.iata.org/ns/cargo#issuedOn
    issuedOn: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedOn")
    # label: otherScreeningMethods
    # comment: Other methods used to secure the cargo
    # iri: https://onerecord.iata.org/ns/cargo#otherScreeningMethods
    otherScreeningMethods: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherScreeningMethods")