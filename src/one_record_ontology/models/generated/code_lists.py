"""
This file was automatically generated from the ONE Record API ontology.

Ontology source: https://onerecord.iata.org/ns/code-lists/ontology.ttl
Ontology version: https://onerecord.iata.org/ns/code-lists/1.1.0
Generated on: 2025-12-31T20:58:49.894673+00:00

DO NOT EDIT MANUALLY.
"""

from __future__ import annotations

from enum import Enum

from rdflib import URIRef

from one_record_ontology.models.base_model import OneRecordBaseModel


class AWBUseIndicator(str, Enum):
    # label: R
    # comment: Revenue AWB
    R = URIRef("https://onerecord.iata.org/ns/code-lists/AWBUseIndicator#R")

    # label: S
    # comment: Service AWB
    S = URIRef("https://onerecord.iata.org/ns/code-lists/AWBUseIndicator#S")

    # label: V
    # comment: Void AWB
    V = URIRef("https://onerecord.iata.org/ns/code-lists/AWBUseIndicator#V")


class AircraftPossibilityCode(str, Enum):
    # label: LLV
    # comment: Truck carrying Containerized Cargo (ULDs)
    LLV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLV")

    # label: BBV
    # comment: Truck carrying Loose Load Cargo
    BBV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#BBV")

    # label: LLF
    # comment: Pure freighter flight carrying Containerized Cargo (ULDs)
    LLF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLF")

    # label: LLJ
    # comment: Passenger flight operated by wide-bodied aircraft carrying Containerized (ULDs)
    LLJ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLJ")

    # label: LPF
    # comment: Pure freighter flight carrying Containerized (ULDs)/Palletized Cargo
    LPF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPF")

    # label: PPQ
    # comment: Mixed configuration aircraft carrying Palletized Cargo on the passenger deck
    PPQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPQ")

    # label: LPQ
    # comment: Mixed configuration (Combi) aircraft carrying Containerized (ULDs)/Palletized Cargo on the passenger deck
    LPQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPQ")

    # label: PPF
    # comment: Pure freighter flight carrying Palletized Cargo
    PPF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPF")

    # label: BBF
    # comment: Pure freighter flight carrying Loose Load Cargo
    BBF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#BBF")

    # label: BBQ
    # comment: Mixed configuration (Combi) aircraft carrying Loose Load Cargo on the passenger deck
    BBQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#BBQ")

    # label: PPV
    # comment: Truck carrying Palletized Cargo
    PPV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPV")

    # label: PPJ
    # comment: Passenger flight operated by wide-bodied aircraft carrying Palletized Cargo
    PPJ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPJ")

    # label: LLQ
    # comment: Mixed configuration (Combi) aircraft carrying Containerized Cargo (ULDs) on the passenger deck
    LLQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLQ")

    # label: LPJ
    # comment: Passenger flight operated by wide-bodied aircraft carrying Containerized (ULDs)/ Palletized Cargo
    LPJ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPJ")

    # label: LPV
    # comment: Truck carrying Containerized (ULDs)/Palletized Cargo
    LPV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPV")


class BasicRateClassCode(str, Enum):
    # label: N
    # comment: Normal Rate
    N = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#N")

    # label: M
    # comment: Minimum Charge
    M = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#M")

    # label: Q
    # comment: Quantity Rate
    Q = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#Q")

    # label: C
    # comment: Specific Commodity Rate
    C = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#C")

    # label: U
    # comment: Unit Load Device Basic Charge or Rate
    U = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#U")


class ChargeCode(str, Enum):
    # label: NC
    # comment: No Charge
    NC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NC")

    # label: PD
    # comment: Partial Prepaid Credit — Partial Collect Cash
    PD = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PD")

    # label: NT
    # comment: No Weight Charge — Other Charges Collect
    NT = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NT")

    # label: CA
    # comment: Partial Collect Credit — Partial Prepaid Cash
    CA = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CA")

    # label: PH
    # comment: Partial Prepaid Credit Card — Partial Collect Credit
    PH = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PH")

    # label: CM
    # comment: Destination Collect by MCO
    CM = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CM")

    # label: NG
    # comment: No Weight Charge — Other Charges Prepaid by GBL
    NG = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NG")

    # label: NZ
    # comment: No Weight Charge — Other Charges Prepaid by Credit Card
    NZ = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NZ")

    # label: PC
    # comment: Partial Prepaid Cash — Partial Collect Cash
    PC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PC")

    # label: CX
    # comment: Destination Collect Credit
    CX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CX")

    # label: CE
    # comment: Partial Collect Credit Card — Partial Prepaid Cash
    CE = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CE")

    # label: PF
    # comment: Partial Prepaid Credit Card — Partial Collect Credit Card
    PF = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PF")

    # label: NP
    # comment: No Weight Charge — Other Charges Prepaid Cash
    NP = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NP")

    # label: CG
    # comment: All Charges Collect by GBL
    CG = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CG")

    # label: PX
    # comment: All Charges Prepaid Credit
    PX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PX")

    # label: PZ
    # comment: All Charges Prepaid by Credit Card
    PZ = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PZ")

    # label: CZ
    # comment: All Charges Collect by Credit Card
    CZ = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CZ")

    # label: NX
    # comment: No Weight Charge — Other Charges Prepaid Credit
    NX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#NX")

    # label: PG
    # comment: All Charges Prepaid by GBL
    PG = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PG")

    # label: CB
    # comment: Partial Collect Credit — Partial Prepaid Credit
    CB = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CB")

    # label: PE
    # comment: Partial Prepaid Credit Card — Partial Collect Cash
    PE = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PE")

    # label: PP
    # comment: All Charges Prepaid Cash
    PP = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#PP")

    # label: CC
    # comment: All Charges Collect
    CC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CC")

    # label: CH
    # comment: Partial Collect Credit Card — Partial Prepaid Credit
    CH = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CH")

    # label: CP
    # comment: Destination Collect Cash
    CP = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeCode#CP")


class ChargeIdentifier(str, Enum):
    # label: OC
    # comment: Total Other Charges Due Carrier
    OC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#OC")

    # label: VC
    # comment: Valuation Charge
    VC = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#VC")

    # label: TX
    # comment: Taxes
    TX = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#TX")

    # label: SI
    # comment: Sales Incentive
    SI = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#SI")

    # label: OA
    # comment: Total Other Charges Due Agent
    OA = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#OA")

    # label: NI
    # comment: CASS Invoice Amount
    NI = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#NI")

    # label: IN
    # comment: Insurance
    IN = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#IN")

    # label: CT
    # comment: Charge Summary Total
    CT = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#CT")

    # label: CO
    # comment: Commission
    CO = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#CO")

    # label: WT
    # comment: Total Weight Charge
    WT = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#WT")

    # label: CN
    # comment: CASS Net Amount
    CN = URIRef("https://onerecord.iata.org/ns/code-lists/ChargeIdentifier#CN")


