from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class ContactDetail(BaseModel):
    # label: contactDetailType
    # comment: Type of the contact details, e.g. Phone number, Mail address
    # iri: https://onerecord.iata.org/ns/cargo#contactDetailType
    contactDetailType: List[ContactDetailType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetailType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")