from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class UnitsPreference(BaseModel):
    # label: currency
    # comment: Preferred unit for currency
    # iri: https://onerecord.iata.org/ns/cargo#currency
    currency: List[CurrencyCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#currency")
    # label: dimensionsUnit
    # comment: Preferred unit for measurement and dimensions
    # iri: https://onerecord.iata.org/ns/cargo#dimensionsUnit
    dimensionsUnit: List[DimensionsUnitCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#dimensionsUnit")
    # label: temperatureUnit
    # comment: Preferred unit for temperature
    # iri: https://onerecord.iata.org/ns/cargo#temperatureUnit
    temperatureUnit: List[TemperatureUnitCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureUnit")
    # label: volumeUnit
    # comment: Preferred unit for volume
    # iri: https://onerecord.iata.org/ns/cargo#volumeUnit
    volumeUnit: List[VolumeUnitCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#volumeUnit")
    # label: weightUnit
    # comment: Preferred unit for weight
    # iri: https://onerecord.iata.org/ns/cargo#weightUnit
    weightUnit: List[WeightUnitCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#weightUnit")