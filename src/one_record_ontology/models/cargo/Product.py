from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class Product(LogisticsObject):
    # label: describedObjects
    # comment: Reference to the Items or Pieces in which the product can be found.
    # iri: https://onerecord.iata.org/ns/cargo#describedObjects
    describedObjects: List[PhysicalLogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#describedObjects")
    # label: hsCode
    # comment: Harmonized Commodity code, refer to hsType used. 6 minimum digits are expected.
    # iri: https://onerecord.iata.org/ns/cargo#hsCode
    hsCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#hsCode")
    # label: manufacturer
    # comment: Manufacturing company details and contacts
    # iri: https://onerecord.iata.org/ns/cargo#manufacturer
    manufacturer: List[Organization] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#manufacturer")
    # label: otherCharacteristics
    # comment: Characteristics of the product
    # iri: https://onerecord.iata.org/ns/cargo#otherCharacteristics
    otherCharacteristics: List[Characteristic] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherCharacteristics")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: commodityItemNumber
    # comment: Indicates the specific commodity on which the rate class code is applied
    # iri: https://onerecord.iata.org/ns/cargo#commodityItemNumber
    commodityItemNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#commodityItemNumber")
    # label: description
    # comment: Natural language description if required
    # iri: https://onerecord.iata.org/ns/cargo#description
    description: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#description")
    # label: hsCommodityDescription
    # comment: Commodity description
    # iri: https://onerecord.iata.org/ns/cargo#hsCommodityDescription
    hsCommodityDescription: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityDescription")
    # label: hsCommodityName
    # comment: If no Code provided, name of commodity
    # iri: https://onerecord.iata.org/ns/cargo#hsCommodityName
    hsCommodityName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#hsCommodityName")
    # label: hsType
    # comment: Reference identifying the type of standard code to be used for the Commodity Classification (Brussels Tariff Nomenclature, EU Harmonized System Code, UN Standard International Trade Classification). Mandatory if the commodity code is more than 6 digits
    # iri: https://onerecord.iata.org/ns/cargo#hsType
    hsType: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#hsType")
    # label: uniqueIdentifier
    # comment: Manufacturer's unique product identifier
    # iri: https://onerecord.iata.org/ns/cargo#uniqueIdentifier
    uniqueIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uniqueIdentifier")