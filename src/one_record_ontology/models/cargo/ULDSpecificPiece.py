from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.PieceGroup import PieceGroup


class ULDSpecificPiece(PieceGroup):
    # label: uldContourCode
    # comment: Contour code as per IATA ULD Regulation
    # iri: https://onerecord.iata.org/ns/cargo#uldContourCode
    uldContourCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldContourCode",
    )
    # label: uldType
    # comment: Type of ULD as per IATA ULD Regulation
    # iri: https://onerecord.iata.org/ns/cargo#uldType
    uldType: Optional[CodeListElement] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#uldType"
    )
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: Optional[int] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#slac"
    )
    # label: uldSerialNumber
    # comment: Serial number that allows to uniquely identify the ULD
    # iri: https://onerecord.iata.org/ns/cargo#uldSerialNumber
    uldSerialNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldSerialNumber",
    )
