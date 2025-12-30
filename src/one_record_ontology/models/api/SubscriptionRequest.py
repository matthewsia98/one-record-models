from pydantic import Field

from one_record_ontology.models.api.ActionRequest import ActionRequest
from one_record_ontology.models.api.Subscription import Subscription


class SubscriptionRequest(ActionRequest):
    # label: has Subscription
    # comment: Link to the requestors Subscription object with all subscription information
    # iri: https://onerecord.iata.org/ns/api#hasSubscription
    hasSubscription: Subscription = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSubscription"
    )
