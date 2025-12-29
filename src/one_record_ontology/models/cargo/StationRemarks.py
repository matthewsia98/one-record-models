from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class StationRemarks(BaseModel):
    # label: station
    # comment: Reference to the station (Airport), mandatory 
    # iri: https://onerecord.iata.org/ns/cargo#station
    station: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#station")
    # label: remarksText
    # comment: Details of the remarks, mandatory
    # iri: https://onerecord.iata.org/ns/cargo#remarksText
    remarksText: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#remarksText")