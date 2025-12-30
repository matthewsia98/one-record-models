from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.BookingOptionRequest import BookingOptionRequest
from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.CustomsInformation import CustomsInformation
from one_record_ontology.models.cargo.Dimensions import Dimensions
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.PieceGroup import PieceGroup
from one_record_ontology.models.cargo.TemperatureInstructions import (
    TemperatureInstructions,
)
from one_record_ontology.models.cargo.Value import Value
from one_record_ontology.models.code_lists.CommodityCode import CommodityCode
from one_record_ontology.models.code_lists.DensityGroupCode import DensityGroupCode
from one_record_ontology.models.code_lists.SpecialHandlingCode import (
    SpecialHandlingCode,
)


class BookingShipment(LogisticsObject):
    # label: chargeableWeight
    # comment: Chargeable weight
    # iri: https://onerecord.iata.org/ns/cargo#chargeableWeight
    chargeableWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeableWeight",
    )
    # label: customsInformation
    # comment: Customs details
    # iri: https://onerecord.iata.org/ns/cargo#customsInformation
    customsInformation: List[CustomsInformation] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#customsInformation",
    )
    # label: densityGroupCode
    # comment: Density Group Code as defined in cXML code list 2
    # iri: https://onerecord.iata.org/ns/cargo#densityGroupCode
    densityGroupCode: Optional[DensityGroupCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#densityGroupCode",
    )
    # label: expectedCommodity
    # comment: Expected commodity of the shipment as per Commodity Code list. Either this or expected HS code required
    # iri: https://onerecord.iata.org/ns/cargo#expectedCommodity
    expectedCommodity: Optional[CommodityCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#expectedCommodity",
    )
    # label: expectedHScode
    # comment: Expected commodity of the shipment as per HS code (at least 6 digits). Either this or expectedCommodityCode required
    # iri: https://onerecord.iata.org/ns/cargo#expectedHScode
    expectedHScode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#expectedHScode",
    )
    # label: forBookingOptionRequest
    # comment: Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOptionRequest
    forBookingOptionRequest: Optional[BookingOptionRequest] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOptionRequest",
    )
    # label: pieceGroups
    # comment: Reference to the Piece groups of the shipment
    # iri: https://onerecord.iata.org/ns/cargo#pieceGroups
    pieceGroups: List[PieceGroup] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#pieceGroups",
    )
    # label: specialHandlingCodes
    # comment: Three-letter special handling code (SPH)
    # iri: https://onerecord.iata.org/ns/cargo#specialHandlingCodes
    specialHandlingCodes: List[SpecialHandlingCode] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialHandlingCodes",
    )
    # label: temperatureInstructions
    # comment: Temperature instructions if a specific range
    # iri: https://onerecord.iata.org/ns/cargo#temperatureInstructions
    temperatureInstructions: Optional[TemperatureInstructions] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#temperatureInstructions",
    )
    # label: totalDimensions
    # comment: Dimensions of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalDimensions
    totalDimensions: Optional[Dimensions] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalDimensions",
    )
    # label: totalGrossWeight
    # comment: Total gross weight of the whole shipment
    # iri: https://onerecord.iata.org/ns/cargo#totalGrossWeight
    totalGrossWeight: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#totalGrossWeight",
    )
    # label: consolidationIndicator
    # comment: Indication if the shipment is a consolidation
    # iri: https://onerecord.iata.org/ns/cargo#consolidationIndicator
    consolidationIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#consolidationIndicator",
    )
    # label: specialServiceRequests
    # comment: Special service requests
    # iri: https://onerecord.iata.org/ns/cargo#specialServiceRequests
    specialServiceRequests: List[str] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialServiceRequests",
    )
    # label: textualHandlingInstructions
    # comment: Strings to provide free text handling instructions such as SSR and OSI
    # iri: https://onerecord.iata.org/ns/cargo#textualHandlingInstructions
    textualHandlingInstructions: List[str] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#textualHandlingInstructions",
    )
