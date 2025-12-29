from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsActivity import LogisticsActivity
class Storage(LogisticsActivity):
    # label: storingActions
    # comment: References to all StoringActions performed for the Storing Activity
    # iri: https://onerecord.iata.org/ns/cargo#storingActions
    storingActions: List[Storing] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#storingActions")
    # label: storingIdentifier
    # comment: Short text holding the process number if necessary
    # iri: https://onerecord.iata.org/ns/cargo#storingIdentifier
    storingIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#storingIdentifier")