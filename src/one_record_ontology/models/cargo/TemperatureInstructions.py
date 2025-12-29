from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class TemperatureInstructions(BaseModel):
    # label: maxTemperature
    # comment: Maximum temperature of the range
    # iri: https://onerecord.iata.org/ns/cargo#maxTemperature
    maxTemperature: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#maxTemperature")
    # label: minTemperature
    # comment: Minimum temperature of the range
    # iri: https://onerecord.iata.org/ns/cargo#minTemperature
    minTemperature: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#minTemperature")