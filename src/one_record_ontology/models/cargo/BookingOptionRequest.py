from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class BookingOptionRequest(LogisticsObject):
    # label: bookingOptions
    # comment: Reference to all Booking Options
    # iri: https://onerecord.iata.org/ns/cargo#bookingOptions
    bookingOptions: List[BookingOption] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingOptions")
    # label: bookingPreference
    # comment: Reference to the Booking preferences
    # iri: https://onerecord.iata.org/ns/cargo#bookingPreference
    bookingPreference: List[BookingPreferences] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingPreference")
    # label: bookingShipmentDetails
    # comment: Reference to the BookingShipment if required
    # iri: https://onerecord.iata.org/ns/cargo#bookingShipmentDetails
    bookingShipmentDetails: List[BookingShipment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingShipmentDetails")
    # label: bookingToUpdate
    # comment: Reference to the Booking to update
    # iri: https://onerecord.iata.org/ns/cargo#bookingToUpdate
    bookingToUpdate: List[Booking] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#bookingToUpdate")
    # label: carrierProduct
    # comment: Reference to the Carrier product if known
    # iri: https://onerecord.iata.org/ns/cargo#carrierProduct
    carrierProduct: List[CarrierProduct] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#carrierProduct")
    # label: involvedParties
    # comment: Information about other Parties involved depending on the context of use
    # iri: https://onerecord.iata.org/ns/cargo#involvedParties
    involvedParties: List[Party] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#involvedParties")
    # label: timePreferences
    # comment: Schedule preferences of the request
    # iri: https://onerecord.iata.org/ns/cargo#timePreferences
    timePreferences: List[BookingTimes] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#timePreferences")
    # label: transportLegs
    # comment: Reference to the Transport Legs of the proposed routing
    # iri: https://onerecord.iata.org/ns/cargo#transportLegs
    transportLegs: List[TransportLegs] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportLegs")
    # label: unitsPreference
    # comment: Reference to unit preferences of the request (e.g. kg or cm)
    # iri: https://onerecord.iata.org/ns/cargo#unitsPreference
    unitsPreference: List[UnitsPreference] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#unitsPreference")
    # label: knownShipper
    # comment: Indication if shipper is a Known Shipper as per TSA grant
    # iri: https://onerecord.iata.org/ns/cargo#knownShipper
    knownShipper: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#knownShipper")