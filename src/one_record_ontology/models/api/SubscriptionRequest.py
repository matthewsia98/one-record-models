from one_record_ontology.models.api.Subscription import Subscription
from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.api.ActionRequest import ActionRequest
class SubscriptionRequest(ActionRequest):
    # label: has Subscription
    # comment: Link to the requestors Subscription object with all subscription information
    # iri: https://onerecord.iata.org/ns/api#hasSubscription
    hasSubscription: Subscription = Field(serialization_alias="https://onerecord.iata.org/ns/api#hasSubscription")