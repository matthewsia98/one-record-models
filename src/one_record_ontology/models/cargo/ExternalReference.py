from datetime import datetime
from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Company import Company
from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject


class ExternalReference(LogisticsObject):
    # label: createdAtLocation
    # comment: Location of the document, e.g. location where the document was emitted
    # iri: https://onerecord.iata.org/ns/cargo#createdAtLocation
    createdAtLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#createdAtLocation",
    )
    # label: originator
    # comment: Document originator details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#originator
    originator: Optional[Company] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#originator",
    )
    # label: referenceForObjects
    # comment: References to the LogisticsObjects referring to this external reference
    # iri: https://onerecord.iata.org/ns/cargo#referenceForObjects
    referenceForObjects: List[LogisticsObject] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#referenceForObjects",
    )
    # label: checksum
    # comment: Checksum of the document to validate its integrity
    # iri: https://onerecord.iata.org/ns/cargo#checksum
    checksum: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checksum"
    )
    # label: documentIdentifier
    # comment: Unique document identifier
    # iri: https://onerecord.iata.org/ns/cargo#documentIdentifier
    documentIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentIdentifier",
    )
    # label: documentLink
    # comment: Link to the document, e.g. URL of the file where it is hosted
    # iri: https://onerecord.iata.org/ns/cargo#documentLink
    documentLink: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentLink",
    )
    # label: documentName
    # comment: If no DocumentType provided, name of the referenced document
    # iri: https://onerecord.iata.org/ns/cargo#documentName
    documentName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentName",
    )
    # label: documentType
    # comment: Type of the referenced document . Can refer UNEDIFACT 11  e.g. 740 - Air Waybill, but not limited to
    # iri: https://onerecord.iata.org/ns/cargo#documentType
    documentType: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentType",
    )
    # label: documentVersion
    # comment: Document version number
    # iri: https://onerecord.iata.org/ns/cargo#documentVersion
    documentVersion: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#documentVersion",
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
