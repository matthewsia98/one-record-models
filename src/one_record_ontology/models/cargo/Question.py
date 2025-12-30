from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Answer import Answer
from one_record_ontology.models.cargo.CheckTemplate import CheckTemplate
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject


class Question(LogisticsObject):
    # label: answer
    # comment: Reference to the Answer to the Question
    # iri: https://onerecord.iata.org/ns/cargo#answer
    answer: Optional[Answer] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#answer"
    )
    # label: checkTemplate
    # comment: Reference to the CheckTemplate the Question is from
    # iri: https://onerecord.iata.org/ns/cargo#checkTemplate
    checkTemplate: Optional[CheckTemplate] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#checkTemplate",
    )
    # label: answerOptionsText
    # comment: Text restrictions to the Answer
    # iri: https://onerecord.iata.org/ns/cargo#answerOptionsText
    answerOptionsText: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsText",
    )
    # label: answerOptionsValue
    # comment: Value restrictions to the answer
    # iri: https://onerecord.iata.org/ns/cargo#answerOptionsValue
    answerOptionsValue: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsValue",
    )
    # label: longText
    # comment: Long text of the question
    # iri: https://onerecord.iata.org/ns/cargo#longText
    longText: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#longText"
    )
    # label: questionNumber
    # comment: Number of the Question within the template (alphanumeric)
    # iri: https://onerecord.iata.org/ns/cargo#questionNumber
    questionNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#questionNumber",
    )
    # label: questionSection
    # comment: Section of the CheckTemplate this Question is part of
    # iri: https://onerecord.iata.org/ns/cargo#questionSection
    questionSection: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#questionSection",
    )
    # label: shortText
    # comment: Short text of the Question
    # iri: https://onerecord.iata.org/ns/cargo#shortText
    shortText: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#shortText",
    )
