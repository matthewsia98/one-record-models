from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class Price(LogisticsObject):
    # label: chargeCode
    # comment: Charge code, refer to CargoXML Code List 1.1
    # iri: https://onerecord.iata.org/ns/cargo#chargeCode
    chargeCode: List[ChargeCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#chargeCode")
    # label: forBookingOption
    # comment: Reference to the BookingOption the LogisticsObject is detailing
    # iri: https://onerecord.iata.org/ns/cargo#forBookingOption
    forBookingOption: List[BookingOption] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forBookingOption")
    # label: ratings
    # comment: Rating used for pricing
    # iri: https://onerecord.iata.org/ns/cargo#ratings
    ratings: List[Ratings] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#ratings")
    # label: grandTotal
    # comment: Total price
    # iri: https://onerecord.iata.org/ns/cargo#grandTotal
    grandTotal: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#grandTotal")