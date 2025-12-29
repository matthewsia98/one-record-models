from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
class Address(BaseModel):
    # label: addressCode
    # comment: Address identifier using special coding systems e.g. US CBP FIRMS code
    # iri: https://onerecord.iata.org/ns/cargo#addressCode
    addressCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#addressCode")
    # label: cityCode
    # comment: UN/LOCODE city code (5 letter) or IATA city code (3 letter)
    # iri: https://onerecord.iata.org/ns/cargo#cityCode
    cityCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#cityCode")
    # label: country
    # comment: Country details. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#country
    country: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#country")
    # label: postalCode
    # comment: Postal / ZIP code
    # iri: https://onerecord.iata.org/ns/cargo#postalCode
    postalCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#postalCode")
    # label: regionCode
    # comment: Region/ State / Department. Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#regionCode
    regionCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#regionCode")
    # label: cityName
    # comment: String holding a city name
    # iri: https://onerecord.iata.org/ns/cargo#cityName
    cityName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#cityName")
    # label: postOfficeBox
    # comment: Post Office box number / code
    # iri: https://onerecord.iata.org/ns/cargo#postOfficeBox
    postOfficeBox: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#postOfficeBox")
    # label: streetAddressLines
    # comment: Street address including street name, street number, building number, apartment etc
    # iri: https://onerecord.iata.org/ns/cargo#streetAddressLines
    streetAddressLines: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#streetAddressLines")
    # label: textualPostCode
    # comment: Postal / ZIP code
    # iri: https://onerecord.iata.org/ns/cargo#textualPostCode
    textualPostCode: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#textualPostCode")