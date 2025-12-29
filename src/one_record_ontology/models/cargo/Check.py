from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
class Check(LogisticsAction):
    # label: checkTotalResult
    # comment: Reference to the result of the Check
    # iri: https://onerecord.iata.org/ns/cargo#checkTotalResult
    checkTotalResult: List[CheckTotalResult] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checkTotalResult")
    # label: checkedObject
    # comment: Reference to the checked Object
    # iri: https://onerecord.iata.org/ns/cargo#checkedObject
    checkedObject: List[LogisticsObject] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checkedObject")
    # label: checker
    # comment: Reference to the Actor performing the Check
    # iri: https://onerecord.iata.org/ns/cargo#checker
    checker: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checker")
    # label: usedTemplate
    # comment: Reference to the Template used in the Check
    # iri: https://onerecord.iata.org/ns/cargo#usedTemplate
    usedTemplate: List[CheckTemplate] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#usedTemplate")