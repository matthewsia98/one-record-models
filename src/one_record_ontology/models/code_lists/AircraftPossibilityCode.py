from enum import Enum

from rdflib import URIRef


class AircraftPossibilityCode(str, Enum):
    """
    label: AircraftPossibilityCode
    comment: Restricted code list corresponding to cXML code list 1.46 Aircraft Possibility Codes
    """

    # label: BBF
    # comment: Pure freighter flight carrying Loose Load Cargo
    BBF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#BBF")
    # label: BBQ
    # comment: Mixed configuration (Combi) aircraft carrying Loose Load Cargo on the passenger deck
    BBQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#BBQ")
    # label: BBV
    # comment: Truck carrying Loose Load Cargo
    BBV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#BBV")
    # label: LLF
    # comment: Pure freighter flight carrying Containerized Cargo (ULDs)
    LLF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLF")
    # label: LLJ
    # comment: Passenger flight operated by wide-bodied aircraft carrying Containerized (ULDs)
    LLJ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLJ")
    # label: LLQ
    # comment: Mixed configuration (Combi) aircraft carrying Containerized Cargo (ULDs) on the passenger deck
    LLQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLQ")
    # label: LLV
    # comment: Truck carrying Containerized Cargo (ULDs)
    LLV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LLV")
    # label: LPF
    # comment: Pure freighter flight carrying Containerized (ULDs)/Palletized Cargo
    LPF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPF")
    # label: LPJ
    # comment: Passenger flight operated by wide-bodied aircraft carrying Containerized (ULDs)/ Palletized Cargo
    LPJ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPJ")
    # label: LPQ
    # comment: Mixed configuration (Combi) aircraft carrying Containerized (ULDs)/Palletized Cargo on the passenger deck
    LPQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPQ")
    # label: LPV
    # comment: Truck carrying Containerized (ULDs)/Palletized Cargo
    LPV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#LPV")
    # label: PPF
    # comment: Pure freighter flight carrying Palletized Cargo
    PPF = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPF")
    # label: PPJ
    # comment: Passenger flight operated by wide-bodied aircraft carrying Palletized Cargo
    PPJ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPJ")
    # label: PPQ
    # comment: Mixed configuration aircraft carrying Palletized Cargo on the passenger deck
    PPQ = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPQ")
    # label: PPV
    # comment: Truck carrying Palletized Cargo
    PPV = URIRef("https://onerecord.iata.org/ns/code-lists/AircraftPossibilityCode#PPV")
