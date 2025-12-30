from enum import Enum

from rdflib import URIRef


class ServiceCode(str, Enum):
    """
    label: ServiceCode
    comment: Restricted code list corresponding to cXML code list 1.38 Service Codes
    """

    # label: A
    # comment: Airport-to-Airport
    A = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#A")
    # label: B
    # comment: Service Shipment
    B = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#B")
    # label: C
    # comment: Company Material
    C = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#C")
    # label: D
    # comment: Door-to-Door Service
    D = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#D")
    # label: E
    # comment: Airport-to-Door
    E = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#E")
    # label: F
    # comment: Flight Specific
    F = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#F")
    # label: G
    # comment: Door-to-Airport
    G = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#G")
    # label: H
    # comment: Company Mail
    H = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#H")
    # label: I
    # comment: Diplomatic Mail
    I = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#I")
    # label: J
    # comment: Priority Service
    J = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#J")
    # label: P
    # comment: Small Package Service
    P = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#P")
    # label: S
    # comment: Substitute Truck
    S = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#S")
    # label: T
    # comment: Charter
    T = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#T")
    # label: X
    # comment: Express Shipments
    X = URIRef("https://onerecord.iata.org/ns/code-lists/ServiceCode#X")
