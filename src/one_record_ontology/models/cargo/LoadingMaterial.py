from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Organization import Organization
from one_record_ontology.models.cargo.OtherIdentifier import OtherIdentifier
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)


class LoadingMaterial(PhysicalLogisticsObject):
    # label: manufacturer
    # comment: Manufacturing company details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#manufacturer
    manufacturer: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer",
    )
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
    )
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
    )
    # label: materialModel
    # comment: Model of the LoadingMaterial if any
    # iri: https://onerecord.iata.org/ns/cargo#materialModel
    materialModel: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#materialModel",
    )
    # label: materialType
    # comment: Type of the LoadingMaterial
    # iri: https://onerecord.iata.org/ns/cargo#materialType
    materialType: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#materialType",
    )
    # label: serialNumber
    # comment: Serial number that allows to uniquely identify the object
    # iri: https://onerecord.iata.org/ns/cargo#serialNumber
    serialNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#serialNumber",
    )
