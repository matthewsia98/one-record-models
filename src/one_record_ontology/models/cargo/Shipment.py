from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class Shipment(LogisticsObject):
    # label: customsInformation
    # comment: Customs details
    # iri: https://onerecord.iata.org/ns/cargo#customsInformation
    customsInformation: List[CustomsInformation] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation")
    # label: incoterms
    # comment: Standard codes as defined by UNCEFACT and ICC that correspond to international rules for the interpretation of the most commonly used trade terms in different countries. UNECE recommendation n. 5 Incoterms 2.
    # iri: https://onerecord.iata.org/ns/cargo#incoterms
    incoterms: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#incoterms")
    # label: insurance
    # comment: Insurance details
    # iri: https://onerecord.iata.org/ns/cargo#insurance
    insurance: List[Insurance] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#insurance")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: pieces
    # comment: References to the Pieces that are part of this Shipment
    # iri: https://onerecord.iata.org/ns/cargo#pieces
    pieces: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieces")
    # label: totalDimensions
    # comment: Dimensions of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalDimensions
    totalDimensions: List[Dimensions] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#totalDimensions")
    # label: totalGrossWeight
    # comment: Total gross weight of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalGrossWeight
    totalGrossWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#totalGrossWeight")
    # label: waybill
    # comment: Reference to the Waybill of the shipment
    # iri: https://onerecord.iata.org/ns/cargo#waybill
    waybill: List[Waybill] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#waybill")
    # label: goodsDescription
    # comment: Description of goods, for the BookingShipment the commodity list defined by Modernizing Cargo Distribution MCD working group can be used as a referential.
    # iri: https://onerecord.iata.org/ns/cargo#goodsDescription
    goodsDescription: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsDescription")
    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    # iri: https://onerecord.iata.org/ns/cargo#textualHandlingInstructions
    textualHandlingInstructions: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions")