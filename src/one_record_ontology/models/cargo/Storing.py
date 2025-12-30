from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)
from one_record_ontology.models.cargo.StoringType import StoringType


class Storing(LogisticsAction):
    # label: storedObjects
    # comment: Reference to the Objects being stored in or stored out
    # iri: https://onerecord.iata.org/ns/cargo#storedObjects
    storedObjects: List[PhysicalLogisticsObject] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#storedObjects",
    )
    # label: storingType
    # comment: Enum stating whether the StoringAction describes the store-in or the store-out
    # iri: https://onerecord.iata.org/ns/cargo#storingType
    storingType: Optional[StoringType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#storingType",
    )
    # label: storagePlaceIdentifier
    # comment: Short text stating the exact place of storage
    # iri: https://onerecord.iata.org/ns/cargo#storagePlaceIdentifier
    storagePlaceIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#storagePlaceIdentifier",
    )
