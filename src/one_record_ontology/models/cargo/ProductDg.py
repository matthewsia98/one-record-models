from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.DgProductRadioactive import DgProductRadioactive
from one_record_ontology.models.cargo.Product import Product
from one_record_ontology.models.code_lists.ExplosiveCompatibilityGroupCode import (
    ExplosiveCompatibilityGroupCode,
)
from one_record_ontology.models.code_lists.PackagingDangerLevelCode import (
    PackagingDangerLevelCode,
)


class ProductDg(Product):
    # label: dgRadioactiveMaterial
    # comment: Dg Radioactive Material
    # iri: https://onerecord.iata.org/ns/cargo#dgRadioactiveMaterial
    dgRadioactiveMaterial: Optional[DgProductRadioactive] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#dgRadioactiveMaterial",
    )
    # label: explosiveCompatibilityGroupCode
    # comment: Specifies the reference to the group which identifies the kind of substances and articles that are deemed to be compatible. Mandatory field in case of transport of explosive articles or substances
    # iri: https://onerecord.iata.org/ns/cargo#explosiveCompatibilityGroupCode
    explosiveCompatibilityGroupCode: Optional[ExplosiveCompatibilityGroupCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#explosiveCompatibilityGroupCode",
    )
    # label: packagingDangerLevelCode
    # comment: Packing group, If used must reference I, II or III
    # iri: https://onerecord.iata.org/ns/cargo#packagingDangerLevelCode
    packagingDangerLevelCode: Optional[PackagingDangerLevelCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packagingDangerLevelCode",
    )
    # label: additionalHazardClassificationId
    # comment: Identifies the subsidiary hazard class / division identification containing a numeric field separated by a decimal. There may be , 1 or 2 subsidiary risk classes or divisions. If there is more than one, each should be separated by a comma. The subsidiary risk must be shown in parentheses.
    # iri: https://onerecord.iata.org/ns/cargo#additionalHazardClassificationId
    additionalHazardClassificationId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#additionalHazardClassificationId",
    )
    # label: authorizationInformation
    # comment: Contains additional information relating to an approval, permission or other specific detail applicable to the commodity (e.g. Dangerous Goods in excepted quantities)
    # iri: https://onerecord.iata.org/ns/cargo#authorizationInformation
    authorizationInformation: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#authorizationInformation",
    )
    # label: hazardClassificationId
    # comment: Identifies the hazard class / division identification containing a numeric field separated by a decimal
    # iri: https://onerecord.iata.org/ns/cargo#hazardClassificationId
    hazardClassificationId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#hazardClassificationId",
    )
    # label: packingInstructionNumber
    # comment: The packing instruction number applicable to the UN number / proper shipping name entry. A three-numeric value which may be preceded by the letter Y.  Mandatory field for air transport (Air)
    # iri: https://onerecord.iata.org/ns/cargo#packingInstructionNumber
    packingInstructionNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#packingInstructionNumber",
    )
    # label: properShippingName
    # comment: The name used to describe the particular article or substance as shown in the UN Model Regulations Dangerous Goods List
    # iri: https://onerecord.iata.org/ns/cargo#properShippingName
    properShippingName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#properShippingName",
    )
    # label: specialProvisionId
    # comment: For Air Mode: Special Provision may show a single, double or triple digit number preceded by the letter A, against appropriate entries in the List of Dangerous Goods
    # iri: https://onerecord.iata.org/ns/cargo#specialProvisionId
    specialProvisionId: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#specialProvisionId",
    )
    # label: technicalName
    # comment: This is additional chemical name(s) required for some proper shipping names. When added the technical must be shown in parentheses immediately following the proper shipping name.
    # iri: https://onerecord.iata.org/ns/cargo#technicalName
    technicalName: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#technicalName",
    )
    # label: unNumber
    # comment: Reference identifying the United Nations Dangerous Goods serial number assigned within the UN to substances and articles contained in a list of the dangerous goods most commonly carried. e.g. 1189 - Ethylene glycol monomethyl ether acetate
    # iri: https://onerecord.iata.org/ns/cargo#unNumber
    unNumber: Optional[str] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#unNumber"
    )
