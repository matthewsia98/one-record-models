from enum import Enum

from rdflib import URIRef


class PackagingDangerLevelCode(str, Enum):
    """
    label: PackagingDangerLevelCode
    comment: Restricted code lists for indication of the relative degree of danger presented by substances within a class or division
    """

    # label: I
    # comment: High danger
    I = URIRef("https://onerecord.iata.org/ns/code-lists/PackagingDangerLevelCode#I")
    # label: II
    # comment: Medium danger
    II = URIRef("https://onerecord.iata.org/ns/code-lists/PackagingDangerLevelCode#II")
    # label: III
    # comment: Low danger
    III = URIRef(
        "https://onerecord.iata.org/ns/code-lists/PackagingDangerLevelCode#III"
    )
