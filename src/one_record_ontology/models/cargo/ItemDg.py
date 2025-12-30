from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.Item import Item
from one_record_ontology.models.cargo.Person import Person
from one_record_ontology.models.cargo.Value import Value


class ItemDg(Item):
    # label: emergencyContact
    # comment: Contains the Emergency contact name (e.g. the name of the agency) and phone number (min required)
    # iri: https://onerecord.iata.org/ns/cargo#emergencyContact
    emergencyContact: Optional[Person] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#emergencyContact",
    )
    # label: netWeightMeasure
    # comment: The total net weight of dangerous goods transported of this line item. For air transport the value must be the volume or mass in each package.
    # iri: https://onerecord.iata.org/ns/cargo#netWeightMeasure
    netWeightMeasure: Optional[Value] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#netWeightMeasure",
    )
    # label: reportableQuantity
    # comment: Reportable quantities, To and from the USA only
    # iri: https://onerecord.iata.org/ns/cargo#reportableQuantity
    reportableQuantity: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#reportableQuantity",
    )
    # label: supplementaryInfoPrefix
    # comment: Additional information that may be added in addition to the proper shipping name to more fully describe the goods or to identify a particular condition
    # iri: https://onerecord.iata.org/ns/cargo#supplementaryInfoPrefix
    supplementaryInfoPrefix: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#supplementaryInfoPrefix",
    )
    # label: supplementaryInfoSuffix
    # comment: Additional information that may be added in addition to the proper shipping to more fully describe the goods or to identify a particular condition
    # iri: https://onerecord.iata.org/ns/cargo#supplementaryInfoSuffix
    supplementaryInfoSuffix: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#supplementaryInfoSuffix",
    )
