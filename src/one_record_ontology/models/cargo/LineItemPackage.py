from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class LineItemPackage(BaseModel):
    # label: packageGrossWeight
    # comment: Information about the total weight of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageGrossWeight
    packageGrossWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#packageGrossWeight")
    # label: packageVolume
    # comment: Information about the total volume of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageVolume
    packageVolume: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#packageVolume")
    # label: pieceReferences
    # comment: References to Pieces for which a rate applies
    # iri: https://onerecord.iata.org/ns/cargo#pieceReferences
    pieceReferences: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#pieceReferences")
    # label: packageSlac
    # comment: Integer holding the total slac of a grouping of pieces
    # iri: https://onerecord.iata.org/ns/cargo#packageSlac
    packageSlac: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#packageSlac")