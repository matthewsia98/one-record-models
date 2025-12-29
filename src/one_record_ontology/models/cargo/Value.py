from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Value(BaseModel):
    # label: unit
    # comment: Unit of measurement as per MeasurementUnitCode codelist. If the code is not present, create an instance of MeasurementUnitCode based on UNECE Rec. 20 Rev. 17e-2021
    # iri: https://onerecord.iata.org/ns/cargo#unit
    unit: List[MeasurementUnitCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#unit")
    # label: numericalValue
    # comment: Numerical value
    # iri: https://onerecord.iata.org/ns/cargo#numericalValue
    numericalValue: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue")