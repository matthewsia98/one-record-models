from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class RATINGSTYPE(DefinedNamespace):
    """
    DESCRIPTION_EDIT_ME_!

    Generated from: SOURCE_RDF_FILE_EDIT_ME_!
    Date: 2025-12-29 02:44:49.989931
    """

    _NS = Namespace("https://onerecord.iata.org/ns/code-lists/RatingsType#")

    _fail = True

    A: URIRef  # Actual
    C: URIRef  # Published
    F: URIRef  # Face
