from typing import Optional

from pydantic import Field

from one_record_ontology.models.cargo.CodeListElement import CodeListElement
from one_record_ontology.models.cargo.LoadingUnit import LoadingUnit
from one_record_ontology.models.code_lists.DemurrageCode import DemurrageCode
from one_record_ontology.models.code_lists.ULDConditionCode import ULDConditionCode
from one_record_ontology.models.code_lists.ULDLoadingIndicator import (
    ULDLoadingIndicator,
)


class ULD(LoadingUnit):
    # label: demurrageCode
    # comment: Contains three designator of demurrage code, refer to RP 1654 (BCC, HHH, XXX, ZZZ)
    # iri: https://onerecord.iata.org/ns/cargo#demurrageCode
    demurrageCode: Optional[DemurrageCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#demurrageCode",
    )
    # label: loadingIndicator
    # comment: ULD height or loading limitation code. Refer CXML Code List 1.47,  e.g. R - ULD Height above 244 centimetres
    # iri: https://onerecord.iata.org/ns/cargo#loadingIndicator
    loadingIndicator: Optional[ULDLoadingIndicator] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#loadingIndicator",
    )
    # label: odlnCode
    # comment: Contains two designator codes of ODLN or Operational Damage Limit Notices. ODLN code is used to define type of damage after visually check the serviceability of ULDs section 7, Standard Specifications 4/3 or 4/4 in ULD Regulations
    # iri: https://onerecord.iata.org/ns/cargo#odlnCode
    odlnCode: Optional[CodeListElement] = Field(
        default=None, serialization_alias="https://onerecord.iata.org/ns/cargo#odlnCode"
    )
    # label: ownerCode
    # comment: Owner code of the ULD in aa, an or na format - owner can be an airline or leasing company
    # iri: https://onerecord.iata.org/ns/cargo#ownerCode
    ownerCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#ownerCode",
    )
    # label: serviceabilityCode
    # comment: Designator of serviceability condition e.g. SER or DAM
    # iri: https://onerecord.iata.org/ns/cargo#serviceabilityCode
    serviceabilityCode: Optional[ULDConditionCode] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#serviceabilityCode",
    )
    # label: uldTypeCode
    # comment: Standard Unit Load Device type code e.g. AKE - Certified Container - Contoured. Refer to IATA ULD Technical Manual
    # iri: https://onerecord.iata.org/ns/cargo#uldTypeCode
    uldTypeCode: Optional[CodeListElement] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldTypeCode",
    )
    # label: ataDesignator
    # comment: US / ATA Unit Load Device type code e.g. M2
    # iri: https://onerecord.iata.org/ns/cargo#ataDesignator
    ataDesignator: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#ataDesignator",
    )
    # label: damageFlag
    # comment: Indicates if the ULD is Damaged
    # iri: https://onerecord.iata.org/ns/cargo#damageFlag
    damageFlag: Optional[bool] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#damageFlag",
    )
    # label: numberOfDoors
    # comment: Number of doors
    # iri: https://onerecord.iata.org/ns/cargo#numberOfDoors
    numberOfDoors: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfDoors",
    )
    # label: numberOfFittings
    # comment: Number of fittings
    # iri: https://onerecord.iata.org/ns/cargo#numberOfFittings
    numberOfFittings: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfFittings",
    )
    # label: numberOfNets
    # comment: Number of nets
    # iri: https://onerecord.iata.org/ns/cargo#numberOfNets
    numberOfNets: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfNets",
    )
    # label: numberOfStraps
    # comment: Number of straps
    # iri: https://onerecord.iata.org/ns/cargo#numberOfStraps
    numberOfStraps: Optional[int] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#numberOfStraps",
    )
    # label: sealNumber
    # comment: ULD seal number if applicable
    # iri: https://onerecord.iata.org/ns/cargo#sealNumber
    sealNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#sealNumber",
    )
    # label: uldSerialNumber
    # comment: Serial number that allows to uniquely identify the ULD
    # iri: https://onerecord.iata.org/ns/cargo#uldSerialNumber
    uldSerialNumber: Optional[str] = Field(
        default=None,
        serialization_alias="https://onerecord.iata.org/ns/cargo#uldSerialNumber",
    )
