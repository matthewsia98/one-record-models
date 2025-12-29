from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Geolocation(BaseModel):
    # label: elevation
    # comment: Elevation from sea level - Change of data type to Value as of ontology v1.1
    # iri: https://onerecord.iata.org/ns/cargo#elevation
    elevation: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#elevation")
    # label: latitude
    # comment: Location latitude decimal
    # iri: https://onerecord.iata.org/ns/cargo#latitude
    latitude: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#latitude")
    # label: longitude
    # comment: Location longitude decimal
    # iri: https://onerecord.iata.org/ns/cargo#longitude
    longitude: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#longitude")