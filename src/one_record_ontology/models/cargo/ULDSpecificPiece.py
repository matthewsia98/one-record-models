from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.PieceGroup import PieceGroup
class ULDSpecificPiece(PieceGroup):
    # label: uldContourCode
    # comment: Contour code as per IATA ULD Regulation
    # iri: https://onerecord.iata.org/ns/cargo#uldContourCode
    uldContourCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldContourCode")
    # label: uldType
    # comment: Type of ULD as per IATA ULD Regulation
    # iri: https://onerecord.iata.org/ns/cargo#uldType
    uldType: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldType")
    # label: slac
    # comment: Shipper's Load And Count  ( total contained piece count as provided by shipper)
    # iri: https://onerecord.iata.org/ns/cargo#slac
    slac: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#slac")
    # label: uldSerialNumber
    # comment: Serial number that allows to uniquely identify the ULD
    # iri: https://onerecord.iata.org/ns/cargo#uldSerialNumber
    uldSerialNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#uldSerialNumber")