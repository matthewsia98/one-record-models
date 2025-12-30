from typing import List, Optional

from pydantic import Field

from one_record_ontology.models.cargo.BookingOption import BookingOption
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.cargo.Ratings import Ratings
from one_record_ontology.models.code_lists.ChargeCode import ChargeCode


class Price(LogisticsObject):
    # label: chargeCode
    # comment: Charge code, refer to CargoXML Code List 1.1
    # iri: https://onerecord.iata.org/ns/cargo#chargeCode
    chargeCode: Optional[ChargeCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#chargeCode",
    )
    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOption
    forBookingOption: Optional[BookingOption] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption",
    )
    # label: ratings
    # comment: Rating used for pricing
    # iri: https://onerecord.iata.org/ns/cargo#ratings
    ratings: List[Ratings] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/cargo#ratings",
    )
    # label: grandTotal
    # comment: Total price
    # iri: https://onerecord.iata.org/ns/cargo#grandTotal
    grandTotal: Optional[float] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#grandTotal",
    )
