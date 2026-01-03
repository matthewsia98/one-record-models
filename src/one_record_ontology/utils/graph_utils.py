from typing import Optional

from rdflib import RDF, Graph, URIRef
from rdflib.graph import _SubjectType

SubjectType = _SubjectType


def get_root_candidates(g: Graph, type: Optional[URIRef] = None) -> set[SubjectType]:
    if type is None:
        subjects = set(g.subjects())
    else:
        subjects = set(g.subjects(RDF.type, type))

    objects = set(g.objects())

    root_candidates = subjects - objects

    return root_candidates


def get_root_subject(g: Graph, type: Optional[URIRef] = None) -> SubjectType:
    # root_candidates = get_root_candidates(g, type)
    root_candidates = set(g.subjects(RDF.type, type))

    if len(root_candidates) == 0:
        raise ValueError("No root candidate found")

    if len(root_candidates) > 1:
        raise ValueError("Multiple root candidates found")

    return next(iter(root_candidates))
