from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.CodeListElement import CodeListElement
class ChargeCode(CodeListElement):
    ...