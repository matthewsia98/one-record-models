from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class AccountNumber(BaseModel):
    # label: accountNumberType
    # comment: Type of the account of the account number
    # iri: https://onerecord.iata.org/ns/cargo#accountNumberType
    accountNumberType: List[AccountType] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#accountNumberType")
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue")