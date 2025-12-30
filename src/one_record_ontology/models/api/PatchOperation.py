from enum import Enum

from rdflib import URIRef


class PatchOperation(str, Enum):
    """
    label: Patch Operation
    """

    # label: ADD
    # comment: Defines a :PatchOperation to be an operation that adds new triples.
    ADD = URIRef("https://onerecord.iata.org/ns/api#ADD")
    # label: DELETE
    DELETE = URIRef("https://onerecord.iata.org/ns/api#DELETE")