class CommodityCode(str, Enum):
    # label: LIVE_MMLS_CATS_Japanese_Bobtail
    # comment: Japanese Bobtail
    LIVE_MMLS_CATS_Japanese_Bobtail = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Japanese_Bobtail"
    )

    # label: RAWM_GRAN
    # comment: Granite slabs
    RAWM_GRAN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_GRAN"
    )

    # label: LIVE_MMLS_CATS_Oriental
    # comment: Oriental
    LIVE_MMLS_CATS_Oriental = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Oriental"
    )

    # label: ELEC_CMPT
    # comment: Computers
    ELEC_CMPT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_CMPT"
    )

    # label: LIVE_MMLS_CATS_Highland_Lynx
    # comment: Highland Lynx
    LIVE_MMLS_CATS_Highland_Lynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Highland_Lynx"
    )

    # label: LIVE_MMLS_DOGS_Komondor
    # comment: Komondor
    LIVE_MMLS_DOGS_Komondor = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Komondor"
    )

    # label: LIVE_MMLS_DOGS_Wire_Fox_Terrier
    # comment: Wire Fox Terrier
    LIVE_MMLS_DOGS_Wire_Fox_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Wire_Fox_Terrier"
    )

    # label: LIVE_BRDH_DUCK
    # comment: Ducks
    LIVE_BRDH_DUCK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_DUCK"
    )

    # label: LIVE_MMLS_DOGS_Polish_Lowland_Sheepdog
    # comment: Polish Lowland Sheepdog
    LIVE_MMLS_DOGS_Polish_Lowland_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Polish_Lowland_Sheepdog"
    )

    # label: CONS_OFSP
    # comment: Office supplies
    CONS_OFSP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_OFSP"
    )

    # label: LIVE_MMLS_DOGS_Catahoula_Bulldog_Catahoula_Leopard_Bulldog
    # comment: Catahoula Bulldog-Catahoula Leopard Bulldog
    LIVE_MMLS_DOGS_Catahoula_Bulldog_Catahoula_Leopard_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Catahoula_Bulldog_Catahoula_Leopard_Bulldog"
    )

    # label: LIVE_MMLS_CATS_Ragdoll
    # comment: Ragdoll
    LIVE_MMLS_CATS_Ragdoll = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ragdoll"
    )

    # label: LIVE_BRDH_HEGG
    # comment: Hatching Eggs
    LIVE_BRDH_HEGG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_HEGG"
    )

    # label: FOOD_PERI
    # comment: Perhishables
    FOOD_PERI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_PERI"
    )

    # label: FOOD_CERE_CAKE
    # comment: Cakes and Pastries
    FOOD_CERE_CAKE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_CERE_CAKE"
    )

    # label: FOOD_FRTV_CMBR
    # comment: Cucumber
    FOOD_FRTV_CMBR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_CMBR"
    )

    # label: ELEC_ECOM
    # comment: Electronic components
    ELEC_ECOM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_ECOM"
    )

    # label: LIVE_MMLS_DOGS_Cane_Corso
    # comment: Cane Corso
    LIVE_MMLS_DOGS_Cane_Corso = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cane_Corso"
    )

    # label: LIVE_MMLS_DOGS_German_Shorthaired_Pointer
    # comment: German Shorthaired Pointer
    LIVE_MMLS_DOGS_German_Shorthaired_Pointer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Shorthaired_Pointer"
    )

    # label: FOOD_CERE
    # comment: Cereal foods
    FOOD_CERE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_CERE"
    )

    # label: FOOD_STUF_CHOC
    # comment: Chocolate
    FOOD_STUF_CHOC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_CHOC"
    )

    # label: LIVE_MMLS_CATS_Donskoy
    # comment: Donskoy
    LIVE_MMLS_CATS_Donskoy = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Donskoy"
    )

    # label: LIVE_MMLS_DOGS_Boston_Terrier
    # comment: Boston Terrier
    LIVE_MMLS_DOGS_Boston_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boston_Terrier"
    )

    # label: LIVE_MMLS_DOGS
    # comment: Dogs
    LIVE_MMLS_DOGS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS"
    )

    # label: LIVE_MMLS_DOGS_Bernese_Mountain_Dog
    # comment: Bernese Mountain Dog
    LIVE_MMLS_DOGS_Bernese_Mountain_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bernese_Mountain_Dog"
    )

    # label: FOOD_STUF_MPWD
    # comment: Milk powder
    FOOD_STUF_MPWD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_MPWD"
    )

    # label: VHCL_SHIP_SMTR
    # comment: Motor and Generator
    VHCL_SHIP_SMTR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SMTR"
    )

    # label: LIVE_MMLS_DOGS_Utonagan_Northern_Inuit_Dog
    # comment: Utonagan-Northern Inuit Dog
    LIVE_MMLS_DOGS_Utonagan_Northern_Inuit_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Utonagan_Northern_Inuit_Dog"
    )

    # label: VHCL_SHIP
    # comment: Ships
    VHCL_SHIP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP"
    )

    # label: LIVE_MMLS_DOGS_Spanish_Water_Dog
    # comment: Spanish Water Dog
    LIVE_MMLS_DOGS_Spanish_Water_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Spanish_Water_Dog"
    )

    # label: LIVE_MMLS_DOGS_Basset_Hound
    # comment: Basset Hound
    LIVE_MMLS_DOGS_Basset_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Basset_Hound"
    )

    # label: LIVE_MMLS_DOGS_Sussex_Spaniel
    # comment: Sussex Spaniel
    LIVE_MMLS_DOGS_Sussex_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sussex_Spaniel"
    )

    # label: VALU
    # comment: Valuables
    VALU = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU")

    # label: LIVE_MMLS_DOGS_Norwegian_Lundehund
    # comment: Norwegian Lundehund
    LIVE_MMLS_DOGS_Norwegian_Lundehund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwegian_Lundehund"
    )

    # label: LIVE_MMLS_DOGS_Shih_Tzu
    # comment: Shih Tzu
    LIVE_MMLS_DOGS_Shih_Tzu = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shih_Tzu"
    )

    # label: PHAR_BIOP
    # comment: Biological products
    PHAR_BIOP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP"
    )

    # label: LIVE_MMLS_DOGS_French_Mastiff
    # comment: French Mastiff
    LIVE_MMLS_DOGS_French_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_French_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_Japanese_Pug
    # comment: Japanese Pug
    LIVE_MMLS_DOGS_Japanese_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Pug"
    )

    # label: LIVE_BRDH_OSTR
    # comment: Ostriches
    LIVE_BRDH_OSTR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_OSTR"
    )

    # label: LIVE_MMLS_DOGS_Canary_Mastiff
    # comment: Canary Mastiff
    LIVE_MMLS_DOGS_Canary_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Canary_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_Presa_Canario
    # comment: Presa Canario
    LIVE_MMLS_DOGS_Presa_Canario = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Presa_Canario"
    )

    # label: LIVE_MMLS_DOGS_Shih_Poo
    # comment: Shih-Poo
    LIVE_MMLS_DOGS_Shih_Poo = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shih_Poo"
    )

    # label: LIVE_MMLS_GOAT
    # comment: Goats
    LIVE_MMLS_GOAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_GOAT"
    )

    # label: LIVE_MMLS_CATS_Maine_Coon
    # comment: Maine Coon
    LIVE_MMLS_CATS_Maine_Coon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Maine_Coon"
    )

    # label: LIVE_MMLS_DOGS_Doxiepoo_Dachshund_Poodle_Mix
    # comment: Doxiepoo-Dachshund Poodle Mix
    LIVE_MMLS_DOGS_Doxiepoo_Dachshund_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Doxiepoo_Dachshund_Poodle_Mix"
    )

    # label: LIVE_MMLS_DOGS_Treeing_Walker_Coonhound
    # comment: Treeing Walker Coonhound
    LIVE_MMLS_DOGS_Treeing_Walker_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Treeing_Walker_Coonhound"
    )

    # label: LIVE_MMLS_DOGS_Anatolian_Shepherd_Dog
    # comment: Anatolian Shepherd Dog
    LIVE_MMLS_DOGS_Anatolian_Shepherd_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Anatolian_Shepherd_Dog"
    )

    # label: LIVE_BRDH_BIRD
    # comment: Birds
    LIVE_BRDH_BIRD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_BIRD"
    )

    # label: LIVE_MMLS_DOGS_Border_Terrier
    # comment: Border Terrier
    LIVE_MMLS_DOGS_Border_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Border_Terrier"
    )

    # label: TXTL_TXEW
    # comment: Textiles excluding Wear
    TXTL_TXEW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW"
    )

    # label: MART_ENGR
    # comment: Engraving
    MART_ENGR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_ENGR"
    )

    # label: RAWM_MIRR
    # comment: Mirre
    RAWM_MIRR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MIRR"
    )

    # label: FOOD_FRTV_TOMA
    # comment: Tomatoes
    FOOD_FRTV_TOMA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_TOMA"
    )

    # label: CONS_CWRE
    # comment: Chinaware and Ceramics
    CONS_CWRE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_CWRE"
    )

    # label: PRIN_ADVM
    # comment: Advertising materials
    PRIN_ADVM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_ADVM"
    )

    # label: VHCL_AIRC_AMTR
    # comment: Aircraft motors
    VHCL_AIRC_AMTR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AMTR"
    )

    # label: PHAR_MDCN_VACC
    # comment: Vaccines
    PHAR_MDCN_VACC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN_VACC"
    )

    # label: LIVE_MMLS_DOGS_Scottish_Deerhound
    # comment: Scottish Deerhound
    LIVE_MMLS_DOGS_Scottish_Deerhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Scottish_Deerhound"
    )

    # label: CONS_EXHB
    # comment: Exhibition goods
    CONS_EXHB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_EXHB"
    )

    # label: LIVE_MMLS_DOGS_Black_and_Tan_Coonhound
    # comment: Black and Tan Coonhound
    LIVE_MMLS_DOGS_Black_and_Tan_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Black_and_Tan_Coonhound"
    )

    # label: LIVE_MMLS_DOGS_Japanese_Boxer
    # comment: Japanese Boxer
    LIVE_MMLS_DOGS_Japanese_Boxer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Boxer"
    )

    # label: LIVE_MMLS_DOGS_Japanese_Mastiff
    # comment: Japanese Mastiff
    LIVE_MMLS_DOGS_Japanese_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_English_Bulldog
    # comment: English Bulldog
    LIVE_MMLS_DOGS_English_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Bulldog"
    )

    # label: LIVE_MMLS_MNKY
    # comment: Monkeys
    LIVE_MMLS_MNKY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_MNKY"
    )

    # label: PRIN
    # comment: Printed Matter
    PRIN = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN")

    # label: SCIN
    # comment: Scientific Instruments
    SCIN = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN")

    # label: VHCL_MACH_COMP
    # comment: Comperssors
    VHCL_MACH_COMP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_COMP"
    )

    # label: LIVE_MMLS_DOGS_Alaskan_Malamute
    # comment: Alaskan Malamute
    LIVE_MMLS_DOGS_Alaskan_Malamute = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Alaskan_Malamute"
    )

    # label: LIVE_MMLS_DOGS_Weimaraner
    # comment: Weimaraner
    LIVE_MMLS_DOGS_Weimaraner = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Weimaraner"
    )

    # label: LIVE_MMLS_DOGS_Pit_Plott_Pitbull_Plott_Hound_Mix
    # comment: Pit Plott-Pitbull Plott Hound Mix
    LIVE_MMLS_DOGS_Pit_Plott_Pitbull_Plott_Hound_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pit_Plott_Pitbull_Plott_Hound_Mix"
    )

    # label: LIVE_MMLS_DOGS_Italian_Mastiff
    # comment: Italian Mastiff
    LIVE_MMLS_DOGS_Italian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Italian_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_Rat_Terrier
    # comment: Rat Terrier
    LIVE_MMLS_DOGS_Rat_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Rat_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Whippet
    # comment: Whippet
    LIVE_MMLS_DOGS_Whippet = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Whippet"
    )

    # label: CONS_TOYS
    # comment: Toys and Games
    CONS_TOYS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_TOYS"
    )

    # label: LIVE_MMLS_CATS_Niebelung
    # comment: Niebelung
    LIVE_MMLS_CATS_Niebelung = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Niebelung"
    )

    # label: LIVE_MMLS_CATS_Pixiebob
    # comment: Pixiebob
    LIVE_MMLS_CATS_Pixiebob = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Pixiebob"
    )

    # label: FOOD_FRTV_LITC
    # comment: Litchies
    FOOD_FRTV_LITC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_LITC"
    )

    # label: LIVE_MMLS_DOGS_Plott_Hound
    # comment: Plott Hound
    LIVE_MMLS_DOGS_Plott_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Plott_Hound"
    )

    # label: LIVE_MLKS_LUGW
    # comment: Lugworms
    LIVE_MLKS_LUGW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MLKS_LUGW"
    )

    # label: PHAR_BIOP_BIOC
    # comment: Biochemicals
    PHAR_BIOP_BIOC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_BIOC"
    )

    # label: CONS_DIPL
    # comment: Diplomatic mail and goods
    CONS_DIPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_DIPL"
    )

    # label: LIVE_MMLS_CATS_Bristol
    # comment: Bristol
    LIVE_MMLS_CATS_Bristol = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Bristol"
    )

    # label: LIVE_MMLS_DOGS_Redbone_Coonhound
    # comment: Redbone Coonhound
    LIVE_MMLS_DOGS_Redbone_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Redbone_Coonhound"
    )

    # label: LIVE_MMLS_DOGS_Alano
    # comment: Alano
    LIVE_MMLS_DOGS_Alano = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Alano"
    )

    # label: LIVE_MMLS_DOGS_Wirehaired_Vizsla
    # comment: Wirehaired Vizsla
    LIVE_MMLS_DOGS_Wirehaired_Vizsla = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Wirehaired_Vizsla"
    )

    # label: LIVE_MMLS_CATS_Russian_Blue
    # comment: Russian Blue
    LIVE_MMLS_CATS_Russian_Blue = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Russian_Blue"
    )

    # label: LIVE_MMLS_DOGS_Spanish_Mastiff
    # comment: Spanish Mastiff
    LIVE_MMLS_DOGS_Spanish_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Spanish_Mastiff"
    )

    # label: MART_PNTG
    # comment: Painting
    MART_PNTG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_PNTG"
    )

    # label: ELEC_CALC
    # comment: Calculators
    ELEC_CALC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_CALC"
    )

    # label: ELEC_CPRT
    # comment: Computer parts
    ELEC_CPRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_CPRT"
    )

    # label: CONS_HRSE
    # comment: Horse equipment
    CONS_HRSE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HRSE"
    )

    # label: LIVE_MMLS_DOGS_Finnish_Spitz
    # comment: Finnish Spitz
    LIVE_MMLS_DOGS_Finnish_Spitz = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Finnish_Spitz"
    )

    # label: CHEM_RADA
    # comment: Radioactive materials
    CHEM_RADA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_RADA"
    )

    # label: LIVE_MMLS_DOGS_Doberman_Pinscher
    # comment: Doberman Pinscher
    LIVE_MMLS_DOGS_Doberman_Pinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Doberman_Pinscher"
    )

    # label: LIVE_MMLS_DOGS_Dutch_Pug
    # comment: Dutch Pug
    LIVE_MMLS_DOGS_Dutch_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dutch_Pug"
    )

    # label: FOOD_TBCO_CIGA
    # comment: Cigars
    FOOD_TBCO_CIGA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_TBCO_CIGA"
    )

    # label: VHCL_MACH_MECH
    # comment: Mechanic products
    VHCL_MACH_MECH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_MECH"
    )

    # label: LIVE_MMLS_DOGS_Dandie_Dinmont_Terrier
    # comment: Dandie Dinmont Terrier
    LIVE_MMLS_DOGS_Dandie_Dinmont_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dandie_Dinmont_Terrier"
    )

    # label: SCIN_PRCI
    # comment: Precision instruments
    SCIN_PRCI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_PRCI"
    )

    # label: LIVE_MMLS_DOGS_Fila_Brasileiro_Brazilian_Mastiff
    # comment: Fila Brasileiro-Brazilian Mastiff
    LIVE_MMLS_DOGS_Fila_Brasileiro_Brazilian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Fila_Brasileiro_Brazilian_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_Border_Collie
    # comment: Border Collie
    LIVE_MMLS_DOGS_Border_Collie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Border_Collie"
    )

    # label: FOOD_FISH_FRZF
    # comment: Frozen fish
    FOOD_FISH_FRZF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_FRZF"
    )

    # label: LIVE_BRDH_CHIC
    # comment: Chicks
    LIVE_BRDH_CHIC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_CHIC"
    )

    # label: LIVE_MMLS_DOGS_English_Foxhound
    # comment: English Foxhound
    LIVE_MMLS_DOGS_English_Foxhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Foxhound"
    )

    # label: ELEC_TELC
    # comment: Telecom equipment
    ELEC_TELC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_TELC"
    )

    # label: LIVE_MMLS_CATS_Scottish_Fold
    # comment: Scottish Fold
    LIVE_MMLS_CATS_Scottish_Fold = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Scottish_Fold"
    )

    # label: TXTL_TXTL
    # comment: Textiles
    TXTL_TXTL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXTL"
    )

    # label: FOOD_FISH_SFIN
    # comment: Shark fin
    FOOD_FISH_SFIN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SFIN"
    )

    # label: TXTL
    # comment: Textiles, Leather and Furs
    TXTL = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL")

    # label: LIVE_VANI
    # comment: Venomous animals
    LIVE_VANI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_VANI"
    )

    # label: VALU_PLAT
    # comment: Platinum
    VALU_PLAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_PLAT"
    )

    # label: LIVE_MMLS_DOGS_Bloodhound
    # comment: Bloodhound
    LIVE_MMLS_DOGS_Bloodhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bloodhound"
    )

    # label: RAWM_MINE
    # comment: Minerals
    RAWM_MINE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MINE"
    )

    # label: FOOD_FRTV_AVOC
    # comment: Avocados
    FOOD_FRTV_AVOC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_AVOC"
    )

    # label: MLTY_MSUP
    # comment: Military supplies
    MLTY_MSUP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_MSUP"
    )

    # label: FOOD_MEAT_PORK
    # comment: Pork products
    FOOD_MEAT_PORK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_PORK"
    )

    # label: CHEM_CDGR
    # comment: Chemicals - Dangerous
    CHEM_CDGR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CDGR"
    )

    # label: PHAR_BIOP_HUSR
    # comment: Human serum
    PHAR_BIOP_HUSR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_HUSR"
    )

    # label: LIVE_MMLS_CATS_Bengal
    # comment: Bengal
    LIVE_MMLS_CATS_Bengal = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Bengal"
    )

    # label: FOOD_FISH_TUNA
    # comment: Tuna
    FOOD_FISH_TUNA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_TUNA"
    )

    # label: LIVE_MMLS_CATS_Exotic_Shorthair
    # comment: Exotic Shorthair
    LIVE_MMLS_CATS_Exotic_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Exotic_Shorthair"
    )

    # label: VALU_PSTN
    # comment: Precious stones
    VALU_PSTN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_PSTN"
    )

    # label: LIVE_MMLS_DOGS_German_Mastiff_Great_Dane
    # comment: German Mastiff-Great Dane
    LIVE_MMLS_DOGS_German_Mastiff_Great_Dane = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Mastiff_Great_Dane"
    )

    # label: FOOD_FRTV_DURI
    # comment: Durian
    FOOD_FRTV_DURI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_DURI"
    )

    # label: CHEM_DGRG
    # comment: Dangerous Goods
    CHEM_DGRG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_DGRG"
    )

    # label: VHCL_AIRC_APRT
    # comment: Aircraft parts
    VHCL_AIRC_APRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_APRT"
    )

    # label: FLWR_FMNT
    # comment: Fresh mint
    FLWR_FMNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FMNT"
    )

    # label: LIVE_MMLS_CATS_York_Chocolate
    # comment: York Chocolate
    LIVE_MMLS_CATS_York_Chocolate = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_York_Chocolate"
    )

    # label: LIVE_MMLS_DOGS_Mal_Shi_Maltese_Shih_Tzu_Mix
    # comment: Mal-Shi-Maltese Shih Tzu Mix
    LIVE_MMLS_DOGS_Mal_Shi_Maltese_Shih_Tzu_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mal_Shi_Maltese_Shih_Tzu_Mix"
    )

    # label: LIVE_MMLS_DOGS_Xoloitzcuintli_Mexican_Hairless_Dog
    # comment: Xoloitzcuintli-Mexican Hairless Dog
    LIVE_MMLS_DOGS_Xoloitzcuintli_Mexican_Hairless_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Xoloitzcuintli_Mexican_Hairless_Dog"
    )

    # label: LIVE_MMLS_DOGS_Australian_Cattle_Dog
    # comment: Australian Cattle Dog
    LIVE_MMLS_DOGS_Australian_Cattle_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Australian_Cattle_Dog"
    )

    # label: FOOD_MEAT_GOSL
    # comment: Goose liver
    FOOD_MEAT_GOSL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_GOSL"
    )

    # label: LIVE_MMLS_DOGS_Vizsla
    # comment: Vizsla
    LIVE_MMLS_DOGS_Vizsla = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Vizsla"
    )

    # label: LIVE_MMLS_CATS_American_Curl
    # comment: American Curl
    LIVE_MMLS_CATS_American_Curl = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Curl"
    )

    # label: PHAR_BIOP_HUBL
    # comment: Human blood
    PHAR_BIOP_HUBL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_HUBL"
    )

    # label: LIVE_MMLS_DOGS_Akita
    # comment: Akita
    LIVE_MMLS_DOGS_Akita = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Akita"
    )

    # label: LIVE_MMLS_DOGS_Bluetick_Coonhound
    # comment: Bluetick Coonhound
    LIVE_MMLS_DOGS_Bluetick_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bluetick_Coonhound"
    )

    # label: LIVE_MMLS_DOGS_Bedlington_Terrier
    # comment: Bedlington Terrier
    LIVE_MMLS_DOGS_Bedlington_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bedlington_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Icelandic_Sheepdog
    # comment: Icelandic Sheepdog
    LIVE_MMLS_DOGS_Icelandic_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Icelandic_Sheepdog"
    )

    # label: LIVE_MMLS_DOGS_Pointer
    # comment: Pointer
    LIVE_MMLS_DOGS_Pointer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pointer"
    )

    # label: LIVE_MMLS_DOGS_Maltese_Shih_Tzu
    # comment: Maltese Shih Tzu
    LIVE_MMLS_DOGS_Maltese_Shih_Tzu = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Maltese_Shih_Tzu"
    )

    # label: LIVE_MMLS_DOGS_Kyi_Leo_Maltese_Lhasa_Apso_Mix
    # comment: Kyi-Leo-Maltese Lhasa Apso Mix
    LIVE_MMLS_DOGS_Kyi_Leo_Maltese_Lhasa_Apso_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kyi_Leo_Maltese_Lhasa_Apso_Mix"
    )

    # label: LIVE_MMLS_DOGS_Boykin_Spaniel
    # comment: Boykin Spaniel
    LIVE_MMLS_DOGS_Boykin_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boykin_Spaniel"
    )

    # label: CONS_GLAS
    # comment: Glassware
    CONS_GLAS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_GLAS"
    )

    # label: LIVE_MMLS_DOGS_Portuguese_Podengo_Pequeno
    # comment: Portuguese Podengo Pequeno
    LIVE_MMLS_DOGS_Portuguese_Podengo_Pequeno = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Portuguese_Podengo_Pequeno"
    )

    # label: LIVE_MMLS_DOGS_Norwegian_Elkhound
    # comment: Norwegian Elkhound
    LIVE_MMLS_DOGS_Norwegian_Elkhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwegian_Elkhound"
    )

    # label: LIVE_MMLS_DOGS_Swedish_Vallhund
    # comment: Swedish Vallhund
    LIVE_MMLS_DOGS_Swedish_Vallhund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Swedish_Vallhund"
    )

    # label: VHCL_SVCL_AUTO
    # comment: Automobiles
    VHCL_SVCL_AUTO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_AUTO"
    )

    # label: VHCL_SVCL_MOTO
    # comment: Motorcycles
    VHCL_SVCL_MOTO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_MOTO"
    )

    # label: LIVE_MMLS_DOGS_Keeshond
    # comment: Keeshond
    LIVE_MMLS_DOGS_Keeshond = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Keeshond"
    )

    # label: CHEM_COSM_COSD
    # comment: Cosmetics - DGR
    CHEM_COSM_COSD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_COSM_COSD"
    )

    # label: PHAR_BIOP_SMPL
    # comment: Samples
    PHAR_BIOP_SMPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_SMPL"
    )

    # label: CONS_HSER
    # comment: House removal
    CONS_HSER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HSER"
    )

    # label: CONS_PERS
    # comment: Personal effects
    CONS_PERS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_PERS"
    )

    # label: LIVE_MMLS_DOGS_Saluki
    # comment: Saluki
    LIVE_MMLS_DOGS_Saluki = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Saluki"
    )

    # label: LIVE_MMLS_DOGS_Schnoodle_Schnauzer_Poodle_Mix
    # comment: Schnoodle-Schnauzer Poodle Mix
    LIVE_MMLS_DOGS_Schnoodle_Schnauzer_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Schnoodle_Schnauzer_Poodle_Mix"
    )

    # label: LIVE_MMLS_DOGS_Havanese
    # comment: Havanese
    LIVE_MMLS_DOGS_Havanese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Havanese"
    )

    # label: VHCL_AIRC_HPRT
    # comment: Helicopter parts
    VHCL_AIRC_HPRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_HPRT"
    )

    # label: LIVE_MMLS_DOGS_Belgian_Malinois
    # comment: Belgian Malinois
    LIVE_MMLS_DOGS_Belgian_Malinois = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Belgian_Malinois"
    )

    # label: FLWR_HERBS
    # comment: Herbs, Leaves and Foliage
    FLWR_HERBS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_HERBS"
    )

    # label: LIVE_MMLS_DOGS_Neapolitan_Mastiff
    # comment: Neapolitan Mastiff
    LIVE_MMLS_DOGS_Neapolitan_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Neapolitan_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_Japanese_Chin
    # comment: Japanese Chin
    LIVE_MMLS_DOGS_Japanese_Chin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Chin"
    )

    # label: FLWR_FLWR_TULP
    # comment: Fresh tulips
    FLWR_FLWR_TULP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR_TULP"
    )

    # label: VHCL_MACH_PUEQ
    # comment: Pumping equipment
    VHCL_MACH_PUEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_PUEQ"
    )

    # label: LIVE_MMLS_CATL
    # comment: Cattle
    LIVE_MMLS_CATL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATL"
    )

    # label: CHEM_CNDG
    # comment: Chemicals - Not dangerous
    CHEM_CNDG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CNDG"
    )

    # label: LIVE_MMLS_CATS_Somali
    # comment: Somali
    LIVE_MMLS_CATS_Somali = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Somali"
    )

    # label: LIVE_MMLS_CATS_British_Shorthair
    # comment: British Shorthair
    LIVE_MMLS_CATS_British_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_British_Shorthair"
    )

    # label: LIVE_MMLS_CATS_Turkish_Van
    # comment: Turkish Van
    LIVE_MMLS_CATS_Turkish_Van = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Turkish_Van"
    )

    # label: LIVE_MMLS_DOGS_Parson_Russell_Terrier
    # comment: Parson Russell Terrier
    LIVE_MMLS_DOGS_Parson_Russell_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Parson_Russell_Terrier"
    )

    # label: CHEM_REAG
    # comment: Reagents
    CHEM_REAG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_REAG"
    )

    # label: TXTL_LTWR
    # comment: Leather wear
    TXTL_LTWR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_LTWR"
    )

    # label: LIVE_MMLS_DOGS_Sheepadoodle_Old_English_Sheepdog_Poodle_Mix
    # comment: Sheepadoodle-Old English Sheepdog Poodle Mix
    LIVE_MMLS_DOGS_Sheepadoodle_Old_English_Sheepdog_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sheepadoodle_Old_English_Sheepdog_Poodle_Mix"
    )

    # label: ELEC_QUAN
    # comment: Quantum
    ELEC_QUAN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_QUAN"
    )

    # label: FOOD_BVRG_COFY
    # comment: Coffee
    FOOD_BVRG_COFY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_COFY"
    )

    # label: LIVE_MMLS_DOGS_American_Eskimo_Dog_Standard
    # comment: American Eskimo Dog-Standard
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Standard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Eskimo_Dog_Standard"
    )

    # label: CONS_FRNT
    # comment: Furniture
    CONS_FRNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_FRNT"
    )

    # label: LIVE_MMLS_DOGS_Papillon
    # comment: Papillon
    LIVE_MMLS_DOGS_Papillon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Papillon"
    )

    # label: RAWM_GUMS
    # comment: Gums-Resines
    RAWM_GUMS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_GUMS"
    )

    # label: LIVE_MMLS_DOGS_Siberian_Husky
    # comment: Siberian Husky
    LIVE_MMLS_DOGS_Siberian_Husky = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Siberian_Husky"
    )

    # label: LIVE_MMLS_DOGS_Old_English_Sheepdog
    # comment: Old English Sheepdog
    LIVE_MMLS_DOGS_Old_English_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Old_English_Sheepdog"
    )

    # label: LIVE_MMLS_DOGS_American_English_Coonhound
    # comment: American English Coonhound
    LIVE_MMLS_DOGS_American_English_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_English_Coonhound"
    )

    # label: TXTL_TXLW_CLTH
    # comment: Clothing
    TXTL_TXLW_CLTH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_CLTH"
    )

    # label: FOOD_FISH_CAVR
    # comment: Caviar
    FOOD_FISH_CAVR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_CAVR"
    )

    # label: FOOD_FRTV_PROD
    # comment: Produce
    FOOD_FRTV_PROD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PROD"
    )

    # label: PHAR_MEDI
    # comment: Medical
    PHAR_MEDI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MEDI"
    )

    # label: RAWM_CLAY
    # comment: Clay products
    RAWM_CLAY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_CLAY"
    )

    # label: RAWM_STNS
    # comment: Stones
    RAWM_STNS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_STNS"
    )

    # label: LIVE_MMLS_DOGS_Rottweiler
    # comment: Rottweiler
    LIVE_MMLS_DOGS_Rottweiler = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Rottweiler"
    )

    # label: LIVE_REPT
    # comment: Reptiles
    LIVE_REPT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_REPT"
    )

    # label: LIVE_MMLS_DOGS_Finnish_Lapphund
    # comment: Finnish Lapphund
    LIVE_MMLS_DOGS_Finnish_Lapphund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Finnish_Lapphund"
    )

    # label: VHCL_AIRC_HELI
    # comment: Helicopter
    VHCL_AIRC_HELI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_HELI"
    )

    # label: LIVE_MMLS_DOGS_American_Cocker_Spaniel
    # comment: American Cocker Spaniel
    LIVE_MMLS_DOGS_American_Cocker_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Cocker_Spaniel"
    )

    # label: CHEM_PAIN
    # comment: Paint
    CHEM_PAIN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_PAIN"
    )

    # label: LIVE_MMLS_CATS_Peterbald
    # comment: Peterbald
    LIVE_MMLS_CATS_Peterbald = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Peterbald"
    )

    # label: MLTY_SPWE
    # comment: Sporting weapons
    MLTY_SPWE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_SPWE"
    )

    # label: VHCL
    # comment: Vehicle / Machinary, Parts, Spares
    VHCL = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL")

    # label: FOOD_DARY_CHSE
    # comment: Cheese
    FOOD_DARY_CHSE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY_CHSE"
    )

    # label: LIVE_MMLS_CATS_Manx
    # comment: Manx
    LIVE_MMLS_CATS_Manx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Manx"
    )

    # label: FOOD_FRTV_CHER
    # comment: Cherries
    FOOD_FRTV_CHER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_CHER"
    )

    # label: CONS_CMPY
    # comment: Company material
    CONS_CMPY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_CMPY"
    )

    # label: LIVE_MMLS_DOGS_Pomsky_Pomeranian_Siberian_Husky_Mix
    # comment: Pomsky-Pomeranian Siberian Husky Mix
    LIVE_MMLS_DOGS_Pomsky_Pomeranian_Siberian_Husky_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomsky_Pomeranian_Siberian_Husky_Mix"
    )

    # label: LIVE_MMLS_DOGS_Ba_Shar_Basset_Hound_Shar_pei_Mix
    # comment: Ba Shar-Basset Hound Shar pei Mix
    LIVE_MMLS_DOGS_Ba_Shar_Basset_Hound_Shar_pei_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Ba_Shar_Basset_Hound_Shar_pei_Mix"
    )

    # label: LIVE_MMLS_DOGS_Pyrenean_Shepherd
    # comment: Pyrenean Shepherd
    LIVE_MMLS_DOGS_Pyrenean_Shepherd = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pyrenean_Shepherd"
    )

    # label: TXTL_TXEW_SKIN
    # comment: Skins
    TXTL_TXEW_SKIN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_SKIN"
    )

    # label: LIVE_MMLS_DOGS_Belgian_Sheepdog
    # comment: Belgian Sheepdog
    LIVE_MMLS_DOGS_Belgian_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Belgian_Sheepdog"
    )

    # label: LIVE_MMLS_DOGS_Boxer
    # comment: Boxer
    LIVE_MMLS_DOGS_Boxer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boxer"
    )

    # label: LIVE_MMLS_DOGS_Australian_Terrier
    # comment: Australian Terrier
    LIVE_MMLS_DOGS_Australian_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Australian_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Kuvasz
    # comment: Kuvasz
    LIVE_MMLS_DOGS_Kuvasz = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kuvasz"
    )

    # label: LIVE_MMLS_DOGS_South_African_Mastiff
    # comment: South African Mastiff
    LIVE_MMLS_DOGS_South_African_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_South_African_Mastiff"
    )

    # label: RAWM_METP
    # comment: Metal products
    RAWM_METP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_METP"
    )

    # label: FOOD_TBCO
    # comment: Tobacco products
    FOOD_TBCO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_TBCO"
    )

    # label: VALU_PMET
    # comment: Precious metal
    VALU_PMET = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_PMET"
    )

    # label: ELEC
    # comment: Electronic equipment
    ELEC = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC")

    # label: LIVE_MMLS_DOGS_Chiweenie_Chihuahua_Dachshund_Mix
    # comment: Chiweenie-Chihuahua Dachshund Mix
    LIVE_MMLS_DOGS_Chiweenie_Chihuahua_Dachshund_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chiweenie_Chihuahua_Dachshund_Mix"
    )

    # label: LIVE_MMLS_DOGS_Irish_Setter
    # comment: Irish Setter
    LIVE_MMLS_DOGS_Irish_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Setter"
    )

    # label: LIVE_MMLS_CATS_Chausie
    # comment: Chausie
    LIVE_MMLS_CATS_Chausie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Chausie"
    )

    # label: LIVE_MMLS_DOGS_Valley_Bulldog
    # comment: Valley Bulldog
    LIVE_MMLS_DOGS_Valley_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Valley_Bulldog"
    )

    # label: LIVE_LFSH
    # comment: Fish
    LIVE_LFSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH"
    )

    # label: LIVE_MMLS_DOGS_Alangu_Mastiff
    # comment: Alangu Mastiff
    LIVE_MMLS_DOGS_Alangu_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Alangu_Mastiff"
    )

    # label: FOOD_MEAT
    # comment: Meat products
    FOOD_MEAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT"
    )

    # label: LIVE_MMLS_CATS_Persian
    # comment: Persian
    LIVE_MMLS_CATS_Persian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Persian"
    )

    # label: LIVE_MMLS_SHEP
    # comment: Sheep
    LIVE_MMLS_SHEP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_SHEP"
    )

    # label: LIVE_MLKS
    # comment: Mollusks
    LIVE_MLKS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MLKS"
    )

    # label: LIVE_MMLS_DOGS_Norwich_Terrier
    # comment: Norwich Terrier
    LIVE_MMLS_DOGS_Norwich_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwich_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Staffordshire_Bull_Terrier
    # comment: Staffordshire Bull Terrier
    LIVE_MMLS_DOGS_Staffordshire_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Staffordshire_Bull_Terrier"
    )

    # label: FOOD_MEAT_HRSP
    # comment: Horse products
    FOOD_MEAT_HRSP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_HRSP"
    )

    # label: FOOD_FRTV_MLNS
    # comment: Melons
    FOOD_FRTV_MLNS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_MLNS"
    )

    # label: FOOD_FISH_SFSH
    # comment: Smoked fish
    FOOD_FISH_SFSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SFSH"
    )

    # label: FOOD_STUF
    # comment: Foodstuffs
    FOOD_STUF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF"
    )

    # label: LIVE_MMLS_DOGS_Soft_Coated_Wheaten_Terrier
    # comment: Soft-Coated Wheaten Terrier
    LIVE_MMLS_DOGS_Soft_Coated_Wheaten_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Soft_Coated_Wheaten_Terrier"
    )

    # label: LIVE_MMLS_CATS_Safari
    # comment: Safari
    LIVE_MMLS_CATS_Safari = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Safari"
    )

    # label: LIVE_MMLS_DOGS_Tibetan_Spaniel
    # comment: Tibetan Spaniel
    LIVE_MMLS_DOGS_Tibetan_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tibetan_Spaniel"
    )

    # label: LIVE_MMLS_DOGS_Olde_English_Bulldog
    # comment: Olde English Bulldog
    LIVE_MMLS_DOGS_Olde_English_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Olde_English_Bulldog"
    )

    # label: LIVE_MMLS_DOGS_Schipperke
    # comment: Schipperke
    LIVE_MMLS_DOGS_Schipperke = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Schipperke"
    )

    # label: LIVE_MMLS_DOGS_Bullmastiff
    # comment: Bullmastiff
    LIVE_MMLS_DOGS_Bullmastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bullmastiff"
    )

    # label: LIVE_MMLS_DOGS_Pharaoh_Hound
    # comment: Pharaoh Hound
    LIVE_MMLS_DOGS_Pharaoh_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pharaoh_Hound"
    )

    # label: FOOD_FRTV_BEAN
    # comment: String beans
    FOOD_FRTV_BEAN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_BEAN"
    )

    # label: FOOD_FRTV_PPYA
    # comment: Papaya
    FOOD_FRTV_PPYA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PPYA"
    )

    # label: LIVE_BRDH_PARR
    # comment: Parrots
    LIVE_BRDH_PARR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_PARR"
    )

    # label: LIVE_MMLS_DOGS_Glen_of_Imaal_Terrier
    # comment: Glen of Imaal Terrier
    LIVE_MMLS_DOGS_Glen_of_Imaal_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Glen_of_Imaal_Terrier"
    )

    # label: VHCL_MACH_COIL
    # comment: Cable coil
    VHCL_MACH_COIL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_COIL"
    )

    # label: TXTL_TXEW_NDLE
    # comment: Needlework
    TXTL_TXEW_NDLE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_NDLE"
    )

    # label: CONS_SPEC
    # comment: Spectacles
    CONS_SPEC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_SPEC"
    )

    # label: LIVE_MMLS_CATS_Selkirk_Rex
    # comment: Selkirk Rex
    LIVE_MMLS_CATS_Selkirk_Rex = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Selkirk_Rex"
    )

    # label: LIVE_MMLS_DOGS_Wirehaired_Pointing_Griffon
    # comment: Wirehaired Pointing Griffon
    LIVE_MMLS_DOGS_Wirehaired_Pointing_Griffon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Wirehaired_Pointing_Griffon"
    )

    # label: LIVE_MMLS_DOGS_Saint_Bernard
    # comment: Saint Bernard
    LIVE_MMLS_DOGS_Saint_Bernard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Saint_Bernard"
    )

    # label: FOOD_FRTV_PEPP
    # comment: Peppers
    FOOD_FRTV_PEPP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PEPP"
    )

    # label: VHCL_MACH_HRDW
    # comment: Hardware and Equipment
    VHCL_MACH_HRDW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_HRDW"
    )

    # label: LIVE_MMLS_DOGS_Kangal_Shepherd_Dog
    # comment: Kangal Shepherd Dog
    LIVE_MMLS_DOGS_Kangal_Shepherd_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kangal_Shepherd_Dog"
    )

    # label: LIVE_MMLS_DOGS_Clumber_Spaniel
    # comment: Clumber Spaniel
    LIVE_MMLS_DOGS_Clumber_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Clumber_Spaniel"
    )

    # label: LIVE_MMLS_CATS_Savannah
    # comment: Savannah
    LIVE_MMLS_CATS_Savannah = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Savannah"
    )

    # label: VHCL_MACH_OILD
    # comment: Oil drilling equipment
    VHCL_MACH_OILD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_OILD"
    )

    # label: LIVE_MMLS_CATS_Javanese
    # comment: Javanese
    LIVE_MMLS_CATS_Javanese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Javanese"
    )

    # label: LIVE_MMLS_DOGS_Poochon_Poodle_Bichon_Frise_Mix
    # comment: Poochon-Poodle Bichon Frise Mix
    LIVE_MMLS_DOGS_Poochon_Poodle_Bichon_Frise_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Poochon_Poodle_Bichon_Frise_Mix"
    )

    # label: TXTL_TXEW_FURN
    # comment: Textile furnish
    TXTL_TXEW_FURN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_FURN"
    )

    # label: LIVE_MMLS_DOGS_Puggle_Pug_Beagle_Mix
    # comment: Puggle-Pug Beagle Mix
    LIVE_MMLS_DOGS_Puggle_Pug_Beagle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Puggle_Pug_Beagle_Mix"
    )

    # label: RAWM_MARB
    # comment: Marble
    RAWM_MARB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MARB"
    )

    # label: LIVE_MMLS_DOGS_Brussels_Griffon
    # comment: Brussels Griffon
    LIVE_MMLS_DOGS_Brussels_Griffon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Brussels_Griffon"
    )

    # label: LIVE_MMLS_DOGS_American_Foxhound
    # comment: American Foxhound
    LIVE_MMLS_DOGS_American_Foxhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Foxhound"
    )

    # label: LIVE_MMLS_DOGS_Newfoundland
    # comment: Newfoundland
    LIVE_MMLS_DOGS_Newfoundland = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Newfoundland"
    )

    # label: FOOD_FISH_REPA
    # comment: Reineta and Palometa
    FOOD_FISH_REPA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_REPA"
    )

    # label: LIVE_MMLS_DOGS_Cardigan_Welsh_Corgi
    # comment: Cardigan Welsh Corgi
    LIVE_MMLS_DOGS_Cardigan_Welsh_Corgi = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cardigan_Welsh_Corgi"
    )

    # label: LIVE_MMLS_CATS_Tiffany
    # comment: Tiffany
    LIVE_MMLS_CATS_Tiffany = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Tiffany"
    )

    # label: TXTL_TXLW
    # comment: Textile wear
    TXTL_TXLW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW"
    )

    # label: LIVE_MMLS_CATS_Singapura
    # comment: Singapura
    LIVE_MMLS_CATS_Singapura = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Singapura"
    )

    # label: LIVE_MMLS_DOGS_American_Water_Spaniel
    # comment: American Water Spaniel
    LIVE_MMLS_DOGS_American_Water_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Water_Spaniel"
    )

    # label: FOOD_FRTV_BERR
    # comment: Berries
    FOOD_FRTV_BERR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_BERR"
    )

    # label: LIVE_MMLS_DOGS_Irish_Red_and_White_Setter
    # comment: Irish Red and White Setter
    LIVE_MMLS_DOGS_Irish_Red_and_White_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Red_and_White_Setter"
    )

    # label: FOOD_FISH_HAKE
    # comment: Hake
    FOOD_FISH_HAKE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_HAKE"
    )

    # label: LIVE_MMLS_DOGS_Gordon_Setter
    # comment: Gordon Setter
    LIVE_MMLS_DOGS_Gordon_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Gordon_Setter"
    )

    # label: LIVE_MMLS_DOGS_Jack_Chi_Chihuahua_Jack_Russell_Terrier_Mix
    # comment: Jack Chi-Chihuahua Jack Russell Terrier Mix
    LIVE_MMLS_DOGS_Jack_Chi_Chihuahua_Jack_Russell_Terrier_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Jack_Chi_Chihuahua_Jack_Russell_Terrier_Mix"
    )

    # label: LIVE_LFSH_EELS
    # comment: Eels
    LIVE_LFSH_EELS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH_EELS"
    )

    # label: LIVE_MMLS_DOGS_Boweimar_Boxer_Weimaraner_Mix
    # comment: Boweimar-Boxer Weimaraner Mix
    LIVE_MMLS_DOGS_Boweimar_Boxer_Weimaraner_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boweimar_Boxer_Weimaraner_Mix"
    )

    # label: LIVE_MMLS_DOGS_Malti_Zu_Maltese_Shih_Tzu_Mix
    # comment: Malti Zu-Maltese Shih Tzu Mix
    LIVE_MMLS_DOGS_Malti_Zu_Maltese_Shih_Tzu_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Malti_Zu_Maltese_Shih_Tzu_Mix"
    )

    # label: LIVE_MMLS_CATS_Himalayan
    # comment: Himalayan
    LIVE_MMLS_CATS_Himalayan = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Himalayan"
    )

    # label: PHAR_BIOP_LHOR
    # comment: Live human organs
    PHAR_BIOP_LHOR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_LHOR"
    )

    # label: VHCL_AIRC_AWHL
    # comment: Aircraft wheels
    VHCL_AIRC_AWHL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AWHL"
    )

    # label: RAWM_WOOD
    # comment: Wood products
    RAWM_WOOD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_WOOD"
    )

    # label: TXTL_FUR
    # comment: Fur
    TXTL_FUR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_FUR")

    # label: FOOD_FRTV_STRW
    # comment: Strawberries
    FOOD_FRTV_STRW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_STRW"
    )

    # label: LIVE_MMLS_CATS_Norwegian_Forest
    # comment: Norwegian Forest
    LIVE_MMLS_CATS_Norwegian_Forest = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Norwegian_Forest"
    )

    # label: LIVE_MMLS_DOGS_Norwegian_Buhund
    # comment: Norwegian Buhund
    LIVE_MMLS_DOGS_Norwegian_Buhund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwegian_Buhund"
    )

    # label: LIVE_MMLS_DOGS_Labradane_Labrador_Retriever_Great_Dane_Mix
    # comment: Labradane-Labrador Retriever Great Dane Mix
    LIVE_MMLS_DOGS_Labradane_Labrador_Retriever_Great_Dane_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labradane_Labrador_Retriever_Great_Dane_Mix"
    )

    # label: LIVE_MMLS_DOGS_Black_Russian_Terrier
    # comment: Black Russian Terrier
    LIVE_MMLS_DOGS_Black_Russian_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Black_Russian_Terrier"
    )

    # label: RAWM
    # comment: Raw materials (Construction, Metals, Wood, Minerals, Plastic)
    RAWM = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM")

    # label: FOOD_FRTV_GRAP
    # comment: Grapes
    FOOD_FRTV_GRAP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_GRAP"
    )

    # label: LIVE_MMLS_DOGS_Beagle
    # comment: Beagle
    LIVE_MMLS_DOGS_Beagle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Beagle"
    )

    # label: LIVE_MMLS_DOGS_Pyrenean_Mastiff
    # comment: Pyrenean Mastiff
    LIVE_MMLS_DOGS_Pyrenean_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pyrenean_Mastiff"
    )

    # label: LIVE_MMLS_CATS_Cymric
    # comment: Cymric
    LIVE_MMLS_CATS_Cymric = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Cymric"
    )

    # label: LIVE_MMLS_DOGS_Cocker_Spaniel
    # comment: Cocker Spaniel
    LIVE_MMLS_DOGS_Cocker_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cocker_Spaniel"
    )

    # label: TXTL_TXEW_CARP
    # comment: Carpets and Rugs
    TXTL_TXEW_CARP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_CARP"
    )

    # label: SCIN_OPTI
    # comment: Optical instruments
    SCIN_OPTI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_OPTI"
    )

    # label: LIVE_MMLS_DOGS_Dachshund
    # comment: Dachshund
    LIVE_MMLS_DOGS_Dachshund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dachshund"
    )

    # label: LIVE_MMLS_RDNT
    # comment: Rodents
    LIVE_MMLS_RDNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_RDNT"
    )

    # label: CHEM
    # comment: Chemicals
    CHEM = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM")

    # label: FOOD_FISH_ALBA
    # comment: Albacora
    FOOD_FISH_ALBA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_ALBA"
    )

    # label: ELEC_EGDS
    # comment: Electronic goods
    ELEC_EGDS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_EGDS"
    )

    # label: LIVE_MMLS_CATS_American_Bobtail
    # comment: American Bobtail
    LIVE_MMLS_CATS_American_Bobtail = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Bobtail"
    )

    # label: RAWM_RUBR_RTYR
    # comment: Rubber tyres
    RAWM_RUBR_RTYR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_RUBR_RTYR"
    )

    # label: LIVE_MMLS_DOGS_Miniature_Pinscher
    # comment: Miniature Pinscher
    LIVE_MMLS_DOGS_Miniature_Pinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_Pinscher"
    )

    # label: LIVE_MMLS_DOGS_Pomapoo_Pomeranian_Poodle_Mix
    # comment: Pomapoo-Pomeranian Poodle Mix
    LIVE_MMLS_DOGS_Pomapoo_Pomeranian_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomapoo_Pomeranian_Poodle_Mix"
    )

    # label: FOOD_DARY_EGGS
    # comment: Eggs
    FOOD_DARY_EGGS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY_EGGS"
    )

    # label: CHEM_DICE
    # comment: Dry ice
    CHEM_DICE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_DICE"
    )

    # label: LIVE_MMLS_DOGS_Shetland_Sheepdog
    # comment: Shetland Sheepdog
    LIVE_MMLS_DOGS_Shetland_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shetland_Sheepdog"
    )

    # label: FOOD_FRTV_BANA
    # comment: Bananas
    FOOD_FRTV_BANA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_BANA"
    )

    # label: LIVE_MMLS_DOGS_Dogo_Argentino
    # comment: Dogo Argentino
    LIVE_MMLS_DOGS_Dogo_Argentino = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dogo_Argentino"
    )

    # label: VHCL_AIRC_ASUP
    # comment: Aircraft supplies
    VHCL_AIRC_ASUP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_ASUP"
    )

    # label: TXTL_TXLW_FOOT
    # comment: Footwear
    TXTL_TXLW_FOOT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_FOOT"
    )

    # label: LIVE_MMLS_DOGS_Yorkipoo_Yorkshire_Terrier_Poodle_Mix
    # comment: Yorkipoo-Yorkshire Terrier Poodle Mix
    LIVE_MMLS_DOGS_Yorkipoo_Yorkshire_Terrier_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Yorkipoo_Yorkshire_Terrier_Poodle_Mix"
    )

    # label: LIVE_MMLS_DOGS_Chihuahua
    # comment: Chihuahua
    LIVE_MMLS_DOGS_Chihuahua = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chihuahua"
    )

    # label: PHAR_MDCN_ANTB
    # comment: Antibiotics and Vitamins
    PHAR_MDCN_ANTB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN_ANTB"
    )

    # label: LIVE_MMLS_DOGS_Basenji
    # comment: Basenji
    LIVE_MMLS_DOGS_Basenji = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Basenji"
    )

    # label: PHAR_MDCN_VETE
    # comment: Vetenary products
    PHAR_MDCN_VETE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN_VETE"
    )

    # label: LIVE_MMLS_DOGS_Greater_Swiss_Mountain_Dog
    # comment: Greater Swiss Mountain Dog
    LIVE_MMLS_DOGS_Greater_Swiss_Mountain_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Greater_Swiss_Mountain_Dog"
    )

    # label: LIVE_MMLS_DOGS_Dalmatian
    # comment: Dalmatian
    LIVE_MMLS_DOGS_Dalmatian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dalmatian"
    )

    # label: LIVE_MMLS_DOGS_Löwchen
    # comment: Löwchen
    LIVE_MMLS_DOGS_Löwchen = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Löwchen"
    )

    # label: FOOD_FISH_SLMN
    # comment: Salmon
    FOOD_FISH_SLMN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SLMN"
    )

    # label: VHCL_SHIP_SPAR
    # comment: Ship parts
    VHCL_SHIP_SPAR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SPAR"
    )

    # label: LIVE_MMLS_DOGS_Pugapoo_Pug_Poodle_Mix
    # comment: Pugapoo-Pug Poodle Mix
    LIVE_MMLS_DOGS_Pugapoo_Pug_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pugapoo_Pug_Poodle_Mix"
    )

    # label: LIVE_MMLS_FERR
    # comment: Ferrets
    LIVE_MMLS_FERR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_FERR"
    )

    # label: LIVE_MMLS_DOGS_English_Setter
    # comment: English Setter
    LIVE_MMLS_DOGS_English_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Setter"
    )

    # label: LIVE_MMLS_DOGS_Cesky_Terrier
    # comment: Cesky Terrier
    LIVE_MMLS_DOGS_Cesky_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cesky_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Harrier
    # comment: Harrier
    LIVE_MMLS_DOGS_Harrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Harrier"
    )

    # label: LIVE_LFSH_TRPF
    # comment: Tropical fish
    LIVE_LFSH_TRPF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH_TRPF"
    )

    # label: LIVE_MMLS_DOGS_Tosa_Japanese_Mastiff
    # comment: Tosa-Japanese Mastiff
    LIVE_MMLS_DOGS_Tosa_Japanese_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tosa_Japanese_Mastiff"
    )

    # label: LIVE_MMLS_CATS_LaPerm
    # comment: LaPerm
    LIVE_MMLS_CATS_LaPerm = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_LaPerm"
    )

    # label: VHCL_AIRC
    # comment: Aircraft
    VHCL_AIRC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC"
    )

    # label: LIVE_MMLS_DOGS_Puli
    # comment: Puli
    LIVE_MMLS_DOGS_Puli = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Puli"
    )

    # label: FOOD_BVRG_TEA
    # comment: Tea
    FOOD_BVRG_TEA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_TEA"
    )

    # label: LIVE_MMLS_DOGS_German_Pinscher
    # comment: German Pinscher
    LIVE_MMLS_DOGS_German_Pinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Pinscher"
    )

    # label: GENE
    # comment: General Cargo
    GENE = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#GENE")

    # label: CHEM_CNMD
    # comment: Chemicals - Not Medical
    CHEM_CNMD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CNMD"
    )

    # label: LIVE_MMLS_DOGS_West_Highland_White_Terrier
    # comment: West Highland White Terrier
    LIVE_MMLS_DOGS_West_Highland_White_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_West_Highland_White_Terrier"
    )

    # label: CONS_HHGD
    # comment: Household goods
    CONS_HHGD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HHGD"
    )

    # label: LIVE_MMLS_DOGS_King_Charles_Spaniel
    # comment: King Charles Spaniel
    LIVE_MMLS_DOGS_King_Charles_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_King_Charles_Spaniel"
    )

    # label: LIVE_MMLS_DOGS_Chesapeake_Bay_Retriever
    # comment: Chesapeake Bay Retriever
    LIVE_MMLS_DOGS_Chesapeake_Bay_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chesapeake_Bay_Retriever"
    )

    # label: LIVE_MMLS_DOGS_Maltese
    # comment: Maltese
    LIVE_MMLS_DOGS_Maltese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Maltese"
    )

    # label: RAWM_PLST
    # comment: Plastic products
    RAWM_PLST = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_PLST"
    )

    # label: ELEC_OFEQ
    # comment: Office equipment
    ELEC_OFEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_OFEQ"
    )

    # label: VHCL_MACH_PART
    # comment: Spare parts
    VHCL_MACH_PART = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_PART"
    )

    # label: LIVE_MMLS_DOGS_Bearded_Collie
    # comment: Bearded Collie
    LIVE_MMLS_DOGS_Bearded_Collie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bearded_Collie"
    )

    # label: LIVE_MMLS_CATS_Asian
    # comment: Asian
    LIVE_MMLS_CATS_Asian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Asian"
    )

    # label: LIVE_MMLS_DOGS_American_Eskimo_Dog_Miniature
    # comment: American Eskimo Dog-Miniature
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Miniature = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Eskimo_Dog_Miniature"
    )

    # label: LIVE_MMLS_CATS_Ocicat
    # comment: Ocicat
    LIVE_MMLS_CATS_Ocicat = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ocicat"
    )

    # label: LIVE_LFSH_KOIF
    # comment: Koi fish
    LIVE_LFSH_KOIF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH_KOIF"
    )

    # label: LIVE_MMLS_DOGS_Peekapoo_Pekingese_Poodle_Mix
    # comment: Peekapoo-Pekingese Poodle Mix
    LIVE_MMLS_DOGS_Peekapoo_Pekingese_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Peekapoo_Pekingese_Poodle_Mix"
    )

    # label: LIVE_MMLS_DOGS_German_Wirehaired_Pointer
    # comment: German Wirehaired Pointer
    LIVE_MMLS_DOGS_German_Wirehaired_Pointer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Wirehaired_Pointer"
    )

    # label: RAWM_RUBR
    # comment: Rubber products
    RAWM_RUBR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_RUBR"
    )

    # label: LIVE_MMLS_DOGS_Aussiedoodle
    # comment: Aussiedoodle
    LIVE_MMLS_DOGS_Aussiedoodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Aussiedoodle"
    )

    # label: LIVE_MMLS_CATS_Bombay
    # comment: Bombay
    LIVE_MMLS_CATS_Bombay = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Bombay"
    )

    # label: LIVE_MMLS_DOGS_Great_Pyrenees
    # comment: Great Pyrenees
    LIVE_MMLS_DOGS_Great_Pyrenees = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Great_Pyrenees"
    )

    # label: LIVE_MMLS_CATS_American_Wirehair
    # comment: American Wirehair
    LIVE_MMLS_CATS_American_Wirehair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Wirehair"
    )

    # label: FOOD_FRTV_PINE
    # comment: Pineapple
    FOOD_FRTV_PINE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PINE"
    )

    # label: LIVE_MMLS_DOGS_Chow_Pei_Chow_Chow_Shar_Pei_Mix
    # comment: Chow Pei-Chow Chow Shar Pei Mix
    LIVE_MMLS_DOGS_Chow_Pei_Chow_Chow_Shar_Pei_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chow_Pei_Chow_Chow_Shar_Pei_Mix"
    )

    # label: LIVE_MMLS_DOGS_Chow_Chow
    # comment: Chow Chow
    LIVE_MMLS_DOGS_Chow_Chow = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chow_Chow"
    )

    # label: PHAR_PHAR
    # comment: Pharmaceutical products
    PHAR_PHAR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_PHAR"
    )

    # label: CHEM_CLNG
    # comment: Cleaning products
    CHEM_CLNG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CLNG"
    )

    # label: LIVE_MMLS_DOGS_Standard_Schnauzer
    # comment: Standard Schnauzer
    LIVE_MMLS_DOGS_Standard_Schnauzer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Standard_Schnauzer"
    )

    # label: LIVE_MMLS_DOGS_Campeiro_Bulldog_Brazilian_Bulldog
    # comment: Campeiro Bulldog-Brazilian Bulldog
    LIVE_MMLS_DOGS_Campeiro_Bulldog_Brazilian_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Campeiro_Bulldog_Brazilian_Bulldog"
    )

    # label: MART
    # comment: Musical Instruments & Art
    MART = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MART")

    # label: LIVE_MMLS_CATS_Viverral_Hybrid_Cat
    # comment: Viverral-Hybrid Cat
    LIVE_MMLS_CATS_Viverral_Hybrid_Cat = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Viverral_Hybrid_Cat"
    )

    # label: FOOD_MEAT_SAUS
    # comment: Sausages
    FOOD_MEAT_SAUS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_SAUS"
    )

    # label: RAWM_BLDM
    # comment: Building material
    RAWM_BLDM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_BLDM"
    )

    # label: LIVE_MMLS_DOGS_American_Bully
    # comment: American Bully
    LIVE_MMLS_DOGS_American_Bully = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Bully"
    )

    # label: FOOD_FISH_FRZS
    # comment: Frozen seafood
    FOOD_FISH_FRZS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_FRZS"
    )

    # label: LIVE_MMLS_DOGS_Welsh_Terrier
    # comment: Welsh Terrier
    LIVE_MMLS_DOGS_Welsh_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Welsh_Terrier"
    )

    # label: VALU_WTCH
    # comment: Watches
    VALU_WTCH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_WTCH"
    )

    # label: LIVE
    # comment: Live Animals
    LIVE = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE")

    # label: PHAR_BIOP_SEME
    # comment: Semen
    PHAR_BIOP_SEME = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_SEME"
    )

    # label: PRIN_PPRP
    # comment: Paper products
    PRIN_PPRP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_PPRP"
    )

    # label: TXTL_FREW
    # comment: Furs excluding Wear
    TXTL_FREW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_FREW"
    )

    # label: LIVE_MMLS_DOGS_Welsh_Springer_Spaniel
    # comment: Welsh Springer Spaniel
    LIVE_MMLS_DOGS_Welsh_Springer_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Welsh_Springer_Spaniel"
    )

    # label: VHCL_AIRC_AENG
    # comment: Aicraft engines
    VHCL_AIRC_AENG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AENG"
    )

    # label: LIVE_MMLS_DOGS_Otterhound
    # comment: Otterhound
    LIVE_MMLS_DOGS_Otterhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Otterhound"
    )

    # label: FOOD_FISH_SHRI
    # comment: Shrimps and Prawns
    FOOD_FISH_SHRI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SHRI"
    )

    # label: VHCL_SHIP_SENG
    # comment: Engines and Turbines
    VHCL_SHIP_SENG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SENG"
    )

    # label: LIVE_MMLS_DOGS_Silky_Terrier
    # comment: Silky Terrier
    LIVE_MMLS_DOGS_Silky_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Silky_Terrier"
    )

    # label: FOOD_FRTV_MANG
    # comment: Mangoes
    FOOD_FRTV_MANG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_MANG"
    )

    # label: LIVE_MMLS_DOGS_Boerboel
    # comment: Boerboel
    LIVE_MMLS_DOGS_Boerboel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boerboel"
    )

    # label: LIVE_MMLS_DOGS_American_Hairless_Terrier
    # comment: American Hairless Terrier
    LIVE_MMLS_DOGS_American_Hairless_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Hairless_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Great_Dane
    # comment: Great Dane
    LIVE_MMLS_DOGS_Great_Dane = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Great_Dane"
    )

    # label: LIVE_MMLS_DOGS_Toy_Fox_Terrier
    # comment: Toy Fox Terrier
    LIVE_MMLS_DOGS_Toy_Fox_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Toy_Fox_Terrier"
    )

    # label: FOOD_MEAT_MEAT
    # comment: Meat
    FOOD_MEAT_MEAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_MEAT"
    )

    # label: HUMR
    # comment: Human Remains
    HUMR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#HUMR")

    # label: LIVE_MMLS_DOGS_Japanese_Spaniel
    # comment: Japanese Spaniel
    LIVE_MMLS_DOGS_Japanese_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Spaniel"
    )

    # label: LIVE_MMLS_DOGS_Bernedoodle
    # comment: Bernedoodle
    LIVE_MMLS_DOGS_Bernedoodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bernedoodle"
    )

    # label: SCIN_MEEQ
    # comment: Medical equipment
    SCIN_MEEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_MEEQ"
    )

    # label: CONS_UBAG
    # comment: Unaccompagnied baggage
    CONS_UBAG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_UBAG"
    )

    # label: LIVE_MMLS_DOGS_Chorkie_Chihuahua_Yorkshire_Terrier_Mix
    # comment: Chorkie-Chihuahua Yorkshire Terrier Mix
    LIVE_MMLS_DOGS_Chorkie_Chihuahua_Yorkshire_Terrier_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chorkie_Chihuahua_Yorkshire_Terrier_Mix"
    )

    # label: FLWR_PLNT_APLN
    # comment: Aquatic plants
    FLWR_PLNT_APLN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_APLN"
    )

    # label: VHCL_SVCL
    # comment: Surface vehicles
    VHCL_SVCL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL"
    )

    # label: LIVE_MMLS_CATS_Havana
    # comment: Havana
    LIVE_MMLS_CATS_Havana = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Havana"
    )

    # label: LIVE_MMLS_CATS_Chinese_Harlequin
    # comment: Chinese Harlequin
    LIVE_MMLS_CATS_Chinese_Harlequin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Chinese_Harlequin"
    )

    # label: LIVE_MMLS_DOGS_Sealyham_Terrier
    # comment: Sealyham Terrier
    LIVE_MMLS_DOGS_Sealyham_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sealyham_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Cockapoo_Cocker_Spaniel_Poodle_Mix
    # comment: Cockapoo-Cocker Spaniel Poodle Mix
    LIVE_MMLS_DOGS_Cockapoo_Cocker_Spaniel_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cockapoo_Cocker_Spaniel_Poodle_Mix"
    )

    # label: LIVE_MMLS_CATS_Desert_Lynx
    # comment: Desert Lynx
    LIVE_MMLS_CATS_Desert_Lynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Desert_Lynx"
    )

    # label: LIVE_MMLS
    # comment: Mammals
    LIVE_MMLS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS"
    )

    # label: LIVE_MMLS_DOGS_Flat_Coated_Retriever
    # comment: Flat-Coated Retriever
    LIVE_MMLS_DOGS_Flat_Coated_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Flat_Coated_Retriever"
    )

    # label: LIVE_MMLS_DOGS_Greyhound
    # comment: Greyhound
    LIVE_MMLS_DOGS_Greyhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Greyhound"
    )

    # label: LIVE_MMLS_DOGS_Norfolk_Terrier
    # comment: Norfolk Terrier
    LIVE_MMLS_DOGS_Norfolk_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norfolk_Terrier"
    )

    # label: TXTL_TXEW_YARN
    # comment: Yarns
    TXTL_TXEW_YARN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_YARN"
    )

    # label: FOOD_MEAT_BEEF
    # comment: Beef products
    FOOD_MEAT_BEEF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_BEEF"
    )

    # label: LIVE_MMLS_DOGS_Borzoi
    # comment: Borzoi
    LIVE_MMLS_DOGS_Borzoi = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Borzoi"
    )

    # label: LIVE_MMLS_DOGS_Labrador_Retriever
    # comment: Labrador Retriever
    LIVE_MMLS_DOGS_Labrador_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labrador_Retriever"
    )

    # label: TXTL_TXEW_FABR
    # comment: Textile fabric
    TXTL_TXEW_FABR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_FABR"
    )

    # label: LIVE_MMLS_DOGS_Manchester_Terrier
    # comment: Manchester Terrier
    LIVE_MMLS_DOGS_Manchester_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Manchester_Terrier"
    )

    # label: VALU_GOLD
    # comment: Gold
    VALU_GOLD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_GOLD"
    )

    # label: LIVE_MMLS_DOGS_French_Bulldog
    # comment: French Bulldog
    LIVE_MMLS_DOGS_French_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_French_Bulldog"
    )

    # label: LIVE_MMLS_DOGS_Nova_Scotia_Duck_Tolling_Retriever
    # comment: Nova Scotia Duck-Tolling Retriever
    LIVE_MMLS_DOGS_Nova_Scotia_Duck_Tolling_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Nova_Scotia_Duck_Tolling_Retriever"
    )

    # label: LIVE_MMLS_DOGS_Pit_Bull
    # comment: Pit Bull
    LIVE_MMLS_DOGS_Pit_Bull = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pit_Bull"
    )

    # label: FLWR_PLNT_MPLN
    # comment: Medicinal plants
    FLWR_PLNT_MPLN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_MPLN"
    )

    # label: LIVE_MMLS_DOGS_Pug
    # comment: Pug
    LIVE_MMLS_DOGS_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pug"
    )

    # label: VHCL_SVCL_CRTA
    # comment: Cartainer
    VHCL_SVCL_CRTA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_CRTA"
    )

    # label: LIVE_MMLS_DOGS_Bouvier_des_Flandres
    # comment: Bouvier des Flandres
    LIVE_MMLS_DOGS_Bouvier_des_Flandres = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bouvier_des_Flandres"
    )

    # label: LIVE_MMLS_DOGS_Field_Spaniel
    # comment: Field Spaniel
    LIVE_MMLS_DOGS_Field_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Field_Spaniel"
    )

    # label: CONS_SPRT
    # comment: Sports equipment
    CONS_SPRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_SPRT"
    )

    # label: LIVE_MMLS_DOGS_Collie
    # comment: Collie
    LIVE_MMLS_DOGS_Collie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Collie"
    )

    # label: LIVE_MMLS_DOGS_Dogue_de_Bordeaux
    # comment: Dogue de Bordeaux
    LIVE_MMLS_DOGS_Dogue_de_Bordeaux = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dogue_de_Bordeaux"
    )

    # label: FOOD
    # comment: Foodstuffs, Drinks and Tobacco
    FOOD = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD")

    # label: PHAR
    # comment: Pharmaceutical, Medical And Biological
    PHAR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR")

    # label: LIVE_MMLS_DOGS_Petit_Basset_Griffon_Vendéen
    # comment: Petit Basset Griffon Vendéen
    LIVE_MMLS_DOGS_Petit_Basset_Griffon_Vendéen = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Petit_Basset_Griffon_Vendéen"
    )

    # label: LIVE_MMLS_DOGS_Labradoodle_Labrador_Retriever_Poodle_Mix
    # comment: Labradoodle Labrador Retriever Poodle Mix
    LIVE_MMLS_DOGS_Labradoodle_Labrador_Retriever_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labradoodle_Labrador_Retriever_Poodle_Mix"
    )

    # label: LIVE_MMLS_DOGS_Bichon_Frise
    # comment: Bichon Frise
    LIVE_MMLS_DOGS_Bichon_Frise = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bichon_Frise"
    )

    # label: FOOD_STUF_CATE
    # comment: Catering products
    FOOD_STUF_CATE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_CATE"
    )

    # label: LIVE_MMLS_DOGS_Chinese_Crested_Dog
    # comment: Chinese Crested Dog
    LIVE_MMLS_DOGS_Chinese_Crested_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinese_Crested_Dog"
    )

    # label: LIVE_MMLS_DOGS_Bully_Kutta_Mastiff_breed
    # comment: Bully Kutta-Mastiff breed
    LIVE_MMLS_DOGS_Bully_Kutta_Mastiff_breed = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bully_Kutta_Mastiff_breed"
    )

    # label: LIVE_ZOOA
    # comment: Zoo animals
    LIVE_ZOOA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_ZOOA"
    )

    # label: LIVE_MMLS_DOGS_Russell_Terrier
    # comment: Russell Terrier
    LIVE_MMLS_DOGS_Russell_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Russell_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Pekingese
    # comment: Pekingese
    LIVE_MMLS_DOGS_Pekingese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pekingese"
    )

    # label: LIVE_MMLS_CATS_Color_Point_Shorthair
    # comment: Color Point Shorthair
    LIVE_MMLS_CATS_Color_Point_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Color_Point_Shorthair"
    )

    # label: VHCL_SHIP_SSPA
    # comment: Ship spares
    VHCL_SHIP_SSPA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SSPA"
    )

    # label: LIVE_MMLS_DOGS_Old_English_Bulldog
    # comment: Old English Bulldog
    LIVE_MMLS_DOGS_Old_English_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Old_English_Bulldog"
    )

    # label: FOOD_TBCO_CGRT
    # comment: Cigarettes
    FOOD_TBCO_CGRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_TBCO_CGRT"
    )

    # label: LIVE_MMLS_DOGS_Cairn_Terrier
    # comment: Cairn Terrier
    LIVE_MMLS_DOGS_Cairn_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cairn_Terrier"
    )

    # label: CHEM_COSM
    # comment: Cosmetics
    CHEM_COSM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_COSM"
    )

    # label: LIVE_MMLS_CATS_Turkish_Angora
    # comment: Turkish Angora
    LIVE_MMLS_CATS_Turkish_Angora = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Turkish_Angora"
    )

    # label: FOOD_FRTV_GARL
    # comment: Garlic
    FOOD_FRTV_GARL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_GARL"
    )

    # label: LIVE_MMLS_DOGS_Irish_Wolfhound
    # comment: Irish Wolfhound
    LIVE_MMLS_DOGS_Irish_Wolfhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Wolfhound"
    )

    # label: LIVE_MMLS_CATS_Tonkinese
    # comment: Tonkinese
    LIVE_MMLS_CATS_Tonkinese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Tonkinese"
    )

    # label: PRIN_DOCU
    # comment: Documents and Tickets
    PRIN_DOCU = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_DOCU"
    )

    # label: LIVE_MMLS_DOGS_Lakeland_Terrier
    # comment: Lakeland Terrier
    LIVE_MMLS_DOGS_Lakeland_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Lakeland_Terrier"
    )

    # label: TXTL_LEXW
    # comment: Leather excluding Wear
    TXTL_LEXW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_LEXW"
    )

    # label: LIVE_MMLS_DOGS_Mastino_Napoletano_Neopolitan_Mastiff
    # comment: Mastino Napoletano-Neopolitan Mastiff
    LIVE_MMLS_DOGS_Mastino_Napoletano_Neopolitan_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastino_Napoletano_Neopolitan_Mastiff"
    )

    # label: LIVE_MMLS_HORS
    # comment: Horses
    LIVE_MMLS_HORS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_HORS"
    )

    # label: LIVE_MMLS_CATS_Snowshoe
    # comment: Snowshoe
    LIVE_MMLS_CATS_Snowshoe = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Snowshoe"
    )

    # label: FOOD_FISH_FFSH
    # comment: Fresh fish
    FOOD_FISH_FFSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_FFSH"
    )

    # label: LIVE_MMLS_DOGS_Bull_Terrier
    # comment: Bull Terrier
    LIVE_MMLS_DOGS_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bull_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Golden_Retriever
    # comment: Golden Retriever
    LIVE_MMLS_DOGS_Golden_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Golden_Retriever"
    )

    # label: TXTL_LTHR
    # comment: Leather
    TXTL_LTHR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_LTHR"
    )

    # label: LIVE_MMLS_DOGS_Chipin_Chihuahua_Minature_Pinscher_Mix
    # comment: Chipin-Chihuahua Minature Pinscher Mix
    LIVE_MMLS_DOGS_Chipin_Chihuahua_Minature_Pinscher_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chipin_Chihuahua_Minature_Pinscher_Mix"
    )

    # label: FOOD_BVRG_WINE
    # comment: Wine
    FOOD_BVRG_WINE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_WINE"
    )

    # label: LIVE_MMLS_CATS_Ragamuffin
    # comment: Ragamuffin
    LIVE_MMLS_CATS_Ragamuffin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ragamuffin"
    )

    # label: LIVE_MMLS_DOGS_Chinese_Shar_Pei
    # comment: Chinese Shar Pei
    LIVE_MMLS_DOGS_Chinese_Shar_Pei = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinese_Shar_Pei"
    )

    # label: VHCL_AIRC_AACC
    # comment: Aircraft accessories
    VHCL_AIRC_AACC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AACC"
    )

    # label: LIVE_MMLS_DOGS_Chinook
    # comment: Chinook
    LIVE_MMLS_DOGS_Chinook = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinook"
    )

    # label: CHEM_PETRO
    # comment: Petroleum derivatives
    CHEM_PETRO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_PETRO"
    )

    # label: MLTY_WPNS
    # comment: Weapons
    MLTY_WPNS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_WPNS"
    )

    # label: LIVE_MMLS_DOGS_Bulli_Kutta
    # comment: Bulli Kutta
    LIVE_MMLS_DOGS_Bulli_Kutta = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bulli_Kutta"
    )

    # label: LIVE_MMLS_CATS_Pantherette
    # comment: Pantherette
    LIVE_MMLS_CATS_Pantherette = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Pantherette"
    )

    # label: LIVE_MMLS_CATS_Australian_Mist
    # comment: Australian Mist
    LIVE_MMLS_CATS_Australian_Mist = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Australian_Mist"
    )

    # label: LIVE_MMLS_CATS_Cornish_Rex
    # comment: Cornish Rex
    LIVE_MMLS_CATS_Cornish_Rex = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Cornish_Rex"
    )

    # label: FOOD_MEAT_GUTS
    # comment: Guts
    FOOD_MEAT_GUTS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_GUTS"
    )

    # label: LIVE_MMLS_DOGS_Jack_Russell_Terrier
    # comment: Jack Russell Terrier
    LIVE_MMLS_DOGS_Jack_Russell_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Jack_Russell_Terrier"
    )

    # label: TXTL_TXEW_TRLS
    # comment: Textile rolls
    TXTL_TXEW_TRLS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_TRLS"
    )

    # label: LIVE_MMLS_DOGS_Cavachon_King_Charles_Spaniel_Bichon_Frise
    # comment: Cavachon-King Charles Spaniel Bichon Frise
    LIVE_MMLS_DOGS_Cavachon_King_Charles_Spaniel_Bichon_Frise = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cavachon_King_Charles_Spaniel_Bichon_Frise"
    )

    # label: TXTL_TXEW_HIDE
    # comment: Hide
    TXTL_TXEW_HIDE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_HIDE"
    )

    # label: LIVE_MMLS_DOGS_Cavalier_King_Charles_Spaniel
    # comment: Cavalier King Charles Spaniel
    LIVE_MMLS_DOGS_Cavalier_King_Charles_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cavalier_King_Charles_Spaniel"
    )

    # label: VALU_BANK
    # comment: Bank notes and Coins
    VALU_BANK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_BANK"
    )

    # label: LIVE_MMLS_DOGS_American_Eskimo_Dog_Toy
    # comment: American Eskimo Dog-Toy
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Toy = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Eskimo_Dog_Toy"
    )

    # label: LIVE_MMLS_DOGS_Airedale_Terrier
    # comment: Airedale Terrier
    LIVE_MMLS_DOGS_Airedale_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Airedale_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Affenpinscher
    # comment: Affenpinscher
    LIVE_MMLS_DOGS_Affenpinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Affenpinscher"
    )

    # label: LIVE_MMLS_DOGS_American_Bulldog
    # comment: American Bulldog
    LIVE_MMLS_DOGS_American_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Bulldog"
    )

    # label: LIVE_MMLS_DOGS_Shar_Pei
    # comment: Shar Pei
    LIVE_MMLS_DOGS_Shar_Pei = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shar_Pei"
    )

    # label: LIVE_MMLS_DOGS_Ibizan_Hound
    # comment: Ibizan Hound
    LIVE_MMLS_DOGS_Ibizan_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Ibizan_Hound"
    )

    # label: LIVE_MMLS_DOGS_Australian_Shepherd
    # comment: Australian Shepherd
    LIVE_MMLS_DOGS_Australian_Shepherd = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Australian_Shepherd"
    )

    # label: RAWM_METL
    # comment: Metals
    RAWM_METL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_METL"
    )

    # label: LIVE_MMLS_DOGS_Coton_de_Tulear
    # comment: Coton de Tulear
    LIVE_MMLS_DOGS_Coton_de_Tulear = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Coton_de_Tulear"
    )

    # label: LIVE_MMLS_DOGS_Miniature_American_Shepherd
    # comment: Miniature American Shepherd
    LIVE_MMLS_DOGS_Miniature_American_Shepherd = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_American_Shepherd"
    )

    # label: TXTL_TXLW_APPR
    # comment: Wearing appareil
    TXTL_TXLW_APPR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_APPR"
    )

    # label: LIVE_MMLS_CATS_Vienna_Woods
    # comment: Vienna Woods
    LIVE_MMLS_CATS_Vienna_Woods = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Vienna_Woods"
    )

    # label: LIVE_MMLS_DOGS_Maltipoo_Maltese_Poodle_Mix
    # comment: Maltipoo-Maltese Poodle Mix
    LIVE_MMLS_DOGS_Maltipoo_Maltese_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Maltipoo_Maltese_Poodle_Mix"
    )

    # label: LIVE_MMLS_DOGS_Tibetan_Terrier
    # comment: Tibetan Terrier
    LIVE_MMLS_DOGS_Tibetan_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tibetan_Terrier"
    )

    # label: VALU_DIAM
    # comment: Diamonds
    VALU_DIAM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_DIAM"
    )

    # label: LIVE_MMLS_DOGS_Goldador_Golden_Retriever_Labrador_Retriever
    # comment: Goldador-Golden Retriever Labrador Retriever
    LIVE_MMLS_DOGS_Goldador_Golden_Retriever_Labrador_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Goldador_Golden_Retriever_Labrador_Retriever"
    )

    # label: LIVE_MMLS_DOGS_Rhodesian_Ridgeback
    # comment: Rhodesian Ridgeback
    LIVE_MMLS_DOGS_Rhodesian_Ridgeback = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Rhodesian_Ridgeback"
    )

    # label: ELEC_ELQP
    # comment: Electrical equipment
    ELEC_ELQP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_ELQP"
    )

    # label: ELEC_EEQP
    # comment: Electronic equipment
    ELEC_EEQP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_EEQP"
    )

    # label: TRPH_HTRH
    # comment: Hunting Trophies
    TRPH_HTRH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TRPH_HTRH"
    )

    # label: FLWR_SEED
    # comment: Seeds
    FLWR_SEED = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_SEED"
    )

    # label: LIVE_MMLS_DOGS_Goldendoodle_Golden_Retriever_Poodle_Mix
    # comment: Goldendoodle-Golden Retriever Poodle Mix
    LIVE_MMLS_DOGS_Goldendoodle_Golden_Retriever_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Goldendoodle_Golden_Retriever_Poodle_Mix"
    )

    # label: FOOD_BVRG_BEER
    # comment: Beer
    FOOD_BVRG_BEER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_BEER"
    )

    # label: LIVE_MMLS_DOGS_English_Toy_Spaniel
    # comment: English Toy Spaniel
    LIVE_MMLS_DOGS_English_Toy_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Toy_Spaniel"
    )

    # label: LIVE_MMLS_DOGS_Bulldog
    # comment: Bulldog
    LIVE_MMLS_DOGS_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bulldog"
    )

    # label: LIVE_MMLS_DOGS_Smooth_Fox_Terrier
    # comment: Smooth Fox Terrier
    LIVE_MMLS_DOGS_Smooth_Fox_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Smooth_Fox_Terrier"
    )

    # label: FLWR_FLWR_TFLW
    # comment: Tropical flowers
    FLWR_FLWR_TFLW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR_TFLW"
    )

    # label: LIVE_MMLS_CATS_Siamese
    # comment: Siamese
    LIVE_MMLS_CATS_Siamese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Siamese"
    )

    # label: FOOD_FRTV_ASPA
    # comment: Asparagus
    FOOD_FRTV_ASPA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_ASPA"
    )

    # label: RAWM_GLAS
    # comment: Glass products
    RAWM_GLAS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_GLAS"
    )

    # label: LIVE_MMLS_CATS_Ojos_Azules
    # comment: Ojos Azules
    LIVE_MMLS_CATS_Ojos_Azules = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ojos_Azules"
    )

    # label: LIVE_MMLS_CATS_Mojave_Spotted
    # comment: Mojave Spotted
    LIVE_MMLS_CATS_Mojave_Spotted = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Mojave_Spotted"
    )

    # label: LIVE_MMLS_DOGS_Canaan_Dog
    # comment: Canaan Dog
    LIVE_MMLS_DOGS_Canaan_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Canaan_Dog"
    )

    # label: FOOD_FISH
    # comment: Fish and Seafood
    FOOD_FISH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH"
    )

    # label: LIVE_MMLS_CATS_Burmese
    # comment: Burmese
    LIVE_MMLS_CATS_Burmese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Burmese"
    )

    # label: PHAR_MDCN
    # comment: Medicines
    PHAR_MDCN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN"
    )

    # label: TXTL_TXEW_CURT
    # comment: Curtains and Drapery
    TXTL_TXEW_CURT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_CURT"
    )

    # label: LIVE_MMLS_PIGS
    # comment: Pigs
    LIVE_MMLS_PIGS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_PIGS"
    )

    # label: VALU_JWRY
    # comment: Jewelery
    VALU_JWRY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_JWRY"
    )

    # label: LIVE_MMLS_CATS_Traditional_Siamese
    # comment: Traditional Siamese
    LIVE_MMLS_CATS_Traditional_Siamese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Traditional_Siamese"
    )

    # label: LIVE_MMLS_DOGS_Mastiff
    # comment: Mastiff
    LIVE_MMLS_DOGS_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastiff"
    )

    # label: VHCL_SVCL_BICY
    # comment: Bicycles
    VHCL_SVCL_BICY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_BICY"
    )

    # label: LIVE_MMLS_DOGS_Pomeranian
    # comment: Pomeranian
    LIVE_MMLS_DOGS_Pomeranian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomeranian"
    )

    # label: FOOD_STUF_NUTS
    # comment: Nuts
    FOOD_STUF_NUTS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_NUTS"
    )

    # label: LIVE_MMLS_CATS_Munchkin
    # comment: Munchkin
    LIVE_MMLS_CATS_Munchkin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Munchkin"
    )

    # label: VHCL_SVCL_TIRE
    # comment: Tires
    VHCL_SVCL_TIRE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_TIRE"
    )

    # label: LIVE_BRDH_TRKY
    # comment: Turkeys
    LIVE_BRDH_TRKY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_TRKY"
    )

    # label: LIVE_MMLS_CATS_Devon_Rex
    # comment: Devon Rex
    LIVE_MMLS_CATS_Devon_Rex = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Devon_Rex"
    )

    # label: LIVE_MMLS_CATS_American_Lynx
    # comment: American Lynx
    LIVE_MMLS_CATS_American_Lynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Lynx"
    )

    # label: LIVE_MMLS_DOGS_German_Shepherd_Dog
    # comment: German Shepherd Dog
    LIVE_MMLS_DOGS_German_Shepherd_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Shepherd_Dog"
    )

    # label: LIVE_MMLS_DOGS_Kerry_Blue_Terrier
    # comment: Kerry Blue Terrier
    LIVE_MMLS_DOGS_Kerry_Blue_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kerry_Blue_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Beauceron
    # comment: Beauceron
    LIVE_MMLS_DOGS_Beauceron = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Beauceron"
    )

    # label: CHEM_DGRG_EXPL
    # comment: Explosives
    CHEM_DGRG_EXPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_DGRG_EXPL"
    )

    # label: LIVE_MMLS_CATS_Sphynx
    # comment: Sphynx
    LIVE_MMLS_CATS_Sphynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Sphynx"
    )

    # label: LIVE_MMLS_DOGS_Yorkshire_Terrier
    # comment: Yorkshire Terrier
    LIVE_MMLS_DOGS_Yorkshire_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Yorkshire_Terrier"
    )

    # label: PHAR_BIOP_HEMO
    # comment: Hemoderivatives
    PHAR_BIOP_HEMO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_HEMO"
    )

    # label: LIVE_MMLS_DOGS_Argentinian_Mastiff
    # comment: Argentinian Mastiff
    LIVE_MMLS_DOGS_Argentinian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Argentinian_Mastiff"
    )

    # label: TRPH_OTRH
    # comment: Trophies (not hunting)
    TRPH_OTRH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TRPH_OTRH"
    )

    # label: MART_MUEQ
    # comment: Musical equipment
    MART_MUEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_MUEQ"
    )

    # label: LIVE_MMLS_CATS_California_Spangled
    # comment: California Spangled
    LIVE_MMLS_CATS_California_Spangled = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_California_Spangled"
    )

    # label: LIVE_MMLS_CATS_American_Polydactyl
    # comment: American Polydactyl
    LIVE_MMLS_CATS_American_Polydactyl = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Polydactyl"
    )

    # label: HUMR_HUMB
    # comment: Human remains not cremated
    HUMR_HUMB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#HUMR_HUMB"
    )

    # label: LIVE_MMLS_DOGS_Malt_Tzu_Maltese_Shih_Tzu_Mix
    # comment: Malt-Tzu-Maltese Shih Tzu Mix
    LIVE_MMLS_DOGS_Malt_Tzu_Maltese_Shih_Tzu_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Malt_Tzu_Maltese_Shih_Tzu_Mix"
    )

    # label: FOOD_FRTV
    # comment: Fruits and Vegetables
    FOOD_FRTV = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV"
    )

    # label: MLTY_AMUN
    # comment: Munitions
    MLTY_AMUN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_AMUN"
    )

    # label: LIVE_MMLS_DOGS_Brittany
    # comment: Brittany
    LIVE_MMLS_DOGS_Brittany = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Brittany"
    )

    # label: PRIN_BOOK
    # comment: Books
    PRIN_BOOK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_BOOK"
    )

    # label: LIVE_MMLS_DOGS_Portuguese_Water_Dog
    # comment: Portuguese Water Dog
    LIVE_MMLS_DOGS_Portuguese_Water_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Portuguese_Water_Dog"
    )

    # label: MAIL
    # comment: Mail
    MAIL = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MAIL")

    # label: MART_HAND
    # comment: Handicraft products
    MART_HAND = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_HAND"
    )

    # label: LIVE_MMLS_DOGS_Brazilian_Mastiff
    # comment: Brazilian Mastiff
    LIVE_MMLS_DOGS_Brazilian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Brazilian_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_Mastin_Espanol_Spanish_Mastiff
    # comment: Mastin Espanol-Spanish Mastiff
    LIVE_MMLS_DOGS_Mastin_Espanol_Spanish_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastin_Espanol_Spanish_Mastiff"
    )

    # label: FLWR_PLNT
    # comment: Plants
    FLWR_PLNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT"
    )

    # label: LIVE_MMLS_DOGS_Skye_Terrier
    # comment: Skye Terrier
    LIVE_MMLS_DOGS_Skye_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Skye_Terrier"
    )

    # label: LIVE_MMLS_DOGS_Entlebucher_Mountain_Dog
    # comment: Entlebucher Mountain Dog
    LIVE_MMLS_DOGS_Entlebucher_Mountain_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Entlebucher_Mountain_Dog"
    )

    # label: LIVE_INSC
    # comment: Insects
    LIVE_INSC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_INSC"
    )

    # label: LIVE_INSC_BEES
    # comment: Bees
    LIVE_INSC_BEES = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_INSC_BEES"
    )

    # label: LIVE_MMLS_DOGS_Mastador_Bullmastiff_Labrador_Retriever_Mix
    # comment: Mastador-Bullmastiff Labrador Retriever Mix
    LIVE_MMLS_DOGS_Mastador_Bullmastiff_Labrador_Retriever_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastador_Bullmastiff_Labrador_Retriever_Mix"
    )

    # label: LIVE_MMLS_DOGS_American_Pit_Bull_Terrier
    # comment: American Pit Bull Terrier
    LIVE_MMLS_DOGS_American_Pit_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Pit_Bull_Terrier"
    )

    # label: VALU_SLVR
    # comment: Silver
    VALU_SLVR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_SLVR"
    )

    # label: FOOD_STUF_SPCE
    # comment: Spices and Roots
    FOOD_STUF_SPCE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_SPCE"
    )

    # label: FOOD_FRTV_APPL
    # comment: Apples
    FOOD_FRTV_APPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_APPL"
    )

    # label: LIVE_MMLS_DOGS_Miniature_Schnauzer
    # comment: Miniature Schnauzer
    LIVE_MMLS_DOGS_Miniature_Schnauzer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_Schnauzer"
    )

    # label: FOOD_STUF_DFRU
    # comment: Dried fruit
    FOOD_STUF_DFRU = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_DFRU"
    )

    # label: LIVE_MMLS_DOGS_Pomchi_Pomeranian_Chihuahua_Mix
    # comment: Pomchi-Pomeranian Chihuahua Mix
    LIVE_MMLS_DOGS_Pomchi_Pomeranian_Chihuahua_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomchi_Pomeranian_Chihuahua_Mix"
    )

    # label: LIVE_MMLS_DOGS_Cavapoo_Cavalier_King_Charles_Spaniel_Poodle
    # comment: Cavapoo-Cavalier King Charles Spaniel Poodle
    LIVE_MMLS_DOGS_Cavapoo_Cavalier_King_Charles_Spaniel_Poodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cavapoo_Cavalier_King_Charles_Spaniel_Poodle"
    )

    # label: LIVE_MMLS_DOGS_Bull_Terrier_Miniature
    # comment: Bull Terrier-Miniature
    LIVE_MMLS_DOGS_Bull_Terrier_Miniature = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bull_Terrier_Miniature"
    )

    # label: CHEM_COSM_PERF
    # comment: Perfume
    CHEM_COSM_PERF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_COSM_PERF"
    )

    # label: FOOD_FRTV_MUSH
    # comment: Mushrooms
    FOOD_FRTV_MUSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_MUSH"
    )

    # label: FOOD_STUF_OOIL
    # comment: Olive oil
    FOOD_STUF_OOIL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_OOIL"
    )

    # label: LIVE_MMLS_DOGS_Shihpoo_Shih_Tzu_Poodle_Mix
    # comment: Shihpoo-Shih Tzu Poodle Mix
    LIVE_MMLS_DOGS_Shihpoo_Shih_Tzu_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shihpoo_Shih_Tzu_Poodle_Mix"
    )

    # label: LIVE_MMLS_DOGS_Spinone_Italiano
    # comment: Spinone Italiano
    LIVE_MMLS_DOGS_Spinone_Italiano = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Spinone_Italiano"
    )

    # label: FLWR_FLWR_CFLW
    # comment: Cut flowers
    FLWR_FLWR_CFLW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR_CFLW"
    )

    # label: SCIN_DIAG
    # comment: Diagnostics equipment
    SCIN_DIAG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_DIAG"
    )

    # label: LIVE_MMLS_CATS_Korat
    # comment: Korat
    LIVE_MMLS_CATS_Korat = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Korat"
    )

    # label: PHAR_PHAR_SUEQ
    # comment: Surgical equipment
    PHAR_PHAR_SUEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_PHAR_SUEQ"
    )

    # label: LIVE_MMLS_DOGS_Afghan_Hound
    # comment: Afghan Hound
    LIVE_MMLS_DOGS_Afghan_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Afghan_Hound"
    )

    # label: MART_ART
    # comment: Art
    MART_ART = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_ART")

    # label: LIVE_MMLS_DOGS_Curly_Coated_Retriever
    # comment: Curly-Coated Retriever
    LIVE_MMLS_DOGS_Curly_Coated_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Curly_Coated_Retriever"
    )

    # label: FLWR
    # comment: Plants, Flowers, Seeds
    FLWR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR")

    # label: SCIN_HEAR
    # comment: Hearing aids
    SCIN_HEAR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_HEAR"
    )

    # label: FOOD_BVRG
    # comment: Beverages
    FOOD_BVRG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG"
    )

    # label: LIVE_MMLS_DOGS_Lhasa_Apso
    # comment: Lhasa Apso
    LIVE_MMLS_DOGS_Lhasa_Apso = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Lhasa_Apso"
    )

    # label: LIVE_MMLS_CATS_Siberian
    # comment: Siberian
    LIVE_MMLS_CATS_Siberian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Siberian"
    )

    # label: LIVE_MMLS_DOGS_American_Staffordshire_Terrier
    # comment: American Staffordshire Terrier
    LIVE_MMLS_DOGS_American_Staffordshire_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Staffordshire_Terrier"
    )

    # label: LIVE_MMLS_CATS_Balinese
    # comment: Balinese
    LIVE_MMLS_CATS_Balinese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Balinese"
    )

    # label: FOOD_MEAT_FRZM
    # comment: Frozen meat
    FOOD_MEAT_FRZM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_FRZM"
    )

    # label: LIVE_MMLS_CATS_Chartreux
    # comment: Chartreux
    LIVE_MMLS_CATS_Chartreux = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Chartreux"
    )

    # label: FLWR_FLWR
    # comment: Fresh flowers
    FLWR_FLWR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR"
    )

    # label: LIVE_MMLS_DOGS_Sloughi_Arabian_Greyhound
    # comment: Sloughi-Arabian Greyhound
    LIVE_MMLS_DOGS_Sloughi_Arabian_Greyhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sloughi_Arabian_Greyhound"
    )

    # label: MART_MUSI
    # comment: Musical instruments
    MART_MUSI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_MUSI"
    )

    # label: RAWM_QRTZ
    # comment: Quartz
    RAWM_QRTZ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_QRTZ"
    )

    # label: FLWR_PLNT_BULB
    # comment: Bulbs and Tubers
    FLWR_PLNT_BULB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_BULB"
    )

    # label: SCIN_LBEQ
    # comment: Laboratory equipment
    SCIN_LBEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_LBEQ"
    )

    # label: SCIN_DEEQ
    # comment: Densist equipment
    SCIN_DEEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_DEEQ"
    )

    # label: TRPH
    # comment: Trophies
    TRPH = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#TRPH")

    # label: LIVE_MMLS_DOGS_English_Cocker_Spaniel
    # comment: English Cocker Spaniel
    LIVE_MMLS_DOGS_English_Cocker_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Cocker_Spaniel"
    )

    # label: RAWM_MICA
    # comment: Mica products
    RAWM_MICA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MICA"
    )

    # label: LIVE_BRDH
    # comment: Birds & Hatching Eggs
    LIVE_BRDH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH"
    )

    # label: MLTY
    # comment: Military, Weapons and Ammunition
    MLTY = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY")

    # label: RAWM_OILS
    # comment: Oils
    RAWM_OILS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_OILS"
    )

    # label: LIVE_MMLS_DOGS_Italian_Greyhound
    # comment: Italian Greyhound
    LIVE_MMLS_DOGS_Italian_Greyhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Italian_Greyhound"
    )

    # label: CONS
    # comment: Consumer goods
    CONS = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS")

    # label: VHCL_MACH
    # comment: Machinery and Tools
    VHCL_MACH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH"
    )

    # label: LIVE_MMLS_DOGS_Eurasier
    # comment: Eurasier
    LIVE_MMLS_DOGS_Eurasier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Eurasier"
    )

    # label: LIVE_MMLS_CATS_Copper
    # comment: Copper
    LIVE_MMLS_CATS_Copper = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Copper"
    )

    # label: LIVE_MMLS_DOGS_Belgian_Tervuren
    # comment: Belgian Tervuren
    LIVE_MMLS_DOGS_Belgian_Tervuren = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Belgian_Tervuren"
    )

    # label: LIVE_MMLS_DOGS_Briard
    # comment: Briard
    LIVE_MMLS_DOGS_Briard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Briard"
    )

    # label: LIVE_MLKS_SNAI
    # comment: Snails
    LIVE_MLKS_SNAI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MLKS_SNAI"
    )

    # label: LIVE_MMLS_CATS_American_Shorthair
    # comment: American Shorthair
    LIVE_MMLS_CATS_American_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Shorthair"
    )

    # label: LIVE_MMLS_CATS_Serengeti
    # comment: Serengeti
    LIVE_MMLS_CATS_Serengeti = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Serengeti"
    )

    # label: LIVE_MMLS_DOGS_Lagotto_Romagnolo
    # comment: Lagotto Romagnolo
    LIVE_MMLS_DOGS_Lagotto_Romagnolo = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Lagotto_Romagnolo"
    )

    # label: LIVE_MMLS_CATS_Egyptian_Mau
    # comment: Egyptian Mau
    LIVE_MMLS_CATS_Egyptian_Mau = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Egyptian_Mau"
    )

    # label: HUMR_HUMC
    # comment: Human remains cremated
    HUMR_HUMC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#HUMR_HUMC"
    )

    # label: LIVE_MMLS_DOGS_Tibetan_Mastiff
    # comment: Tibetan Mastiff
    LIVE_MMLS_DOGS_Tibetan_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tibetan_Mastiff"
    )

    # label: LIVE_MMLS_DOGS_Bergamasco
    # comment: Bergamasco
    LIVE_MMLS_DOGS_Bergamasco = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bergamasco"
    )

    # label: LIVE_MMLS_DOGS_Chinese_Pug
    # comment: Chinese Pug
    LIVE_MMLS_DOGS_Chinese_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinese_Pug"
    )

    # label: LIVE_MMLS_DOGS_Mixed_Invalid_Breed_Type
    # comment: Mixed-Invalid Breed Type
    LIVE_MMLS_DOGS_Mixed_Invalid_Breed_Type = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mixed_Invalid_Breed_Type"
    )

    # label: TXTL_FURW
    # comment: Furs wear
    TXTL_FURW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_FURW"
    )

    # label: LIVE_MMLS_DOGS_Berger_Picard
    # comment: Berger Picard
    LIVE_MMLS_DOGS_Berger_Picard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Berger_Picard"
    )

    # label: LIVE_MMLS_DOGS_Miniature_Bull_Terrier
    # comment: Miniature Bull Terrier
    LIVE_MMLS_DOGS_Miniature_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_Bull_Terrier"
    )

    # label: CONS_HAID
    # comment: Humanitarian aid
    CONS_HAID = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HAID"
    )

    # label: FOOD_DARY_ICEC
    # comment: Ice cream
    FOOD_DARY_ICEC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY_ICEC"
    )

    # label: LIVE_MMLS_DOGS_Shiba_Inu
    # comment: Shiba Inu
    LIVE_MMLS_DOGS_Shiba_Inu = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shiba_Inu"
    )

    # label: FOOD_FISH_LOBS
    # comment: Lobsters and Crabs
    FOOD_FISH_LOBS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_LOBS"
    )

    # label: LIVE_MMLS_DOGS_Irish_Water_Spaniel
    # comment: Irish Water Spaniel
    LIVE_MMLS_DOGS_Irish_Water_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Water_Spaniel"
    )

    # label: VHCL_SVCL_PART
    # comment: Automobile parts
    VHCL_SVCL_PART = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_PART"
    )

    # label: LIVE_MMLS_DOGS_English_Springer_Spaniel
    # comment: English Springer Spaniel
    LIVE_MMLS_DOGS_English_Springer_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Springer_Spaniel"
    )

    # label: LIVE_MMLS_DOGS_Irish_Terrier
    # comment: Irish Terrier
    LIVE_MMLS_DOGS_Irish_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Terrier"
    )

    # label: PRIN_EDUM
    # comment: Educational materials
    PRIN_EDUM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_EDUM"
    )

    # label: LIVE_MMLS_CATS_Abyssinian
    # comment: Abyssinian
    LIVE_MMLS_CATS_Abyssinian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Abyssinian"
    )

    # label: FLWR_PLNT_TPLN
    # comment: Tropical plants
    FLWR_PLNT_TPLN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_TPLN"
    )

    # label: FOOD_DARY
    # comment: Dairy products
    FOOD_DARY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY"
    )

    # label: LIVE_MMLS_DOGS_Giant_Schnauzer
    # comment: Giant Schnauzer
    LIVE_MMLS_DOGS_Giant_Schnauzer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Giant_Schnauzer"
    )

    # label: LIVE_MMLS_DOGS_Pembroke_Welsh_Corgi
    # comment: Pembroke Welsh Corgi
    LIVE_MMLS_DOGS_Pembroke_Welsh_Corgi = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pembroke_Welsh_Corgi"
    )

    # label: LIVE_MMLS_DOGS_Scottish_Terrier
    # comment: Scottish Terrier
    LIVE_MMLS_DOGS_Scottish_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Scottish_Terrier"
    )

    # label: PRIN_NEWS
    # comment: Newspapers and Magazines
    PRIN_NEWS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_NEWS"
    )

    # label: LIVE_MMLS_DOGS_Leonberger
    # comment: Leonberger
    LIVE_MMLS_DOGS_Leonberger = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Leonberger"
    )

    # label: LIVE_MMLS_CATS
    # comment: Cats
    LIVE_MMLS_CATS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS"
    )

    # label: ELEC_AVEQ
    # comment: Audio-Video-HiFi equipment
    ELEC_AVEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_AVEQ"
    )

    # label: LIVE_MMLS_DOGS_Labrabull_Labrador_Retriever_American_Pit_Bull
    # comment: Labrabull-Labrador Retriever American Pit Bull
    LIVE_MMLS_DOGS_Labrabull_Labrador_Retriever_American_Pit_Bull = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labrabull_Labrador_Retriever_American_Pit_Bull"
    )

    # label: LIVE_MMLS_DOGS_Poodle
    # comment: Poodle
    LIVE_MMLS_DOGS_Poodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Poodle"
    )

    # label: FOOD_CERE_BRED
    # comment: Bread
    FOOD_CERE_BRED = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_CERE_BRED"
    )

    # label: LIVE_MMLS_DOGS_Samoyed
    # comment: Samoyed
    LIVE_MMLS_DOGS_Samoyed = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Samoyed"
    )

    # label: FOOD_MEAT_DRIM
    # comment: Dried meat
    FOOD_MEAT_DRIM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_DRIM"
    )

    # label: LIVE_MMLS_DOGS_Cirneco_dell_Etna
    # comment: Cirneco dell Etna
    LIVE_MMLS_DOGS_Cirneco_dell_Etna = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cirneco_dell_Etna"
    )

    # label: LIVE_MMLS_CATS_American_Keuda
    # comment: American Keuda
    LIVE_MMLS_CATS_American_Keuda = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Keuda"
    )

    # label: LIVE_MMLS_DOGS_English_Mastiff
    # comment: English Mastiff
    LIVE_MMLS_DOGS_English_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Mastiff"
    )

    # label: TXTL_TXLW_GARM
    # comment: Garments
    TXTL_TXLW_GARM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_GARM"
    )

    # label: VHCL_MACH_MTSP
    # comment: Machinery supplies and Parts
    VHCL_MACH_MTSP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_MTSP"
    )

    # label: LIVE_MMLS_CATS_Birman
    # comment: Birman
    LIVE_MMLS_CATS_Birman = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Birman"
    )


