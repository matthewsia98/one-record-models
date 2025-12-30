from pydantic import Field

from one_record_ontology.models.api.ActionRequest import ActionRequest
from one_record_ontology.models.api.Verification import Verification


class VerificationRequest(ActionRequest):
    # label: has Verification
    # comment: Links to the Verification class
    # iri: https://onerecord.iata.org/ns/api#hasVerification
    hasVerification: Verification = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasVerification"
    )
