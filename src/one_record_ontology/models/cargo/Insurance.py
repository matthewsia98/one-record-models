from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class Insurance(LogisticsObject):
    # label: coveringOrganization
    # comment: Party covering the insurance 
    # iri: https://onerecord.iata.org/ns/cargo#coveringOrganization
    coveringOrganization: List[Organization] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#coveringOrganization")
    # label: insuredAmount
    # comment: Insured amount - amount covered by the insurance policy
    # iri: https://onerecord.iata.org/ns/cargo#insuredAmount
    insuredAmount: List[CurrencyValue] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#insuredAmount")
    # label: insuredShipments
    # comment: Reference to the shipments insured
    # iri: https://onerecord.iata.org/ns/cargo#insuredShipments
    insuredShipments: List[Shipment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#insuredShipments")