class CurrencyCode(str, Enum):
    pass


class DangerousGoodsCode(str, Enum):
    # label: REX
    # comment: To be reserved for normally forbidden Explosives, Divisions 1.1, 1.2, 1.3, 1.4F, 1.5 and 1.6
    REX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#REX")

    # label: CAO
    # comment: Cargo Aircraft Only
    CAO = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#CAO")

    # label: ELM
    # comment: Lithium Metal Batteries otherwise excepted from the IATA DGR
    ELM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ELM")

    # label: EBM
    # comment: Lithium metal batteries excepted as per Section II of PI 968
    EBM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#EBM")

    # label: RXB
    # comment: Explosives 1.4B
    RXB = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXB")

    # label: RBM
    # comment: Fully regulated lithium metal batteries (Class 9, UN 3090) as per Section IA and IB of PI 968
    RBM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RBM")

    # label: RXC
    # comment: Explosives 1.4C
    RXC = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXC")

    # label: RLI
    # comment: Fully Regulated Lithium Ion Batteries (Class 9)
    RLI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RLI")

    # label: RCM
    # comment: Corrosive
    RCM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RCM")

    # label: RIS
    # comment: Infectious Substance
    RIS = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RIS")

    # label: RNG
    # comment: Non-Flammable Non-Toxic Gas
    RNG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RNG")

    # label: RXE
    # comment: Explosives 1.4E
    RXE = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXE")

    # label: RFL
    # comment: Flammable Liquid
    RFL = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFL")

    # label: EBI
    # comment: Lithium ion batteries excepted as per Section II of PI 965
    EBI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#EBI")

    # label: RGX
    # comment: Explosives 1.3G
    RGX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RGX")

    # label: MAG
    # comment: Magnetized Material
    MAG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#MAG")

    # label: RRW
    # comment: Radioactive Material Category I-White
    RRW = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RRW")

    # label: RSC
    # comment: Spontaneously Combustible
    RSC = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RSC")

    # label: RMD
    # comment: Miscellaneous Dangerous Goods
    RMD = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RMD")

    # label: ROP
    # comment: Organic Peroxide
    ROP = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ROP")

    # label: RFS
    # comment: Flammable Solid
    RFS = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFS")

    # label: RXG
    # comment: Explosives 1.4G
    RXG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXG")

    # label: RLM
    # comment: Fully Regulated Lithium Metal Batteries (Class 9)
    RLM = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RLM")

    # label: RFW
    # comment: Dangerous When Wet
    RFW = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFW")

    # label: ELI
    # comment: Lithium Ion Batteries otherwise excepted from the IATA DGR
    ELI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ELI")

    # label: RPB
    # comment: Toxic Substance
    RPB = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RPB")

    # label: RCL
    # comment: Cryogenic Liquids
    RCL = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RCL")

    # label: RFG
    # comment: Flammable Gas
    RFG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RFG")

    # label: RRY
    # comment: Radioactive Material Categories II-Yellow and III-Yellow
    RRY = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RRY")

    # label: RSB
    # comment: Polymeric Beads
    RSB = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RSB")

    # label: RPG
    # comment: Toxic Gas
    RPG = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RPG")

    # label: ICE
    # comment: Dry Ice
    ICE = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ICE")

    # label: RXD
    # comment: Explosives 1.4D
    RXD = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXD")

    # label: RBI
    # comment: Fully regulated lithium ion batteries (Class 9, UN 3480) as per Section IA and IB of PI 965
    RBI = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RBI")

    # label: RXS
    # comment: Explosives 1.4S
    RXS = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RXS")

    # label: ROX
    # comment: Oxidizer
    ROX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#ROX")

    # label: RCX
    # comment: Explosives 1.3C
    RCX = URIRef("https://onerecord.iata.org/ns/code-lists/DangerousGoodsCode#RCX")


