from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PhysicalLogisticsObject import PhysicalLogisticsObject
class LoadingUnit(PhysicalLogisticsObject):
    # label: inUnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#inUnitComposition
    inUnitComposition: List[UnitComposition] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#inUnitComposition")
    # label: tareWeight
    # comment: Tare weight of the empty ULD
    # iri: https://onerecord.iata.org/ns/cargo#tareWeight
    tareWeight: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#tareWeight")
    # label: remarks
    # comment: Remarks or Supplement Information
    # iri: https://onerecord.iata.org/ns/cargo#remarks
    remarks: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#remarks")