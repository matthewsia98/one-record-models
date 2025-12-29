from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class Answer(LogisticsObject):
    # label: answerActor
    # comment: Reference to the Actor giving the Answer
    # iri: https://onerecord.iata.org/ns/cargo#answerActor
    answerActor: List[Actor] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#answerActor")
    # label: answerValue
    # comment: Information about an answer Value of any kind of the Answer
    # iri: https://onerecord.iata.org/ns/cargo#answerValue
    answerValue: List[Value] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#answerValue")
    # label: givenAtLocation
    # comment: Reference to the Location from which the Question was answered, relevant for split checks with documentary and physical elements
    # iri: https://onerecord.iata.org/ns/cargo#givenAtLocation
    givenAtLocation: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#givenAtLocation")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: question
    # comment: Reference to the Question the Answer is for
    # iri: https://onerecord.iata.org/ns/cargo#question
    question: List[Question] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#question")
    # label: text
    # comment: Text for the Answer
    # iri: https://onerecord.iata.org/ns/cargo#text
    text: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#text")