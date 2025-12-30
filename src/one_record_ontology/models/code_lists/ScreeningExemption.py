from enum import Enum

from rdflib import URIRef


class ScreeningExemption(str, Enum):
    """
    label: ScreeningExemption
    comment: Restricted code list corresponding to cXML code list 1.104 Screening Exemptions
    """

    # label: BIOM
    # comment: Bio-Medical Samples
    BIOM = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#BIOM")
    # label: DIPL
    # comment: Diplomatic Bags or Diplomatic Mail
    DIPL = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#DIPL")
    # label: LFSM
    # comment: Life-Saving Materials (Save Human Life)
    LFSM = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#LFSM")
    # label: MAIL
    # comment: Mail
    MAIL = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#MAIL")
    # label: NUCL
    # comment: Nuclear Material
    NUCL = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#NUCL")
    # label: SMUS
    # comment: Small Undersized Shipments
    SMUS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#SMUS")
    # label: TRNS
    # comment: Transfer or Transshipment
    TRNS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#TRNS")
