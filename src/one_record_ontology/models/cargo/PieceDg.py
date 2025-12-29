from pydantic import AnyUrl, BaseModel, Field
from typing import List, Optional
from rdflib import URIRef
from one_record_ontology.models.cargo.Piece import Piece
class PieceDg(Piece):
    # label: dgDeclaration
    # comment: Reference to the Dangerous Goods declaration
    # iri: https://onerecord.iata.org/ns/cargo#dgDeclaration
    dgDeclaration: List[DgDeclaration] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#dgDeclaration")
    # label: overpackTypeCode
    # comment: Identifies the Logistic Unit package type. UN Recommendation on Transport of Dangerous Goods, Model Regulations 
    # iri: https://onerecord.iata.org/ns/cargo#overpackTypeCode
    overpackTypeCode: List[CodeListElement] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackTypeCode")
    # label: allPackedInOneIndicator
    # comment: A statement identifying that the dangerous goods listed above are all contained in the same outer packaging. Takes the form All packed in one aaaa (description of packaging type) x nn (number of packages). Applies to air transport only. (Air) 
    # iri: https://onerecord.iata.org/ns/cargo#allPackedInOneIndicator
    allPackedInOneIndicator: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#allPackedInOneIndicator")
    # label: overpackCriticalitySafetyIndexNumeric
    # comment: Applies to fissile material only, other than fissile excepted. A numeric value expressed to one decimal place preceded by the letters CSI. 
    # iri: https://onerecord.iata.org/ns/cargo#overpackCriticalitySafetyIndexNumeric
    overpackCriticalitySafetyIndexNumeric: List[str] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackCriticalitySafetyIndexNumeric")
    # label: overpackIndicator
    # comment: Overpack indicator 
    # iri: https://onerecord.iata.org/ns/cargo#overpackIndicator
    overpackIndicator: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackIndicator")
    # label: overpackT1
    # comment: A single number assigned to a package, overpack or freight container to provide control over radiation exposure. 
    # iri: https://onerecord.iata.org/ns/cargo#overpackT1
    overpackT1: List[bool] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#overpackT1")
    # label: qValueNumeric
    # comment: Most instances of all packed in one will require the addition of the Q value which  1. Applies to air transport only. (Air)  
    # iri: https://onerecord.iata.org/ns/cargo#qValueNumeric
    qValueNumeric: List[float] = Field(default_factory=list, serialization_alias="https://onerecord.iata.org/ns/cargo#qValueNumeric")