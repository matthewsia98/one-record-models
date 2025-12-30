from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.PieceGroup import PieceGroup


class VolumePieceGroup(PieceGroup):
    # label: stackable
    # comment: Stackable indicator for the pieces (boolean)
    # iri: https://onerecord.iata.org/ns/cargo#stackable
    stackable: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#stackable",
    )
