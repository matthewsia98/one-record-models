from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.LogisticsObject import LogisticsObject
class DgProductRadioactive(LogisticsObject):
    # label: dgRaTypeCode
    # comment: The category of the package or all packed in one. Complete text to be transmitted: I-White, II-Yellow, III-Yellow instead of I, II, III
    # iri: https://onerecord.iata.org/ns/cargo#dgRaTypeCode
    dgRaTypeCode: List[RaTypeCode] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#dgRaTypeCode")
    # label: forProductDg
    # comment: Reference to the ProductDg this DgProductRadioactive details
    # iri: https://onerecord.iata.org/ns/cargo#forProductDg
    forProductDg: List[ProductDg] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#forProductDg")
    # label: isotopes
    # comment: DgRadioactiveIsotope.
    # iri: https://onerecord.iata.org/ns/cargo#isotopes
    isotopes: List[DgRadioactiveIsotope] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#isotopes")
    # label: fissileExceptionIndicator
    # comment: Indicates if Fissile is excepted
    # iri: https://onerecord.iata.org/ns/cargo#fissileExceptionIndicator
    fissileExceptionIndicator: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#fissileExceptionIndicator")
    # label: fissileExceptionReference
    # comment: Fissile exception reference, mandatory if Fissile Exception Indicator is true.
    # iri: https://onerecord.iata.org/ns/cargo#fissileExceptionReference
    fissileExceptionReference: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#fissileExceptionReference")
    # label: transportIndexNumeric
    # comment: Radioactive Transport-Index value of the package or all packed in one. Conditionally mandatory and applies to categories II-Yellow and III-Yellow only; field only contains the value, if printed, TI must be added as a prefix to the value  to be printed in the Packing Instructions column
    # iri: https://onerecord.iata.org/ns/cargo#transportIndexNumeric
    transportIndexNumeric: List[int] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#transportIndexNumeric")