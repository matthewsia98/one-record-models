from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class Question(LogisticsObject):
    # label: answer
    # comment: Reference to the Answer to the Question
    # iri: https://onerecord.iata.org/ns/cargo#answer
    answer: List[Answer] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#answer")
    # label: checkTemplate
    # comment: Reference to the CheckTemplate the Question is from
    # iri: https://onerecord.iata.org/ns/cargo#checkTemplate
    checkTemplate: List[CheckTemplate] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#checkTemplate")
    # label: answerOptionsText
    # comment: Text restrictions to the Answer
    # iri: https://onerecord.iata.org/ns/cargo#answerOptionsText
    answerOptionsText: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsText")
    # label: answerOptionsValue
    # comment: Value restrictions to the answer
    # iri: https://onerecord.iata.org/ns/cargo#answerOptionsValue
    answerOptionsValue: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#answerOptionsValue")
    # label: longText
    # comment: Long text of the question
    # iri: https://onerecord.iata.org/ns/cargo#longText
    longText: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#longText")
    # label: questionNumber
    # comment: Number of the Question within the template (alphanumeric)
    # iri: https://onerecord.iata.org/ns/cargo#questionNumber
    questionNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#questionNumber")
    # label: questionSection
    # comment: Section of the CheckTemplate this Question is part of
    # iri: https://onerecord.iata.org/ns/cargo#questionSection
    questionSection: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#questionSection")
    # label: shortText
    # comment: Short text of the Question
    # iri: https://onerecord.iata.org/ns/cargo#shortText
    shortText: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#shortText")