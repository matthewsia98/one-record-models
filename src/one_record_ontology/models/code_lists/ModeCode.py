from enum import Enum

from rdflib import URIRef


class ModeCode(str, Enum):
    """
    comment: Restricted Code List of mode codes, UNECE Recommendation No. 19
    """

    # label: AIR_TRANSPORT
    # comment: Indicates the transport mode to be Air Transport (4)
    AIR_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#AIR_TRANSPORT"
    )
    # label: FIXED_TRANSPORT_INSTALLATION
    # comment: Indicates that the transport mode is a Fixed Transport Installation (7)
    FIXED_TRANSPORT_INSTALLATION = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#FIXED_TRANSPORT_INSTALLATION"
    )
    # label: INLAND_WATER_TRANSPORT
    # comment: Indicates that the transport mode to be Inland Water Transport (8)
    INLAND_WATER_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#INLAND_WATER_TRANSPORT"
    )
    # label: MARITIME_TRANSPORT
    # comment: Indicates the transport mode to be Maritime Transport (1)
    MARITIME_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#MARITIME_TRANSPORT"
    )
    # label: MULTIMODAL_TRANSPORT
    # comment: Indicates a Multimodal Transport (6)
    MULTIMODAL_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#MULTIMODAL_TRANSPORT"
    )
    # label: RAIL_TRANSPORT
    # comment: Indicates the transport mode to be Rail Transport (2)
    RAIL_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#RAIL_TRANSPORT"
    )
    # label: ROAD_TRANSPORT
    # comment: Indicates the transport mode to be Road Transport (3)
    ROAD_TRANSPORT = URIRef(
        "https://onerecord.iata.org/ns/code-lists/ModeCode#ROAD_TRANSPORT"
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
