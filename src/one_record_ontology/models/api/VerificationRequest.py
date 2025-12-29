from one_record_ontology.models.api.Verification import Verification
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.api.ActionRequest import ActionRequest
class VerificationRequest(ActionRequest):
    # label: has Verification
    # comment: Links to the Verification class
    # iri: https://onerecord.iata.org/ns/api#hasVerification
    hasVerification: Verification = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasVerification")