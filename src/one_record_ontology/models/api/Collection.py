from typing import List

from one_record_ontology.models.api.Any import Any
from pydantic import BaseModel, Field


class Collection(BaseModel):
    # label: has Item
    # comment: Item that is contained in a collection
    # iri: https://onerecord.iata.org/ns/api#hasItem
    hasItem: List[Any] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/api#hasItem",
    )
    # label: Total items
    # comment: The number of total items contained in a collection
    # iri: https://onerecord.iata.org/ns/api#hasTotalItems
    hasTotalItems: int = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasTotalItems"
    )
