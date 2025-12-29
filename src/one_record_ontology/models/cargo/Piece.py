from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PhysicalLogisticsObject import PhysicalLogisticsObject
class Piece(PhysicalLogisticsObject):
    # label: containedItems
    # comment: Reference to the item(s) contained in the piece
    # iri: https://onerecord.iata.org/ns/cargo#containedItems
    containedItems: List[Item] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#containedItems")
    # label: containedPieces
    # comment: Details of contained piece(s)
    # iri: https://onerecord.iata.org/ns/cargo#containedPieces
    containedPieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#containedPieces")
    # label: contentProductionCountry
    # comment: Goods production country, mandatory when there are no Items. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#contentProductionCountry
    contentProductionCountry: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contentProductionCountry")
    # label: contentProducts
    # comment: Reference to the Products describing the content of the Piece, mandatory if no data on Item level is used
    # iri: https://onerecord.iata.org/ns/cargo#contentProducts
    contentProducts: List[Product] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contentProducts")
    # label: customsInformation
    # comment: Customs details
    # iri: https://onerecord.iata.org/ns/cargo#customsInformation
    customsInformation: List[CustomsInformation] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation")
    # label: dimensions
    # comment: Dimensions details
    # iri: https://onerecord.iata.org/ns/cargo#dimensions
    dimensions: List[Dimensions] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#dimensions")
    # label: fulfillsUldTypeCode
    # comment: Text holding an ULD Type Code if the Piece fulfills it before UnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#fulfillsUldTypeCode
    fulfillsUldTypeCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#fulfillsUldTypeCode")
    # label: grossWeight
    # comment: Weight details
    # iri: https://onerecord.iata.org/ns/cargo#grossWeight
    grossWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#grossWeight")
    # label: inPiece
    # comment: Reference to the Piece this Item or Piece is contained in
    # iri: https://onerecord.iata.org/ns/cargo#inPiece
    inPiece: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#inPiece")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: loadType
    # comment: Load type of the shipment or piece (Bulk, ULD, Pallet, Loose)
    # iri: https://onerecord.iata.org/ns/cargo#loadType
    loadType: List[LoadType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#loadType")
    # label: ofShipment
    # comment: Reference to the Shipment the Piece is assigned to
    # iri: https://onerecord.iata.org/ns/cargo#ofShipment
    ofShipment: List[Shipment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ofShipment")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: packageMarkCoded
    # comment: Reference identifying how the package is marked. Field is hardcode to "SSCC-18", "UPC" or "Other"
    # iri: https://onerecord.iata.org/ns/cargo#packageMarkCoded
    packageMarkCoded: List[PackageMarkCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#packageMarkCoded")
    # label: packagingType
    # comment: Packaging details 
    # iri: https://onerecord.iata.org/ns/cargo#packagingType
    packagingType: List[PackagingType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#packagingType")
    # label: securityDeclarations
    # comment: Security details of the piece
    # iri: https://onerecord.iata.org/ns/cargo#securityDeclarations
    securityDeclarations: List[SecurityDeclaration] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#securityDeclarations")
    # label: specialHandlingCodes
    # comment: Three-letter special handling code (SPH)
    # iri: https://onerecord.iata.org/ns/cargo#specialHandlingCodes
    specialHandlingCodes: List[SpecialHandlingCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#specialHandlingCodes")
    # label: temperatureInstructions
    # comment: Temperature instructions if a specific range
    # iri: https://onerecord.iata.org/ns/cargo#temperatureInstructions
    temperatureInstructions: List[TemperatureInstructions] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureInstructions")
    # label: coload
    # comment: Coload indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#coload
    coload: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#coload")
    # label: goodsDescription
    # comment: Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    # iri: https://onerecord.iata.org/ns/cargo#goodsDescription
    goodsDescription: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsDescription")
    # label: nvdForCarriage
    # comment: When no value is declared for Carriage, this field may be completed with the value TRUE otherwise FALSE
    # iri: https://onerecord.iata.org/ns/cargo#nvdForCarriage
    nvdForCarriage: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCarriage")
    # label: nvdForCustoms
    # comment: When no value is declared for Customs, this field may be completed with the value TRUE otherwise FALSE
    # iri: https://onerecord.iata.org/ns/cargo#nvdForCustoms
    nvdForCustoms: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#nvdForCustoms")
    # label: packagedeIdentifier
    # comment: SSCC-18 code for the value of the package mark, company or bar code, free text, pallet code, etc.
    # iri: https://onerecord.iata.org/ns/cargo#packagedeIdentifier
    packagedeIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#packagedeIdentifier")
    # label: shippingMarks
    # comment: Shipping marks
    # iri: https://onerecord.iata.org/ns/cargo#shippingMarks
    shippingMarks: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingMarks")
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#slac")
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#stackable")
    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    # iri: https://onerecord.iata.org/ns/cargo#textualHandlingInstructions
    textualHandlingInstructions: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions")
    # label: turnable
    # comment: Turnable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#turnable
    turnable: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#turnable")
    # label: upid
    # comment: Unique Piece Identifier (UPID) of the piece. Refer IATA Recommended Practice 1689
    # iri: https://onerecord.iata.org/ns/cargo#upid
    upid: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#upid")