class DemurrageCode(str, Enum):
    # label: HHH
    # comment: HHH
    HHH = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#HHH")

    # label: ZZZ
    # comment: ZZZ
    ZZZ = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#ZZZ")

    # label: BCC
    # comment: BCC
    BCC = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#BCC")

    # label: XXX
    # comment: XXX
    XXX = URIRef("https://onerecord.iata.org/ns/code-lists/DemurrageCode#XXX")


class DensityGroupCode(str, Enum):
    # label: 8
    # comment: 400 kg per mc or 25 lbs per cf
    _8 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#8")

    # label: 6
    # comment: 250 kg per mc or 15.6 lbs per cf
    _6 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#6")

    # label: 5
    # comment: 60 kg per mc or 3.8 lbs per cf
    _5 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#5")

    # label: 0
    # comment: 160kg per mc or 10 lbs per cf
    _0 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#0")

    # label: 10
    # comment: 950 kg per mc or 59.3 lbs per cf
    _10 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#10")

    # label: 3
    # comment: 120 kg per mc or 7.5 lbs per cf
    _3 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#3")

    # label: 2
    # comment: 90 kg per mc or 5.6 lbs per cf
    _2 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#2")

    # label: 9
    # comment: 600 kg per mc or 37.5 lbs per cf
    _9 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#9")

    # label: 4
    # comment: 220 kg per mc or 13.8 lbs per cf
    _4 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#4")

    # label: 1
    # comment: 300 kg per mc or 18.6 lbs per cf
    _1 = URIRef("https://onerecord.iata.org/ns/code-lists/DensityGroupCode#1")


