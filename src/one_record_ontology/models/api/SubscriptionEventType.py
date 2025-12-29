from enum import Enum
from rdflib import URIRef
class SubscriptionEventType(str, Enum):
    # label: LOGISTICS_EVENT_RECEIVED
    LOGISTICS_EVENT_RECEIVED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_EVENT_RECEIVED")
    # label: LOGISTICS_OBJECT_CREATED
    LOGISTICS_OBJECT_CREATED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_CREATED")
    # label: LOGISTICS_OBJECT_UPDATED
    LOGISTICS_OBJECT_UPDATED = URIRef("https://onerecord.iata.org/ns/api#LOGISTICS_OBJECT_UPDATED")