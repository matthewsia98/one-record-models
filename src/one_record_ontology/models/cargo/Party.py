from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Party(BaseModel):
    # label: accountNumbers
    # comment: Information about account numbers
    # iri: https://onerecord.iata.org/ns/cargo#accountNumbers
    accountNumbers: List[AccountNumber] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#accountNumbers")
    # label: otherIdentifiers
    # comment: Details about any other identifier, depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#otherIdentifiers
    otherIdentifiers: List[OtherIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#otherIdentifiers")
    # label: partyDetails
    # comment: Reference to the Agent described by the role of the Party
    # iri: https://onerecord.iata.org/ns/cargo#partyDetails
    partyDetails: List[LogisticsAgent] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#partyDetails")
    # label: partyRole
    # comment: Role fo the Company in the context. Can refer to Code List 1.36 in the CXML Toolkit
    # iri: https://onerecord.iata.org/ns/cargo#partyRole
    partyRole: List[ParticipantIdentifier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#partyRole")