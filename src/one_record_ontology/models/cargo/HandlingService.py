from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.LogisticsService import LogisticsService
from one_record_ontology.models.cargo.Party import Party
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)
from one_record_ontology.models.cargo.Waybill import Waybill


class HandlingService(LogisticsService):
    # label: handlingServiceFor
    # iri: https://onerecord.iata.org/ns/cargo#handlingServiceFor
    handlingServiceFor: List[PhysicalLogisticsObject] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#handlingServiceFor",
    )
    # label: serviceForWaybills
    # comment: Reference to the Waybills this service is to be performed for. To be used if a service is to be performed for a specific shipment or set of
    # iri: https://onerecord.iata.org/ns/cargo#serviceForWaybills
    serviceForWaybills: List[Waybill] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceForWaybills",
    )
    # label: serviceProvider
    # comment: Reference to the Party providing the service
    # iri: https://onerecord.iata.org/ns/cargo#serviceProvider
    serviceProvider: Optional[Party] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceProvider",
    )
    # label: serviceRequestor
    # comment: Reference to the Party requesting the service
    # iri: https://onerecord.iata.org/ns/cargo#serviceRequestor
    serviceRequestor: Optional[Party] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceRequestor",
    )
