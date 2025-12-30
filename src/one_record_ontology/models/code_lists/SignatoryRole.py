from enum import Enum

from rdflib import URIRef


class SignatoryRole(str, Enum):
    """
    label: SignatoryRole
    comment: Restricted code list indicating the role of the signatory in CITES context
    """

    # label: APPLICANT
    # comment: Applicant
    APPLICANT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#APPLICANT"
    )
    # label: EXAMINING_AUTHORITY
    # comment: Examining Authority
    EXAMINING_AUTHORITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#EXAMINING_AUTHORITY"
    )
    # label: ISSUING_AUTHORITY
    # comment: Issuing Authority
    ISSUING_AUTHORITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#ISSUING_AUTHORITY"
    )
    # label: MANAGEMENT_AUTHORITY
    # comment: Management Authority
    MANAGEMENT_AUTHORITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#MANAGEMENT_AUTHORITY"
    )
    # label: PERMIT_ISSUER
    # comment: Permit Issuer
    PERMIT_ISSUER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#PERMIT_ISSUER"
    )