class DimensionsUnitCode(str, Enum):
    # label: CMT
    # comment: Centimetre
    CMT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CMT")

    # label: INH
    # comment: Inch
    INH = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#INH")

    # label: MTR
    # comment: Metre
    MTR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MTR")

    # label: FOT
    # comment: Foot
    FOT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FOT")


class EntitlementCode(str, Enum):
    # label: A
    # comment: Other Charges due Agent
    A = URIRef("https://onerecord.iata.org/ns/code-lists/EntitlementCode#A")

    # label: C
    # comment: Other Charges due Carrier
    C = URIRef("https://onerecord.iata.org/ns/code-lists/EntitlementCode#C")


class ExplosiveCompatibilityGroupCode(str, Enum):
    # label: C
    # comment: Propellant explosive substance or other deflagrating explosive substance or article containing such explosive substance (Hazard Division 1.1; 1.2; 1.3; 1.4)
    C = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#C"
    )

    # label: S
    # comment: Article or substance so packed or designed that any hazardous effects arising from accidental functioning are confined within the package unless the package has been degraded by fire, in which case all blast or projection effects are limited to the extent that they do not significantly hinder or prohibit fire fighting or other emergency response efforts in the immediate vicinity of the package (Hazard Division 1.4)
    S = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#S"
    )

    # label: G
    # comment: Pyrotechnic substance, or article containing a pyrotechnic substance, or article containing both an explosive substance and an illuminating, incendiary, tear- or smoke-producing substance (other than a water -activated article or one containing white phosphorus, phosphide, a pyrophoric substance, a flammable liquid or get or hypergolic liquids) (Hazard Division 1.1; 1.2; 1.3; 1.4)
    G = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#G"
    )

    # label: J
    # comment: Article containing both an explosive substance and a flammable liquid or gel (Hazard Division 1.1; 1.2; 1.3)
    J = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#J"
    )

    # label: L
    # comment: Explosive article or substance containing an explosive substance and presenting a special risk (e.g. due to water activation, or the presence of hypergolic liquids, phosphides or a pyrophoric substance) and needing isolation of each type (Hazard Division 1.2; 1.2; 1.3)
    L = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#L"
    )

    # label: A
    # comment: Primary explosive substance (Hazard Division 1.1)
    A = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#A"
    )

    # label: E
    # comment: Article containing a secondary detonating explosive substance, without means of initiation, with a propelling charge (other than one containing a flammable liquid or gel or hypergolic liquids) or without a propelling charge (Hazard Division 1.1; 1.2; 1.4)
    E = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#E"
    )

    # label: B
    # comment: Article containing a primary explosive substance and not containing two or more effective protective features. Some articles, such as detonators for blasting, detonator assemblies for blasting and primers, cap type, are included, even though they do not contain primary explosives (Hazard Division 1.1; 1.2; 1.4)
    B = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#B"
    )

    # label: D
    # comment: Secondary detonating explosive substance or black powder or article containing a secondary detonating explosive substance, in each case without means of initiation and without a propelling charge or article containing a primary explosive substance and containing two or more effective protective features (Hazard Division 1.1; 1.2; 1.4; 1.5)
    D = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#D"
    )

    # label: H
    # comment: Article containing both an explosive substance and white phosphorus (Hazard Division 1.2; 1.3)
    H = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#H"
    )

    # label: K
    # comment: Article containing both an explosive substance and a toxic chemical agent (Hazard Division 1.1; 1.3)
    K = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#K"
    )

    # label: F
    # comment: Article containing a secondary detonating explosive substance, with its own means of initiation, with a propelling charge (other than one containing a flammable liquid or gel or hypergolic liquids) or without a propelling charge (Hazard Division 1.1; 1.2; 1.3; 1.4)
    F = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#F"
    )

    # label: N
    # comment: Article containing only extremely insensitive detonating substances (Hazard Division 1.6)
    N = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ExplosiveCompatibilityGroupCode#N"
    )


