import json
from typing import List

from pydantic import AnyUrl, BaseModel, Field


class ServerInformation(BaseModel):
    # label: has Data Holder
    # comment: The data holder of the servers data.
    # iri: https://onerecord.iata.org/ns/api#hasDataHolder
    # hasDataHolder: Organization = Field(
    #     serialization_alias="https://onerecord.iata.org/ns/api#hasDataHolder"
    # )

    # label: Supported encoding
    # comment: Optional list of supported encodings of the ONE Record server, e.g. gzip
    # iri: https://onerecord.iata.org/ns/api#hasSupportedEncoding
    hasSupportedEncoding: List[str] = Field(
        default_factory=list,
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedEncoding",
    )

    # label: Supported API version
    # comment: Supported ONE Record API versions by the server, MUST include at least one supported version.
    # iri: https://onerecord.iata.org/ns/api#hasSupportedApiVersion
    hasSupportedApiVersion: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedApiVersion"
    )

    # label: Supported content type
    # comment: Supported content types of the server, MUST contain at least application/ld+json
    # iri: https://onerecord.iata.org/ns/api#hasSupportedContentType
    hasSupportedContentType: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedContentType"
    )

    # label: Supported language
    # comment: Supported languages of the ONE Record API, minimum is en-US (American English)
    # iri: https://onerecord.iata.org/ns/api#hasSupportedLanguage
    hasSupportedLanguage: List[str] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedLanguage"
    )

    # label: Supported ontology
    # comment: Supported ontologies on the server, MUST be non-versioned IRIs
    # iri: https://onerecord.iata.org/ns/api#hasSupportedOntology
    hasSupportedOntology: List[AnyUrl] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedOntology"
    )

    # label: Supported ontology version
    # comment: Supported ontology versions on the server, MUST be versioned IRIs
    # iri: https://onerecord.iata.org/ns/api#hasSupportedOntologyVersion
    hasSupportedOntologyVersion: List[AnyUrl] = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasSupportedOntologyVersion"
    )

    # label: Server endpoint
    # comment: ONE Record API endpoint
    # iri: https://onerecord.iata.org/ns/api#hasServerEndpoint
    hasServerEndpoint: AnyUrl = Field(
        serialization_alias="https://onerecord.iata.org/ns/api#hasServerEndpoint"
    )


print(json.dumps(ServerInformation.model_json_schema(), indent=4))
