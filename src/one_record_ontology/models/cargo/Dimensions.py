from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Dimensions(BaseModel):
    # label: height
    # comment: Height
    # iri: https://onerecord.iata.org/ns/cargo#height
    height: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#height")
    # label: length
    # comment: Length
    # iri: https://onerecord.iata.org/ns/cargo#length
    length: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#length")
    # label: volume
    # comment: Volume
    # iri: https://onerecord.iata.org/ns/cargo#volume
    volume: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#volume")
    # label: width
    # comment: Width
    # iri: https://onerecord.iata.org/ns/cargo#width
    width: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#width")