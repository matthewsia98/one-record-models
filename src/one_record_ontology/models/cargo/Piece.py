from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.CustomsInformation import CustomsInformation
from one_record_ontology.models.cargo.Dimensions import Dimensions
from one_record_ontology.models.cargo.Item import Item
from one_record_ontology.models.cargo.LoadType import LoadType
from one_record_ontology.models.cargo.OtherIdentifier import OtherIdentifier
from one_record_ontology.models.cargo.PackagingType import PackagingType
from one_record_ontology.models.cargo.Party import Party
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)
from one_record_ontology.models.cargo.Product import Product
from one_record_ontology.models.cargo.SecurityDeclaration import SecurityDeclaration
from one_record_ontology.models.cargo.Shipment import Shipment
from one_record_ontology.models.cargo.TemperatureInstructions import (
    TemperatureInstructions,
)
from one_record_ontology.models.cargo.Value import Value
from one_record_ontology.models.code_lists.PackageMarkCode import PackageMarkCode
from one_record_ontology.models.code_lists.SpecialHandlingCode import (
    SpecialHandlingCode,
)


class Piece(PhysicalLogisticsObject):
    # label: containedItems
    # comment: Reference to the item(s) contained in the piece
    # iri: https://onerecord.iata.org/ns/cargo#containedItems
    containedItems: List[Item] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#containedItems",
    )
    # label: containedPieces
    # comment: Details of contained piece(s)
    # iri: https://onerecord.iata.org/ns/cargo#containedPieces
    containedPieces: List[Piece] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#containedPieces",
    )
    # label: contentProductionCountry
    # comment: Goods production country, mandatory when there are no Items. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#contentProductionCountry
    contentProductionCountry: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contentProductionCountry",
    )
    # label: contentProducts
    # comment: Reference to the Products describing the content of the Piece, mandatory if no data on Item level is used
    # iri: https://onerecord.iata.org/ns/cargo#contentProducts
    contentProducts: List[Product] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contentProducts",
    )
    # label: customsInformation
    # comment: Customs details
    # iri: https://onerecord.iata.org/ns/cargo#customsInformation
    customsInformation: List[CustomsInformation] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation",
    )
    # label: dimensions
    # comment: Dimensions details
    # iri: https://onerecord.iata.org/ns/cargo#dimensions
    dimensions: Optional[Dimensions] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#dimensions",
    )
    # label: fulfillsUldTypeCode
    # comment: Text holding an ULD Type Code if the Piece fulfills it before UnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#fulfillsUldTypeCode
    fulfillsUldTypeCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#fulfillsUldTypeCode",
    )
    # label: grossWeight
    # comment: Weight details
    # iri: https://onerecord.iata.org/ns/cargo#grossWeight
    grossWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#grossWeight",
    )
    # label: inPiece
    # comment: Reference to the Piece this Item or Piece is contained in
    # iri: https://onerecord.iata.org/ns/cargo#inPiece
    inPiece: Optional[Piece] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#inPiece"
    )
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties",
    )
    # label: loadType
    # comment: Load type of the shipment or piece (Bulk, ULD, Pallet, Loose)
    # iri: https://onerecord.iata.org/ns/cargo#loadType
    loadType: Optional[LoadType] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#loadType"
    )
    # label: ofShipment
    # comment: Reference to the Shipment the Piece is assigned to
    # iri: https://onerecord.iata.org/ns/cargo#ofShipment
    ofShipment: List[Shipment] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#ofShipment",
    )
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers",
    )
    # label: packageMarkCoded
    # comment: Reference identifying how the package is marked. Field is hardcode to "SSCC-18", "UPC" or "Other"
    # iri: https://onerecord.iata.org/ns/cargo#packageMarkCoded
    packageMarkCoded: Optional[PackageMarkCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packageMarkCoded",
    )
    # label: packagingType
    # comment: Packaging details
    # iri: https://onerecord.iata.org/ns/cargo#packagingType
    packagingType: Optional[PackagingType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packagingType",
    )
    # label: securityDeclarations
    # comment: Security details of the piece
    # iri: https://onerecord.iata.org/ns/cargo#securityDeclarations
    securityDeclarations: List[SecurityDeclaration] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#securityDeclarations",
    )
    # label: specialHandlingCodes
    # comment: Three-letter special handling code (SPH)
    # iri: https://onerecord.iata.org/ns/cargo#specialHandlingCodes
    specialHandlingCodes: List[SpecialHandlingCode] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialHandlingCodes",
    )
    # label: temperatureInstructions
    # comment: Temperature instructions if a specific range
    # iri: https://onerecord.iata.org/ns/cargo#temperatureInstructions
    temperatureInstructions: Optional[TemperatureInstructions] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureInstructions",
    )
    # label: coload
    # comment: Coload indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#coload
    coload: Optional[bool] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#coload"
    )
    # label: goodsDescription
    # comment: Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    # iri: https://onerecord.iata.org/ns/cargo#goodsDescription
    goodsDescription: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#goodsDescription",
    )
    # label: nvdForCarriage
    # comment: When no value is declared for Carriage, this field may be completed with the value TRUE otherwise FALSE
    # iri: https://onerecord.iata.org/ns/cargo#nvdForCarriage
    nvdForCarriage: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCarriage",
    )
    # label: nvdForCustoms
    # comment: When no value is declared for Customs, this field may be completed with the value TRUE otherwise FALSE
    # iri: https://onerecord.iata.org/ns/cargo#nvdForCustoms
    nvdForCustoms: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCustoms",
    )
    # label: packagedeIdentifier
    # comment: SSCC-18 code for the value of the package mark, company or bar code, free text, pallet code, etc.
    # iri: https://onerecord.iata.org/ns/cargo#packagedeIdentifier
    packagedeIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packagedeIdentifier",
    )
    # label: shippingMarks
    # comment: Shipping marks
    # iri: https://onerecord.iata.org/ns/cargo#shippingMarks
    shippingMarks: List[str] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingMarks",
    )
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac"
    )
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#stackable",
    )
    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    # iri: https://onerecord.iata.org/ns/cargo#textualHandlingInstructions
    textualHandlingInstructions: List[str] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions",
    )
    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#turnable
    turnable: Optional[bool] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#turnable"
    )
    # label: upid
    # comment: Unique Piece Identifier (UPID) of the piece. Refer IATA Recommended Practice 1689
    # iri: https://onerecord.iata.org/ns/cargo#upid
    upid: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#upid"
    )
