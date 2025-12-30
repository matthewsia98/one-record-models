from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.LiveAnimalsEpermit import LiveAnimalsEpermit
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.PieceLiveAnimals import PieceLiveAnimals
from one_record_ontology.models.cargo.Value import Value


class EpermitConsignment(LogisticsObject):
    # label: consignmentItems
    # comment: Reference to te pieces (Live Animals) of the permit
    # iri: https://onerecord.iata.org/ns/cargo#consignmentItems
    consignmentItems: Optional[PieceLiveAnimals] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#consignmentItems",
    )
    # label: epermit
    # comment: Reference to the Epermit of the consignment
    # iri: https://onerecord.iata.org/ns/cargo#epermit
    epermit: Optional[LiveAnimalsEpermit] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#epermit"
    )
    # label: examiningQuantity
    # comment: Quantity measured by the examining authority (box 14)
    # iri: https://onerecord.iata.org/ns/cargo#examiningQuantity
    examiningQuantity: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#examiningQuantity",
    )
    # label: usedToDateQuotaQuantity
    # comment: total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    # iri: https://onerecord.iata.org/ns/cargo#usedToDateQuotaQuantity
    usedToDateQuotaQuantity: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#usedToDateQuotaQuantity",
    )
