from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Characteristic import Characteristic
from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Organization import Organization
from one_record_ontology.models.cargo.OtherIdentifier import OtherIdentifier
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)


class Product(LogisticsObject):
    # label: describedObjects
    # comment: Reference to the Items or Pieces in which the product can be found.
    # iri: https://onerecord.iata.org/ns/cargo#describedObjects
    describedObjects: List[PhysicalLogisticsObject] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#describedObjects",
    )
    # label: hsCode
    # comment: Harmonized Commodity code, refer to hsType used. 6 minimum digits are expected.
    # iri: https://onerecord.iata.org/ns/cargo#hsCode
    hsCode: Optional[CodeListElement] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#hsCode"
    )
    # label: manufacturer
    # comment: Manufacturing company details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#manufacturer
    manufacturer: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer",
    )
    # label: otherCharacteristics
    # comment: Characteristics of the product
    # iri: https://onerecord.iata.org/ns/cargo#otherCharacteristics
    otherCharacteristics: List[Characteristic] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherCharacteristics",
    )
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
    )
    # label: commodityItemNumber
    # comment: Indicates the specific commodity on which the rate class code is applied
    # iri: https://onerecord.iata.org/ns/cargo#commodityItemNumber
    commodityItemNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#commodityItemNumber",
    )
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#description",
    )
    # label: hsCommodityDescription
    # comment: Commodity description
    # iri: https://onerecord.iata.org/ns/cargo#hsCommodityDescription
    hsCommodityDescription: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityDescription",
    )
    # label: hsCommodityName
    # comment: If no Code provided, name of commodity
    # iri: https://onerecord.iata.org/ns/cargo#hsCommodityName
    hsCommodityName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityName",
    )
    # label: hsType
    # comment: Reference identifying the type of standard code to be used for the Commodity Classification (Brussels Tariff Nomenclature, EU Harmonized System Code, UN Standard International Trade Classification). Mandatory if the commodity code is more than 6 digits
    # iri: https://onerecord.iata.org/ns/cargo#hsType
    hsType: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#hsType"
    )
    # label: uniqueIdentifier
    # comment: Manufacturer's unique product identifier
    # iri: https://onerecord.iata.org/ns/cargo#uniqueIdentifier
    uniqueIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uniqueIdentifier",
    )
