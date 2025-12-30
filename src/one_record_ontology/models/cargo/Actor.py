from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.LogisticsAgent import LogisticsAgent
from one_record_ontology.models.cargo.Organization import Organization


class Actor(LogisticsAgent):
    # label: associatedOrganization
    # comment: Reference to the Organization the Actor is associated with
    # iri: https://onerecord.iata.org/ns/cargo#associatedOrganization
    associatedOrganization: Optional[Organization] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#associatedOrganization",
    )
