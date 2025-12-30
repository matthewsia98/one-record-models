from enum import Enum

from rdflib import URIRef


class SignatureTypeCode(str, Enum):
    """
    label: SignatureTypeCode
    comment: Restricted code list of governmental action in CITES context
    """

    # label: DETENTION
    # comment: Detention
    DETENTION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#DETENTION"
    )
    # label: FUMIGATION
    # comment: Fumigation
    FUMIGATION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#FUMIGATION"
    )
    # label: INSPECTION
    # comment: Inspection
    INSPECTION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#INSPECTION"
    )
    # label: SECURITY
    # comment: Security
    SECURITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#SECURITY"
    )
