from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Check import Check
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Person import Person
from one_record_ontology.models.cargo.Value import Value


class CheckTotalResult(LogisticsObject):
    # label: certifiedByActor
    # comment: Reference to the Actor certifying the result of the Check if required
    # iri: https://onerecord.iata.org/ns/cargo#certifiedByActor
    certifiedByActor: Optional[Person] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#certifiedByActor",
    )
    # label: resultOfCheck
    # iri: https://onerecord.iata.org/ns/cargo#resultOfCheck
    resultOfCheck: Optional[Check] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#resultOfCheck",
    )
    # label: resultValue
    # comment: Information about a result Value of any kind of the Check
    # iri: https://onerecord.iata.org/ns/cargo#resultValue
    resultValue: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#resultValue",
    )
    # label: checkRemark
    # comment: Free text remarks to the check result
    # iri: https://onerecord.iata.org/ns/cargo#checkRemark
    checkRemark: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkRemark",
    )
    # label: passed
    # comment: Boolean indicating whether the Check was passed
    # iri: https://onerecord.iata.org/ns/cargo#passed
    passed: Optional[bool] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#passed"
    )
