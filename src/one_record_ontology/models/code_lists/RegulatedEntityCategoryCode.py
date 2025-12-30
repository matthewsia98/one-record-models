from enum import Enum

from rdflib import URIRef


class RegulatedEntityCategoryCode(str, Enum):
    """
    label: RegulatedEntityCategoryCode
    comment: Full detailed descriptions for RA, KC & AC are contained in Cargo Services Conference Recommended Practice 1630 CARGO SECURITY
    """

    # label: AO
    # comment: Aircraft Operator
    AO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#AO"
    )
    # label: KC
    # comment: Known Consignor (consignor for both passenger and all cargo aircraft only)
    KC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#KC"
    )
    # label: RA
    # comment: Regulated Agent
    RA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#RA"
    )
    # label: RC
    # comment: Regulated Carrier
    RC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#RC"
    )
