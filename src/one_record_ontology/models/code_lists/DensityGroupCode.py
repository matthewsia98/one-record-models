from enum import Enum

from rdflib import URIRef


class DensityGroupCode(str, Enum):
    """
    label: DensityGroupCode
    comment: Restricted code list corresponding to cXML code list 2 Density Group Codes
    """

    # label: 0
    # comment: 160kg per mc or 10 lbs per cf
    _0 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#0")
    # label: 1
    # comment: 300 kg per mc or 18.6 lbs per cf
    _1 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#1")
    # label: 10
    # comment: 950 kg per mc or 59.3 lbs per cf
    _10 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#10")
    # label: 2
    # comment: 90 kg per mc or 5.6 lbs per cf
    _2 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#2")
    # label: 3
    # comment: 120 kg per mc or 7.5 lbs per cf
    _3 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#3")
    # label: 4
    # comment: 220 kg per mc or 13.8 lbs per cf
    _4 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#4")
    # label: 5
    # comment: 60 kg per mc or 3.8 lbs per cf
    _5 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#5")
    # label: 6
    # comment: 250 kg per mc or 15.6 lbs per cf
    _6 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#6")
    # label: 8
    # comment: 400 kg per mc or 25 lbs per cf
    _8 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#8")
    # label: 9
    # comment: 600 kg per mc or 37.5 lbs per cf
    _9 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#9")
