from typing import Optional

from pydantic import BaseModel, Field

from one_record_ontology.models.code_lists.CurrencyCode import CurrencyCode
from one_record_ontology.models.code_lists.DimensionsUnitCode import DimensionsUnitCode
from one_record_ontology.models.code_lists.TemperatureUnitCode import (
    TemperatureUnitCode,
)
from one_record_ontology.models.code_lists.VolumeUnitCode import VolumeUnitCode
from one_record_ontology.models.code_lists.WeightUnitCode import WeightUnitCode


class UnitsPreference(BaseModel):
    # label: currency
    # comment: Preferred unit for currency
    # iri: https://onerecord.iata.org/ns/cargo#currency
    currency: Optional[CurrencyCode] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#currency"
    )
    # label: dimensionsUnit
    # comment: Preferred unit for measurement and dimensions
    # iri: https://onerecord.iata.org/ns/cargo#dimensionsUnit
    dimensionsUnit: Optional[DimensionsUnitCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#dimensionsUnit",
    )
    # label: temperatureUnit
    # comment: Preferred unit for temperature
    # iri: https://onerecord.iata.org/ns/cargo#temperatureUnit
    temperatureUnit: Optional[TemperatureUnitCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureUnit",
    )
    # label: volumeUnit
    # comment: Preferred unit for volume
    # iri: https://onerecord.iata.org/ns/cargo#volumeUnit
    volumeUnit: Optional[VolumeUnitCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#volumeUnit",
    )
    # label: weightUnit
    # comment: Preferred unit for weight
    # iri: https://onerecord.iata.org/ns/cargo#weightUnit
    weightUnit: Optional[WeightUnitCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#weightUnit",
    )
