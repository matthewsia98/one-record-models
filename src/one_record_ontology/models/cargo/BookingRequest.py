from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class BookingRequest(LogisticsObject):
    # label: booking
    # comment: Reference to the Booking
    # iri: https://onerecord.iata.org/ns/cargo#booking
    booking: List[Booking] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#booking")
    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOption
    forBookingOption: List[BookingOption] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption")
    # label: waybillNumber
    # comment: House or Master Waybill unique identifier
    # iri: https://onerecord.iata.org/ns/cargo#waybillNumber
    waybillNumber: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillNumber")
    # label: waybillPrefix
    # comment: Prefix used for the Waybill Number. Refer to IATA Airlines Codes
    # iri: https://onerecord.iata.org/ns/cargo#waybillPrefix
    waybillPrefix: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#waybillPrefix")