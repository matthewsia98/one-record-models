from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Actor import Actor
from one_record_ontology.models.cargo.CheckTemplate import CheckTemplate
from one_record_ontology.models.cargo.CheckTotalResult import CheckTotalResult
from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject


class Check(LogisticsAction):
    # label: checkTotalResult
    # comment: Reference to the result of the Check
    # iri: https://onerecord.iata.org/ns/cargo#checkTotalResult
    checkTotalResult: Optional[CheckTotalResult] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkTotalResult",
    )
    # label: checkedObject
    # comment: Reference to the checked Object
    # iri: https://onerecord.iata.org/ns/cargo#checkedObject
    checkedObject: Optional[LogisticsObject] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkedObject",
    )
    # label: checker
    # comment: Reference to the Actor performing the Check
    # iri: https://onerecord.iata.org/ns/cargo#checker
    checker: Optional[Actor] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#checker"
    )
    # label: usedTemplate
    # comment: Reference to the Template used in the Check
    # iri: https://onerecord.iata.org/ns/cargo#usedTemplate
    usedTemplate: Optional[CheckTemplate] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#usedTemplate",
    )
