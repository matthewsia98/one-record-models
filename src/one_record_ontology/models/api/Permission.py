from enum import Enum

from rdflib import URIRef


class Permission(str, Enum):
    """
    label: Permission
    """

    # label: GET_LOGISTICS_EVENT
    # comment: :Permission to get a :LogisticsEvent
    GET_LOGISTICS_EVENT = URIRef(
        "https://onerecord.iata.org/ns/api#GET_LOGISTICS_EVENT"
    )
    # label: GET_LOGISTICS_OBJECT
    # comment: :Permission to get a :LogisticsObject
    GET_LOGISTICS_OBJECT = URIRef(
        "https://onerecord.iata.org/ns/api#GET_LOGISTICS_OBJECT"
    )
    # label: PATCH_LOGISTICS_OBJECT
    PATCH_LOGISTICS_OBJECT = URIRef(
        "https://onerecord.iata.org/ns/api#PATCH_LOGISTICS_OBJECT"
    )
    # label: POST_LOGISTICS_EVENT
    # comment: :Permission to add a logistics event.
    POST_LOGISTICS_EVENT = URIRef(
        "https://onerecord.iata.org/ns/api#POST_LOGISTICS_EVENT"
    )
