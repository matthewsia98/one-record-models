from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Booking import Booking
from one_record_ontology.models.cargo.BookingOption import BookingOption
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject


class BookingRequest(LogisticsObject):
    # label: booking
    # comment: Reference to the Booking
    # iri: https://onerecord.iata.org/ns/cargo#booking
    booking: Optional[Booking] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#booking"
    )
    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOption
    forBookingOption: Optional[BookingOption] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption",
    )
    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    # iri: https://onerecord.iata.org/ns/cargo#waybillNumber
    waybillNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber",
    )
    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    # iri: https://onerecord.iata.org/ns/cargo#waybillPrefix
    waybillPrefix: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix",
    )
