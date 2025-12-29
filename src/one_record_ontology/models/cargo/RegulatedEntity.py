from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class RegulatedEntity(BaseModel):
    # label: owningOrganization
    # comment: Reference to the Organization for which the RegulatedEntity information is valid
    # iri: https://onerecord.iata.org/ns/cargo#owningOrganization
    owningOrganization: List[Organization] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#owningOrganization")
    # label: regulatedEntityCategory
    # comment: Category code of the Regulated Entity
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityCategory
    regulatedEntityCategory: List[RegulatedEntityCategoryCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityCategory")
    # label: regulatedEntityExpiryDate
    # comment: Expiry date 4 digits month/year
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityExpiryDate
    regulatedEntityExpiryDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityExpiryDate")
    # label: regulatedEntityIdentifier
    # comment: Regulated entity identifier as per IATA e-CSD/CSD Resolution 65
    # iri: https://onerecord.iata.org/ns/cargo#regulatedEntityIdentifier
    regulatedEntityIdentifier: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#regulatedEntityIdentifier")