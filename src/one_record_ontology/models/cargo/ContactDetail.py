from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.ContactDetailType import ContactDetailType


class ContactDetail(BaseModel):
    # label: contactDetailType
    # comment: Type of the contact details, e.g. Phone number, Mail address
    # iri: https://onerecord.iata.org/ns/cargo#contactDetailType
    contactDetailType: Optional[ContactDetailType] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contactDetailType",
    )
    # label: textualValue
    # comment: Textual value filled on use context (eg. characteristic colour, contactDetail mail address, etc.)
    # iri: https://onerecord.iata.org/ns/cargo#textualValue
    textualValue: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualValue",
    )
