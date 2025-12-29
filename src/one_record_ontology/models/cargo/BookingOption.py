from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class BookingOption(LogisticsObject):
    # label: bookingTimes
    # comment: Information about the Booking Times of a provided Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#bookingTimes
    bookingTimes: List[BookingTimes] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingTimes")
    # label: carrier
    # comment: Reference to the operating carrier
    # iri: https://onerecord.iata.org/ns/cargo#carrier
    carrier: List[Carrier] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#carrier")
    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    # iri: https://onerecord.iata.org/ns/cargo#carrierProduct
    carrierProduct: List[CarrierProduct] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct")
    # label: forBookingOptionRequest
    # comment: Reference to the BookingOptionRequest the information of the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOptionRequest
    forBookingOptionRequest: List[BookingOptionRequest] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOptionRequest")
    # label: forBookingRequest
    # comment: Reference to the Booking Request the of the Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#forBookingRequest
    forBookingRequest: List[BookingRequest] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingRequest")
    # label: price
    # comment: Price of the Booking (if different from the offer)
    # iri: https://onerecord.iata.org/ns/cargo#price
    price: List[Price] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#price")
    # label: stationRemarks
    # comment: Remarks related to specific stations in the routing (e.g. Embargo in XXX)
    # iri: https://onerecord.iata.org/ns/cargo#stationRemarks
    stationRemarks: List[StationRemarks] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#stationRemarks")
    # label: statusBookingOption
    # comment: Status of the Booking Option
    # iri: https://onerecord.iata.org/ns/cargo#statusBookingOption
    statusBookingOption: List[BookingOptionStatus] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#statusBookingOption")
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs")
    # label: unitsPreference
    # comment: Reference to unit preferences of the request (e.g. kg or cm)
    # iri: https://onerecord.iata.org/ns/cargo#unitsPreference
    unitsPreference: List[UnitsPreference] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#unitsPreference")
    # label: additionalInformation
    # comment: Additional information related to the Booking Option, e.g. sales details
    # iri: https://onerecord.iata.org/ns/cargo#additionalInformation
    additionalInformation: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#additionalInformation")
    # label: alternatives
    # comment: Description of the alternatives proposed that do not match the Booking Option Request
    # iri: https://onerecord.iata.org/ns/cargo#alternatives
    alternatives: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#alternatives")
    # label: offerValidFrom
    # comment: Date and time of beginning of offer validity
    # iri: https://onerecord.iata.org/ns/cargo#offerValidFrom
    offerValidFrom: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidFrom")
    # label: offerValidTo
    # comment: Date and time of end of offer validity
    # iri: https://onerecord.iata.org/ns/cargo#offerValidTo
    offerValidTo: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#offerValidTo")
    # label: requestMatch
    # comment: Indicates if the Booking Option is a match to the Booking Option Request preferences
    # iri: https://onerecord.iata.org/ns/cargo#requestMatch
    requestMatch: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#requestMatch")