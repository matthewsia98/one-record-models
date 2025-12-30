from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.cargo.Value import Value


class VolumetricWeight(BaseModel):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight",
    )
    # label: conversionFactor
    # comment: Volume to weight conversion factor
    # iri: https://onerecord.iata.org/ns/cargo#conversionFactor
    conversionFactor: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#conversionFactor",
    )
