from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class AccountingNote(BaseModel):
    # label: accountingNoteIdentifier
    # comment: String holding accounting information (AWB box 10)
    # iri: https://onerecord.iata.org/ns/cargo#accountingNoteIdentifier
    accountingNoteIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteIdentifier")
    # label: accountingNoteText
    # comment: String holding the identifier in an accounting note (AWB box 10)
    # iri: https://onerecord.iata.org/ns/cargo#accountingNoteText
    accountingNoteText: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteText")