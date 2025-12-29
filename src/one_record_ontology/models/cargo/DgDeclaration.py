from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class DgDeclaration(LogisticsObject):
    # label: arrivalLocation
    # comment: Reference to the arrival Location
    # iri: https://onerecord.iata.org/ns/cargo#arrivalLocation
    arrivalLocation: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#arrivalLocation")
    # label: declarationPlace
    # comment: Reference to the Location the DgDeclaration was declared at
    # iri: https://onerecord.iata.org/ns/cargo#declarationPlace
    declarationPlace: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#declarationPlace")
    # label: departureLocation
    # comment: Reference to the departure Location
    # iri: https://onerecord.iata.org/ns/cargo#departureLocation
    departureLocation: List[Location] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#departureLocation")
    # label: issuedForPiece
    # comment: Reference to the Piece the document was issued for
    # iri: https://onerecord.iata.org/ns/cargo#issuedForPiece
    issuedForPiece: List[Piece] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#issuedForPiece")
    # label: aircraftLimitationInformation
    # comment: Contains the Special Handling Code related to the prescribed limitation. Hardcoded to PASSENGER AND CARGO AIRCRAFT or CARGO AIRCRAFT ONLY. This field is mandatory for air (Air) 
    # iri: https://onerecord.iata.org/ns/cargo#aircraftLimitationInformation
    aircraftLimitationInformation: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#aircraftLimitationInformation")
    # label: complianceDeclarationText
    # comment: Contains the warning message complying with the regulations text note. This field is mandatory for air (Air) 
    # iri: https://onerecord.iata.org/ns/cargo#complianceDeclarationText
    complianceDeclarationText: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#complianceDeclarationText")
    # label: declarationDate
    # comment: Date and time at which the DgDeclaration was declared
    # iri: https://onerecord.iata.org/ns/cargo#declarationDate
    declarationDate: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#declarationDate")
    # label: exclusiveUseIndicator
    # comment: Indicates an exclusive use shipment
    # iri: https://onerecord.iata.org/ns/cargo#exclusiveUseIndicator
    exclusiveUseIndicator: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#exclusiveUseIndicator")
    # label: handlingInformation
    # comment: Free text. This may include items such as Control temperature for substances stabilized by temperature control, name and telephone number of a responsible person for infectious substances. 
    # iri: https://onerecord.iata.org/ns/cargo#handlingInformation
    handlingInformation: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#handlingInformation")
    # label: shipperDeclarationText
    # comment: Contains the shipper's declaration to comply with the regulations text note. Free text . This field is mandatory for air (Air)
    # iri: https://onerecord.iata.org/ns/cargo#shipperDeclarationText
    shipperDeclarationText: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#shipperDeclarationText")
    # label: shippingRefNo
    # comment: Optional shipping reference number if any
    # iri: https://onerecord.iata.org/ns/cargo#shippingRefNo
    shippingRefNo: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#shippingRefNo")