from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class OtherIdentifier(BaseModel):
    # label: otherIdentifierType
    # comment: Identifier type or description
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifierType
    otherIdentifierType: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifierType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")