from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Ranges(BaseModel):
    # label: rateClassCode
    # comment: Rate class code e.g. Q. Refer to CXML Code List 1.4 Rate Class Codes
    # iri: https://onerecord.iata.org/ns/cargo#rateClassCode
    rateClassCode: List[RateClassCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#rateClassCode")
    # label: uldRateClassType
    # comment: ULD Rate information - ULD Rate Class Type
    # iri: https://onerecord.iata.org/ns/cargo#uldRateClassType
    uldRateClassType: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldRateClassType")
    # label: maximumQuantity
    # comment: Maximum quantity
    # iri: https://onerecord.iata.org/ns/cargo#maximumQuantity
    maximumQuantity: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#maximumQuantity")
    # label: minimumQuantity
    # comment: Minimum quantity
    # iri: https://onerecord.iata.org/ns/cargo#minimumQuantity
    minimumQuantity: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#minimumQuantity")
    # label: unitBasis
    # comment: Specific commodity code linked to commodity
    # iri: https://onerecord.iata.org/ns/cargo#unitBasis
    unitBasis: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#unitBasis")