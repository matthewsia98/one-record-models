from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class VolumetricWeight(BaseModel):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight")
    # label: conversionFactor
    # comment: Volume to weight conversion factor
    # iri: https://onerecord.iata.org/ns/cargo#conversionFactor
    conversionFactor: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor")