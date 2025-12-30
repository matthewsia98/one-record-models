from enum import Enum

from rdflib import URIRef


class OtherChargeCode(str, Enum):
    """
    label: OtherChargeCode
    comment: Restricted code list corresponding to cXML code list 1.2 Other Charge Codes
    """

    # label: AC
    # comment: Animal Container
    AC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AC")
    # label: AS
    # comment: Assembly Service Fee
    AS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AS")
    # label: AT
    # comment: Attendant
    AT = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AT")
    # label: AW
    # comment: Air Waybill Fee
    AW = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#AW")
    # label: BA
    # comment: Advances and/or guarantees
    BA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BA")
    # label: BB
    # comment: Appraisal Service
    BB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BB")
    # label: BC
    # comment: AWB Copy
    BC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BC")
    # label: BE
    # comment: Collection of funds
    BE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BE")
    # label: BF
    # comment: Copies of documents
    BF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BF")
    # label: BH
    # comment: Messenger service
    BH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BH")
    # label: BI
    # comment: Import/export documents processing
    BI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BI")
    # label: BL
    # comment: Blacklist Certificate
    BL = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BL")
    # label: BM
    # comment: Withdrawal of shipment after clearance
    BM = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BM")
    # label: BR
    # comment: Bank Release
    BR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#BR")
    # label: CA
    # comment: Bonding
    CA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CA")
    # label: CB
    # comment: Completion/preparation of documents
    CB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CB")
    # label: CC
    # comment: Manual data entry for customs purposes
    CC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CC")
    # label: CD
    # comment: Clearance and Handling — Destination
    CD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CD")
    # label: CE
    # comment: Export/Import warrant
    CE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CE")
    # label: CF
    # comment: Inventory and/or inspection
    CF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CF")
    # label: CG
    # comment: Electronic processing or transmission of data for customs purposes
    CG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CG")
    # label: CH
    # comment: Clearance and Handling — Origin
    CH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CH")
    # label: CI
    # comment: Overtime and Other Customs Imposed Charges
    CI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CI")
    # label: CJ
    # comment: Removal (carrier warehouse to warehouse)
    CJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#CJ")
    # label: DB
    # comment: Disbursement Fee
    DB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DB")
    # label: DC
    # comment: Certificate of Origin
    DC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DC")
    # label: DD
    # comment: Preparation of Cargo manifest
    DD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DD")
    # label: DF
    # comment: Distribution Service Fee
    DF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DF")
    # label: DG
    # comment: AWB Cancellation
    DG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DG")
    # label: DH
    # comment: AWB Charges Correction Advice
    DH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DH")
    # label: DI
    # comment: AWB Re-waybilling
    DI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DI")
    # label: DJ
    # comment: Proof of delivery (documentation)
    DJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DJ")
    # label: DK
    # comment: Release order
    DK = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DK")
    # label: DV
    # comment: Veterinary and/or Phytosanitary purposes
    DV = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#DV")
    # label: EA
    # comment: Handling (Express)
    EA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#EA")
    # label: FA
    # comment: Airport arrival
    FA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FA")
    # label: FB
    # comment: Domestic shipments
    FB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FB")
    # label: FC
    # comment: Charges Collect Fee
    FC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FC")
    # label: FD
    # comment: Priority
    FD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FD")
    # label: FE
    # comment: General (Handling)
    FE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FE")
    # label: FF
    # comment: Loading/unloading
    FF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FF")
    # label: FI
    # comment: Weighing
    FI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#FI")
    # label: GA
    # comment: Diplomatic consignment
    GA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#GA")
    # label: GT
    # comment: Government Tax
    GT = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#GT")
    # label: HB
    # comment: Mortuary
    HB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#HB")
    # label: HR
    # comment: Human Remains
    HR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#HR")
    # label: IA
    # comment: Very important cargo (VIC)
    IA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#IA")
    # label: IN
    # comment: Insurance Premium
    IN = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#IN")
    # label: JA
    # comment: Clearance, General
    JA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#JA")
    # label: KA
    # comment: Handling (Heavy/Bulky cargo)
    KA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#KA")
    # label: KB
    # comment: Loading/unloading equipment (forklift etc.)
    KB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#KB")
    # label: LA
    # comment: Live Animals
    LA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LA")
    # label: LC
    # comment: Cleaning
    LC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LC")
    # label: LE
    # comment: Hotel
    LE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LE")
    # label: LF
    # comment: Quarantine
    LF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LF")
    # label: LG
    # comment: Veterinary inspection
    LG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LG")
    # label: LH
    # comment: Storage (Live animals)
    LH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LH")
    # label: LI
    # comment: Cleaning of stalls/pens
    LI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LI")
    # label: LJ
    # comment: Rental of Stalls/pens
    LJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#LJ")
    # label: MA
    # comment: Miscellaneous — Due Agent (see Note 1)
    MA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MA")
    # label: MB
    # comment: Miscellaneous — Unassigned (see Note 2)
    MB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MB")
    # label: MC
    # comment: Miscellaneous — Due Carrier (see Note 3)
    MC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MC")
    # label: MD
    # comment: Miscellaneous — Due Last Carrier
    MD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MD")
    # label: ME
    # comment: Miscellaneous — Due Last Carrier
    ME = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ME")
    # label: MF
    # comment: Miscellaneous — Due Last Carrier
    MF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MF")
    # label: MG
    # comment: Miscellaneous — Due Last Carrier
    MG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MG")
    # label: MH
    # comment: Miscellaneous — Due Last Carrier
    MH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MH")
    # label: MI
    # comment: Miscellaneous — Due Last Carrier
    MI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MI")
    # label: MJ
    # comment: Miscellaneous — Due Last Carrier
    MJ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MJ")
    # label: MK
    # comment: Miscellaneous — Due Last Carrier
    MK = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MK")
    # label: ML
    # comment: Miscellaneous — Due Last Carrier
    ML = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ML")
    # label: MM
    # comment: Miscellaneous — Due Last Carrier
    MM = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MM")
    # label: MN
    # comment: Miscellaneous — Due Last Carrier
    MN = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MN")
    # label: MO
    # comment: Miscellaneous — Due Issuing Carrier
    MO = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MO")
    # label: MP
    # comment: Miscellaneous — Due Issuing Carrier
    MP = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MP")
    # label: MQ
    # comment: Miscellaneous — Due Issuing Carrier
    MQ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MQ")
    # label: MR
    # comment: Miscellaneous — Due Issuing Carrier
    MR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MR")
    # label: MS
    # comment: Miscellaneous — Due Issuing Carrier
    MS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MS")
    # label: MT
    # comment: Miscellaneous — Due Issuing Carrier
    MT = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MT")
    # label: MU
    # comment: Miscellaneous — Due Issuing Carrier
    MU = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MU")
    # label: MV
    # comment: Miscellaneous — Due Issuing Carrier
    MV = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MV")
    # label: MW
    # comment: Miscellaneous — Due Issuing Carrier
    MW = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MW")
    # label: MX
    # comment: Miscellaneous — Due Issuing Carrier
    MX = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MX")
    # label: MY
    # comment: Fuel Surcharge — Due Issuing Carrier
    MY = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MY")
    # label: MZ
    # comment: Miscellaneous — Due Issuing Carrier
    MZ = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#MZ")
    # label: NS
    # comment: Navigation Surcharge — Due Issuing Carrier
    NS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#NS")
    # label: PA
    # comment: Handling (Perishables)
    PA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PA")
    # label: PB
    # comment: Cool/Cold room, freezer (Perishables)
    PB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PB")
    # label: PK
    # comment: Packing/Repacking
    PK = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PK")
    # label: PU
    # comment: Pick-Up
    PU = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#PU")
    # label: RA
    # comment: Dangerous Goods Fee
    RA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RA")
    # label: RB
    # comment: Rejection
    RB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RB")
    # label: RC
    # comment: Referral of Charge
    RC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RC")
    # label: RD
    # comment: Radio-active room
    RD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RD")
    # label: RF
    # comment: Remit Following Collection Fee
    RF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#RF")
    # label: SA
    # comment: Delivery
    SA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SA")
    # label: SB
    # comment: Delivery notification
    SB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SB")
    # label: SC
    # comment: Security Charge
    SC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SC")
    # label: SD
    # comment: Surface Charge — Destination
    SD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SD")
    # label: SE
    # comment: Proof of delivery (pickup and delivery)
    SE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SE")
    # label: SF
    # comment: Delivery Order
    SF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SF")
    # label: SI
    # comment: Stop in Transit
    SI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SI")
    # label: SO
    # comment: Storage — Origin
    SO = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SO")
    # label: SP
    # comment: Separate Early Release
    SP = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SP")
    # label: SR
    # comment: Storage — Destination
    SR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SR")
    # label: SS
    # comment: Signature Service
    SS = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SS")
    # label: ST
    # comment: State Sales Tax
    ST = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ST")
    # label: SU
    # comment: Surface Charge — Origin
    SU = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#SU")
    # label: TA
    # comment: Postal Tax
    TA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TA")
    # label: TB
    # comment: Sales Tax
    TB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TB")
    # label: TC
    # comment: Stamp Tax
    TC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TC")
    # label: TD
    # comment: State Tax
    TD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TD")
    # label: TE
    # comment: Statistical Tax
    TE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TE")
    # label: TI
    # comment: Value Added Tax (For Import only)
    TI = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TI")
    # label: TR
    # comment: Transit
    TR = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TR")
    # label: TV
    # comment: Value Added Tax (General or for Export)
    TV = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TV")
    # label: TX
    # comment: General Taxes
    TX = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#TX")
    # label: UB
    # comment: Disassembly
    UB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UB")
    # label: UC
    # comment: Adjusting of improperly loaded ULD
    UC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UC")
    # label: UD
    # comment: Demurrage
    UD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UD")
    # label: UE
    # comment: Leasing
    UE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UE")
    # label: UF
    # comment: Recontouring
    UF = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UF")
    # label: UG
    # comment: Unloading (Unit Load Device)
    UG = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UG")
    # label: UH
    # comment: Handling (Unit Load Device)
    UH = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#UH")
    # label: VA
    # comment: Handling (Valuable Cargo)
    VA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#VA")
    # label: VB
    # comment: Security (armed guard/escort) handling
    VB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#VB")
    # label: VC
    # comment: Strongroom
    VC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#VC")
    # label: WA
    # comment: Handling (Vulnerable cargo)
    WA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#WA")
    # label: XB
    # comment: Security (Surcharge/premiums)
    XB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XB")
    # label: XC
    # comment: Time
    XC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XC")
    # label: XD
    # comment: War risk
    XD = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XD")
    # label: XE
    # comment: Weight
    XE = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#XE")
    # label: ZA
    # comment: Re-warehousing
    ZA = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ZA")
    # label: ZB
    # comment: General (Storage)
    ZB = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ZB")
    # label: ZC
    # comment: Cool/Cold room, freezer (Storage)
    ZC = URIRef("https://onerecord.iata.org/ns/code-lists/OtherChargeCode#ZC")
