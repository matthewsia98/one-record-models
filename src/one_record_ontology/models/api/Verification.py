from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.api.Error import Error
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Verification(BaseModel):
    # label: has Error
    # comment: Error object(s) if the processing was not successful
    # iri: https://onerecord.iata.org/ns/api#hasError
    hasError: List[Error] = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasError")
    # label: has Logistics Object
    # comment: A reference to a cargo:LogisticsObject.
    # iri: https://onerecord.iata.org/ns/api#hasLogisticsObject
    hasLogisticsObject: LogisticsObject = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasLogisticsObject")
    # label: Revision
    # comment: Revision number of the Logistics Object, starting with 0 for changing the initial revision of a Logistics Object
    # iri: https://onerecord.iata.org/ns/api#hasRevision
    hasRevision: int = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasRevision")