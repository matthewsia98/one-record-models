from typing import Optional

from pydantic import BaseModel, Field


class AccountingNote(BaseModel):
    # label: accountingNoteIdentifier
    # comment: String holding accounting information (AWB box 10)
    # iri: https://onerecord.iata.org/ns/cargo#accountingNoteIdentifier
    accountingNoteIdentifier: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteIdentifier",
    )
    # label: accountingNoteText
    # comment: String holding the identifier in an accounting note (AWB box 10)
    # iri: https://onerecord.iata.org/ns/cargo#accountingNoteText
    accountingNoteText: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountingNoteText",
    )
