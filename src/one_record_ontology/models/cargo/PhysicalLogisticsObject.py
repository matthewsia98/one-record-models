from typing import List

from pydantic import Field

from one_record_ontology.models.cargo.IotDevice import IotDevice
from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject


class PhysicalLogisticsObject(LogisticsObject):
    # label: attachedIotDevices
    # comment: References to all connected IotDevices
    # iri: https://onerecord.iata.org/ns/cargo#attachedIotDevices
    attachedIotDevices: List[IotDevice] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#attachedIotDevices",
    )
    # label: involvedInActions
    # comment: References to the Actions the object is involved in
    # iri: https://onerecord.iata.org/ns/cargo#involvedInActions
    involvedInActions: List[LogisticsAction] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#involvedInActions",
    )
