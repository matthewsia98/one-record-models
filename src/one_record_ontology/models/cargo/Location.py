from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.Address import Address
from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.Geolocation import Geolocation
from one_record_ontology.models.cargo.LogisticsAction import LogisticsAction
from one_record_ontology.models.cargo.PhysicalLogisticsObject import (
    PhysicalLogisticsObject,
)


class Location(PhysicalLogisticsObject):
    # label: address
    # comment: Address details
    # iri: https://onerecord.iata.org/ns/cargo#address
    address: Optional[Address] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#address"
    )
    # label: geolocation
    # comment: Geolocation details
    # iri: https://onerecord.iata.org/ns/cargo#geolocation
    geolocation: Optional[Geolocation] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#geolocation",
    )
    # label: locationCodes
    # comment: Location code of airport, freight terminal, seaport, rail station. UN/LOCODE city code (5 letter) or IATA airport code (3 letter)
    # iri: https://onerecord.iata.org/ns/cargo#locationCodes
    locationCodes: List[CodeListElement] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationCodes",
    )
    # label: onsiteActions
    # comment: References to the Actions happening at the Location
    # iri: https://onerecord.iata.org/ns/cargo#onsiteActions
    onsiteActions: List[LogisticsAction] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#onsiteActions",
    )
    # comment: Reference to the Location this is a Sublocation of
    # iri: https://onerecord.iata.org/ns/cargo#subLocationOf
    subLocationOf: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#subLocationOf",
    )
    # comment: References to Sublocations that describe the Location in more detail
    # iri: https://onerecord.iata.org/ns/cargo#subLocations
    subLocations: List[Location] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#subLocations",
    )
    # label: locationName
    # comment: Full name of the location
    # iri: https://onerecord.iata.org/ns/cargo#locationName
    locationName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationName",
    )
    # label: locationType
    # comment: Location type - e.g. Airport, Freight terminal, Rail station, Seaport, etc
    # iri: https://onerecord.iata.org/ns/cargo#locationType
    locationType: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#locationType",
    )
