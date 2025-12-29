from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Characteristic(BaseModel):
    # label: characteristicType
    # comment: Product characteristics code - e.g. CLR - Color. Not restricted to a list.
    # iri: https://onerecord.iata.org/ns/cargo#characteristicType
    characteristicType: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#characteristicType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")