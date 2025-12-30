from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Organization import Organization


class Company(Organization):
    # label: iataCargoAgentCode
    # comment: IATA accredited cargo agent 7 digit number
    # iri: https://onerecord.iata.org/ns/cargo#iataCargoAgentCode
    iataCargoAgentCode: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentCode",
    )
    # label: iataCargoAgentLocationIdentifier
    # comment: IATA CASS cargo agent 4 digit branch number / location identifier
    # iri: https://onerecord.iata.org/ns/cargo#iataCargoAgentLocationIdentifier
    iataCargoAgentLocationIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#iataCargoAgentLocationIdentifier",
    )
