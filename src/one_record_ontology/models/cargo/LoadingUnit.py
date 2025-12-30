from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)
from one_record_ontology.models.cargo.UnitComposition import UnitComposition
from one_record_ontology.models.cargo.Value import Value


class LoadingUnit(PhysicalLogisticsObject):
    # label: inUnitComposition
    # iri: https://onerecord.iata.org/ns/cargo#inUnitComposition
    inUnitComposition: Optional[UnitComposition] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#inUnitComposition",
    )
    # label: tareWeight
    # comment: Tare weight of the empty ULD
    # iri: https://onerecord.iata.org/ns/cargo#tareWeight
    tareWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#tareWeight",
    )
    # label: remarks
    # comment: Remarks or Supplement Information
    # iri: https://onerecord.iata.org/ns/cargo#remarks
    remarks: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#remarks"
    )
