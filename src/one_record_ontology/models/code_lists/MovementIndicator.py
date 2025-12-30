from enum import Enum

from rdflib import URIRef


class MovementIndicator(str, Enum):
    """
    label: MovementIndicator
    comment: NOT FINAL YET - Open code list corresponding to cXML code list 1.92 Movement Indicators
    """

    # label: AA
    # comment: Actual Arrival (Touchdown)
    AA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AA")
    # label: AB
    # comment: Actual On-block
    AB = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AB")
    # label: AD
    # comment: Actual Departure (Take off)
    AD = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AD")
    # label: AG
    # comment: Actual gate in time - Relates to gate passing of trucks
    AG = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AG")
    # label: AH
    # comment: Actual gate out time - Relates t gate passing of trucks
    AH = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AH")
    # label: AK
    # comment: Actual end of unloading time
    AK = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AK")
    # label: AL
    # comment: Actual end of loading time
    AL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AL")
    # label: AO
    # comment: Actual Off-block
    AO = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AO")
    # label: AR
    # comment: Actual driver reporting time
    AR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#AR")
    # label: CN
    # comment: Cancellation
    CN = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#CN")
    # label: DA
    # comment: Doc Arrival
    DA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#DA")
    # label: DL
    # comment: Delayed
    DL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#DL")
    # label: DV
    # comment: Diversion
    DV = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#DV")
    # label: EA
    # comment: Estimated Arrival (Touchdown)
    EA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EA")
    # label: EB
    # comment: Estimated On-block
    EB = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EB")
    # label: ED
    # comment: Estimated Departure (Take off)
    ED = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#ED")
    # label: EK
    # comment: Estimated end of unloading time
    EK = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EK")
    # label: EL
    # comment: Estimated end of loading time
    EL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EL")
    # label: EO
    # comment: Estimated Off-block
    EO = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#EO")
    # label: ER
    # comment: Estimated driver reporting time
    ER = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#ER")
    # label: FR
    # comment: Force Return
    FR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#FR")
    # label: NI
    # comment: Next Information
    NI = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#NI")
    # label: PA
    # comment: Pre-announcement of the truck - to enable to pre-announce data (driver name, license plates, etc.) to GHA at departure station
    PA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#PA")
    # label: RR
    # comment: Return to RAMP
    RR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#RR")
    # label: SA
    # comment: Scheduled Arrival
    SA = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SA")
    # label: SD
    # comment: Scheduled Departure
    SD = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SD")
    # label: SK
    # comment: Scheduled end of unloading time
    SK = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SK")
    # label: SL
    # comment: Scheduled end of loading time
    SL = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SL")
    # label: SR
    # comment: Scheduled latest driver reporting time for collection and/or delivery
    SR = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SR")
    # label: SS
    # comment: Scheduled earliest driver reporting time for collection and/or delivery
    SS = URIRef("https://onerecord.iata.org/ns/code-lists/MovementIndicator#SS")
