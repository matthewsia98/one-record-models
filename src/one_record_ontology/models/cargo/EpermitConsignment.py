from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class EpermitConsignment(LogisticsObject):
    # label: consignmentItems
    # comment: Reference to te pieces (Live Animals) of the permit
    # iri: https://onerecord.iata.org/ns/cargo#consignmentItems
    consignmentItems: List[PieceLiveAnimals] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#consignmentItems")
    # label: epermit
    # comment: Reference to the Epermit of the consignment
    # iri: https://onerecord.iata.org/ns/cargo#epermit
    epermit: List[LiveAnimalsEpermit] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#epermit")
    # label: examiningQuantity
    # comment: Quantity measured by the examining authority (box 14)
    # iri: https://onerecord.iata.org/ns/cargo#examiningQuantity
    examiningQuantity: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#examiningQuantity")
    # label: usedToDateQuotaQuantity
    # comment: total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    # iri: https://onerecord.iata.org/ns/cargo#usedToDateQuotaQuantity
    usedToDateQuotaQuantity: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#usedToDateQuotaQuantity")