from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.DgProductRadioactive import DgProductRadioactive
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
from one_record_ontology.models.code_lists.RadioactiveMaterialClassification import (
    RadioactiveMaterialClassification,
)


class DgRadioactiveIsotope(LogisticsObject):
    # label: contentOfDgProductRadioactive
    # comment: Reference to the DgProductRadioactive this Isotope is contained in
    # iri: https://onerecord.iata.org/ns/cargo#contentOfDgProductRadioactive
    contentOfDgProductRadioactive: Optional[DgProductRadioactive] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#contentOfDgProductRadioactive",
    )
    # label: physicalChemicalForm
    # comment: A description of the physical and chemical form of the material.
    # iri: https://onerecord.iata.org/ns/cargo#physicalChemicalForm
    physicalChemicalForm: Optional[RadioactiveMaterialClassification] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#physicalChemicalForm",
    )
    # label: activityLevelMeasure
    # comment: Numeric expression of the activity of a radioactive Item
    # iri: https://onerecord.iata.org/ns/cargo#activityLevelMeasure
    activityLevelMeasure: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#activityLevelMeasure",
    )
    # label: criticalitySafetyIndexNumeric
    # comment: Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI.
    # iri: https://onerecord.iata.org/ns/cargo#criticalitySafetyIndexNumeric
    criticalitySafetyIndexNumeric: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#criticalitySafetyIndexNumeric",
    )
    # label: isotopeId
    # comment: Id of each radionuclide or for mixtures of radionuclides.
    # iri: https://onerecord.iata.org/ns/cargo#isotopeId
    isotopeId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#isotopeId",
    )
    # label: isotopeName
    # comment: The name or symbol of each radionuclide or for mixtures of radionuclides, an appropriate general description, or a list of the most restrictive radionuclides.
    # iri: https://onerecord.iata.org/ns/cargo#isotopeName
    isotopeName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#isotopeName",
    )
    # label: lowDispersibleIndicator
    # comment: A notation that the material is low dispersible radioactive material.
    # iri: https://onerecord.iata.org/ns/cargo#lowDispersibleIndicator
    lowDispersibleIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#lowDispersibleIndicator",
    )
    # label: specialFormIndicator
    # comment: A notation that the material is special form
    # iri: https://onerecord.iata.org/ns/cargo#specialFormIndicator
    specialFormIndicator: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialFormIndicator",
    )
