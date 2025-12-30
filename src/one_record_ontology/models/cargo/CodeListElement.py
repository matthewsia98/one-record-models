from typing import Optional

from pydantic import BaseModel, Field


class CodeListElement(BaseModel):
    # label: code
    # comment: Code or short version of a code, for example "CH" for Switzerland when referring to the UN/LOCODE code list
    # iri: https://onerecord.iata.org/ns/cargo#code
    code: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#code"
    )
    # label: codeDescription
    # comment: Description or long version of the code, for example "Switzerland" for Switzerland when referring to the UN/LOCODE code list
    # iri: https://onerecord.iata.org/ns/cargo#codeDescription
    codeDescription: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeDescription",
    )
    # label: codeLevel
    # comment: Integer indicating the level of a code if a codelists is hierarchical, for example HS-Codes
    # iri: https://onerecord.iata.org/ns/cargo#codeLevel
    codeLevel: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeLevel",
    )
    # label: codeListName
    # comment: Official name of the code list without version number when direct reference is not possible, for example "UN/LOCODE" when referring to the UN/LOCODE code list
    # iri: https://onerecord.iata.org/ns/cargo#codeListName
    codeListName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeListName",
    )
    # label: codeListReference
    # comment: URL to access the code list the code is taken from, for example "https://unece.org/trade/cefact/unlocode-code-list-country-and-territory" for UN/LOCODE.
    # iri: https://onerecord.iata.org/ns/cargo#codeListReference
    codeListReference: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeListReference",
    )
    # label: codeListVersion
    # comment: Version of the code list, for example "223-1" for UN/LOCODE. Used if the property codeListName is used or the version is not apparent from the resource referred to in property codeListReference.
    # iri: https://onerecord.iata.org/ns/cargo#codeListVersion
    codeListVersion: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#codeListVersion",
    )
