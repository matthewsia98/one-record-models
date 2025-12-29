from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class CarrierProduct(BaseModel):
    # label: productCode
    # comment: Carrier's product code
    # iri: https://onerecord.iata.org/ns/cargo#productCode
    productCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#productCode")
    # label: serviceLevelCode
    # comment: Service level code
    # iri: https://onerecord.iata.org/ns/cargo#serviceLevelCode
    serviceLevelCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#serviceLevelCode")
    # label: productDescription
    # comment: Carrier's product description
    # iri: https://onerecord.iata.org/ns/cargo#productDescription
    productDescription: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#productDescription")