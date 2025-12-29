from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PhysicalLogisticsObject import PhysicalLogisticsObject
class Item(PhysicalLogisticsObject):
    # label: dimensions
    # comment: Dimensions details
    # iri: https://onerecord.iata.org/ns/cargo#dimensions
    dimensions: List[Dimensions] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#dimensions")
    # label: inPiece
    # comment: Reference to the Piece this Item or Piece is contained in
    # iri: https://onerecord.iata.org/ns/cargo#inPiece
    inPiece: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#inPiece")
    # label: itemQuantity
    # comment: Quantity of the item when applicable, with associated units of measure
    # iri: https://onerecord.iata.org/ns/cargo#itemQuantity
    itemQuantity: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#itemQuantity")
    # label: ofProduct
    # comment: Reference to the Product describing the Item
    # iri: https://onerecord.iata.org/ns/cargo#ofProduct
    ofProduct: List[Product] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ofProduct")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: productionCountry
    # comment: Production country details. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#productionCountry
    productionCountry: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#productionCountry")
    # label: targetCountry
    # comment: Item target country. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#targetCountry
    targetCountry: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#targetCountry")
    # label: unitPrice
    # comment: Product price per unit in the base
    # iri: https://onerecord.iata.org/ns/cargo#unitPrice
    unitPrice: List[CurrencyValue] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#unitPrice")
    # label: weight
    # comment: Weight of the item
    # iri: https://onerecord.iata.org/ns/cargo#weight
    weight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#weight")
    # label: batchNumber
    # comment: Production batch number / reference
    # iri: https://onerecord.iata.org/ns/cargo#batchNumber
    batchNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#batchNumber")
    # label: expiryDate
    # comment: Product expiry date - e.g. for perishables goods or goods with programmed obsolescence
    # iri: https://onerecord.iata.org/ns/cargo#expiryDate
    expiryDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#expiryDate")
    # label: lotNumber
    # comment: Production lot number / reference
    # iri: https://onerecord.iata.org/ns/cargo#lotNumber
    lotNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#lotNumber")
    # label: productionDate
    # comment: Production date
    # iri: https://onerecord.iata.org/ns/cargo#productionDate
    productionDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#productionDate")
    # label: quantityForUnitPrice
    # comment: Product quantity for unit price - e.g. 12 (eggs for one USD 1)
    # iri: https://onerecord.iata.org/ns/cargo#quantityForUnitPrice
    quantityForUnitPrice: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#quantityForUnitPrice")