class GoodsTypeCode(str, Enum):
    # label: I
    # comment: Species included in Appendix I of CITES
    I = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeCode#I")

    # label: III
    # comment: Species included in Appendix III of CITES
    III = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeCode#III")

    # label: II
    # comment: Species included in Appendix II of CITES
    II = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeCode#II")


class GoodsTypeExtensionCode(str, Enum):
    # label: D
    # comment: Captive-bred animal or artificially propagated plant
    D = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#D")

    # label: I
    # comment: Confiscated or seized
    I = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#I")

    # label: O
    # comment: Pre-Convention
    O = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#O")

    # label: U
    # comment: Unknown
    U = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#U")

    # label: A
    # comment: Artificially propagated plant
    A = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#A")

    # label: W
    # comment: Wild
    W = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#W")

    # label: R
    # comment: Ranched animal
    R = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#R")

    # label: F
    # comment: Born in captivity
    F = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#F")

    # label: X
    # comment: Marine environment
    X = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#X")

    # label: C
    # comment: Bred in captivity
    C = URIRef("https://onerecord.iata.org/ns/code-lists/GoodsTypeExtensionCode#C")


class MeasurementUnitCode(str, Enum):
    # label: KEL
    # comment: Kelvin
    KEL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KEL")

    # label: KBQ
    # comment: Kilobecquerel
    KBQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KBQ")

    # label: QTL
    # comment: Liquid Quart (0.946353 DM3)
    QTL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#QTL")

    # label: MGM
    # comment: Milligram
    MGM = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MGM")

    # label: TBQ
    # comment: Terabecquerel
    TBQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#TBQ")

    # label: DLT
    # comment: Decilitre
    DLT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#DLT")

    # label: FTQ
    # comment: Cubic Foot
    FTQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FTQ")

    # label: CLT
    # comment: Centilitre
    CLT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CLT")

    # label: LBR
    # comment: Pound UK, US (0.45359237 KGM)
    LBR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#LBR")

    # label: CEL
    # comment: Degree Celsius
    CEL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CEL")

    # label: GRM
    # comment: Gram
    GRM = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#GRM")

    # label: KGM
    # comment: Kilogram
    KGM = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KGM")

    # label: YRD
    # comment: Yard (0.9144 MTR)
    YRD = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#YRD")

    # label: BQL
    # comment: Becquerel
    BQL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#BQL")

    # label: CUR
    # comment: Curie
    CUR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CUR")

    # label: PTI
    # comment: Pint (0.568262 DM3)
    PTI = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#PTI")

    # label: CGM
    # comment: Centigram
    CGM = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CGM")

    # label: MTR
    # comment: Metre
    MTR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MTR")

    # label: ONZ
    # comment: Ounce UK, US (28.949523 GRM)
    ONZ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#ONZ")

    # label: OZI
    # comment: Fluid Ounce (28.413 CM3)
    OZI = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#OZI")

    # label: LTR
    # comment: Litre (1 DM3)
    LTR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#LTR")

    # label: MTQ
    # comment: Cubic Metre
    MTQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MTQ")

    # label: PTL
    # comment: Liquid Pint (0.473176 DM3)
    PTL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#PTL")

    # label: QTI
    # comment: Quart (1.136523 DM3)
    QTI = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#QTI")

    # label: INQ
    # comment: Cubic Inch
    INQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#INQ")

    # label: CMQ
    # comment: Cubic Centimetre
    CMQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CMQ")

    # label: FAH
    # comment: Degree Fahrenheit
    FAH = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FAH")

    # label: MBQ
    # comment: Megabecquerel
    MBQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MBQ")

    # label: GLL
    # comment: Liquid Gallon (3.78541 DM3)
    GLL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#GLL")

    # label: DMT
    # comment: Decimetre
    DMT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#DMT")

    # label: MMT
    # comment: Millimetre
    MMT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MMT")

    # label: OZA
    # comment: Fluid Ounce (29.5795 CM3)
    OZA = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#OZA")

    # label: GII
    # comment: Gigabecquerel GBQ Gill (0.142065 DM3)
    GII = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#GII")

    # label: CMT
    # comment: Centimetre
    CMT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CMT")

    # label: GIA
    # comment: Gill (11.8294 CM3)
    GIA = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#GIA")

    # label: INH
    # comment: Inch
    INH = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#INH")

    # label: FOT
    # comment: Foot
    FOT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FOT")

    # label: MLT
    # comment: Millilitre
    MLT = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MLT")

    # label: GLI
    # comment: Gallon (4.546092 DM3)
    GLI = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#GLI")

    # label: NDA
    # comment: No Dimensions Available
    NDA = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#NDA")


class ModeCode(str, Enum):
    # label: MAIL
    # comment: Indicates the transport mode to be Mail (5)
    MAIL = URIRef("https://onerecord.iata.org/ns/code-lists/ModeCode#MAIL")

    # label: MULTIMODAL_TRANSPORT
    # comment: Indicates a Multimodal Transport (6)
    MULTIMODAL_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#MULTIMODAL_TRANSPORT"
    )

    # label: TRANSPORT_MODE_NOT_APPLICABLE
    # comment: Indicates that no transport mode is applicable (9)
    TRANSPORT_MODE_NOT_APPLICABLE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#TRANSPORT_MODE_NOT_APPLICABLE"
    )

    # label: TRANSPORT_MODE_NOT_SPECIFIED
    # comment: Indicates that the Transport Mode is not specified (0)
    TRANSPORT_MODE_NOT_SPECIFIED = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#TRANSPORT_MODE_NOT_SPECIFIED"
    )

    # label: RAIL_TRANSPORT
    # comment: Indicates the transport mode to be Rail Transport (2)
    RAIL_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#RAIL_TRANSPORT"
    )

    # label: MARITIME_TRANSPORT
    # comment: Indicates the transport mode to be Maritime Transport (1)
    MARITIME_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#MARITIME_TRANSPORT"
    )

    # label: AIR_TRANSPORT
    # comment: Indicates the transport mode to be Air Transport (4)
    AIR_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#AIR_TRANSPORT"
    )

    # label: INLAND_WATER_TRANSPORT
    # comment: Indicates that the transport mode to be Inland Water Transport (8)
    INLAND_WATER_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#INLAND_WATER_TRANSPORT"
    )

    # label: FIXED_TRANSPORT_INSTALLATION
    # comment: Indicates that the transport mode is a Fixed Transport Installation (7)
    FIXED_TRANSPORT_INSTALLATION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#FIXED_TRANSPORT_INSTALLATION"
    )

    # label: ROAD_TRANSPORT
    # comment: Indicates the transport mode to be Road Transport (3)
    ROAD_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#ROAD_TRANSPORT"
    )


