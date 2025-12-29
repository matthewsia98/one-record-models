from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class CurrencyValue(BaseModel):
    # label: currencyUnit
    # comment: Information about the currency used in a CurrencyValue. Create an instance of CurrencyCode based on ISO 4217
    # iri: https://onerecord.iata.org/ns/cargo#currencyUnit
    currencyUnit: List[CurrencyCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#currencyUnit")
    # label: numericalValue
    # comment: Numerical value
    # iri: https://onerecord.iata.org/ns/cargo#numericalValue
    numericalValue: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue")