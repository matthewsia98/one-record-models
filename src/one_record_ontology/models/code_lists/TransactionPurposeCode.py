from enum import Enum

from rdflib import URIRef


class TransactionPurposeCode(str, Enum):
    """
    label: TransactionPurposeCode
    comment: Restricted code list of purpose-of-transaction-codes
    """

    # label: B
    # comment: Breeding in captivity or artificial propagation
    B = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#B")
    # label: E
    # comment: Educational
    E = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#E")
    # label: G
    # comment: Botanical garden
    G = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#G")
    # label: H
    # comment: Hunting trophy
    H = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#H")
    # label: L
    # comment: Law enforcement / judicial / forensic
    L = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#L")
    # label: M
    # comment: Medical (including biomedical research)
    M = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#M")
    # label: N
    # comment: Reintroduction or introduction into the wild
    N = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#N")
    # label: P
    # comment: Personal
    P = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#P")
    # label: Q
    # comment: Circus or travelling exhibition
    Q = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#Q")
    # label: S
    # comment: Scientific
    S = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#S")
    # label: T
    # comment: Commercial
    T = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#T")
    # label: Z
    # comment: Zoo
    Z = URIRef("https://onerecord.iata.org/ns/code-lists/TransactionPurposeCode#Z")