class MovementIndicator(str, Enum):
    # label: CN
    # comment: Cancellation
    CN = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#CN")

    # label: FR
    # comment: Force Return
    FR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#FR")

    # label: AO
    # comment: Actual Off-block
    AO = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AO")

    # label: DA
    # comment: Doc Arrival
    DA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#DA")

    # label: AK
    # comment: Actual end of unloading time
    AK = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AK")

    # label: ER
    # comment: Estimated driver reporting time
    ER = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#ER")

    # label: AA
    # comment: Actual Arrival (Touchdown)
    AA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AA")

    # label: AR
    # comment: Actual driver reporting time
    AR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AR")

    # label: PA
    # comment: Pre-announcement of the truck - to enable to pre-announce data (driver name, license plates, etc.) to GHA at departure station
    PA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#PA")

    # label: AB
    # comment: Actual On-block
    AB = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AB")

    # label: SS
    # comment: Scheduled earliest driver reporting time for collection and/or delivery
    SS = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SS")

    # label: SL
    # comment: Scheduled end of loading time
    SL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SL")

    # label: AD
    # comment: Actual Departure (Take off)
    AD = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AD")

    # label: SD
    # comment: Scheduled Departure
    SD = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SD")

    # label: EL
    # comment: Estimated end of loading time
    EL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EL")

    # label: DL
    # comment: Delayed
    DL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#DL")

    # label: EB
    # comment: Estimated On-block
    EB = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EB")

    # label: RR
    # comment: Return to RAMP
    RR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#RR")

    # label: EA
    # comment: Estimated Arrival (Touchdown)
    EA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EA")

    # label: AH
    # comment: Actual gate out time - Relates t gate passing of trucks
    AH = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AH")

    # label: SA
    # comment: Scheduled Arrival
    SA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SA")

    # label: EO
    # comment: Estimated Off-block
    EO = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EO")

    # label: ED
    # comment: Estimated Departure (Take off)
    ED = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#ED")

    # label: SR
    # comment: Scheduled latest driver reporting time for collection and/or delivery
    SR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SR")

    # label: NI
    # comment: Next Information
    NI = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#NI")

    # label: EK
    # comment: Estimated end of unloading time
    EK = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EK")

    # label: AG
    # comment: Actual gate in time - Relates to gate passing of trucks
    AG = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AG")

    # label: SK
    # comment: Scheduled end of unloading time
    SK = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SK")

    # label: AL
    # comment: Actual end of loading time
    AL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AL")

    # label: DV
    # comment: Diversion
    DV = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#DV")


class OtherChargeCode(str, Enum):
    # label: CE
    # comment: Export/Import warrant
    CE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CE")

    # label: AC
    # comment: Animal Container
    AC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AC")

    # label: SP
    # comment: Separate Early Release
    SP = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SP")

    # label: UB
    # comment: Disassembly
    UB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UB")

    # label: IA
    # comment: Very important cargo (VIC)
    IA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#IA")

    # label: RA
    # comment: Dangerous Goods Fee
    RA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RA")

    # label: DK
    # comment: Release order
    DK = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DK")

    # label: RB
    # comment: Rejection
    RB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RB")

    # label: CI
    # comment: Overtime and Other Customs Imposed Charges
    CI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CI")

    # label: HB
    # comment: Mortuary
    HB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#HB")

    # label: SB
    # comment: Delivery notification
    SB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SB")

    # label: MW
    # comment: Miscellaneous — Due Issuing Carrier
    MW = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MW")

    # label: TX
    # comment: General Taxes
    TX = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TX")

    # label: SO
    # comment: Storage — Origin
    SO = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SO")

    # label: MO
    # comment: Miscellaneous — Due Issuing Carrier
    MO = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MO")

    # label: UH
    # comment: Handling (Unit Load Device)
    UH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UH")

    # label: SU
    # comment: Surface Charge — Origin
    SU = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SU")

    # label: BB
    # comment: Appraisal Service
    BB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BB")

    # label: LJ
    # comment: Rental of Stalls/pens
    LJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LJ")

    # label: GT
    # comment: Government Tax
    GT = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#GT")

    # label: SC
    # comment: Security Charge
    SC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SC")

    # label: DC
    # comment: Certificate of Origin
    DC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DC")

    # label: MX
    # comment: Miscellaneous — Due Issuing Carrier
    MX = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MX")

    # label: AW
    # comment: Air Waybill Fee
    AW = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AW")

    # label: MB
    # comment: Miscellaneous — Unassigned (see Note 2)
    MB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MB")

    # label: KB
    # comment: Loading/unloading equipment (forklift etc.)
    KB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#KB")

    # label: PK
    # comment: Packing/Repacking
    PK = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PK")

    # label: MH
    # comment: Miscellaneous — Due Last Carrier
    MH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MH")

    # label: HR
    # comment: Human Remains
    HR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#HR")

    # label: IN
    # comment: Insurance Premium
    IN = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#IN")

    # label: DD
    # comment: Preparation of Cargo manifest
    DD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DD")

    # label: MR
    # comment: Miscellaneous — Due Issuing Carrier
    MR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MR")

    # label: TA
    # comment: Postal Tax
    TA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TA")

    # label: MM
    # comment: Miscellaneous — Due Last Carrier
    MM = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MM")

    # label: KA
    # comment: Handling (Heavy/Bulky cargo)
    KA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#KA")

    # label: TE
    # comment: Statistical Tax
    TE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TE")

    # label: MG
    # comment: Miscellaneous — Due Last Carrier
    MG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MG")

    # label: VB
    # comment: Security (armed guard/escort) handling
    VB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#VB")

    # label: AS
    # comment: Assembly Service Fee
    AS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AS")

    # label: BC
    # comment: AWB Copy
    BC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BC")

    # label: CF
    # comment: Inventory and/or inspection
    CF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CF")

    # label: BM
    # comment: Withdrawal of shipment after clearance
    BM = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BM")

    # label: MK
    # comment: Miscellaneous — Due Last Carrier
    MK = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MK")

    # label: FC
    # comment: Charges Collect Fee
    FC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FC")

    # label: MU
    # comment: Miscellaneous — Due Issuing Carrier
    MU = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MU")

    # label: NS
    # comment: Navigation Surcharge — Due Issuing Carrier
    NS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#NS")

    # label: CA
    # comment: Bonding
    CA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CA")

    # label: SS
    # comment: Signature Service
    SS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SS")

    # label: XD
    # comment: War risk
    XD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XD")

    # label: LE
    # comment: Hotel
    LE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LE")

    # label: PU
    # comment: Pick-Up
    PU = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PU")

    # label: UD
    # comment: Demurrage
    UD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UD")

    # label: LG
    # comment: Veterinary inspection
    LG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LG")

    # label: VC
    # comment: Strongroom
    VC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#VC")

    # label: BH
    # comment: Messenger service
    BH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BH")

    # label: LA
    # comment: Live Animals
    LA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LA")

    # label: DH
    # comment: AWB Charges Correction Advice
    DH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DH")

    # label: RF
    # comment: Remit Following Collection Fee
    RF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RF")

    # label: MV
    # comment: Miscellaneous — Due Issuing Carrier
    MV = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MV")

    # label: MZ
    # comment: Miscellaneous — Due Issuing Carrier
    MZ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MZ")

    # label: BI
    # comment: Import/export documents processing
    BI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BI")

    # label: ZA
    # comment: Re-warehousing
    ZA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ZA")

    # label: LH
    # comment: Storage (Live animals)
    LH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LH")

    # label: ST
    # comment: State Sales Tax
    ST = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ST")

    # label: TR
    # comment: Transit
    TR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TR")

    # label: CD
    # comment: Clearance and Handling — Destination
    CD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CD")

    # label: ZC
    # comment: Cool/Cold room, freezer (Storage)
    ZC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ZC")

    # label: UF
    # comment: Recontouring
    UF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UF")

    # label: MD
    # comment: Miscellaneous — Due Last Carrier
    MD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MD")

    # label: MS
    # comment: Miscellaneous — Due Issuing Carrier
    MS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MS")

    # label: FE
    # comment: General (Handling)
    FE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FE")

    # label: SR
    # comment: Storage — Destination
    SR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SR")

    # label: MQ
    # comment: Miscellaneous — Due Issuing Carrier
    MQ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MQ")

    # label: DV
    # comment: Veterinary and/or Phytosanitary purposes
    DV = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DV")

    # label: EA
    # comment: Handling (Express)
    EA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#EA")

    # label: FA
    # comment: Airport arrival
    FA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FA")

    # label: WA
    # comment: Handling (Vulnerable cargo)
    WA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#WA")

    # label: LF
    # comment: Quarantine
    LF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LF")

    # label: XE
    # comment: Weight
    XE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XE")

    # label: AT
    # comment: Attendant
    AT = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AT")

    # label: CB
    # comment: Completion/preparation of documents
    CB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CB")

    # label: PA
    # comment: Handling (Perishables)
    PA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PA")

    # label: TV
    # comment: Value Added Tax (General or for Export)
    TV = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TV")

    # label: BL
    # comment: Blacklist Certificate
    BL = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BL")

    # label: MC
    # comment: Miscellaneous — Due Carrier (see Note 3)
    MC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MC")

    # label: SF
    # comment: Delivery Order
    SF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SF")

    # label: DB
    # comment: Disbursement Fee
    DB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DB")

    # label: FB
    # comment: Domestic shipments
    FB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FB")

    # label: CC
    # comment: Manual data entry for customs purposes
    CC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CC")

    # label: TD
    # comment: State Tax
    TD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TD")

    # label: TB
    # comment: Sales Tax
    TB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TB")

    # label: MJ
    # comment: Miscellaneous — Due Last Carrier
    MJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MJ")

    # label: CJ
    # comment: Removal (carrier warehouse to warehouse)
    CJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CJ")

    # label: MY
    # comment: Fuel Surcharge — Due Issuing Carrier
    MY = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MY")

    # label: DG
    # comment: AWB Cancellation
    DG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DG")

    # label: RC
    # comment: Referral of Charge
    RC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RC")

    # label: PB
    # comment: Cool/Cold room, freezer (Perishables)
    PB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PB")

    # label: UE
    # comment: Leasing
    UE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UE")

    # label: DF
    # comment: Distribution Service Fee
    DF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DF")

    # label: CG
    # comment: Electronic processing or transmission of data for customs purposes
    CG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CG")

    # label: XB
    # comment: Security (Surcharge/premiums)
    XB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XB")

    # label: MP
    # comment: Miscellaneous — Due Issuing Carrier
    MP = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MP")

    # label: SI
    # comment: Stop in Transit
    SI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SI")

    # label: FF
    # comment: Loading/unloading
    FF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FF")

    # label: SE
    # comment: Proof of delivery (pickup and delivery)
    SE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SE")

    # label: VA
    # comment: Handling (Valuable Cargo)
    VA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#VA")

    # label: LC
    # comment: Cleaning
    LC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LC")

    # label: RD
    # comment: Radio-active room
    RD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RD")

    # label: TC
    # comment: Stamp Tax
    TC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TC")

    # label: MA
    # comment: Miscellaneous — Due Agent (see Note 1)
    MA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MA")

    # label: ML
    # comment: Miscellaneous — Due Last Carrier
    ML = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ML")

    # label: ME
    # comment: Miscellaneous — Due Last Carrier
    ME = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ME")

    # label: SA
    # comment: Delivery
    SA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SA")

    # label: SD
    # comment: Surface Charge — Destination
    SD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SD")

    # label: DJ
    # comment: Proof of delivery (documentation)
    DJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DJ")

    # label: BF
    # comment: Copies of documents
    BF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BF")

    # label: MF
    # comment: Miscellaneous — Due Last Carrier
    MF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MF")

    # label: BA
    # comment: Advances and/or guarantees
    BA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BA")

    # label: FI
    # comment: Weighing
    FI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FI")

    # label: CH
    # comment: Clearance and Handling — Origin
    CH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CH")

    # label: FD
    # comment: Priority
    FD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FD")

    # label: JA
    # comment: Clearance, General
    JA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#JA")

    # label: XC
    # comment: Time
    XC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XC")

    # label: MI
    # comment: Miscellaneous — Due Last Carrier
    MI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MI")

    # label: BE
    # comment: Collection of funds
    BE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BE")

    # label: DI
    # comment: AWB Re-waybilling
    DI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DI")

    # label: MN
    # comment: Miscellaneous — Due Last Carrier
    MN = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MN")

    # label: GA
    # comment: Diplomatic consignment
    GA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#GA")

    # label: MT
    # comment: Miscellaneous — Due Issuing Carrier
    MT = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MT")

    # label: UC
    # comment: Adjusting of improperly loaded ULD
    UC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UC")

    # label: BR
    # comment: Bank Release
    BR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BR")

    # label: TI
    # comment: Value Added Tax (For Import only)
    TI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TI")

    # label: UG
    # comment: Unloading (Unit Load Device)
    UG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UG")

    # label: ZB
    # comment: General (Storage)
    ZB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ZB")

    # label: LI
    # comment: Cleaning of stalls/pens
    LI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LI")


class PackageMarkCode(str, Enum):
    # label: SSCC_18
    # comment: Serial Shipping Container Code-18 / EAN-18
    SSCC_18 = URIRef("https://onerecord.iata.org/ns/code-lists/PackageMarkCode#SSCC_18")

    # label: UPC
    # comment: Universal Product Code
    UPC = URIRef("https://onerecord.iata.org/ns/code-lists/PackageMarkCode#UPC")


class PackagingDangerLevelCode(str, Enum):
    # label: I
    # comment: High danger
    I = URIRef("https://onerecord.iata.org/ns/code-lists/PackagingDangerLevelCode#I")

    # label: II
    # comment: Medium danger
    II = URIRef("https://onerecord.iata.org/ns/code-lists/PackagingDangerLevelCode#II")

    # label: III
    # comment: Low danger
    III = URIRef(
        "https://onerecord.iata.org/ns/code-lists/PackagingDangerLevelCode#III"
    )


class ParticipantIdentifier(str, Enum):
    # label: DEC
    # comment: Deconsolidator
    DEC = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#DEC")

    # label: NFY
    # comment: Notify
    NFY = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#NFY")

    # label: PTT
    # comment: Post Office
    PTT = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#PTT")

    # label: TRK
    # comment: Trucker
    TRK = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#TRK")

    # label: APT
    # comment: Airport Authority
    APT = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#APT")

    # label: GHA
    # comment: Ground Handling Agent
    GHA = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#GHA")

    # label: CTM
    # comment: Customs
    CTM = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#CTM")

    # label: FFW
    # comment: Freight Forwarder
    FFW = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#FFW")

    # label: DCL
    # comment: Declarant
    DCL = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#DCL")

    # label: AGT
    # comment: Agent
    AGT = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#AGT")

    # label: CAG
    # comment: Commissionable Agent
    CAG = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#CAG")

    # label: SHP
    # comment: Shipper
    SHP = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#SHP")

    # label: BRK
    # comment: Broker
    BRK = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#BRK")

    # label: CNE
    # comment: Consignee
    CNE = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#CNE")

    # label: AIR
    # comment: Airline
    AIR = URIRef("https://onerecord.iata.org/ns/code-lists/ParticipantIdentifier#AIR")


class PrepaidCollectIndicator(str, Enum):
    # label: C
    # comment: Collect Indicator
    C = URIRef("https://onerecord.iata.org/ns/code-lists/PrepaidCollectIndicator#C")

    # label: P
    # comment: Prepaid Indicator
    P = URIRef("https://onerecord.iata.org/ns/code-lists/PrepaidCollectIndicator#P")


class RaTypeCode(str, Enum):
    # label: I_WHITE
    # comment: I-Yellow
    I_WHITE = URIRef("https://onerecord.iata.org/ns/code-lists/RaTypeCode#I_WHITE")

    # label: III_YELLOW
    # comment: III-Yellow
    III_YELLOW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RaTypeCode#III_YELLOW"
    )

    # label: II_YELLOW
    # comment: II-Yellow
    II_YELLOW = URIRef("https://onerecord.iata.org/ns/code-lists/RaTypeCode#II_YELLOW")


class RadioactiveMaterialClassification(str, Enum):
    # label: LOW_DISPERSIBLE
    # comment: Low Dispersible
    LOW_DISPERSIBLE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RadioactiveMaterialClassification#LOW_DISPERSIBLE"
    )

    # label: SPECIAL_FORM
    # comment: Special Form
    SPECIAL_FORM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RadioactiveMaterialClassification#SPECIAL_FORM"
    )

    # label: PHYSICAL_CHEMICAL_FORM
    # comment: Physical Chemical Form
    PHYSICAL_CHEMICAL_FORM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RadioactiveMaterialClassification#PHYSICAL_CHEMICAL_FORM"
    )


class RateClassCode(str, Enum):
    # label: N
    # comment: Normal Rate
    N = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#N")

    # label: K
    # comment: Rate per Kilogram
    K = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#K")

    # label: B
    # comment: Basic Charge
    B = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#B")

    # label: X
    # comment: Unit Load Device Additional Information
    X = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#X")

    # label: Q
    # comment: Quantity Rate
    Q = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#Q")

    # label: E
    # comment: Unit Load Device Additional Rate
    E = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#E")

    # label: R
    # comment: Class Rate Reduction
    R = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#R")

    # label: Y
    # comment: Unit Load Device Discount
    Y = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#Y")

    # label: W
    # comment: Weight Increase
    W = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#W")

    # label: M
    # comment: Minimum Charge
    M = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#M")

    # label: S
    # comment: Class Rate Surcharge
    S = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#S")

    # label: C
    # comment: Specific Commodity Rate
    C = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#C")

    # label: P
    # comment: International Priority Service Rate
    P = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#P")

    # label: U
    # comment: Unit Load Device Basic Charge or Rate
    U = URIRef("https://onerecord.iata.org/ns/code-lists/RateClassCode#U")


class RatingsType(str, Enum):
    # label: C
    # comment: Published
    C = URIRef("https://onerecord.iata.org/ns/code-lists/RatingsType#C")

    # label: A
    # comment: Actual
    A = URIRef("https://onerecord.iata.org/ns/code-lists/RatingsType#A")

    # label: F
    # comment: Face
    F = URIRef("https://onerecord.iata.org/ns/code-lists/RatingsType#F")


class RegulatedEntityCategoryCode(str, Enum):
    # label: KC
    # comment: Known Consignor (consignor for both passenger and all cargo aircraft only)
    KC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#KC"
    )

    # label: AO
    # comment: Aircraft Operator
    AO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#AO"
    )

    # label: RC
    # comment: Regulated Carrier
    RC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#RC"
    )

    # label: RA
    # comment: Regulated Agent
    RA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/RegulatedEntityCategoryCode#RA"
    )


class ScreeningExemption(str, Enum):
    # label: NUCL
    # comment: Nuclear Material
    NUCL = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#NUCL")

    # label: TRNS
    # comment: Transfer or Transshipment
    TRNS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#TRNS")

    # label: MAIL
    # comment: Mail
    MAIL = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#MAIL")

    # label: SMUS
    # comment: Small Undersized Shipments
    SMUS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#SMUS")

    # label: LFSM
    # comment: Life-Saving Materials (Save Human Life)
    LFSM = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#LFSM")

    # label: BIOM
    # comment: Bio-Medical Samples
    BIOM = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#BIOM")

    # label: DIPL
    # comment: Diplomatic Bags or Diplomatic Mail
    DIPL = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningExemption#DIPL")


class ScreeningMethod(str, Enum):
    # label: AOM
    # comment: Subjected to Any Other Means
    AOM = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#AOM")

    # label: ETD
    # comment: Explosives Trace Detection Equipment - Particles or Vapor
    ETD = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#ETD")

    # label: EDD
    # comment: Explosive Detection Dogs
    EDD = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#EDD")

    # label: VCK
    # comment: Visualcheck
    VCK = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#VCK")

    # label: EDS
    # comment: Explosive Detection System
    EDS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#EDS")

    # label: CMD
    # comment: Cargo Metal Detection
    CMD = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#CMD")

    # label: PHS
    # comment: Physical Inspection and/or Hand Search
    PHS = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#PHS")

    # label: XRY
    # comment: X-ray Equipment
    XRY = URIRef("https://onerecord.iata.org/ns/code-lists/ScreeningMethod#XRY")


class SecurityStatus(str, Enum):
    # label: SCO
    # comment: Cargo Secure for All-Cargo Aircraft Only
    SCO = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#SCO")

    # label: SPX
    # comment: Cargo Secure for Passenger and All-Cargo Aircraft
    SPX = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#SPX")

    # label: NSC
    # comment: Cargo Has Not Been Secured Yet for Passenger or All-Cargo Aircraft
    NSC = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#NSC")

    # label: SHR
    # comment: Secure for Passenger, All-Cargo and All-Mail Aircraft in Accordance with High Risk Requirements
    SHR = URIRef("https://onerecord.iata.org/ns/code-lists/SecurityStatus#SHR")


class ServiceCode(str, Enum):
    # label: B
    # comment: Service Shipment
    B = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#B")

    # label: E
    # comment: Airport-to-Door
    E = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#E")

    # label: D
    # comment: Door-to-Door Service
    D = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#D")

    # label: S
    # comment: Substitute Truck
    S = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#S")

    # label: P
    # comment: Small Package Service
    P = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#P")

    # label: H
    # comment: Company Mail
    H = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#H")

    # label: X
    # comment: Express Shipments
    X = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#X")

    # label: C
    # comment: Company Material
    C = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#C")

    # label: A
    # comment: Airport-to-Airport
    A = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#A")

    # label: F
    # comment: Flight Specific
    F = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#F")

    # label: T
    # comment: Charter
    T = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#T")

    # label: I
    # comment: Diplomatic Mail
    I = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#I")

    # label: J
    # comment: Priority Service
    J = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#J")

    # label: G
    # comment: Door-to-Airport
    G = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#G")


class ShipmentSecurityStatus(str, Enum):
    # label: NCR
    # comment: Screened
    NCR = URIRef("https://onerecord.iata.org/ns/code-lists/ShipmentSecurityStatus#NCR")

    # label: SCR
    # comment: Not Screened
    SCR = URIRef("https://onerecord.iata.org/ns/code-lists/ShipmentSecurityStatus#SCR")


