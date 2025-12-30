from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.CodeListElement import CodeListElement


class CarrierProduct(BaseModel):
    # label: productCode
    # comment: Carrier's product code
    # iri: https://onerecord.iata.org/ns/cargo#productCode
    productCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#productCode",
    )
    # label: serviceLevelCode
    # comment: Service level code
    # iri: https://onerecord.iata.org/ns/cargo#serviceLevelCode
    serviceLevelCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceLevelCode",
    )
    # label: productDescription
    # comment: Carrier's product description
    # iri: https://onerecord.iata.org/ns/cargo#productDescription
    productDescription: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#productDescription",
    )
