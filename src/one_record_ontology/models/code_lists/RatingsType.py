from enum import Enum

from rdflib import URIRef


class RatingsType(str, Enum):
    """
    label: RatingsType
    comment: Restricted code list to describe whether a rating is Face, Published or Actual
    """

    # label: A
    # comment: Actual
    A = URIRef("https://onerecord.iata.org/ns/code-lists/RatingsType#A")
    # label: C
    # comment: Published
    C = URIRef("https://onerecord.iata.org/ns/code-lists/RatingsType#C")
    # label: F
    # comment: Face
    F = URIRef("https://onerecord.iata.org/ns/code-lists/RatingsType#F")
