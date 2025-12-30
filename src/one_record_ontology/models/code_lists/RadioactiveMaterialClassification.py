from enum import Enum

from rdflib import URIRef


class RadioactiveMaterialClassification(str, Enum):
    """
    label: RadioactiveMaterialClassification
    comment: Restricted code list based on DGR 10.3.3
    """

    # label: LOW_DISPERSIBLE
    # comment: Low Dispersible
    LOW_DISPERSIBLE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RadioactiveMaterialClassification#LOW_DISPERSIBLE"
    )
    # label: PHYSICAL_CHEMICAL_FORM
    # comment: Physical Chemical Form
    PHYSICAL_CHEMICAL_FORM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RadioactiveMaterialClassification#PHYSICAL_CHEMICAL_FORM"
    )
    # label: SPECIAL_FORM
    # comment: Special Form
    SPECIAL_FORM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RadioactiveMaterialClassification#SPECIAL_FORM"
    )
