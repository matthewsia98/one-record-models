from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.code_lists.CurrencyCode import CurrencyCode


class CurrencyValue(BaseModel):
    # label: currencyUnit
    # comment: Information about the currency used in a CurrencyValue. Create an instance of CurrencyCode based on ISO 4217
    # iri: https://onerecord.iata.org/ns/cargo#currencyUnit
    currencyUnit: Optional[CurrencyCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#currencyUnit",
    )
    # label: numericalValue
    # comment: Numerical value
    # iri: https://onerecord.iata.org/ns/cargo#numericalValue
    numericalValue: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#numericalValue",
    )
