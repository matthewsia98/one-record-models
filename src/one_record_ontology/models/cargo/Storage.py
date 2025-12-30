from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.LogisticsActivity import LogisticsActivity
from one_record_ontology.models.cargo.Storing import Storing


class Storage(LogisticsActivity):
    # label: storingActions
    # comment: References to all StoringActions performed for the Storing Activity
    # iri: https://onerecord.iata.org/ns/cargo#storingActions
    storingActions: List[Storing] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#storingActions",
    )
    # label: storingIdentifier
    # comment: Short text holding the process number if necessary
    # iri: https://onerecord.iata.org/ns/cargo#storingIdentifier
    storingIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#storingIdentifier",
    )
