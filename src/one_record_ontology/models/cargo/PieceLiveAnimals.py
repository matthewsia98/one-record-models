from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.Piece import Piece
class PieceLiveAnimals(Piece):
    # label: associatedEpermit
    # comment: Reference to the permits associated with the Live Animals
    # iri: https://onerecord.iata.org/ns/cargo#associatedEpermit
    associatedEpermit: List[EpermitConsignment] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#associatedEpermit")
    # label: exportTradeCountry
    # comment: Country of last re-export (box 12a). Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#exportTradeCountry
    exportTradeCountry: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#exportTradeCountry")
    # label: goodsTypeCode
    # comment: Appendix number of the convention (I, II or III) (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#goodsTypeCode
    goodsTypeCode: List[GoodsTypeCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsTypeCode")
    # label: goodsTypeExtensionCode
    # comment: Appendix number of the convention (I, II or III) (box 1)
    # iri: https://onerecord.iata.org/ns/cargo#goodsTypeExtensionCode
    goodsTypeExtensionCode: List[GoodsTypeExtensionCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#goodsTypeExtensionCode")
    # label: originReferencePermitTypeCode
    # comment: Document type code of origin reference permit or re-export reference Certificate (box 12/12a)
    # iri: https://onerecord.iata.org/ns/cargo#originReferencePermitTypeCode
    originReferencePermitTypeCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitTypeCode")
    # label: originTradeCountry
    # comment: country of origin (box 12). Refer ISO 3166-2
    # iri: https://onerecord.iata.org/ns/cargo#originTradeCountry
    originTradeCountry: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#originTradeCountry")
    # label: specimenTypeCode
    # comment: Description of specimens, CITES type code (box 9)
    # iri: https://onerecord.iata.org/ns/cargo#specimenTypeCode
    specimenTypeCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#specimenTypeCode")
    # label: acquisitionDateTime
    # comment: Defined in Resolution Conf. 13.6 and is required for pre-Convention specimens (box 12b)
    # iri: https://onerecord.iata.org/ns/cargo#acquisitionDateTime
    acquisitionDateTime: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#acquisitionDateTime")
    # label: annualQuotaQuantity
    # comment: total number of specimens exported in the current calendar year and the current annual quota for the species concerned (box 11a)
    # iri: https://onerecord.iata.org/ns/cargo#annualQuotaQuantity
    annualQuotaQuantity: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#annualQuotaQuantity")
    # label: categoryCode
    # comment: Operations code ID. Refers to the number of the registered captive-breeding or artificial propagation operation (box 12b)
    # iri: https://onerecord.iata.org/ns/cargo#categoryCode
    categoryCode: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#categoryCode")
    # label: originReferencePermitDateTime
    # comment: Issuing date for Origin reference permit or re-export reference Certificate (box 12)
    # iri: https://onerecord.iata.org/ns/cargo#originReferencePermitDateTime
    originReferencePermitDateTime: List[datetime] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitDateTime")
    # label: originReferencePermitId
    # comment: identifier of Origin reference permit or re-export reference Certificate (box 12/12a)
    # iri: https://onerecord.iata.org/ns/cargo#originReferencePermitId
    originReferencePermitId: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#originReferencePermitId")
    # label: quantityAnimals
    # comment: Quantity including units (box 11)
    # iri: https://onerecord.iata.org/ns/cargo#quantityAnimals
    quantityAnimals: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#quantityAnimals")
    # label: speciesCommonName
    # comment: Species common name (box 8)
    # iri: https://onerecord.iata.org/ns/cargo#speciesCommonName
    speciesCommonName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#speciesCommonName")
    # label: speciesScientificName
    # comment: Species scientific name (box 7)
    # iri: https://onerecord.iata.org/ns/cargo#speciesScientificName
    speciesScientificName: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#speciesScientificName")
    # label: specimenDescription
    # comment: Description of specimens, including age and sex if LA (box 9)
    # iri: https://onerecord.iata.org/ns/cargo#specimenDescription
    specimenDescription: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#specimenDescription")