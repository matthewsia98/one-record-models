from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.CurrencyValue import CurrencyValue
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Organization import Organization
from one_record_ontology.models.cargo.Shipment import Shipment


class Insurance(LogisticsObject):
    # label: coveringOrganization
    # comment: Party covering the insurance
    # iri: https://onerecord.iata.org/ns/cargo#coveringOrganization
    coveringOrganization: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#coveringOrganization",
    )
    # label: insuredAmount
    # comment: Insured amount - amount covered by the insurance policy
    # iri: https://onerecord.iata.org/ns/cargo#insuredAmount
    insuredAmount: Optional[CurrencyValue] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#insuredAmount",
    )
    # label: insuredShipments
    # comment: Reference to the shipments insured
    # iri: https://onerecord.iata.org/ns/cargo#insuredShipments
    insuredShipments: List[Shipment] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#insuredShipments",
    )
