from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class CheckTotalResult(LogisticsObject):
    # label: certifiedByActor
    # comment: Reference to the Actor certifying the result of the Check if required
    # iri: https://onerecord.iata.org/ns/cargo#certifiedByActor
    certifiedByActor: List[Person] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#certifiedByActor")
    # label: resultOfCheck
    # iri: https://onerecord.iata.org/ns/cargo#resultOfCheck
    resultOfCheck: List[Check] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#resultOfCheck")
    # label: resultValue
    # comment: Information about a result Value of any kind of the Check
    # iri: https://onerecord.iata.org/ns/cargo#resultValue
    resultValue: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#resultValue")
    # label: checkRemark
    # comment: Free text remarks to the check result
    # iri: https://onerecord.iata.org/ns/cargo#checkRemark
    checkRemark: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checkRemark")
    # label: passed
    # comment: Boolean indicating whether the Check was passed
    # iri: https://onerecord.iata.org/ns/cargo#passed
    passed: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#passed")