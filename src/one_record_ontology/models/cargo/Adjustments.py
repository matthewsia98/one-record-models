from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Adjustments(BaseModel):
    # label: correctionNumber
    # comment: Number of the adjustment
    # iri: https://onerecord.iata.org/ns/cargo#correctionNumber
    correctionNumber: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#correctionNumber")
    # label: correctionSerialNumber
    # comment: Serial Number of the correction
    # iri: https://onerecord.iata.org/ns/cargo#correctionSerialNumber
    correctionSerialNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#correctionSerialNumber")
    # label: reasonsForAdjustments
    # comment: A free text for user to include a reason for correction
    # iri: https://onerecord.iata.org/ns/cargo#reasonsForAdjustments
    reasonsForAdjustments: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#reasonsForAdjustments")