from enum import Enum

from rdflib import URIRef


class CommodityCode(str, Enum):
    """
    label: CommodityCode
    comment: Restricted code list of accepted commodities in carrier bookings when no HS code available
    """

    # label: CHEM
    # comment: Chemicals
    CHEM = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM")
    # label: CHEM_CDGR
    # comment: Chemicals - Dangerous
    CHEM_CDGR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CDGR"
    )
    # label: CHEM_CLNG
    # comment: Cleaning products
    CHEM_CLNG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CLNG"
    )
    # label: CHEM_CNDG
    # comment: Chemicals - Not dangerous
    CHEM_CNDG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CNDG"
    )
    # label: CHEM_CNMD
    # comment: Chemicals - Not Medical
    CHEM_CNMD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_CNMD"
    )
    # label: CHEM_COSM
    # comment: Cosmetics
    CHEM_COSM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_COSM"
    )
    # label: CHEM_COSM_COSD
    # comment: Cosmetics - DGR
    CHEM_COSM_COSD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_COSM_COSD"
    )
    # label: CHEM_COSM_PERF
    # comment: Perfume
    CHEM_COSM_PERF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_COSM_PERF"
    )
    # label: CHEM_DGRG
    # comment: Dangerous Goods
    CHEM_DGRG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_DGRG"
    )
    # label: CHEM_DGRG_EXPL
    # comment: Explosives
    CHEM_DGRG_EXPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_DGRG_EXPL"
    )
    # label: CHEM_DICE
    # comment: Dry ice
    CHEM_DICE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_DICE"
    )
    # label: CHEM_PAIN
    # comment: Paint
    CHEM_PAIN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_PAIN"
    )
    # label: CHEM_PETRO
    # comment: Petroleum derivatives
    CHEM_PETRO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_PETRO"
    )
    # label: CHEM_RADA
    # comment: Radioactive materials
    CHEM_RADA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_RADA"
    )
    # label: CHEM_REAG
    # comment: Reagents
    CHEM_REAG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CHEM_REAG"
    )
    # label: CONS
    # comment: Consumer goods
    CONS = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS")
    # label: CONS_CMPY
    # comment: Company material
    CONS_CMPY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_CMPY"
    )
    # label: CONS_CWRE
    # comment: Chinaware and Ceramics
    CONS_CWRE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_CWRE"
    )
    # label: CONS_DIPL
    # comment: Diplomatic mail and goods
    CONS_DIPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_DIPL"
    )
    # label: CONS_EXHB
    # comment: Exhibition goods
    CONS_EXHB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_EXHB"
    )
    # label: CONS_FRNT
    # comment: Furniture
    CONS_FRNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_FRNT"
    )
    # label: CONS_GLAS
    # comment: Glassware
    CONS_GLAS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_GLAS"
    )
    # label: CONS_HAID
    # comment: Humanitarian aid
    CONS_HAID = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HAID"
    )
    # label: CONS_HHGD
    # comment: Household goods
    CONS_HHGD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HHGD"
    )
    # label: CONS_HRSE
    # comment: Horse equipment
    CONS_HRSE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HRSE"
    )
    # label: CONS_HSER
    # comment: House removal
    CONS_HSER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_HSER"
    )
    # label: CONS_OFSP
    # comment: Office supplies
    CONS_OFSP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_OFSP"
    )
    # label: CONS_PERS
    # comment: Personal effects
    CONS_PERS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_PERS"
    )
    # label: CONS_SPEC
    # comment: Spectacles
    CONS_SPEC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_SPEC"
    )
    # label: CONS_SPRT
    # comment: Sports equipment
    CONS_SPRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_SPRT"
    )
    # label: CONS_TOYS
    # comment: Toys and Games
    CONS_TOYS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_TOYS"
    )
    # label: CONS_UBAG
    # comment: Unaccompagnied baggage
    CONS_UBAG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#CONS_UBAG"
    )
    # label: ELEC
    # comment: Electronic equipment
    ELEC = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC")
    # label: ELEC_AVEQ
    # comment: Audio-Video-HiFi equipment
    ELEC_AVEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_AVEQ"
    )
    # label: ELEC_CALC
    # comment: Calculators
    ELEC_CALC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_CALC"
    )
    # label: ELEC_CMPT
    # comment: Computers
    ELEC_CMPT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_CMPT"
    )
    # label: ELEC_CPRT
    # comment: Computer parts
    ELEC_CPRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_CPRT"
    )
    # label: ELEC_ECOM
    # comment: Electronic components
    ELEC_ECOM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_ECOM"
    )
    # label: ELEC_EEQP
    # comment: Electronic equipment
    ELEC_EEQP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_EEQP"
    )
    # label: ELEC_EGDS
    # comment: Electronic goods
    ELEC_EGDS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_EGDS"
    )
    # label: ELEC_ELQP
    # comment: Electrical equipment
    ELEC_ELQP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_ELQP"
    )
    # label: ELEC_OFEQ
    # comment: Office equipment
    ELEC_OFEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_OFEQ"
    )
    # label: ELEC_QUAN
    # comment: Quantum
    ELEC_QUAN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_QUAN"
    )
    # label: ELEC_TELC
    # comment: Telecom equipment
    ELEC_TELC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#ELEC_TELC"
    )
    # label: FLWR
    # comment: Plants, Flowers, Seeds
    FLWR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR")
    # label: FLWR_FLWR
    # comment: Fresh flowers
    FLWR_FLWR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR"
    )
    # label: FLWR_FLWR_CFLW
    # comment: Cut flowers
    FLWR_FLWR_CFLW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR_CFLW"
    )
    # label: FLWR_FLWR_TFLW
    # comment: Tropical flowers
    FLWR_FLWR_TFLW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR_TFLW"
    )
    # label: FLWR_FLWR_TULP
    # comment: Fresh tulips
    FLWR_FLWR_TULP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FLWR_TULP"
    )
    # label: FLWR_FMNT
    # comment: Fresh mint
    FLWR_FMNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_FMNT"
    )
    # label: FLWR_HERBS
    # comment: Herbs, Leaves and Foliage
    FLWR_HERBS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_HERBS"
    )
    # label: FLWR_PLNT
    # comment: Plants
    FLWR_PLNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT"
    )
    # label: FLWR_PLNT_APLN
    # comment: Aquatic plants
    FLWR_PLNT_APLN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_APLN"
    )
    # label: FLWR_PLNT_BULB
    # comment: Bulbs and Tubers
    FLWR_PLNT_BULB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_BULB"
    )
    # label: FLWR_PLNT_MPLN
    # comment: Medicinal plants
    FLWR_PLNT_MPLN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_MPLN"
    )
    # label: FLWR_PLNT_TPLN
    # comment: Tropical plants
    FLWR_PLNT_TPLN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_PLNT_TPLN"
    )
    # label: FLWR_SEED
    # comment: Seeds
    FLWR_SEED = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FLWR_SEED"
    )
    # label: FOOD
    # comment: Foodstuffs, Drinks and Tobacco
    FOOD = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD")
    # label: FOOD_BVRG
    # comment: Beverages
    FOOD_BVRG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG"
    )
    # label: FOOD_BVRG_BEER
    # comment: Beer
    FOOD_BVRG_BEER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_BEER"
    )
    # label: FOOD_BVRG_COFY
    # comment: Coffee
    FOOD_BVRG_COFY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_COFY"
    )
    # label: FOOD_BVRG_TEA
    # comment: Tea
    FOOD_BVRG_TEA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_TEA"
    )
    # label: FOOD_BVRG_WINE
    # comment: Wine
    FOOD_BVRG_WINE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_BVRG_WINE"
    )
    # label: FOOD_CERE
    # comment: Cereal foods
    FOOD_CERE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_CERE"
    )
    # label: FOOD_CERE_BRED
    # comment: Bread
    FOOD_CERE_BRED = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_CERE_BRED"
    )
    # label: FOOD_CERE_CAKE
    # comment: Cakes and Pastries
    FOOD_CERE_CAKE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_CERE_CAKE"
    )
    # label: FOOD_DARY
    # comment: Dairy products
    FOOD_DARY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY"
    )
    # label: FOOD_DARY_CHSE
    # comment: Cheese
    FOOD_DARY_CHSE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY_CHSE"
    )
    # label: FOOD_DARY_EGGS
    # comment: Eggs
    FOOD_DARY_EGGS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY_EGGS"
    )
    # label: FOOD_DARY_ICEC
    # comment: Ice cream
    FOOD_DARY_ICEC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_DARY_ICEC"
    )
    # label: FOOD_FISH
    # comment: Fish and Seafood
    FOOD_FISH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH"
    )
    # label: FOOD_FISH_ALBA
    # comment: Albacora
    FOOD_FISH_ALBA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_ALBA"
    )
    # label: FOOD_FISH_CAVR
    # comment: Caviar
    FOOD_FISH_CAVR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_CAVR"
    )
    # label: FOOD_FISH_FFSH
    # comment: Fresh fish
    FOOD_FISH_FFSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_FFSH"
    )
    # label: FOOD_FISH_FRZF
    # comment: Frozen fish
    FOOD_FISH_FRZF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_FRZF"
    )
    # label: FOOD_FISH_FRZS
    # comment: Frozen seafood
    FOOD_FISH_FRZS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_FRZS"
    )
    # label: FOOD_FISH_HAKE
    # comment: Hake
    FOOD_FISH_HAKE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_HAKE"
    )
    # label: FOOD_FISH_LOBS
    # comment: Lobsters and Crabs
    FOOD_FISH_LOBS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_LOBS"
    )
    # label: FOOD_FISH_REPA
    # comment: Reineta and Palometa
    FOOD_FISH_REPA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_REPA"
    )
    # label: FOOD_FISH_SFIN
    # comment: Shark fin
    FOOD_FISH_SFIN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SFIN"
    )
    # label: FOOD_FISH_SFSH
    # comment: Smoked fish
    FOOD_FISH_SFSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SFSH"
    )
    # label: FOOD_FISH_SHRI
    # comment: Shrimps and Prawns
    FOOD_FISH_SHRI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SHRI"
    )
    # label: FOOD_FISH_SLMN
    # comment: Salmon
    FOOD_FISH_SLMN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_SLMN"
    )
    # label: FOOD_FISH_TUNA
    # comment: Tuna
    FOOD_FISH_TUNA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FISH_TUNA"
    )
    # label: FOOD_FRTV
    # comment: Fruits and Vegetables
    FOOD_FRTV = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV"
    )
    # label: FOOD_FRTV_APPL
    # comment: Apples
    FOOD_FRTV_APPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_APPL"
    )
    # label: FOOD_FRTV_ASPA
    # comment: Asparagus
    FOOD_FRTV_ASPA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_ASPA"
    )
    # label: FOOD_FRTV_AVOC
    # comment: Avocados
    FOOD_FRTV_AVOC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_AVOC"
    )
    # label: FOOD_FRTV_BANA
    # comment: Bananas
    FOOD_FRTV_BANA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_BANA"
    )
    # label: FOOD_FRTV_BEAN
    # comment: String beans
    FOOD_FRTV_BEAN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_BEAN"
    )
    # label: FOOD_FRTV_BERR
    # comment: Berries
    FOOD_FRTV_BERR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_BERR"
    )
    # label: FOOD_FRTV_CHER
    # comment: Cherries
    FOOD_FRTV_CHER = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_CHER"
    )
    # label: FOOD_FRTV_CMBR
    # comment: Cucumber
    FOOD_FRTV_CMBR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_CMBR"
    )
    # label: FOOD_FRTV_DURI
    # comment: Durian
    FOOD_FRTV_DURI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_DURI"
    )
    # label: FOOD_FRTV_GARL
    # comment: Garlic
    FOOD_FRTV_GARL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_GARL"
    )
    # label: FOOD_FRTV_GRAP
    # comment: Grapes
    FOOD_FRTV_GRAP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_GRAP"
    )
    # label: FOOD_FRTV_LITC
    # comment: Litchies
    FOOD_FRTV_LITC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_LITC"
    )
    # label: FOOD_FRTV_MANG
    # comment: Mangoes
    FOOD_FRTV_MANG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_MANG"
    )
    # label: FOOD_FRTV_MLNS
    # comment: Melons
    FOOD_FRTV_MLNS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_MLNS"
    )
    # label: FOOD_FRTV_MUSH
    # comment: Mushrooms
    FOOD_FRTV_MUSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_MUSH"
    )
    # label: FOOD_FRTV_PEPP
    # comment: Peppers
    FOOD_FRTV_PEPP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PEPP"
    )
    # label: FOOD_FRTV_PINE
    # comment: Pineapple
    FOOD_FRTV_PINE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PINE"
    )
    # label: FOOD_FRTV_PPYA
    # comment: Papaya
    FOOD_FRTV_PPYA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PPYA"
    )
    # label: FOOD_FRTV_PROD
    # comment: Produce
    FOOD_FRTV_PROD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_PROD"
    )
    # label: FOOD_FRTV_STRW
    # comment: Strawberries
    FOOD_FRTV_STRW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_STRW"
    )
    # label: FOOD_FRTV_TOMA
    # comment: Tomatoes
    FOOD_FRTV_TOMA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_FRTV_TOMA"
    )
    # label: FOOD_MEAT
    # comment: Meat products
    FOOD_MEAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT"
    )
    # label: FOOD_MEAT_BEEF
    # comment: Beef products
    FOOD_MEAT_BEEF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_BEEF"
    )
    # label: FOOD_MEAT_DRIM
    # comment: Dried meat
    FOOD_MEAT_DRIM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_DRIM"
    )
    # label: FOOD_MEAT_FRZM
    # comment: Frozen meat
    FOOD_MEAT_FRZM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_FRZM"
    )
    # label: FOOD_MEAT_GOSL
    # comment: Goose liver
    FOOD_MEAT_GOSL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_GOSL"
    )
    # label: FOOD_MEAT_GUTS
    # comment: Guts
    FOOD_MEAT_GUTS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_GUTS"
    )
    # label: FOOD_MEAT_HRSP
    # comment: Horse products
    FOOD_MEAT_HRSP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_HRSP"
    )
    # label: FOOD_MEAT_MEAT
    # comment: Meat
    FOOD_MEAT_MEAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_MEAT"
    )
    # label: FOOD_MEAT_PORK
    # comment: Pork products
    FOOD_MEAT_PORK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_PORK"
    )
    # label: FOOD_MEAT_SAUS
    # comment: Sausages
    FOOD_MEAT_SAUS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_MEAT_SAUS"
    )
    # label: FOOD_PERI
    # comment: Perhishables
    FOOD_PERI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_PERI"
    )
    # label: FOOD_STUF
    # comment: Foodstuffs
    FOOD_STUF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF"
    )
    # label: FOOD_STUF_CATE
    # comment: Catering products
    FOOD_STUF_CATE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_CATE"
    )
    # label: FOOD_STUF_CHOC
    # comment: Chocolate
    FOOD_STUF_CHOC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_CHOC"
    )
    # label: FOOD_STUF_DFRU
    # comment: Dried fruit
    FOOD_STUF_DFRU = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_DFRU"
    )
    # label: FOOD_STUF_MPWD
    # comment: Milk powder
    FOOD_STUF_MPWD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_MPWD"
    )
    # label: FOOD_STUF_NUTS
    # comment: Nuts
    FOOD_STUF_NUTS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_NUTS"
    )
    # label: FOOD_STUF_OOIL
    # comment: Olive oil
    FOOD_STUF_OOIL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_OOIL"
    )
    # label: FOOD_STUF_SPCE
    # comment: Spices and Roots
    FOOD_STUF_SPCE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_STUF_SPCE"
    )
    # label: FOOD_TBCO
    # comment: Tobacco products
    FOOD_TBCO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_TBCO"
    )
    # label: FOOD_TBCO_CGRT
    # comment: Cigarettes
    FOOD_TBCO_CGRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_TBCO_CGRT"
    )
    # label: FOOD_TBCO_CIGA
    # comment: Cigars
    FOOD_TBCO_CIGA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#FOOD_TBCO_CIGA"
    )
    # label: GENE
    # comment: General Cargo
    GENE = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#GENE")
    # label: HUMR
    # comment: Human Remains
    HUMR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#HUMR")
    # label: HUMR_HUMB
    # comment: Human remains not cremated
    HUMR_HUMB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#HUMR_HUMB"
    )
    # label: HUMR_HUMC
    # comment: Human remains cremated
    HUMR_HUMC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#HUMR_HUMC"
    )
    # label: LIVE
    # comment: Live Animals
    LIVE = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE")
    # label: LIVE_BRDH
    # comment: Birds & Hatching Eggs
    LIVE_BRDH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH"
    )
    # label: LIVE_BRDH_BIRD
    # comment: Birds
    LIVE_BRDH_BIRD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_BIRD"
    )
    # label: LIVE_BRDH_CHIC
    # comment: Chicks
    LIVE_BRDH_CHIC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_CHIC"
    )
    # label: LIVE_BRDH_DUCK
    # comment: Ducks
    LIVE_BRDH_DUCK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_DUCK"
    )
    # label: LIVE_BRDH_HEGG
    # comment: Hatching Eggs
    LIVE_BRDH_HEGG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_HEGG"
    )
    # label: LIVE_BRDH_OSTR
    # comment: Ostriches
    LIVE_BRDH_OSTR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_OSTR"
    )
    # label: LIVE_BRDH_PARR
    # comment: Parrots
    LIVE_BRDH_PARR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_PARR"
    )
    # label: LIVE_BRDH_TRKY
    # comment: Turkeys
    LIVE_BRDH_TRKY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_BRDH_TRKY"
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
    # label: LIVE_LFSH
    # comment: Fish
    LIVE_LFSH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH"
    )
    # label: LIVE_LFSH_EELS
    # comment: Eels
    LIVE_LFSH_EELS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH_EELS"
    )
    # label: LIVE_LFSH_KOIF
    # comment: Koi fish
    LIVE_LFSH_KOIF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH_KOIF"
    )
    # label: LIVE_LFSH_TRPF
    # comment: Tropical fish
    LIVE_LFSH_TRPF = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_LFSH_TRPF"
    )
    # label: LIVE_MLKS
    # comment: Mollusks
    LIVE_MLKS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MLKS"
    )
    # label: LIVE_MLKS_LUGW
    # comment: Lugworms
    LIVE_MLKS_LUGW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MLKS_LUGW"
    )
    # label: LIVE_MLKS_SNAI
    # comment: Snails
    LIVE_MLKS_SNAI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MLKS_SNAI"
    )
    # label: LIVE_MMLS
    # comment: Mammals
    LIVE_MMLS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS"
    )
    # label: LIVE_MMLS_CATL
    # comment: Cattle
    LIVE_MMLS_CATL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATL"
    )
    # label: LIVE_MMLS_CATS
    # comment: Cats
    LIVE_MMLS_CATS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS"
    )
    # label: LIVE_MMLS_CATS_Abyssinian
    # comment: Abyssinian
    LIVE_MMLS_CATS_Abyssinian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Abyssinian"
    )
    # label: LIVE_MMLS_CATS_American_Bobtail
    # comment: American Bobtail
    LIVE_MMLS_CATS_American_Bobtail = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Bobtail"
    )
    # label: LIVE_MMLS_CATS_American_Curl
    # comment: American Curl
    LIVE_MMLS_CATS_American_Curl = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Curl"
    )
    # label: LIVE_MMLS_CATS_American_Keuda
    # comment: American Keuda
    LIVE_MMLS_CATS_American_Keuda = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Keuda"
    )
    # label: LIVE_MMLS_CATS_American_Lynx
    # comment: American Lynx
    LIVE_MMLS_CATS_American_Lynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Lynx"
    )
    # label: LIVE_MMLS_CATS_American_Polydactyl
    # comment: American Polydactyl
    LIVE_MMLS_CATS_American_Polydactyl = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Polydactyl"
    )
    # label: LIVE_MMLS_CATS_American_Shorthair
    # comment: American Shorthair
    LIVE_MMLS_CATS_American_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Shorthair"
    )
    # label: LIVE_MMLS_CATS_American_Wirehair
    # comment: American Wirehair
    LIVE_MMLS_CATS_American_Wirehair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_American_Wirehair"
    )
    # label: LIVE_MMLS_CATS_Asian
    # comment: Asian
    LIVE_MMLS_CATS_Asian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Asian"
    )
    # label: LIVE_MMLS_CATS_Australian_Mist
    # comment: Australian Mist
    LIVE_MMLS_CATS_Australian_Mist = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Australian_Mist"
    )
    # label: LIVE_MMLS_CATS_Balinese
    # comment: Balinese
    LIVE_MMLS_CATS_Balinese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Balinese"
    )
    # label: LIVE_MMLS_CATS_Bengal
    # comment: Bengal
    LIVE_MMLS_CATS_Bengal = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Bengal"
    )
    # label: LIVE_MMLS_CATS_Birman
    # comment: Birman
    LIVE_MMLS_CATS_Birman = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Birman"
    )
    # label: LIVE_MMLS_CATS_Bombay
    # comment: Bombay
    LIVE_MMLS_CATS_Bombay = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Bombay"
    )
    # label: LIVE_MMLS_CATS_Bristol
    # comment: Bristol
    LIVE_MMLS_CATS_Bristol = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Bristol"
    )
    # label: LIVE_MMLS_CATS_British_Shorthair
    # comment: British Shorthair
    LIVE_MMLS_CATS_British_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_British_Shorthair"
    )
    # label: LIVE_MMLS_CATS_Burmese
    # comment: Burmese
    LIVE_MMLS_CATS_Burmese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Burmese"
    )
    # label: LIVE_MMLS_CATS_California_Spangled
    # comment: California Spangled
    LIVE_MMLS_CATS_California_Spangled = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_California_Spangled"
    )
    # label: LIVE_MMLS_CATS_Chartreux
    # comment: Chartreux
    LIVE_MMLS_CATS_Chartreux = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Chartreux"
    )
    # label: LIVE_MMLS_CATS_Chausie
    # comment: Chausie
    LIVE_MMLS_CATS_Chausie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Chausie"
    )
    # label: LIVE_MMLS_CATS_Chinese_Harlequin
    # comment: Chinese Harlequin
    LIVE_MMLS_CATS_Chinese_Harlequin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Chinese_Harlequin"
    )
    # label: LIVE_MMLS_CATS_Color_Point_Shorthair
    # comment: Color Point Shorthair
    LIVE_MMLS_CATS_Color_Point_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Color_Point_Shorthair"
    )
    # label: LIVE_MMLS_CATS_Copper
    # comment: Copper
    LIVE_MMLS_CATS_Copper = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Copper"
    )
    # label: LIVE_MMLS_CATS_Cornish_Rex
    # comment: Cornish Rex
    LIVE_MMLS_CATS_Cornish_Rex = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Cornish_Rex"
    )
    # label: LIVE_MMLS_CATS_Cymric
    # comment: Cymric
    LIVE_MMLS_CATS_Cymric = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Cymric"
    )
    # label: LIVE_MMLS_CATS_Desert_Lynx
    # comment: Desert Lynx
    LIVE_MMLS_CATS_Desert_Lynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Desert_Lynx"
    )
    # label: LIVE_MMLS_CATS_Devon_Rex
    # comment: Devon Rex
    LIVE_MMLS_CATS_Devon_Rex = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Devon_Rex"
    )
    # label: LIVE_MMLS_CATS_Donskoy
    # comment: Donskoy
    LIVE_MMLS_CATS_Donskoy = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Donskoy"
    )
    # label: LIVE_MMLS_CATS_Egyptian_Mau
    # comment: Egyptian Mau
    LIVE_MMLS_CATS_Egyptian_Mau = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Egyptian_Mau"
    )
    # label: LIVE_MMLS_CATS_Exotic_Shorthair
    # comment: Exotic Shorthair
    LIVE_MMLS_CATS_Exotic_Shorthair = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Exotic_Shorthair"
    )
    # label: LIVE_MMLS_CATS_Havana
    # comment: Havana
    LIVE_MMLS_CATS_Havana = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Havana"
    )
    # label: LIVE_MMLS_CATS_Highland_Lynx
    # comment: Highland Lynx
    LIVE_MMLS_CATS_Highland_Lynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Highland_Lynx"
    )
    # label: LIVE_MMLS_CATS_Himalayan
    # comment: Himalayan
    LIVE_MMLS_CATS_Himalayan = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Himalayan"
    )
    # label: LIVE_MMLS_CATS_Japanese_Bobtail
    # comment: Japanese Bobtail
    LIVE_MMLS_CATS_Japanese_Bobtail = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Japanese_Bobtail"
    )
    # label: LIVE_MMLS_CATS_Javanese
    # comment: Javanese
    LIVE_MMLS_CATS_Javanese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Javanese"
    )
    # label: LIVE_MMLS_CATS_Korat
    # comment: Korat
    LIVE_MMLS_CATS_Korat = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Korat"
    )
    # label: LIVE_MMLS_CATS_LaPerm
    # comment: LaPerm
    LIVE_MMLS_CATS_LaPerm = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_LaPerm"
    )
    # label: LIVE_MMLS_CATS_Maine_Coon
    # comment: Maine Coon
    LIVE_MMLS_CATS_Maine_Coon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Maine_Coon"
    )
    # label: LIVE_MMLS_CATS_Manx
    # comment: Manx
    LIVE_MMLS_CATS_Manx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Manx"
    )
    # label: LIVE_MMLS_CATS_Mojave_Spotted
    # comment: Mojave Spotted
    LIVE_MMLS_CATS_Mojave_Spotted = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Mojave_Spotted"
    )
    # label: LIVE_MMLS_CATS_Munchkin
    # comment: Munchkin
    LIVE_MMLS_CATS_Munchkin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Munchkin"
    )
    # label: LIVE_MMLS_CATS_Niebelung
    # comment: Niebelung
    LIVE_MMLS_CATS_Niebelung = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Niebelung"
    )
    # label: LIVE_MMLS_CATS_Norwegian_Forest
    # comment: Norwegian Forest
    LIVE_MMLS_CATS_Norwegian_Forest = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Norwegian_Forest"
    )
    # label: LIVE_MMLS_CATS_Ocicat
    # comment: Ocicat
    LIVE_MMLS_CATS_Ocicat = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ocicat"
    )
    # label: LIVE_MMLS_CATS_Ojos_Azules
    # comment: Ojos Azules
    LIVE_MMLS_CATS_Ojos_Azules = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ojos_Azules"
    )
    # label: LIVE_MMLS_CATS_Oriental
    # comment: Oriental
    LIVE_MMLS_CATS_Oriental = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Oriental"
    )
    # label: LIVE_MMLS_CATS_Pantherette
    # comment: Pantherette
    LIVE_MMLS_CATS_Pantherette = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Pantherette"
    )
    # label: LIVE_MMLS_CATS_Persian
    # comment: Persian
    LIVE_MMLS_CATS_Persian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Persian"
    )
    # label: LIVE_MMLS_CATS_Peterbald
    # comment: Peterbald
    LIVE_MMLS_CATS_Peterbald = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Peterbald"
    )
    # label: LIVE_MMLS_CATS_Pixiebob
    # comment: Pixiebob
    LIVE_MMLS_CATS_Pixiebob = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Pixiebob"
    )
    # label: LIVE_MMLS_CATS_Ragamuffin
    # comment: Ragamuffin
    LIVE_MMLS_CATS_Ragamuffin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ragamuffin"
    )
    # label: LIVE_MMLS_CATS_Ragdoll
    # comment: Ragdoll
    LIVE_MMLS_CATS_Ragdoll = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Ragdoll"
    )
    # label: LIVE_MMLS_CATS_Russian_Blue
    # comment: Russian Blue
    LIVE_MMLS_CATS_Russian_Blue = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Russian_Blue"
    )
    # label: LIVE_MMLS_CATS_Safari
    # comment: Safari
    LIVE_MMLS_CATS_Safari = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Safari"
    )
    # label: LIVE_MMLS_CATS_Savannah
    # comment: Savannah
    LIVE_MMLS_CATS_Savannah = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Savannah"
    )
    # label: LIVE_MMLS_CATS_Scottish_Fold
    # comment: Scottish Fold
    LIVE_MMLS_CATS_Scottish_Fold = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Scottish_Fold"
    )
    # label: LIVE_MMLS_CATS_Selkirk_Rex
    # comment: Selkirk Rex
    LIVE_MMLS_CATS_Selkirk_Rex = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Selkirk_Rex"
    )
    # label: LIVE_MMLS_CATS_Serengeti
    # comment: Serengeti
    LIVE_MMLS_CATS_Serengeti = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Serengeti"
    )
    # label: LIVE_MMLS_CATS_Siamese
    # comment: Siamese
    LIVE_MMLS_CATS_Siamese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Siamese"
    )
    # label: LIVE_MMLS_CATS_Siberian
    # comment: Siberian
    LIVE_MMLS_CATS_Siberian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Siberian"
    )
    # label: LIVE_MMLS_CATS_Singapura
    # comment: Singapura
    LIVE_MMLS_CATS_Singapura = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Singapura"
    )
    # label: LIVE_MMLS_CATS_Snowshoe
    # comment: Snowshoe
    LIVE_MMLS_CATS_Snowshoe = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Snowshoe"
    )
    # label: LIVE_MMLS_CATS_Somali
    # comment: Somali
    LIVE_MMLS_CATS_Somali = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Somali"
    )
    # label: LIVE_MMLS_CATS_Sphynx
    # comment: Sphynx
    LIVE_MMLS_CATS_Sphynx = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Sphynx"
    )
    # label: LIVE_MMLS_CATS_Tiffany
    # comment: Tiffany
    LIVE_MMLS_CATS_Tiffany = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Tiffany"
    )
    # label: LIVE_MMLS_CATS_Tonkinese
    # comment: Tonkinese
    LIVE_MMLS_CATS_Tonkinese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Tonkinese"
    )
    # label: LIVE_MMLS_CATS_Traditional_Siamese
    # comment: Traditional Siamese
    LIVE_MMLS_CATS_Traditional_Siamese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Traditional_Siamese"
    )
    # label: LIVE_MMLS_CATS_Turkish_Angora
    # comment: Turkish Angora
    LIVE_MMLS_CATS_Turkish_Angora = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Turkish_Angora"
    )
    # label: LIVE_MMLS_CATS_Turkish_Van
    # comment: Turkish Van
    LIVE_MMLS_CATS_Turkish_Van = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Turkish_Van"
    )
    # label: LIVE_MMLS_CATS_Vienna_Woods
    # comment: Vienna Woods
    LIVE_MMLS_CATS_Vienna_Woods = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Vienna_Woods"
    )
    # label: LIVE_MMLS_CATS_Viverral_Hybrid_Cat
    # comment: Viverral-Hybrid Cat
    LIVE_MMLS_CATS_Viverral_Hybrid_Cat = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_Viverral_Hybrid_Cat"
    )
    # label: LIVE_MMLS_CATS_York_Chocolate
    # comment: York Chocolate
    LIVE_MMLS_CATS_York_Chocolate = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_CATS_York_Chocolate"
    )
    # label: LIVE_MMLS_DOGS
    # comment: Dogs
    LIVE_MMLS_DOGS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS"
    )
    # label: LIVE_MMLS_DOGS_Affenpinscher
    # comment: Affenpinscher
    LIVE_MMLS_DOGS_Affenpinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Affenpinscher"
    )
    # label: LIVE_MMLS_DOGS_Afghan_Hound
    # comment: Afghan Hound
    LIVE_MMLS_DOGS_Afghan_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Afghan_Hound"
    )
    # label: LIVE_MMLS_DOGS_Airedale_Terrier
    # comment: Airedale Terrier
    LIVE_MMLS_DOGS_Airedale_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Airedale_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Akita
    # comment: Akita
    LIVE_MMLS_DOGS_Akita = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Akita"
    )
    # label: LIVE_MMLS_DOGS_Alangu_Mastiff
    # comment: Alangu Mastiff
    LIVE_MMLS_DOGS_Alangu_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Alangu_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Alano
    # comment: Alano
    LIVE_MMLS_DOGS_Alano = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Alano"
    )
    # label: LIVE_MMLS_DOGS_Alaskan_Malamute
    # comment: Alaskan Malamute
    LIVE_MMLS_DOGS_Alaskan_Malamute = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Alaskan_Malamute"
    )
    # label: LIVE_MMLS_DOGS_American_Bulldog
    # comment: American Bulldog
    LIVE_MMLS_DOGS_American_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_American_Bully
    # comment: American Bully
    LIVE_MMLS_DOGS_American_Bully = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Bully"
    )
    # label: LIVE_MMLS_DOGS_American_Cocker_Spaniel
    # comment: American Cocker Spaniel
    LIVE_MMLS_DOGS_American_Cocker_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Cocker_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_American_English_Coonhound
    # comment: American English Coonhound
    LIVE_MMLS_DOGS_American_English_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_English_Coonhound"
    )
    # label: LIVE_MMLS_DOGS_American_Eskimo_Dog_Miniature
    # comment: American Eskimo Dog-Miniature
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Miniature = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Eskimo_Dog_Miniature"
    )
    # label: LIVE_MMLS_DOGS_American_Eskimo_Dog_Standard
    # comment: American Eskimo Dog-Standard
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Standard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Eskimo_Dog_Standard"
    )
    # label: LIVE_MMLS_DOGS_American_Eskimo_Dog_Toy
    # comment: American Eskimo Dog-Toy
    LIVE_MMLS_DOGS_American_Eskimo_Dog_Toy = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Eskimo_Dog_Toy"
    )
    # label: LIVE_MMLS_DOGS_American_Foxhound
    # comment: American Foxhound
    LIVE_MMLS_DOGS_American_Foxhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Foxhound"
    )
    # label: LIVE_MMLS_DOGS_American_Hairless_Terrier
    # comment: American Hairless Terrier
    LIVE_MMLS_DOGS_American_Hairless_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Hairless_Terrier"
    )
    # label: LIVE_MMLS_DOGS_American_Pit_Bull_Terrier
    # comment: American Pit Bull Terrier
    LIVE_MMLS_DOGS_American_Pit_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Pit_Bull_Terrier"
    )
    # label: LIVE_MMLS_DOGS_American_Staffordshire_Terrier
    # comment: American Staffordshire Terrier
    LIVE_MMLS_DOGS_American_Staffordshire_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Staffordshire_Terrier"
    )
    # label: LIVE_MMLS_DOGS_American_Water_Spaniel
    # comment: American Water Spaniel
    LIVE_MMLS_DOGS_American_Water_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_American_Water_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Anatolian_Shepherd_Dog
    # comment: Anatolian Shepherd Dog
    LIVE_MMLS_DOGS_Anatolian_Shepherd_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Anatolian_Shepherd_Dog"
    )
    # label: LIVE_MMLS_DOGS_Argentinian_Mastiff
    # comment: Argentinian Mastiff
    LIVE_MMLS_DOGS_Argentinian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Argentinian_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Aussiedoodle
    # comment: Aussiedoodle
    LIVE_MMLS_DOGS_Aussiedoodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Aussiedoodle"
    )
    # label: LIVE_MMLS_DOGS_Australian_Cattle_Dog
    # comment: Australian Cattle Dog
    LIVE_MMLS_DOGS_Australian_Cattle_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Australian_Cattle_Dog"
    )
    # label: LIVE_MMLS_DOGS_Australian_Shepherd
    # comment: Australian Shepherd
    LIVE_MMLS_DOGS_Australian_Shepherd = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Australian_Shepherd"
    )
    # label: LIVE_MMLS_DOGS_Australian_Terrier
    # comment: Australian Terrier
    LIVE_MMLS_DOGS_Australian_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Australian_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Ba_Shar_Basset_Hound_Shar_pei_Mix
    # comment: Ba Shar-Basset Hound Shar pei Mix
    LIVE_MMLS_DOGS_Ba_Shar_Basset_Hound_Shar_pei_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Ba_Shar_Basset_Hound_Shar_pei_Mix"
    )
    # label: LIVE_MMLS_DOGS_Basenji
    # comment: Basenji
    LIVE_MMLS_DOGS_Basenji = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Basenji"
    )
    # label: LIVE_MMLS_DOGS_Basset_Hound
    # comment: Basset Hound
    LIVE_MMLS_DOGS_Basset_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Basset_Hound"
    )
    # label: LIVE_MMLS_DOGS_Beagle
    # comment: Beagle
    LIVE_MMLS_DOGS_Beagle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Beagle"
    )
    # label: LIVE_MMLS_DOGS_Bearded_Collie
    # comment: Bearded Collie
    LIVE_MMLS_DOGS_Bearded_Collie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bearded_Collie"
    )
    # label: LIVE_MMLS_DOGS_Beauceron
    # comment: Beauceron
    LIVE_MMLS_DOGS_Beauceron = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Beauceron"
    )
    # label: LIVE_MMLS_DOGS_Bedlington_Terrier
    # comment: Bedlington Terrier
    LIVE_MMLS_DOGS_Bedlington_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bedlington_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Belgian_Malinois
    # comment: Belgian Malinois
    LIVE_MMLS_DOGS_Belgian_Malinois = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Belgian_Malinois"
    )
    # label: LIVE_MMLS_DOGS_Belgian_Sheepdog
    # comment: Belgian Sheepdog
    LIVE_MMLS_DOGS_Belgian_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Belgian_Sheepdog"
    )
    # label: LIVE_MMLS_DOGS_Belgian_Tervuren
    # comment: Belgian Tervuren
    LIVE_MMLS_DOGS_Belgian_Tervuren = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Belgian_Tervuren"
    )
    # label: LIVE_MMLS_DOGS_Bergamasco
    # comment: Bergamasco
    LIVE_MMLS_DOGS_Bergamasco = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bergamasco"
    )
    # label: LIVE_MMLS_DOGS_Berger_Picard
    # comment: Berger Picard
    LIVE_MMLS_DOGS_Berger_Picard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Berger_Picard"
    )
    # label: LIVE_MMLS_DOGS_Bernedoodle
    # comment: Bernedoodle
    LIVE_MMLS_DOGS_Bernedoodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bernedoodle"
    )
    # label: LIVE_MMLS_DOGS_Bernese_Mountain_Dog
    # comment: Bernese Mountain Dog
    LIVE_MMLS_DOGS_Bernese_Mountain_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bernese_Mountain_Dog"
    )
    # label: LIVE_MMLS_DOGS_Bichon_Frise
    # comment: Bichon Frise
    LIVE_MMLS_DOGS_Bichon_Frise = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bichon_Frise"
    )
    # label: LIVE_MMLS_DOGS_Black_Russian_Terrier
    # comment: Black Russian Terrier
    LIVE_MMLS_DOGS_Black_Russian_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Black_Russian_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Black_and_Tan_Coonhound
    # comment: Black and Tan Coonhound
    LIVE_MMLS_DOGS_Black_and_Tan_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Black_and_Tan_Coonhound"
    )
    # label: LIVE_MMLS_DOGS_Bloodhound
    # comment: Bloodhound
    LIVE_MMLS_DOGS_Bloodhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bloodhound"
    )
    # label: LIVE_MMLS_DOGS_Bluetick_Coonhound
    # comment: Bluetick Coonhound
    LIVE_MMLS_DOGS_Bluetick_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bluetick_Coonhound"
    )
    # label: LIVE_MMLS_DOGS_Boerboel
    # comment: Boerboel
    LIVE_MMLS_DOGS_Boerboel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boerboel"
    )
    # label: LIVE_MMLS_DOGS_Border_Collie
    # comment: Border Collie
    LIVE_MMLS_DOGS_Border_Collie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Border_Collie"
    )
    # label: LIVE_MMLS_DOGS_Border_Terrier
    # comment: Border Terrier
    LIVE_MMLS_DOGS_Border_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Border_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Borzoi
    # comment: Borzoi
    LIVE_MMLS_DOGS_Borzoi = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Borzoi"
    )
    # label: LIVE_MMLS_DOGS_Boston_Terrier
    # comment: Boston Terrier
    LIVE_MMLS_DOGS_Boston_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boston_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Bouvier_des_Flandres
    # comment: Bouvier des Flandres
    LIVE_MMLS_DOGS_Bouvier_des_Flandres = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bouvier_des_Flandres"
    )
    # label: LIVE_MMLS_DOGS_Boweimar_Boxer_Weimaraner_Mix
    # comment: Boweimar-Boxer Weimaraner Mix
    LIVE_MMLS_DOGS_Boweimar_Boxer_Weimaraner_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boweimar_Boxer_Weimaraner_Mix"
    )
    # label: LIVE_MMLS_DOGS_Boxer
    # comment: Boxer
    LIVE_MMLS_DOGS_Boxer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boxer"
    )
    # label: LIVE_MMLS_DOGS_Boykin_Spaniel
    # comment: Boykin Spaniel
    LIVE_MMLS_DOGS_Boykin_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Boykin_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Brazilian_Mastiff
    # comment: Brazilian Mastiff
    LIVE_MMLS_DOGS_Brazilian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Brazilian_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Briard
    # comment: Briard
    LIVE_MMLS_DOGS_Briard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Briard"
    )
    # label: LIVE_MMLS_DOGS_Brittany
    # comment: Brittany
    LIVE_MMLS_DOGS_Brittany = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Brittany"
    )
    # label: LIVE_MMLS_DOGS_Brussels_Griffon
    # comment: Brussels Griffon
    LIVE_MMLS_DOGS_Brussels_Griffon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Brussels_Griffon"
    )
    # label: LIVE_MMLS_DOGS_Bull_Terrier
    # comment: Bull Terrier
    LIVE_MMLS_DOGS_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bull_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Bull_Terrier_Miniature
    # comment: Bull Terrier-Miniature
    LIVE_MMLS_DOGS_Bull_Terrier_Miniature = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bull_Terrier_Miniature"
    )
    # label: LIVE_MMLS_DOGS_Bulldog
    # comment: Bulldog
    LIVE_MMLS_DOGS_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_Bulli_Kutta
    # comment: Bulli Kutta
    LIVE_MMLS_DOGS_Bulli_Kutta = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bulli_Kutta"
    )
    # label: LIVE_MMLS_DOGS_Bullmastiff
    # comment: Bullmastiff
    LIVE_MMLS_DOGS_Bullmastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bullmastiff"
    )
    # label: LIVE_MMLS_DOGS_Bully_Kutta_Mastiff_breed
    # comment: Bully Kutta-Mastiff breed
    LIVE_MMLS_DOGS_Bully_Kutta_Mastiff_breed = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Bully_Kutta_Mastiff_breed"
    )
    # label: LIVE_MMLS_DOGS_Cairn_Terrier
    # comment: Cairn Terrier
    LIVE_MMLS_DOGS_Cairn_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cairn_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Campeiro_Bulldog_Brazilian_Bulldog
    # comment: Campeiro Bulldog-Brazilian Bulldog
    LIVE_MMLS_DOGS_Campeiro_Bulldog_Brazilian_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Campeiro_Bulldog_Brazilian_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_Canaan_Dog
    # comment: Canaan Dog
    LIVE_MMLS_DOGS_Canaan_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Canaan_Dog"
    )
    # label: LIVE_MMLS_DOGS_Canary_Mastiff
    # comment: Canary Mastiff
    LIVE_MMLS_DOGS_Canary_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Canary_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Cane_Corso
    # comment: Cane Corso
    LIVE_MMLS_DOGS_Cane_Corso = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cane_Corso"
    )
    # label: LIVE_MMLS_DOGS_Cardigan_Welsh_Corgi
    # comment: Cardigan Welsh Corgi
    LIVE_MMLS_DOGS_Cardigan_Welsh_Corgi = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cardigan_Welsh_Corgi"
    )
    # label: LIVE_MMLS_DOGS_Catahoula_Bulldog_Catahoula_Leopard_Bulldog
    # comment: Catahoula Bulldog-Catahoula Leopard Bulldog
    LIVE_MMLS_DOGS_Catahoula_Bulldog_Catahoula_Leopard_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Catahoula_Bulldog_Catahoula_Leopard_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_Cavachon_King_Charles_Spaniel_Bichon_Frise
    # comment: Cavachon-King Charles Spaniel Bichon Frise
    LIVE_MMLS_DOGS_Cavachon_King_Charles_Spaniel_Bichon_Frise = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cavachon_King_Charles_Spaniel_Bichon_Frise"
    )
    # label: LIVE_MMLS_DOGS_Cavalier_King_Charles_Spaniel
    # comment: Cavalier King Charles Spaniel
    LIVE_MMLS_DOGS_Cavalier_King_Charles_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cavalier_King_Charles_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Cavapoo_Cavalier_King_Charles_Spaniel_Poodle
    # comment: Cavapoo-Cavalier King Charles Spaniel Poodle
    LIVE_MMLS_DOGS_Cavapoo_Cavalier_King_Charles_Spaniel_Poodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cavapoo_Cavalier_King_Charles_Spaniel_Poodle"
    )
    # label: LIVE_MMLS_DOGS_Cesky_Terrier
    # comment: Cesky Terrier
    LIVE_MMLS_DOGS_Cesky_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cesky_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Chesapeake_Bay_Retriever
    # comment: Chesapeake Bay Retriever
    LIVE_MMLS_DOGS_Chesapeake_Bay_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chesapeake_Bay_Retriever"
    )
    # label: LIVE_MMLS_DOGS_Chihuahua
    # comment: Chihuahua
    LIVE_MMLS_DOGS_Chihuahua = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chihuahua"
    )
    # label: LIVE_MMLS_DOGS_Chinese_Crested_Dog
    # comment: Chinese Crested Dog
    LIVE_MMLS_DOGS_Chinese_Crested_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinese_Crested_Dog"
    )
    # label: LIVE_MMLS_DOGS_Chinese_Pug
    # comment: Chinese Pug
    LIVE_MMLS_DOGS_Chinese_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinese_Pug"
    )
    # label: LIVE_MMLS_DOGS_Chinese_Shar_Pei
    # comment: Chinese Shar Pei
    LIVE_MMLS_DOGS_Chinese_Shar_Pei = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinese_Shar_Pei"
    )
    # label: LIVE_MMLS_DOGS_Chinook
    # comment: Chinook
    LIVE_MMLS_DOGS_Chinook = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chinook"
    )
    # label: LIVE_MMLS_DOGS_Chipin_Chihuahua_Minature_Pinscher_Mix
    # comment: Chipin-Chihuahua Minature Pinscher Mix
    LIVE_MMLS_DOGS_Chipin_Chihuahua_Minature_Pinscher_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chipin_Chihuahua_Minature_Pinscher_Mix"
    )
    # label: LIVE_MMLS_DOGS_Chiweenie_Chihuahua_Dachshund_Mix
    # comment: Chiweenie-Chihuahua Dachshund Mix
    LIVE_MMLS_DOGS_Chiweenie_Chihuahua_Dachshund_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chiweenie_Chihuahua_Dachshund_Mix"
    )
    # label: LIVE_MMLS_DOGS_Chorkie_Chihuahua_Yorkshire_Terrier_Mix
    # comment: Chorkie-Chihuahua Yorkshire Terrier Mix
    LIVE_MMLS_DOGS_Chorkie_Chihuahua_Yorkshire_Terrier_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chorkie_Chihuahua_Yorkshire_Terrier_Mix"
    )
    # label: LIVE_MMLS_DOGS_Chow_Chow
    # comment: Chow Chow
    LIVE_MMLS_DOGS_Chow_Chow = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chow_Chow"
    )
    # label: LIVE_MMLS_DOGS_Chow_Pei_Chow_Chow_Shar_Pei_Mix
    # comment: Chow Pei-Chow Chow Shar Pei Mix
    LIVE_MMLS_DOGS_Chow_Pei_Chow_Chow_Shar_Pei_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Chow_Pei_Chow_Chow_Shar_Pei_Mix"
    )
    # label: LIVE_MMLS_DOGS_Cirneco_dell_Etna
    # comment: Cirneco dell Etna
    LIVE_MMLS_DOGS_Cirneco_dell_Etna = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cirneco_dell_Etna"
    )
    # label: LIVE_MMLS_DOGS_Clumber_Spaniel
    # comment: Clumber Spaniel
    LIVE_MMLS_DOGS_Clumber_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Clumber_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Cockapoo_Cocker_Spaniel_Poodle_Mix
    # comment: Cockapoo-Cocker Spaniel Poodle Mix
    LIVE_MMLS_DOGS_Cockapoo_Cocker_Spaniel_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cockapoo_Cocker_Spaniel_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Cocker_Spaniel
    # comment: Cocker Spaniel
    LIVE_MMLS_DOGS_Cocker_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Cocker_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Collie
    # comment: Collie
    LIVE_MMLS_DOGS_Collie = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Collie"
    )
    # label: LIVE_MMLS_DOGS_Coton_de_Tulear
    # comment: Coton de Tulear
    LIVE_MMLS_DOGS_Coton_de_Tulear = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Coton_de_Tulear"
    )
    # label: LIVE_MMLS_DOGS_Curly_Coated_Retriever
    # comment: Curly-Coated Retriever
    LIVE_MMLS_DOGS_Curly_Coated_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Curly_Coated_Retriever"
    )
    # label: LIVE_MMLS_DOGS_Dachshund
    # comment: Dachshund
    LIVE_MMLS_DOGS_Dachshund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dachshund"
    )
    # label: LIVE_MMLS_DOGS_Dalmatian
    # comment: Dalmatian
    LIVE_MMLS_DOGS_Dalmatian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dalmatian"
    )
    # label: LIVE_MMLS_DOGS_Dandie_Dinmont_Terrier
    # comment: Dandie Dinmont Terrier
    LIVE_MMLS_DOGS_Dandie_Dinmont_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dandie_Dinmont_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Doberman_Pinscher
    # comment: Doberman Pinscher
    LIVE_MMLS_DOGS_Doberman_Pinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Doberman_Pinscher"
    )
    # label: LIVE_MMLS_DOGS_Dogo_Argentino
    # comment: Dogo Argentino
    LIVE_MMLS_DOGS_Dogo_Argentino = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dogo_Argentino"
    )
    # label: LIVE_MMLS_DOGS_Dogue_de_Bordeaux
    # comment: Dogue de Bordeaux
    LIVE_MMLS_DOGS_Dogue_de_Bordeaux = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dogue_de_Bordeaux"
    )
    # label: LIVE_MMLS_DOGS_Doxiepoo_Dachshund_Poodle_Mix
    # comment: Doxiepoo-Dachshund Poodle Mix
    LIVE_MMLS_DOGS_Doxiepoo_Dachshund_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Doxiepoo_Dachshund_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Dutch_Pug
    # comment: Dutch Pug
    LIVE_MMLS_DOGS_Dutch_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Dutch_Pug"
    )
    # label: LIVE_MMLS_DOGS_English_Bulldog
    # comment: English Bulldog
    LIVE_MMLS_DOGS_English_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_English_Cocker_Spaniel
    # comment: English Cocker Spaniel
    LIVE_MMLS_DOGS_English_Cocker_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Cocker_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_English_Foxhound
    # comment: English Foxhound
    LIVE_MMLS_DOGS_English_Foxhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Foxhound"
    )
    # label: LIVE_MMLS_DOGS_English_Mastiff
    # comment: English Mastiff
    LIVE_MMLS_DOGS_English_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_English_Setter
    # comment: English Setter
    LIVE_MMLS_DOGS_English_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Setter"
    )
    # label: LIVE_MMLS_DOGS_English_Springer_Spaniel
    # comment: English Springer Spaniel
    LIVE_MMLS_DOGS_English_Springer_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Springer_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_English_Toy_Spaniel
    # comment: English Toy Spaniel
    LIVE_MMLS_DOGS_English_Toy_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_English_Toy_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Entlebucher_Mountain_Dog
    # comment: Entlebucher Mountain Dog
    LIVE_MMLS_DOGS_Entlebucher_Mountain_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Entlebucher_Mountain_Dog"
    )
    # label: LIVE_MMLS_DOGS_Eurasier
    # comment: Eurasier
    LIVE_MMLS_DOGS_Eurasier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Eurasier"
    )
    # label: LIVE_MMLS_DOGS_Field_Spaniel
    # comment: Field Spaniel
    LIVE_MMLS_DOGS_Field_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Field_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Fila_Brasileiro_Brazilian_Mastiff
    # comment: Fila Brasileiro-Brazilian Mastiff
    LIVE_MMLS_DOGS_Fila_Brasileiro_Brazilian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Fila_Brasileiro_Brazilian_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Finnish_Lapphund
    # comment: Finnish Lapphund
    LIVE_MMLS_DOGS_Finnish_Lapphund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Finnish_Lapphund"
    )
    # label: LIVE_MMLS_DOGS_Finnish_Spitz
    # comment: Finnish Spitz
    LIVE_MMLS_DOGS_Finnish_Spitz = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Finnish_Spitz"
    )
    # label: LIVE_MMLS_DOGS_Flat_Coated_Retriever
    # comment: Flat-Coated Retriever
    LIVE_MMLS_DOGS_Flat_Coated_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Flat_Coated_Retriever"
    )
    # label: LIVE_MMLS_DOGS_French_Bulldog
    # comment: French Bulldog
    LIVE_MMLS_DOGS_French_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_French_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_French_Mastiff
    # comment: French Mastiff
    LIVE_MMLS_DOGS_French_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_French_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_German_Mastiff_Great_Dane
    # comment: German Mastiff-Great Dane
    LIVE_MMLS_DOGS_German_Mastiff_Great_Dane = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Mastiff_Great_Dane"
    )
    # label: LIVE_MMLS_DOGS_German_Pinscher
    # comment: German Pinscher
    LIVE_MMLS_DOGS_German_Pinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Pinscher"
    )
    # label: LIVE_MMLS_DOGS_German_Shepherd_Dog
    # comment: German Shepherd Dog
    LIVE_MMLS_DOGS_German_Shepherd_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Shepherd_Dog"
    )
    # label: LIVE_MMLS_DOGS_German_Shorthaired_Pointer
    # comment: German Shorthaired Pointer
    LIVE_MMLS_DOGS_German_Shorthaired_Pointer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Shorthaired_Pointer"
    )
    # label: LIVE_MMLS_DOGS_German_Wirehaired_Pointer
    # comment: German Wirehaired Pointer
    LIVE_MMLS_DOGS_German_Wirehaired_Pointer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_German_Wirehaired_Pointer"
    )
    # label: LIVE_MMLS_DOGS_Giant_Schnauzer
    # comment: Giant Schnauzer
    LIVE_MMLS_DOGS_Giant_Schnauzer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Giant_Schnauzer"
    )
    # label: LIVE_MMLS_DOGS_Glen_of_Imaal_Terrier
    # comment: Glen of Imaal Terrier
    LIVE_MMLS_DOGS_Glen_of_Imaal_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Glen_of_Imaal_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Goldador_Golden_Retriever_Labrador_Retriever
    # comment: Goldador-Golden Retriever Labrador Retriever
    LIVE_MMLS_DOGS_Goldador_Golden_Retriever_Labrador_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Goldador_Golden_Retriever_Labrador_Retriever"
    )
    # label: LIVE_MMLS_DOGS_Golden_Retriever
    # comment: Golden Retriever
    LIVE_MMLS_DOGS_Golden_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Golden_Retriever"
    )
    # label: LIVE_MMLS_DOGS_Goldendoodle_Golden_Retriever_Poodle_Mix
    # comment: Goldendoodle-Golden Retriever Poodle Mix
    LIVE_MMLS_DOGS_Goldendoodle_Golden_Retriever_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Goldendoodle_Golden_Retriever_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Gordon_Setter
    # comment: Gordon Setter
    LIVE_MMLS_DOGS_Gordon_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Gordon_Setter"
    )
    # label: LIVE_MMLS_DOGS_Great_Dane
    # comment: Great Dane
    LIVE_MMLS_DOGS_Great_Dane = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Great_Dane"
    )
    # label: LIVE_MMLS_DOGS_Great_Pyrenees
    # comment: Great Pyrenees
    LIVE_MMLS_DOGS_Great_Pyrenees = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Great_Pyrenees"
    )
    # label: LIVE_MMLS_DOGS_Greater_Swiss_Mountain_Dog
    # comment: Greater Swiss Mountain Dog
    LIVE_MMLS_DOGS_Greater_Swiss_Mountain_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Greater_Swiss_Mountain_Dog"
    )
    # label: LIVE_MMLS_DOGS_Greyhound
    # comment: Greyhound
    LIVE_MMLS_DOGS_Greyhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Greyhound"
    )
    # label: LIVE_MMLS_DOGS_Harrier
    # comment: Harrier
    LIVE_MMLS_DOGS_Harrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Harrier"
    )
    # label: LIVE_MMLS_DOGS_Havanese
    # comment: Havanese
    LIVE_MMLS_DOGS_Havanese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Havanese"
    )
    # label: LIVE_MMLS_DOGS_Ibizan_Hound
    # comment: Ibizan Hound
    LIVE_MMLS_DOGS_Ibizan_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Ibizan_Hound"
    )
    # label: LIVE_MMLS_DOGS_Icelandic_Sheepdog
    # comment: Icelandic Sheepdog
    LIVE_MMLS_DOGS_Icelandic_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Icelandic_Sheepdog"
    )
    # label: LIVE_MMLS_DOGS_Irish_Red_and_White_Setter
    # comment: Irish Red and White Setter
    LIVE_MMLS_DOGS_Irish_Red_and_White_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Red_and_White_Setter"
    )
    # label: LIVE_MMLS_DOGS_Irish_Setter
    # comment: Irish Setter
    LIVE_MMLS_DOGS_Irish_Setter = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Setter"
    )
    # label: LIVE_MMLS_DOGS_Irish_Terrier
    # comment: Irish Terrier
    LIVE_MMLS_DOGS_Irish_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Irish_Water_Spaniel
    # comment: Irish Water Spaniel
    LIVE_MMLS_DOGS_Irish_Water_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Water_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Irish_Wolfhound
    # comment: Irish Wolfhound
    LIVE_MMLS_DOGS_Irish_Wolfhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Irish_Wolfhound"
    )
    # label: LIVE_MMLS_DOGS_Italian_Greyhound
    # comment: Italian Greyhound
    LIVE_MMLS_DOGS_Italian_Greyhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Italian_Greyhound"
    )
    # label: LIVE_MMLS_DOGS_Italian_Mastiff
    # comment: Italian Mastiff
    LIVE_MMLS_DOGS_Italian_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Italian_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Jack_Chi_Chihuahua_Jack_Russell_Terrier_Mix
    # comment: Jack Chi-Chihuahua Jack Russell Terrier Mix
    LIVE_MMLS_DOGS_Jack_Chi_Chihuahua_Jack_Russell_Terrier_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Jack_Chi_Chihuahua_Jack_Russell_Terrier_Mix"
    )
    # label: LIVE_MMLS_DOGS_Jack_Russell_Terrier
    # comment: Jack Russell Terrier
    LIVE_MMLS_DOGS_Jack_Russell_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Jack_Russell_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Japanese_Boxer
    # comment: Japanese Boxer
    LIVE_MMLS_DOGS_Japanese_Boxer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Boxer"
    )
    # label: LIVE_MMLS_DOGS_Japanese_Chin
    # comment: Japanese Chin
    LIVE_MMLS_DOGS_Japanese_Chin = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Chin"
    )
    # label: LIVE_MMLS_DOGS_Japanese_Mastiff
    # comment: Japanese Mastiff
    LIVE_MMLS_DOGS_Japanese_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Japanese_Pug
    # comment: Japanese Pug
    LIVE_MMLS_DOGS_Japanese_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Pug"
    )
    # label: LIVE_MMLS_DOGS_Japanese_Spaniel
    # comment: Japanese Spaniel
    LIVE_MMLS_DOGS_Japanese_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Japanese_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Kangal_Shepherd_Dog
    # comment: Kangal Shepherd Dog
    LIVE_MMLS_DOGS_Kangal_Shepherd_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kangal_Shepherd_Dog"
    )
    # label: LIVE_MMLS_DOGS_Keeshond
    # comment: Keeshond
    LIVE_MMLS_DOGS_Keeshond = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Keeshond"
    )
    # label: LIVE_MMLS_DOGS_Kerry_Blue_Terrier
    # comment: Kerry Blue Terrier
    LIVE_MMLS_DOGS_Kerry_Blue_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kerry_Blue_Terrier"
    )
    # label: LIVE_MMLS_DOGS_King_Charles_Spaniel
    # comment: King Charles Spaniel
    LIVE_MMLS_DOGS_King_Charles_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_King_Charles_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Komondor
    # comment: Komondor
    LIVE_MMLS_DOGS_Komondor = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Komondor"
    )
    # label: LIVE_MMLS_DOGS_Kuvasz
    # comment: Kuvasz
    LIVE_MMLS_DOGS_Kuvasz = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kuvasz"
    )
    # label: LIVE_MMLS_DOGS_Kyi_Leo_Maltese_Lhasa_Apso_Mix
    # comment: Kyi-Leo-Maltese Lhasa Apso Mix
    LIVE_MMLS_DOGS_Kyi_Leo_Maltese_Lhasa_Apso_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Kyi_Leo_Maltese_Lhasa_Apso_Mix"
    )
    # label: LIVE_MMLS_DOGS_Labrabull_Labrador_Retriever_American_Pit_Bull
    # comment: Labrabull-Labrador Retriever American Pit Bull
    LIVE_MMLS_DOGS_Labrabull_Labrador_Retriever_American_Pit_Bull = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labrabull_Labrador_Retriever_American_Pit_Bull"
    )
    # label: LIVE_MMLS_DOGS_Labradane_Labrador_Retriever_Great_Dane_Mix
    # comment: Labradane-Labrador Retriever Great Dane Mix
    LIVE_MMLS_DOGS_Labradane_Labrador_Retriever_Great_Dane_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labradane_Labrador_Retriever_Great_Dane_Mix"
    )
    # label: LIVE_MMLS_DOGS_Labradoodle_Labrador_Retriever_Poodle_Mix
    # comment: Labradoodle Labrador Retriever Poodle Mix
    LIVE_MMLS_DOGS_Labradoodle_Labrador_Retriever_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labradoodle_Labrador_Retriever_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Labrador_Retriever
    # comment: Labrador Retriever
    LIVE_MMLS_DOGS_Labrador_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Labrador_Retriever"
    )
    # label: LIVE_MMLS_DOGS_Lagotto_Romagnolo
    # comment: Lagotto Romagnolo
    LIVE_MMLS_DOGS_Lagotto_Romagnolo = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Lagotto_Romagnolo"
    )
    # label: LIVE_MMLS_DOGS_Lakeland_Terrier
    # comment: Lakeland Terrier
    LIVE_MMLS_DOGS_Lakeland_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Lakeland_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Leonberger
    # comment: Leonberger
    LIVE_MMLS_DOGS_Leonberger = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Leonberger"
    )
    # label: LIVE_MMLS_DOGS_Lhasa_Apso
    # comment: Lhasa Apso
    LIVE_MMLS_DOGS_Lhasa_Apso = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Lhasa_Apso"
    )
    # label: LIVE_MMLS_DOGS_Löwchen
    # comment: Löwchen
    LIVE_MMLS_DOGS_Löwchen = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Löwchen"
    )
    # label: LIVE_MMLS_DOGS_Mal_Shi_Maltese_Shih_Tzu_Mix
    # comment: Mal-Shi-Maltese Shih Tzu Mix
    LIVE_MMLS_DOGS_Mal_Shi_Maltese_Shih_Tzu_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mal_Shi_Maltese_Shih_Tzu_Mix"
    )
    # label: LIVE_MMLS_DOGS_Malt_Tzu_Maltese_Shih_Tzu_Mix
    # comment: Malt-Tzu-Maltese Shih Tzu Mix
    LIVE_MMLS_DOGS_Malt_Tzu_Maltese_Shih_Tzu_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Malt_Tzu_Maltese_Shih_Tzu_Mix"
    )
    # label: LIVE_MMLS_DOGS_Maltese
    # comment: Maltese
    LIVE_MMLS_DOGS_Maltese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Maltese"
    )
    # label: LIVE_MMLS_DOGS_Maltese_Shih_Tzu
    # comment: Maltese Shih Tzu
    LIVE_MMLS_DOGS_Maltese_Shih_Tzu = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Maltese_Shih_Tzu"
    )
    # label: LIVE_MMLS_DOGS_Malti_Zu_Maltese_Shih_Tzu_Mix
    # comment: Malti Zu-Maltese Shih Tzu Mix
    LIVE_MMLS_DOGS_Malti_Zu_Maltese_Shih_Tzu_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Malti_Zu_Maltese_Shih_Tzu_Mix"
    )
    # label: LIVE_MMLS_DOGS_Maltipoo_Maltese_Poodle_Mix
    # comment: Maltipoo-Maltese Poodle Mix
    LIVE_MMLS_DOGS_Maltipoo_Maltese_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Maltipoo_Maltese_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Manchester_Terrier
    # comment: Manchester Terrier
    LIVE_MMLS_DOGS_Manchester_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Manchester_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Mastador_Bullmastiff_Labrador_Retriever_Mix
    # comment: Mastador-Bullmastiff Labrador Retriever Mix
    LIVE_MMLS_DOGS_Mastador_Bullmastiff_Labrador_Retriever_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastador_Bullmastiff_Labrador_Retriever_Mix"
    )
    # label: LIVE_MMLS_DOGS_Mastiff
    # comment: Mastiff
    LIVE_MMLS_DOGS_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Mastin_Espanol_Spanish_Mastiff
    # comment: Mastin Espanol-Spanish Mastiff
    LIVE_MMLS_DOGS_Mastin_Espanol_Spanish_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastin_Espanol_Spanish_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Mastino_Napoletano_Neopolitan_Mastiff
    # comment: Mastino Napoletano-Neopolitan Mastiff
    LIVE_MMLS_DOGS_Mastino_Napoletano_Neopolitan_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mastino_Napoletano_Neopolitan_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Miniature_American_Shepherd
    # comment: Miniature American Shepherd
    LIVE_MMLS_DOGS_Miniature_American_Shepherd = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_American_Shepherd"
    )
    # label: LIVE_MMLS_DOGS_Miniature_Bull_Terrier
    # comment: Miniature Bull Terrier
    LIVE_MMLS_DOGS_Miniature_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_Bull_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Miniature_Pinscher
    # comment: Miniature Pinscher
    LIVE_MMLS_DOGS_Miniature_Pinscher = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_Pinscher"
    )
    # label: LIVE_MMLS_DOGS_Miniature_Schnauzer
    # comment: Miniature Schnauzer
    LIVE_MMLS_DOGS_Miniature_Schnauzer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Miniature_Schnauzer"
    )
    # label: LIVE_MMLS_DOGS_Mixed_Invalid_Breed_Type
    # comment: Mixed-Invalid Breed Type
    LIVE_MMLS_DOGS_Mixed_Invalid_Breed_Type = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Mixed_Invalid_Breed_Type"
    )
    # label: LIVE_MMLS_DOGS_Neapolitan_Mastiff
    # comment: Neapolitan Mastiff
    LIVE_MMLS_DOGS_Neapolitan_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Neapolitan_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Newfoundland
    # comment: Newfoundland
    LIVE_MMLS_DOGS_Newfoundland = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Newfoundland"
    )
    # label: LIVE_MMLS_DOGS_Norfolk_Terrier
    # comment: Norfolk Terrier
    LIVE_MMLS_DOGS_Norfolk_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norfolk_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Norwegian_Buhund
    # comment: Norwegian Buhund
    LIVE_MMLS_DOGS_Norwegian_Buhund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwegian_Buhund"
    )
    # label: LIVE_MMLS_DOGS_Norwegian_Elkhound
    # comment: Norwegian Elkhound
    LIVE_MMLS_DOGS_Norwegian_Elkhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwegian_Elkhound"
    )
    # label: LIVE_MMLS_DOGS_Norwegian_Lundehund
    # comment: Norwegian Lundehund
    LIVE_MMLS_DOGS_Norwegian_Lundehund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwegian_Lundehund"
    )
    # label: LIVE_MMLS_DOGS_Norwich_Terrier
    # comment: Norwich Terrier
    LIVE_MMLS_DOGS_Norwich_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Norwich_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Nova_Scotia_Duck_Tolling_Retriever
    # comment: Nova Scotia Duck-Tolling Retriever
    LIVE_MMLS_DOGS_Nova_Scotia_Duck_Tolling_Retriever = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Nova_Scotia_Duck_Tolling_Retriever"
    )
    # label: LIVE_MMLS_DOGS_Old_English_Bulldog
    # comment: Old English Bulldog
    LIVE_MMLS_DOGS_Old_English_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Old_English_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_Old_English_Sheepdog
    # comment: Old English Sheepdog
    LIVE_MMLS_DOGS_Old_English_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Old_English_Sheepdog"
    )
    # label: LIVE_MMLS_DOGS_Olde_English_Bulldog
    # comment: Olde English Bulldog
    LIVE_MMLS_DOGS_Olde_English_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Olde_English_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_Otterhound
    # comment: Otterhound
    LIVE_MMLS_DOGS_Otterhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Otterhound"
    )
    # label: LIVE_MMLS_DOGS_Papillon
    # comment: Papillon
    LIVE_MMLS_DOGS_Papillon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Papillon"
    )
    # label: LIVE_MMLS_DOGS_Parson_Russell_Terrier
    # comment: Parson Russell Terrier
    LIVE_MMLS_DOGS_Parson_Russell_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Parson_Russell_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Peekapoo_Pekingese_Poodle_Mix
    # comment: Peekapoo-Pekingese Poodle Mix
    LIVE_MMLS_DOGS_Peekapoo_Pekingese_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Peekapoo_Pekingese_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Pekingese
    # comment: Pekingese
    LIVE_MMLS_DOGS_Pekingese = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pekingese"
    )
    # label: LIVE_MMLS_DOGS_Pembroke_Welsh_Corgi
    # comment: Pembroke Welsh Corgi
    LIVE_MMLS_DOGS_Pembroke_Welsh_Corgi = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pembroke_Welsh_Corgi"
    )
    # label: LIVE_MMLS_DOGS_Petit_Basset_Griffon_Vendéen
    # comment: Petit Basset Griffon Vendéen
    LIVE_MMLS_DOGS_Petit_Basset_Griffon_Vendéen = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Petit_Basset_Griffon_Vendéen"
    )
    # label: LIVE_MMLS_DOGS_Pharaoh_Hound
    # comment: Pharaoh Hound
    LIVE_MMLS_DOGS_Pharaoh_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pharaoh_Hound"
    )
    # label: LIVE_MMLS_DOGS_Pit_Bull
    # comment: Pit Bull
    LIVE_MMLS_DOGS_Pit_Bull = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pit_Bull"
    )
    # label: LIVE_MMLS_DOGS_Pit_Plott_Pitbull_Plott_Hound_Mix
    # comment: Pit Plott-Pitbull Plott Hound Mix
    LIVE_MMLS_DOGS_Pit_Plott_Pitbull_Plott_Hound_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pit_Plott_Pitbull_Plott_Hound_Mix"
    )
    # label: LIVE_MMLS_DOGS_Plott_Hound
    # comment: Plott Hound
    LIVE_MMLS_DOGS_Plott_Hound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Plott_Hound"
    )
    # label: LIVE_MMLS_DOGS_Pointer
    # comment: Pointer
    LIVE_MMLS_DOGS_Pointer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pointer"
    )
    # label: LIVE_MMLS_DOGS_Polish_Lowland_Sheepdog
    # comment: Polish Lowland Sheepdog
    LIVE_MMLS_DOGS_Polish_Lowland_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Polish_Lowland_Sheepdog"
    )
    # label: LIVE_MMLS_DOGS_Pomapoo_Pomeranian_Poodle_Mix
    # comment: Pomapoo-Pomeranian Poodle Mix
    LIVE_MMLS_DOGS_Pomapoo_Pomeranian_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomapoo_Pomeranian_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Pomchi_Pomeranian_Chihuahua_Mix
    # comment: Pomchi-Pomeranian Chihuahua Mix
    LIVE_MMLS_DOGS_Pomchi_Pomeranian_Chihuahua_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomchi_Pomeranian_Chihuahua_Mix"
    )
    # label: LIVE_MMLS_DOGS_Pomeranian
    # comment: Pomeranian
    LIVE_MMLS_DOGS_Pomeranian = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomeranian"
    )
    # label: LIVE_MMLS_DOGS_Pomsky_Pomeranian_Siberian_Husky_Mix
    # comment: Pomsky-Pomeranian Siberian Husky Mix
    LIVE_MMLS_DOGS_Pomsky_Pomeranian_Siberian_Husky_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pomsky_Pomeranian_Siberian_Husky_Mix"
    )
    # label: LIVE_MMLS_DOGS_Poochon_Poodle_Bichon_Frise_Mix
    # comment: Poochon-Poodle Bichon Frise Mix
    LIVE_MMLS_DOGS_Poochon_Poodle_Bichon_Frise_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Poochon_Poodle_Bichon_Frise_Mix"
    )
    # label: LIVE_MMLS_DOGS_Poodle
    # comment: Poodle
    LIVE_MMLS_DOGS_Poodle = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Poodle"
    )
    # label: LIVE_MMLS_DOGS_Portuguese_Podengo_Pequeno
    # comment: Portuguese Podengo Pequeno
    LIVE_MMLS_DOGS_Portuguese_Podengo_Pequeno = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Portuguese_Podengo_Pequeno"
    )
    # label: LIVE_MMLS_DOGS_Portuguese_Water_Dog
    # comment: Portuguese Water Dog
    LIVE_MMLS_DOGS_Portuguese_Water_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Portuguese_Water_Dog"
    )
    # label: LIVE_MMLS_DOGS_Presa_Canario
    # comment: Presa Canario
    LIVE_MMLS_DOGS_Presa_Canario = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Presa_Canario"
    )
    # label: LIVE_MMLS_DOGS_Pug
    # comment: Pug
    LIVE_MMLS_DOGS_Pug = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pug"
    )
    # label: LIVE_MMLS_DOGS_Pugapoo_Pug_Poodle_Mix
    # comment: Pugapoo-Pug Poodle Mix
    LIVE_MMLS_DOGS_Pugapoo_Pug_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pugapoo_Pug_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Puggle_Pug_Beagle_Mix
    # comment: Puggle-Pug Beagle Mix
    LIVE_MMLS_DOGS_Puggle_Pug_Beagle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Puggle_Pug_Beagle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Puli
    # comment: Puli
    LIVE_MMLS_DOGS_Puli = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Puli"
    )
    # label: LIVE_MMLS_DOGS_Pyrenean_Mastiff
    # comment: Pyrenean Mastiff
    LIVE_MMLS_DOGS_Pyrenean_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pyrenean_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Pyrenean_Shepherd
    # comment: Pyrenean Shepherd
    LIVE_MMLS_DOGS_Pyrenean_Shepherd = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Pyrenean_Shepherd"
    )
    # label: LIVE_MMLS_DOGS_Rat_Terrier
    # comment: Rat Terrier
    LIVE_MMLS_DOGS_Rat_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Rat_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Redbone_Coonhound
    # comment: Redbone Coonhound
    LIVE_MMLS_DOGS_Redbone_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Redbone_Coonhound"
    )
    # label: LIVE_MMLS_DOGS_Rhodesian_Ridgeback
    # comment: Rhodesian Ridgeback
    LIVE_MMLS_DOGS_Rhodesian_Ridgeback = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Rhodesian_Ridgeback"
    )
    # label: LIVE_MMLS_DOGS_Rottweiler
    # comment: Rottweiler
    LIVE_MMLS_DOGS_Rottweiler = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Rottweiler"
    )
    # label: LIVE_MMLS_DOGS_Russell_Terrier
    # comment: Russell Terrier
    LIVE_MMLS_DOGS_Russell_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Russell_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Saint_Bernard
    # comment: Saint Bernard
    LIVE_MMLS_DOGS_Saint_Bernard = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Saint_Bernard"
    )
    # label: LIVE_MMLS_DOGS_Saluki
    # comment: Saluki
    LIVE_MMLS_DOGS_Saluki = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Saluki"
    )
    # label: LIVE_MMLS_DOGS_Samoyed
    # comment: Samoyed
    LIVE_MMLS_DOGS_Samoyed = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Samoyed"
    )
    # label: LIVE_MMLS_DOGS_Schipperke
    # comment: Schipperke
    LIVE_MMLS_DOGS_Schipperke = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Schipperke"
    )
    # label: LIVE_MMLS_DOGS_Schnoodle_Schnauzer_Poodle_Mix
    # comment: Schnoodle-Schnauzer Poodle Mix
    LIVE_MMLS_DOGS_Schnoodle_Schnauzer_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Schnoodle_Schnauzer_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Scottish_Deerhound
    # comment: Scottish Deerhound
    LIVE_MMLS_DOGS_Scottish_Deerhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Scottish_Deerhound"
    )
    # label: LIVE_MMLS_DOGS_Scottish_Terrier
    # comment: Scottish Terrier
    LIVE_MMLS_DOGS_Scottish_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Scottish_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Sealyham_Terrier
    # comment: Sealyham Terrier
    LIVE_MMLS_DOGS_Sealyham_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sealyham_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Shar_Pei
    # comment: Shar Pei
    LIVE_MMLS_DOGS_Shar_Pei = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shar_Pei"
    )
    # label: LIVE_MMLS_DOGS_Sheepadoodle_Old_English_Sheepdog_Poodle_Mix
    # comment: Sheepadoodle-Old English Sheepdog Poodle Mix
    LIVE_MMLS_DOGS_Sheepadoodle_Old_English_Sheepdog_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sheepadoodle_Old_English_Sheepdog_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Shetland_Sheepdog
    # comment: Shetland Sheepdog
    LIVE_MMLS_DOGS_Shetland_Sheepdog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shetland_Sheepdog"
    )
    # label: LIVE_MMLS_DOGS_Shiba_Inu
    # comment: Shiba Inu
    LIVE_MMLS_DOGS_Shiba_Inu = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shiba_Inu"
    )
    # label: LIVE_MMLS_DOGS_Shih_Poo
    # comment: Shih-Poo
    LIVE_MMLS_DOGS_Shih_Poo = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shih_Poo"
    )
    # label: LIVE_MMLS_DOGS_Shih_Tzu
    # comment: Shih Tzu
    LIVE_MMLS_DOGS_Shih_Tzu = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shih_Tzu"
    )
    # label: LIVE_MMLS_DOGS_Shihpoo_Shih_Tzu_Poodle_Mix
    # comment: Shihpoo-Shih Tzu Poodle Mix
    LIVE_MMLS_DOGS_Shihpoo_Shih_Tzu_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Shihpoo_Shih_Tzu_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Siberian_Husky
    # comment: Siberian Husky
    LIVE_MMLS_DOGS_Siberian_Husky = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Siberian_Husky"
    )
    # label: LIVE_MMLS_DOGS_Silky_Terrier
    # comment: Silky Terrier
    LIVE_MMLS_DOGS_Silky_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Silky_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Skye_Terrier
    # comment: Skye Terrier
    LIVE_MMLS_DOGS_Skye_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Skye_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Sloughi_Arabian_Greyhound
    # comment: Sloughi-Arabian Greyhound
    LIVE_MMLS_DOGS_Sloughi_Arabian_Greyhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sloughi_Arabian_Greyhound"
    )
    # label: LIVE_MMLS_DOGS_Smooth_Fox_Terrier
    # comment: Smooth Fox Terrier
    LIVE_MMLS_DOGS_Smooth_Fox_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Smooth_Fox_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Soft_Coated_Wheaten_Terrier
    # comment: Soft-Coated Wheaten Terrier
    LIVE_MMLS_DOGS_Soft_Coated_Wheaten_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Soft_Coated_Wheaten_Terrier"
    )
    # label: LIVE_MMLS_DOGS_South_African_Mastiff
    # comment: South African Mastiff
    LIVE_MMLS_DOGS_South_African_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_South_African_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Spanish_Mastiff
    # comment: Spanish Mastiff
    LIVE_MMLS_DOGS_Spanish_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Spanish_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Spanish_Water_Dog
    # comment: Spanish Water Dog
    LIVE_MMLS_DOGS_Spanish_Water_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Spanish_Water_Dog"
    )
    # label: LIVE_MMLS_DOGS_Spinone_Italiano
    # comment: Spinone Italiano
    LIVE_MMLS_DOGS_Spinone_Italiano = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Spinone_Italiano"
    )
    # label: LIVE_MMLS_DOGS_Staffordshire_Bull_Terrier
    # comment: Staffordshire Bull Terrier
    LIVE_MMLS_DOGS_Staffordshire_Bull_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Staffordshire_Bull_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Standard_Schnauzer
    # comment: Standard Schnauzer
    LIVE_MMLS_DOGS_Standard_Schnauzer = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Standard_Schnauzer"
    )
    # label: LIVE_MMLS_DOGS_Sussex_Spaniel
    # comment: Sussex Spaniel
    LIVE_MMLS_DOGS_Sussex_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Sussex_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Swedish_Vallhund
    # comment: Swedish Vallhund
    LIVE_MMLS_DOGS_Swedish_Vallhund = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Swedish_Vallhund"
    )
    # label: LIVE_MMLS_DOGS_Tibetan_Mastiff
    # comment: Tibetan Mastiff
    LIVE_MMLS_DOGS_Tibetan_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tibetan_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Tibetan_Spaniel
    # comment: Tibetan Spaniel
    LIVE_MMLS_DOGS_Tibetan_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tibetan_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Tibetan_Terrier
    # comment: Tibetan Terrier
    LIVE_MMLS_DOGS_Tibetan_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tibetan_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Tosa_Japanese_Mastiff
    # comment: Tosa-Japanese Mastiff
    LIVE_MMLS_DOGS_Tosa_Japanese_Mastiff = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Tosa_Japanese_Mastiff"
    )
    # label: LIVE_MMLS_DOGS_Toy_Fox_Terrier
    # comment: Toy Fox Terrier
    LIVE_MMLS_DOGS_Toy_Fox_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Toy_Fox_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Treeing_Walker_Coonhound
    # comment: Treeing Walker Coonhound
    LIVE_MMLS_DOGS_Treeing_Walker_Coonhound = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Treeing_Walker_Coonhound"
    )
    # label: LIVE_MMLS_DOGS_Utonagan_Northern_Inuit_Dog
    # comment: Utonagan-Northern Inuit Dog
    LIVE_MMLS_DOGS_Utonagan_Northern_Inuit_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Utonagan_Northern_Inuit_Dog"
    )
    # label: LIVE_MMLS_DOGS_Valley_Bulldog
    # comment: Valley Bulldog
    LIVE_MMLS_DOGS_Valley_Bulldog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Valley_Bulldog"
    )
    # label: LIVE_MMLS_DOGS_Vizsla
    # comment: Vizsla
    LIVE_MMLS_DOGS_Vizsla = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Vizsla"
    )
    # label: LIVE_MMLS_DOGS_Weimaraner
    # comment: Weimaraner
    LIVE_MMLS_DOGS_Weimaraner = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Weimaraner"
    )
    # label: LIVE_MMLS_DOGS_Welsh_Springer_Spaniel
    # comment: Welsh Springer Spaniel
    LIVE_MMLS_DOGS_Welsh_Springer_Spaniel = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Welsh_Springer_Spaniel"
    )
    # label: LIVE_MMLS_DOGS_Welsh_Terrier
    # comment: Welsh Terrier
    LIVE_MMLS_DOGS_Welsh_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Welsh_Terrier"
    )
    # label: LIVE_MMLS_DOGS_West_Highland_White_Terrier
    # comment: West Highland White Terrier
    LIVE_MMLS_DOGS_West_Highland_White_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_West_Highland_White_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Whippet
    # comment: Whippet
    LIVE_MMLS_DOGS_Whippet = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Whippet"
    )
    # label: LIVE_MMLS_DOGS_Wire_Fox_Terrier
    # comment: Wire Fox Terrier
    LIVE_MMLS_DOGS_Wire_Fox_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Wire_Fox_Terrier"
    )
    # label: LIVE_MMLS_DOGS_Wirehaired_Pointing_Griffon
    # comment: Wirehaired Pointing Griffon
    LIVE_MMLS_DOGS_Wirehaired_Pointing_Griffon = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Wirehaired_Pointing_Griffon"
    )
    # label: LIVE_MMLS_DOGS_Wirehaired_Vizsla
    # comment: Wirehaired Vizsla
    LIVE_MMLS_DOGS_Wirehaired_Vizsla = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Wirehaired_Vizsla"
    )
    # label: LIVE_MMLS_DOGS_Xoloitzcuintli_Mexican_Hairless_Dog
    # comment: Xoloitzcuintli-Mexican Hairless Dog
    LIVE_MMLS_DOGS_Xoloitzcuintli_Mexican_Hairless_Dog = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Xoloitzcuintli_Mexican_Hairless_Dog"
    )
    # label: LIVE_MMLS_DOGS_Yorkipoo_Yorkshire_Terrier_Poodle_Mix
    # comment: Yorkipoo-Yorkshire Terrier Poodle Mix
    LIVE_MMLS_DOGS_Yorkipoo_Yorkshire_Terrier_Poodle_Mix = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Yorkipoo_Yorkshire_Terrier_Poodle_Mix"
    )
    # label: LIVE_MMLS_DOGS_Yorkshire_Terrier
    # comment: Yorkshire Terrier
    LIVE_MMLS_DOGS_Yorkshire_Terrier = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_DOGS_Yorkshire_Terrier"
    )
    # label: LIVE_MMLS_FERR
    # comment: Ferrets
    LIVE_MMLS_FERR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_FERR"
    )
    # label: LIVE_MMLS_GOAT
    # comment: Goats
    LIVE_MMLS_GOAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_GOAT"
    )
    # label: LIVE_MMLS_HORS
    # comment: Horses
    LIVE_MMLS_HORS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_HORS"
    )
    # label: LIVE_MMLS_MNKY
    # comment: Monkeys
    LIVE_MMLS_MNKY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_MNKY"
    )
    # label: LIVE_MMLS_PIGS
    # comment: Pigs
    LIVE_MMLS_PIGS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_PIGS"
    )
    # label: LIVE_MMLS_RDNT
    # comment: Rodents
    LIVE_MMLS_RDNT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_RDNT"
    )
    # label: LIVE_MMLS_SHEP
    # comment: Sheep
    LIVE_MMLS_SHEP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_MMLS_SHEP"
    )
    # label: LIVE_REPT
    # comment: Reptiles
    LIVE_REPT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_REPT"
    )
    # label: LIVE_VANI
    # comment: Venomous animals
    LIVE_VANI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_VANI"
    )
    # label: LIVE_ZOOA
    # comment: Zoo animals
    LIVE_ZOOA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#LIVE_ZOOA"
    )
    # label: MAIL
    # comment: Mail
    MAIL = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MAIL")
    # label: MART
    # comment: Musical Instruments & Art
    MART = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MART")
    # label: MART_ART
    # comment: Art
    MART_ART = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_ART")
    # label: MART_ENGR
    # comment: Engraving
    MART_ENGR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_ENGR"
    )
    # label: MART_HAND
    # comment: Handicraft products
    MART_HAND = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_HAND"
    )
    # label: MART_MUEQ
    # comment: Musical equipment
    MART_MUEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_MUEQ"
    )
    # label: MART_MUSI
    # comment: Musical instruments
    MART_MUSI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_MUSI"
    )
    # label: MART_PNTG
    # comment: Painting
    MART_PNTG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MART_PNTG"
    )
    # label: MLTY
    # comment: Military, Weapons and Ammunition
    MLTY = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY")
    # label: MLTY_AMUN
    # comment: Munitions
    MLTY_AMUN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_AMUN"
    )
    # label: MLTY_MSUP
    # comment: Military supplies
    MLTY_MSUP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_MSUP"
    )
    # label: MLTY_SPWE
    # comment: Sporting weapons
    MLTY_SPWE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_SPWE"
    )
    # label: MLTY_WPNS
    # comment: Weapons
    MLTY_WPNS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#MLTY_WPNS"
    )
    # label: PHAR
    # comment: Pharmaceutical, Medical And Biological
    PHAR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR")
    # label: PHAR_BIOP
    # comment: Biological products
    PHAR_BIOP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP"
    )
    # label: PHAR_BIOP_BIOC
    # comment: Biochemicals
    PHAR_BIOP_BIOC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_BIOC"
    )
    # label: PHAR_BIOP_HEMO
    # comment: Hemoderivatives
    PHAR_BIOP_HEMO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_HEMO"
    )
    # label: PHAR_BIOP_HUBL
    # comment: Human blood
    PHAR_BIOP_HUBL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_HUBL"
    )
    # label: PHAR_BIOP_HUSR
    # comment: Human serum
    PHAR_BIOP_HUSR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_HUSR"
    )
    # label: PHAR_BIOP_LHOR
    # comment: Live human organs
    PHAR_BIOP_LHOR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_LHOR"
    )
    # label: PHAR_BIOP_SEME
    # comment: Semen
    PHAR_BIOP_SEME = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_SEME"
    )
    # label: PHAR_BIOP_SMPL
    # comment: Samples
    PHAR_BIOP_SMPL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_BIOP_SMPL"
    )
    # label: PHAR_MDCN
    # comment: Medicines
    PHAR_MDCN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN"
    )
    # label: PHAR_MDCN_ANTB
    # comment: Antibiotics and Vitamins
    PHAR_MDCN_ANTB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN_ANTB"
    )
    # label: PHAR_MDCN_VACC
    # comment: Vaccines
    PHAR_MDCN_VACC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN_VACC"
    )
    # label: PHAR_MDCN_VETE
    # comment: Vetenary products
    PHAR_MDCN_VETE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MDCN_VETE"
    )
    # label: PHAR_MEDI
    # comment: Medical
    PHAR_MEDI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_MEDI"
    )
    # label: PHAR_PHAR
    # comment: Pharmaceutical products
    PHAR_PHAR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_PHAR"
    )
    # label: PHAR_PHAR_SUEQ
    # comment: Surgical equipment
    PHAR_PHAR_SUEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PHAR_PHAR_SUEQ"
    )
    # label: PRIN
    # comment: Printed Matter
    PRIN = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN")
    # label: PRIN_ADVM
    # comment: Advertising materials
    PRIN_ADVM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_ADVM"
    )
    # label: PRIN_BOOK
    # comment: Books
    PRIN_BOOK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_BOOK"
    )
    # label: PRIN_DOCU
    # comment: Documents and Tickets
    PRIN_DOCU = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_DOCU"
    )
    # label: PRIN_EDUM
    # comment: Educational materials
    PRIN_EDUM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_EDUM"
    )
    # label: PRIN_NEWS
    # comment: Newspapers and Magazines
    PRIN_NEWS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_NEWS"
    )
    # label: PRIN_PPRP
    # comment: Paper products
    PRIN_PPRP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#PRIN_PPRP"
    )
    # label: RAWM
    # comment: Raw materials (Construction, Metals, Wood, Minerals, Plastic)
    RAWM = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM")
    # label: RAWM_BLDM
    # comment: Building material
    RAWM_BLDM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_BLDM"
    )
    # label: RAWM_CLAY
    # comment: Clay products
    RAWM_CLAY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_CLAY"
    )
    # label: RAWM_GLAS
    # comment: Glass products
    RAWM_GLAS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_GLAS"
    )
    # label: RAWM_GRAN
    # comment: Granite slabs
    RAWM_GRAN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_GRAN"
    )
    # label: RAWM_GUMS
    # comment: Gums-Resines
    RAWM_GUMS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_GUMS"
    )
    # label: RAWM_MARB
    # comment: Marble
    RAWM_MARB = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MARB"
    )
    # label: RAWM_METL
    # comment: Metals
    RAWM_METL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_METL"
    )
    # label: RAWM_METP
    # comment: Metal products
    RAWM_METP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_METP"
    )
    # label: RAWM_MICA
    # comment: Mica products
    RAWM_MICA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MICA"
    )
    # label: RAWM_MINE
    # comment: Minerals
    RAWM_MINE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MINE"
    )
    # label: RAWM_MIRR
    # comment: Mirre
    RAWM_MIRR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_MIRR"
    )
    # label: RAWM_OILS
    # comment: Oils
    RAWM_OILS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_OILS"
    )
    # label: RAWM_PLST
    # comment: Plastic products
    RAWM_PLST = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_PLST"
    )
    # label: RAWM_QRTZ
    # comment: Quartz
    RAWM_QRTZ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_QRTZ"
    )
    # label: RAWM_RUBR
    # comment: Rubber products
    RAWM_RUBR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_RUBR"
    )
    # label: RAWM_RUBR_RTYR
    # comment: Rubber tyres
    RAWM_RUBR_RTYR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_RUBR_RTYR"
    )
    # label: RAWM_STNS
    # comment: Stones
    RAWM_STNS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_STNS"
    )
    # label: RAWM_WOOD
    # comment: Wood products
    RAWM_WOOD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#RAWM_WOOD"
    )
    # label: SCIN
    # comment: Scientific Instruments
    SCIN = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN")
    # label: SCIN_DEEQ
    # comment: Densist equipment
    SCIN_DEEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_DEEQ"
    )
    # label: SCIN_DIAG
    # comment: Diagnostics equipment
    SCIN_DIAG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_DIAG"
    )
    # label: SCIN_HEAR
    # comment: Hearing aids
    SCIN_HEAR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_HEAR"
    )
    # label: SCIN_LBEQ
    # comment: Laboratory equipment
    SCIN_LBEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_LBEQ"
    )
    # label: SCIN_MEEQ
    # comment: Medical equipment
    SCIN_MEEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_MEEQ"
    )
    # label: SCIN_OPTI
    # comment: Optical instruments
    SCIN_OPTI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_OPTI"
    )
    # label: SCIN_PRCI
    # comment: Precision instruments
    SCIN_PRCI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#SCIN_PRCI"
    )
    # label: TRPH
    # comment: Trophies
    TRPH = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#TRPH")
    # label: TRPH_HTRH
    # comment: Hunting Trophies
    TRPH_HTRH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TRPH_HTRH"
    )
    # label: TRPH_OTRH
    # comment: Trophies (not hunting)
    TRPH_OTRH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TRPH_OTRH"
    )
    # label: TXTL
    # comment: Textiles, Leather and Furs
    TXTL = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL")
    # label: TXTL_FREW
    # comment: Furs excluding Wear
    TXTL_FREW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_FREW"
    )
    # label: TXTL_FUR
    # comment: Fur
    TXTL_FUR = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_FUR")
    # label: TXTL_FURW
    # comment: Furs wear
    TXTL_FURW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_FURW"
    )
    # label: TXTL_LEXW
    # comment: Leather excluding Wear
    TXTL_LEXW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_LEXW"
    )
    # label: TXTL_LTHR
    # comment: Leather
    TXTL_LTHR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_LTHR"
    )
    # label: TXTL_LTWR
    # comment: Leather wear
    TXTL_LTWR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_LTWR"
    )
    # label: TXTL_TXEW
    # comment: Textiles excluding Wear
    TXTL_TXEW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW"
    )
    # label: TXTL_TXEW_CARP
    # comment: Carpets and Rugs
    TXTL_TXEW_CARP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_CARP"
    )
    # label: TXTL_TXEW_CURT
    # comment: Curtains and Drapery
    TXTL_TXEW_CURT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_CURT"
    )
    # label: TXTL_TXEW_FABR
    # comment: Textile fabric
    TXTL_TXEW_FABR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_FABR"
    )
    # label: TXTL_TXEW_FURN
    # comment: Textile furnish
    TXTL_TXEW_FURN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_FURN"
    )
    # label: TXTL_TXEW_HIDE
    # comment: Hide
    TXTL_TXEW_HIDE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_HIDE"
    )
    # label: TXTL_TXEW_NDLE
    # comment: Needlework
    TXTL_TXEW_NDLE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_NDLE"
    )
    # label: TXTL_TXEW_SKIN
    # comment: Skins
    TXTL_TXEW_SKIN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_SKIN"
    )
    # label: TXTL_TXEW_TRLS
    # comment: Textile rolls
    TXTL_TXEW_TRLS = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_TRLS"
    )
    # label: TXTL_TXEW_YARN
    # comment: Yarns
    TXTL_TXEW_YARN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXEW_YARN"
    )
    # label: TXTL_TXLW
    # comment: Textile wear
    TXTL_TXLW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW"
    )
    # label: TXTL_TXLW_APPR
    # comment: Wearing appareil
    TXTL_TXLW_APPR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_APPR"
    )
    # label: TXTL_TXLW_CLTH
    # comment: Clothing
    TXTL_TXLW_CLTH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_CLTH"
    )
    # label: TXTL_TXLW_FOOT
    # comment: Footwear
    TXTL_TXLW_FOOT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_FOOT"
    )
    # label: TXTL_TXLW_GARM
    # comment: Garments
    TXTL_TXLW_GARM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXLW_GARM"
    )
    # label: TXTL_TXTL
    # comment: Textiles
    TXTL_TXTL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#TXTL_TXTL"
    )
    # label: VALU
    # comment: Valuables
    VALU = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU")
    # label: VALU_BANK
    # comment: Bank notes and Coins
    VALU_BANK = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_BANK"
    )
    # label: VALU_DIAM
    # comment: Diamonds
    VALU_DIAM = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_DIAM"
    )
    # label: VALU_GOLD
    # comment: Gold
    VALU_GOLD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_GOLD"
    )
    # label: VALU_JWRY
    # comment: Jewelery
    VALU_JWRY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_JWRY"
    )
    # label: VALU_PLAT
    # comment: Platinum
    VALU_PLAT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_PLAT"
    )
    # label: VALU_PMET
    # comment: Precious metal
    VALU_PMET = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_PMET"
    )
    # label: VALU_PSTN
    # comment: Precious stones
    VALU_PSTN = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_PSTN"
    )
    # label: VALU_SLVR
    # comment: Silver
    VALU_SLVR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_SLVR"
    )
    # label: VALU_WTCH
    # comment: Watches
    VALU_WTCH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VALU_WTCH"
    )
    # label: VHCL
    # comment: Vehicle / Machinary, Parts, Spares
    VHCL = URIRef("https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL")
    # label: VHCL_AIRC
    # comment: Aircraft
    VHCL_AIRC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC"
    )
    # label: VHCL_AIRC_AACC
    # comment: Aircraft accessories
    VHCL_AIRC_AACC = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AACC"
    )
    # label: VHCL_AIRC_AENG
    # comment: Aicraft engines
    VHCL_AIRC_AENG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AENG"
    )
    # label: VHCL_AIRC_AMTR
    # comment: Aircraft motors
    VHCL_AIRC_AMTR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AMTR"
    )
    # label: VHCL_AIRC_APRT
    # comment: Aircraft parts
    VHCL_AIRC_APRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_APRT"
    )
    # label: VHCL_AIRC_ASUP
    # comment: Aircraft supplies
    VHCL_AIRC_ASUP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_ASUP"
    )
    # label: VHCL_AIRC_AWHL
    # comment: Aircraft wheels
    VHCL_AIRC_AWHL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_AWHL"
    )
    # label: VHCL_AIRC_HELI
    # comment: Helicopter
    VHCL_AIRC_HELI = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_HELI"
    )
    # label: VHCL_AIRC_HPRT
    # comment: Helicopter parts
    VHCL_AIRC_HPRT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_AIRC_HPRT"
    )
    # label: VHCL_MACH
    # comment: Machinery and Tools
    VHCL_MACH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH"
    )
    # label: VHCL_MACH_COIL
    # comment: Cable coil
    VHCL_MACH_COIL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_COIL"
    )
    # label: VHCL_MACH_COMP
    # comment: Comperssors
    VHCL_MACH_COMP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_COMP"
    )
    # label: VHCL_MACH_HRDW
    # comment: Hardware and Equipment
    VHCL_MACH_HRDW = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_HRDW"
    )
    # label: VHCL_MACH_MECH
    # comment: Mechanic products
    VHCL_MACH_MECH = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_MECH"
    )
    # label: VHCL_MACH_MTSP
    # comment: Machinery supplies and Parts
    VHCL_MACH_MTSP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_MTSP"
    )
    # label: VHCL_MACH_OILD
    # comment: Oil drilling equipment
    VHCL_MACH_OILD = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_OILD"
    )
    # label: VHCL_MACH_PART
    # comment: Spare parts
    VHCL_MACH_PART = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_PART"
    )
    # label: VHCL_MACH_PUEQ
    # comment: Pumping equipment
    VHCL_MACH_PUEQ = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_MACH_PUEQ"
    )
    # label: VHCL_SHIP
    # comment: Ships
    VHCL_SHIP = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP"
    )
    # label: VHCL_SHIP_SENG
    # comment: Engines and Turbines
    VHCL_SHIP_SENG = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SENG"
    )
    # label: VHCL_SHIP_SMTR
    # comment: Motor and Generator
    VHCL_SHIP_SMTR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SMTR"
    )
    # label: VHCL_SHIP_SPAR
    # comment: Ship parts
    VHCL_SHIP_SPAR = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SPAR"
    )
    # label: VHCL_SHIP_SSPA
    # comment: Ship spares
    VHCL_SHIP_SSPA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SHIP_SSPA"
    )
    # label: VHCL_SVCL
    # comment: Surface vehicles
    VHCL_SVCL = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL"
    )
    # label: VHCL_SVCL_AUTO
    # comment: Automobiles
    VHCL_SVCL_AUTO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_AUTO"
    )
    # label: VHCL_SVCL_BICY
    # comment: Bicycles
    VHCL_SVCL_BICY = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_BICY"
    )
    # label: VHCL_SVCL_CRTA
    # comment: Cartainer
    VHCL_SVCL_CRTA = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_CRTA"
    )
    # label: VHCL_SVCL_MOTO
    # comment: Motorcycles
    VHCL_SVCL_MOTO = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_MOTO"
    )
    # label: VHCL_SVCL_PART
    # comment: Automobile parts
    VHCL_SVCL_PART = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_PART"
    )
    # label: VHCL_SVCL_TIRE
    # comment: Tires
    VHCL_SVCL_TIRE = URIRef(
        "https://onerecord.iata.org/ns/code-lists/CommodityCode#VHCL_SVCL_TIRE"
    )