class SignatoryRole(str, Enum):
    # label: ISSUING_AUTHORITY
    # comment: Issuing Authority
    ISSUING_AUTHORITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#ISSUING_AUTHORITY"
    )

    # label: APPLICANT
    # comment: Applicant
    APPLICANT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#APPLICANT"
    )

    # label: MANAGEMENT_AUTHORITY
    # comment: Management Authority
    MANAGEMENT_AUTHORITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#MANAGEMENT_AUTHORITY"
    )

    # label: PERMIT_ISSUER
    # comment: Permit Issuer
    PERMIT_ISSUER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#PERMIT_ISSUER"
    )

    # label: EXAMINING_AUTHORITY
    # comment: Examining Authority
    EXAMINING_AUTHORITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatoryRole#EXAMINING_AUTHORITY"
    )


class SignatureTypeCode(str, Enum):
    # label: DETENTION
    # comment: Detention
    DETENTION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#DETENTION"
    )

    # label: INSPECTION
    # comment: Inspection
    INSPECTION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#INSPECTION"
    )

    # label: FUMIGATION
    # comment: Fumigation
    FUMIGATION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#FUMIGATION"
    )

    # label: SECURITY
    # comment: Security
    SECURITY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/SignatureTypeCode#SECURITY"
    )


class SpaceAllocationCode(str, Enum):
    # label: UU
    # comment: Advice Code - Unable
    UU = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#UU")

    # label: HL
    # comment: Status Code - Holding Wait List
    HL = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#HL")

    # label: LL
    # comment: Advice Code - Wait List
    LL = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#LL")

    # label: KK
    # comment: Advice Code - Confirming
    KK = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#KK")

    # label: HN
    # comment: Status Code - Have Requested Space Allocation
    HN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#HN")

    # label: XX
    # comment: Action Code - Cancel Any Previous Space Allocation
    XX = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#XX")

    # label: NL
    # comment: Action Code - Requesting Space Allocation, for Wait List
    NL = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#NL")

    # label: NN
    # comment: Action Code - Requesting Space Allocation, Will Not Accept Alternative
    NN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#NN")

    # label: SS
    # comment: Action Code - Reporting Sale
    SS = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#SS")

    # label: CA
    # comment: Action code - Selling Space Allocation Against Allotment
    CA = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#CA")

    # label: CN
    # comment: Advice Code - Cancellation Noted
    CN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#CN")

    # label: NA
    # comment: Action code - Requesting Space Allocation, if Not Available Will Accept Alternative
    NA = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#NA")

    # label: HK
    # comment: Status Code - Holding Confirmed
    HK = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#HK")

    # label: UN
    # comment: Advice Code - Unable, Flight Does Not Operate
    UN = URIRef("https://onerecord.iata.org/ns/code-lists/SpaceAllocationCode#UN")


class SpecialHandlingCode(str, Enum):
    # label: HUM
    # comment: Human Remains in Coffin
    HUM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#HUM")

    # label: NWP
    # comment: Newspapers, Magazines
    NWP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#NWP")

    # label: EMD
    # comment: Electronic Monitoring Devices on/in Cargo/Container
    EMD = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#EMD")

    # label: RFG
    # comment: Flammable Gas
    RFG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RFG")

    # label: LIC
    # comment: License Required
    LIC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#LIC")

    # label: RXB
    # comment: Explosives 1.4B
    RXB = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RXB")

    # label: CAO
    # comment: Cargo Aircraft Only
    CAO = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#CAO")

    # label: VOL
    # comment: Volume
    VOL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#VOL")

    # label: RAC
    # comment: Reserved Air Cargo
    RAC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RAC")

    # label: PEB
    # comment: Animal products for non-human consumption
    PEB = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PEB")

    # label: RLI
    # comment: Fully Regulated Lithium Ion Batteries (Class 9)
    RLI = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RLI")

    # label: RRY
    # comment: Radioactive Material Categories II-Yellow and III-Yellow
    RRY = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RRY")

    # label: EBM
    # comment: Lithium metal batteries excepted as per Section II of PI 968
    EBM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#EBM")

    # label: AVI
    # comment: Live Animal
    AVI = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#AVI")

    # label: RPB
    # comment: Toxic Substance
    RPB = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RPB")

    # label: VIC
    # comment: Very Important Cargo
    VIC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#VIC")

    # label: ACT
    # comment: Active Temperature Controlled System
    ACT = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ACT")

    # label: EBI
    # comment: Lithium ion batteries excepted as per Section II of PI 965
    EBI = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#EBI")

    # label: FIL
    # comment: Undeveloped/Unexposed Film
    FIL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#FIL")

    # label: RCM
    # comment: Corrosive
    RCM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RCM")

    # label: PAC
    # comment: Passenger and Cargo
    PAC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PAC")

    # label: VAL
    # comment: Valuable Cargo
    VAL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#VAL")

    # label: ELI
    # comment: Lithium Ion Batteries otherwise excepted from the IATA DGR
    ELI = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ELI")

    # label: REQ
    # comment: Excepted Quantities of Dangerous Goods
    REQ = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#REQ")

    # label: RRW
    # comment: Radioactive Material Category I-White
    RRW = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RRW")

    # label: ATT
    # comment: Goods Attached to Air Waybill
    ATT = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ATT")

    # label: RNG
    # comment: Non-Flammable Non-Toxic Gas
    RNG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RNG")

    # label: HEA
    # comment: Heavy Cargo/150 kilograms and over per piece
    HEA = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#HEA")

    # label: MAL
    # comment: Mail
    MAL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#MAL")

    # label: RFW
    # comment: Dangerous When Wet
    RFW = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RFW")

    # label: RXG
    # comment: Explosives 1.4G
    RXG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RXG")

    # label: WET
    # comment: Shipments of Wet Material not Packed in Watertight Containers
    WET = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#WET")

    # label: RGX
    # comment: Explosives 1.3G
    RGX = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RGX")

    # label: RXS
    # comment: Explosives 1.4S
    RXS = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RXS")

    # label: RFL
    # comment: Flammable Liquid
    RFL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RFL")

    # label: SWP
    # comment: Sporting Weapons
    SWP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#SWP")

    # label: RBM
    # comment: Fully regulated lithium metal batteries (Class 9, UN 3090) as per Section IA and IB of PI 968
    RBM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RBM")

    # label: PEP
    # comment: Fruits and Vegetables
    PEP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PEP")

    # label: ECP
    # comment: Consignment established with a paper air waybill contract being printed under an e-AWB agreement
    ECP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ECP")

    # label: ROX
    # comment: Oxidizer
    ROX = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ROX")

    # label: RLM
    # comment: Fully Regulated Lithium Metal Batteries (Class 9)
    RLM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RLM")

    # label: COM
    # comment: Company Mail
    COM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#COM")

    # label: RXC
    # comment: Explosives 1.4C
    RXC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RXC")

    # label: ICE
    # comment: Dry Ice
    ICE = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ICE")

    # label: RSB
    # comment: Polymeric Beads
    RSB = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RSB")

    # label: PEM
    # comment: Meat
    PEM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PEM")

    # label: FRI
    # comment: Frozen Goods Subject to Veterinary/Phytosanitary Inspections
    FRI = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#FRI")

    # label: RFS
    # comment: Flammable Solid
    RFS = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RFS")

    # label: RBI
    # comment: Fully regulated lithium ion batteries (Class 9, UN 3480) as per Section IA and IB of PI 965
    RBI = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RBI")

    # label: PER
    # comment: Perishable Cargo
    PER = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PER")

    # label: CRT
    # comment: Control Room Temperature +15°C to +25°C
    CRT = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#CRT")

    # label: GOH
    # comment: Hanging Garments
    GOH = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#GOH")

    # label: SUR
    # comment: Surface Transportation
    SUR = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#SUR")

    # label: RPG
    # comment: Toxic Gas
    RPG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RPG")

    # label: RSC
    # comment: Spontaneously Combustible
    RSC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RSC")

    # label: XPS
    # comment: Priority Small Package
    XPS = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#XPS")

    # label: FRO
    # comment: Frozen Goods
    FRO = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#FRO")

    # label: EAW
    # comment: e-freight Consignment with No Accompanying Paper Documents
    EAW = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#EAW")

    # label: RCL
    # comment: Cryogenic Liquids
    RCL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RCL")

    # label: ELM
    # comment: Lithium Metal Batteries otherwise excepted from the IATA DGR
    ELM = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ELM")

    # label: QRT
    # comment: Quick Ramp Transfer
    QRT = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#QRT")

    # label: RCX
    # comment: Explosives 1.3C
    RCX = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RCX")

    # label: EAP
    # comment: e-freight Consignment with Accompanying Paper Documents
    EAP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#EAP")

    # label: OBX
    # comment: Obnoxious Cargo
    OBX = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#OBX")

    # label: ECC
    # comment: Consignment established with an electronically concluded cargo contract with no accompanying paper airwaybill
    ECC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ECC")

    # label: RMD
    # comment: Miscellaneous Dangerous Goods
    RMD = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RMD")

    # label: CAT
    # comment: Cargo Attendant Accompanying Shipment
    CAT = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#CAT")

    # label: CIC
    # comment: Cargo may be loaded in the passenger cabin
    CIC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#CIC")

    # label: SPX
    # comment: Cargo Secure for Passenger and All-Cargo Aircraft
    SPX = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#SPX")

    # label: VUN
    # comment: Vulnerable Cargo
    VUN = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#VUN")

    # label: SCO
    # comment: Cargo Secure for All-Cargo Aircraft Only
    SCO = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#SCO")

    # label: PES
    # comment: Fish/Seafood
    PES = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PES")

    # label: RIS
    # comment: Infectious Substance
    RIS = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RIS")

    # label: ERT
    # comment: Extended Room Temperature +2°C to +25°C
    ERT = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ERT")

    # label: NST
    # comment: Non Stackable Cargo
    NST = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#NST")

    # label: EAT
    # comment: Foodstuffs
    EAT = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#EAT")

    # label: PIL
    # comment: Pharmaceuticals
    PIL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PIL")

    # label: ROP
    # comment: Organic Peroxide
    ROP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#ROP")

    # label: BUP
    # comment: Bulk Unitization Programme, Shipper/Consignee Handled Unit
    BUP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#BUP")

    # label: RXD
    # comment: Explosives 1.4D
    RXD = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RXD")

    # label: PHY
    # comment: Goods subject to phytosanitary inspections
    PHY = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PHY")

    # label: SPF
    # comment: Laboratory Animals
    SPF = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#SPF")

    # label: HEG
    # comment: Hatching Eggs
    HEG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#HEG")

    # label: MUW
    # comment: Munitions of War
    MUW = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#MUW")

    # label: REX
    # comment: To be reserved for normally forbidden Explosives, Divisions 1.1, 1.2, 1.3, 1.4F, 1.5 and 1.6
    REX = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#REX")

    # label: LHO
    # comment: Living Human Organs/Blood
    LHO = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#LHO")

    # label: SHL
    # comment: Save Human Life
    SHL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#SHL")

    # label: COL
    # comment: Cool Goods
    COL = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#COL")

    # label: OHG
    # comment: Overhang Item
    OHG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#OHG")

    # label: SHR
    # comment: Secure for Passenger, All-Cargo and All-Mail Aircraft in Accordance with High Risk Requirements
    SHR = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#SHR")

    # label: PEF
    # comment: Flowers
    PEF = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PEF")

    # label: MAG
    # comment: Magnetized Material
    MAG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#MAG")

    # label: RXE
    # comment: Explosives 1.4E
    RXE = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RXE")

    # label: PEA
    # comment: Hunting trophies, skin, hide and all articles made from or containing parts of species listed in the CITES (Convention on International Trade in Endangered Species) appendices
    PEA = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PEA")

    # label: NSC
    # comment: Cargo Has Not Been Secured Yet for Passenger or All-Cargo Aircraft
    NSC = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#NSC")

    # label: AOG
    # comment: Aircraft on Ground
    AOG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#AOG")

    # label: DIP
    # comment: Diplomatic Mail
    DIP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#DIP")

    # label: BIG
    # comment: Outsized
    BIG = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#BIG")

    # label: PIP
    # comment: Passive Insulated Packaging
    PIP = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#PIP")

    # label: RRE
    # comment: Excepted Quantities of Radioactive Material
    RRE = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RRE")

    # label: RDS
    # comment: Diagnostic Specimens
    RDS = URIRef("https://onerecord.iata.org/ns/code-lists/SpecialHandlingCode#RDS")


class StatusCode(str, Enum):
    # label: DIS_MSAV
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Mail Document
    DIS_MSAV = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSAV")

    # label: RCS
    # comment: The consignment has been physically received from the shipper or the shipper’s agent and is considered by the carrier as ready for carriage on this date at this location
    RCS = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#RCS")

    # label: DIS_FDMB
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Mailbag
    DIS_FDMB = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDMB")

    # label: DOC
    # comment: Documents Received by Handling Party
    DOC = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DOC")

    # label: TRM
    # comment: The consignment has been manifested and/or will be physically transferred to this carrier at this location
    TRM = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#TRM")

    # label: DIS_OFLD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Offloaded
    DIS_OFLD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_OFLD")

    # label: DIS_MSMB
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Mailbag
    DIS_MSMB = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSMB")

    # label: DIS_MSAW
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Air Waybill
    DIS_MSAW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSAW")

    # label: OSI
    # comment: Other Service Information
    OSI = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#OSI")

    # label: FOH
    # comment: The consignment is on hand on this date at this location pending “ready for carriage” determination
    FOH = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#FOH")

    # label: OCI
    # comment: Other Customs, Security and Regulatory Control Information
    OCI = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#OCI")

    # label: CCD
    # comment: The consignment has been cleared by the Customs authorities on this date at this location
    CCD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#CCD")

    # label: DLV
    # comment: The consignment has been physically delivered to the consignee or the Consignee’s agent on this date at this location
    DLV = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DLV")

    # label: BKD
    # comment: The consignment has been booked for transport between these locations on this scheduled date and this flight
    BKD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#BKD")

    # label: RCF
    # comment: The consignment has been physically received from a given flight or surface transport of the given airline
    RCF = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#RCF")

    # label: DIS_FDAV
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Mail Document
    DIS_FDAV = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDAV")

    # label: DIS_OVCD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Overcarried
    DIS_OVCD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_OVCD")

    # label: DDL
    # comment: The consignment has been physically delivered to the consignee’s door on this date at this location
    DDL = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DDL")

    # label: MAN
    # comment: The consignment has been manifested for this flight on this scheduled date for transport between these locations
    MAN = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#MAN")

    # label: DIS_FDAW
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Air Waybill
    DIS_FDAW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDAW")

    # label: TFD
    # comment: The consignment has been physically transferred to this carrier on this date at this location
    TFD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#TFD")

    # label: NFD
    # comment: The consignee or the consignee’s agent has been notified, on this date at this location, of the arrival of the consignment
    NFD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#NFD")

    # label: TGC
    # comment: The consignment has been transferred to Customs/Government control
    TGC = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#TGC")

    # label: CRC
    # comment: The consignment has been reported to the Customs authorities on this date at this location
    CRC = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#CRC")

    # label: RCT
    # comment: The consignment has been physically received from this carrier on this date at this location
    RCT = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#RCT")

    # label: DIS_DFLD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Definitely Loaded
    DIS_DFLD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_DFLD")

    # label: PRE
    # comment: The consignment has been prepared for loading on this flight for transport between these locations on this scheduled date
    PRE = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#PRE")

    # label: FOW
    # comment: Freight Out of Warehouse Control
    FOW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#FOW")

    # label: AWR
    # comment: The arrival documentation has been physically received from a scheduled flight at this location
    AWR = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#AWR")

    # label: FIW
    # comment: Freight Into Warehouse Control
    FIW = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#FIW")

    # label: DEP
    # comment: The consignment has physically departed this location on this scheduled date and flight for transport to the arrival location
    DEP = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DEP")

    # label: DPU
    # comment: The consignment has been physically picked up from the shipper’s door on this date at this location
    DPU = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DPU")

    # label: ARR
    # comment: The consignment has arrived on a scheduled flight at this location
    ARR = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#ARR")

    # label: DIS_MSCA
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Missing Cargo
    DIS_MSCA = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_MSCA")

    # label: DIS_FDCA
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Found Cargo
    DIS_FDCA = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_FDCA")

    # label: DIS_SSPD
    # comment: An apparent error has occurred, on this date at this location, with the handling of the consignment or its documentation: Shortshipped
    DIS_SSPD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#DIS_SSPD")

    # label: AWD
    # comment: The arrival documentation has been physically delivered to the consignee or the consignee’s agent on this date at this location
    AWD = URIRef("https://onerecord.iata.org/ns/code-lists/StatusCode#AWD")


class TemperatureUnitCode(str, Enum):
    # label: KEL
    # comment: Kelvin
    KEL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KEL")

    # label: FAH
    # comment: Degree Fahrenheit
    FAH = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FAH")

    # label: CEL
    # comment: Degree Celsius
    CEL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CEL")


class TransactionPurposeCode(str, Enum):
    # label: T
    # comment: Commercial
    T = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#T")

    # label: N
    # comment: Reintroduction or introduction into the wild
    N = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#N")

    # label: E
    # comment: Educational
    E = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#E")

    # label: P
    # comment: Personal
    P = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#P")

    # label: M
    # comment: Medical (including biomedical research)
    M = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#M")

    # label: S
    # comment: Scientific
    S = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#S")

    # label: L
    # comment: Law enforcement / judicial / forensic
    L = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#L")

    # label: H
    # comment: Hunting trophy
    H = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#H")

    # label: Q
    # comment: Circus or travelling exhibition
    Q = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#Q")

    # label: B
    # comment: Breeding in captivity or artificial propagation
    B = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#B")

    # label: Z
    # comment: Zoo
    Z = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#Z")

    # label: G
    # comment: Botanical garden
    G = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#G")


class TransportMeansServiceType(str, Enum):
    # label: TRUCK
    # comment: Transport leg performed by truck
    TRUCK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#TRUCK"
    )

    # label: FREIGHTER
    # comment: Transport leg performed by freighter aircraft
    FREIGHTER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#FREIGHTER"
    )

    # label: MIXED_CONFIGURATION_COMBI
    # comment: Transport leg performed by mixed configuration combi aircraft
    MIXED_CONFIGURATION_COMBI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#MIXED_CONFIGURATION_COMBI"
    )

    # label: PASSENGER
    # comment: Transport leg performed by passenger aircraft
    PASSENGER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/TransportMeansServiceType#PASSENGER"
    )


class ULDChargeCode(str, Enum):
    # label: B
    # comment: First Minimum Charge — minimum weight
    B = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#B")

    # label: C
    # comment: First over pivot rate per kilogram
    C = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#C")

    # label: A
    # comment: Pivot Rate per kilogram
    A = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#A")

    # label: E
    # comment: Second over pivot rate per kilogram
    E = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#E")

    # label: I
    # comment: Flat Charge — maximum weight
    I = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#I")

    # label: F
    # comment: Third Minimum Charge — minimum weight
    F = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#F")

    # label: H
    # comment: Flat Charge — (without weight or with minimum weight)
    H = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#H")

    # label: D
    # comment: Second Minimum Charge — minimum weight
    D = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#D")

    # label: G
    # comment: Third over pivot rate per kilogram
    G = URIRef("https://onerecord.iata.org/ns/code-lists/ULDChargeCode#G")


class ULDConditionCode(str, Enum):
    # label: DAM
    # comment: Damaged But Still Serviceable
    DAM = URIRef("https://onerecord.iata.org/ns/code-lists/ULDConditionCode#DAM")

    # label: SER
    # comment: Serviceable
    SER = URIRef("https://onerecord.iata.org/ns/code-lists/ULDConditionCode#SER")


class ULDLoadingIndicator(str, Enum):
    # label: M
    # comment: Main Deck Loading only
    M = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#M")

    # label: U
    # comment: ULD Height between 160 centimetres and 244 centimetres
    U = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#U")

    # label: L
    # comment: ULD Height below 160 centimetres
    L = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#L")

    # label: R
    # comment: ULD Height above 244 centimetres
    R = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#R")

    # label: N
    # comment: Nose Door Loading only
    N = URIRef("https://onerecord.iata.org/ns/code-lists/ULDLoadingIndicator#N")


class VolumeUnitCode(str, Enum):
    # label: FTQ
    # comment: Cubic Foot
    FTQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#FTQ")

    # label: LTR
    # comment: Litre (1 DM3)
    LTR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#LTR")

    # label: GLL
    # comment: Liquid Gallon (3.78541 DM3)
    GLL = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#GLL")

    # label: MTQ
    # comment: Cubic Metre
    MTQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#MTQ")

    # label: INQ
    # comment: Cubic Inch
    INQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#INQ")

    # label: CMQ
    # comment: Cubic Centimetre
    CMQ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#CMQ")


class WeightUnitCode(str, Enum):
    # label: ONZ
    # comment: Ounce UK, US (28.949523 GRM)
    ONZ = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#ONZ")

    # label: KGM
    # comment: Kilogram
    KGM = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#KGM")

    # label: LBR
    # comment: Pound UK, US (0.45359237 KGM)
    LBR = URIRef("https://onerecord.iata.org/ns/code-lists/MeasurementUnitCode#LBR")


for _cls in list(locals().values()):
    if isinstance(_cls, type) and issubclass(_cls, OneRecordBaseModel):
        result = _cls.model_rebuild()
        if result is False:
            raise RuntimeError(f"Failed to rebuild model for class {_cls.__name__}")
