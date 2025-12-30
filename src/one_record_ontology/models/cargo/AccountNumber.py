from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.AccountType import AccountType


class AccountNumber(BaseModel):
    # label: accountNumberType
    # comment: Type of the account of the account number
    # iri: https://onerecord.iata.org/ns/cargo#accountNumberType
    accountNumberType: Optional[AccountType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#accountNumberType",
    )
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
    )
