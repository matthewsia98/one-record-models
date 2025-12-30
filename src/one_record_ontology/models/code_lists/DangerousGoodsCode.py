from enum import Enum

from rdflib import URIRef


class DangerousGoodsCode(str, Enum):
    """
    label: DangerousGoodsCode
    comment: Restricted code list corresponding to cXML code list 1.14 Dangerous Goods Codes
    """

    # label: CAO
    # comment: Cargo Aircraft Only
    CAO = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#CAO")
    # label: EBI
    # comment: Lithium ion batteries excepted as per Section II of PI 965
    EBI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#EBI")
    # label: EBM
    # comment: Lithium metal batteries excepted as per Section II of PI 968
    EBM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#EBM")
    # label: ELI
    # comment: Lithium Ion Batteries otherwise excepted from the IATA DGR
    ELI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ELI")
    # label: ELM
    # comment: Lithium Metal Batteries otherwise excepted from the IATA DGR
    ELM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ELM")
    # label: ICE
    # comment: Dry Ice
    ICE = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ICE")
    # label: MAG
    # comment: Magnetized Material
    MAG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#MAG")
    # label: RBI
    # comment: Fully regulated lithium ion batteries (Class 9, UN 3480) as per Section IA and IB of PI 965
    RBI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RBI")
    # label: RBM
    # comment: Fully regulated lithium metal batteries (Class 9, UN 3090) as per Section IA and IB of PI 968
    RBM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RBM")
    # label: RCL
    # comment: Cryogenic Liquids
    RCL = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RCL")
    # label: RCM
    # comment: Corrosive
    RCM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RCM")
    # label: RCX
    # comment: Explosives 1.3C
    RCX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RCX")
    # label: REX
    # comment: To be reserved for normally forbidden Explosives, Divisions 1.1, 1.2, 1.3, 1.4F, 1.5 and 1.6
    REX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#REX")
    # label: RFG
    # comment: Flammable Gas
    RFG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFG")
    # label: RFL
    # comment: Flammable Liquid
    RFL = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFL")
    # label: RFS
    # comment: Flammable Solid
    RFS = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFS")
    # label: RFW
    # comment: Dangerous When Wet
    RFW = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFW")
    # label: RGX
    # comment: Explosives 1.3G
    RGX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RGX")
    # label: RIS
    # comment: Infectious Substance
    RIS = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RIS")
    # label: RLI
    # comment: Fully Regulated Lithium Ion Batteries (Class 9)
    RLI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RLI")
    # label: RLM
    # comment: Fully Regulated Lithium Metal Batteries (Class 9)
    RLM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RLM")
    # label: RMD
    # comment: Miscellaneous Dangerous Goods
    RMD = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RMD")
    # label: RNG
    # comment: Non-Flammable Non-Toxic Gas
    RNG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RNG")
    # label: ROP
    # comment: Organic Peroxide
    ROP = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ROP")
    # label: ROX
    # comment: Oxidizer
    ROX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ROX")
    # label: RPB
    # comment: Toxic Substance
    RPB = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RPB")
    # label: RPG
    # comment: Toxic Gas
    RPG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RPG")
    # label: RRW
    # comment: Radioactive Material Category I-White
    RRW = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RRW")
    # label: RRY
    # comment: Radioactive Material Categories II-Yellow and III-Yellow
    RRY = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RRY")
    # label: RSB
    # comment: Polymeric Beads
    RSB = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RSB")
    # label: RSC
    # comment: Spontaneously Combustible
    RSC = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RSC")
    # label: RXB
    # comment: Explosives 1.4B
    RXB = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXB")
    # label: RXC
    # comment: Explosives 1.4C
    RXC = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXC")
    # label: RXD
    # comment: Explosives 1.4D
    RXD = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXD")
    # label: RXE
    # comment: Explosives 1.4E
    RXE = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXE")
    # label: RXG
    # comment: Explosives 1.4G
    RXG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXG")
    # label: RXS
    # comment: Explosives 1.4S
    RXS = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXS")
