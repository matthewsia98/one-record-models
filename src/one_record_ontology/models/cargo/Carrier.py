from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Company import Company


class Carrier(Company):
    # label: airlineCode
    # comment: IATA two-character airline code
    # iri: https://onerecord.iata.org/ns/cargo#airlineCode
    airlineCode: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#airlineCode",
    )
    # label: prefix
    # comment: IATA three-numeric airline prefix number
    # iri: https://onerecord.iata.org/ns/cargo#prefix
    prefix: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#prefix"
    )
