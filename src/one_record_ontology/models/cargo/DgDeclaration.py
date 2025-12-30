from datetime import datetime
from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Location import Location
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Piece import Piece


class DgDeclaration(LogisticsObject):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation",
    )
    # label: declarationPlace
    # comment: Reference to the Location the DgDeclaration was declared at
    # iri: https://onerecord.iata.org/ns/cargo#declarationPlace
    declarationPlace: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#declarationPlace",
    )
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: Optional[Location] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation",
    )
    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForPiece
    issuedForPiece: Optional[Piece] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece",
    )
    # label: aircraftLimitationInformation
    # comment: Contains the Special Handling Code related to the prescribed limitation. Hardcoded to PASSENGER AND CARGO AIRCRAFT or CARGO AIRCRAFT ONLY. This field is mandatory for air (Air)
    # iri: https://onerecord.iata.org/ns/cargo#aircraftLimitationInformation
    aircraftLimitationInformation: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#aircraftLimitationInformation",
    )
    # label: complianceDeclarationText
    # comment: Contains the warning message complying with the regulations text note. This field is mandatory for air (Air)
    # iri: https://onerecord.iata.org/ns/cargo#complianceDeclarationText
    complianceDeclarationText: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#complianceDeclarationText",
    )
    # label: declarationDate
    # comment: Date and time at which the DgDeclaration was declared
    # iri: https://onerecord.iata.org/ns/cargo#declarationDate
    declarationDate: Optional[datetime] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#declarationDate",
    )
    # label: exclusiveUseIndicator
    # comment: Indicates an exclusive use shipment
    # iri: https://onerecord.iata.org/ns/cargo#exclusiveUseIndicator
    exclusiveUseIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#exclusiveUseIndicator",
    )
    # label: handlingInformation
    # comment: Free text. This may include items such as Control temperature for substances stabilized by temperature control, name and telephone number of a responsible person for infectious substances.
    # iri: https://onerecord.iata.org/ns/cargo#handlingInformation
    handlingInformation: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#handlingInformation",
    )
    # label: shipperDeclarationText
    # comment: Contains the shipper's declaration to comply with the regulations text note. Free text . This field is mandatory for air (Air)
    # iri: https://onerecord.iata.org/ns/cargo#shipperDeclarationText
    shipperDeclarationText: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#shipperDeclarationText",
    )
    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    # iri: https://onerecord.iata.org/ns/cargo#shippingRefNo
    shippingRefNo: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo",
    )
