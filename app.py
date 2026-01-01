from devtools import debug
from fastapi import FastAPI, Request, Response
from pydantic import AnyUrl
from rdflib import URIRef

from one_record_ontology.models.generated.api import (
    ServerInformation,
    Subscription,
    SubscriptionEventType,
    TopicType,
)
from one_record_ontology.models.generated.cargo import Organization, OtherIdentifier

app = FastAPI()


@app.get(
    "/",
    # response_class=Response,
    response_model=ServerInformation,
)
async def read_root(request: Request):
    base_url = str(request.base_url).rstrip("/")
    data_holder = "/".join([base_url, "logistics-objects", "_data-holder"])

    organization = Organization(
        subject=URIRef(data_holder),
        name="TEST ORG",
        otherIdentifiers=[
            OtherIdentifier(textualValue="ID1"),
            OtherIdentifier(textualValue="ID2"),
        ],
    )

    server_info = ServerInformation(
        subject=URIRef(base_url),
        hasServerEndpoint=AnyUrl(base_url),
        hasDataHolder=organization,
        hasSupportedApiVersion=["2.2.0"],
        hasSupportedContentType=["application/ld+json"],
        hasSupportedLanguage=["en-US"],
        hasSupportedOntology=[
            AnyUrl("https://onerecord.iata.org/ns/cargo/3.2.0"),
            AnyUrl("https://onerecord.iata.org/ns/api/2.2.0"),
        ],
        hasSupportedOntologyVersion=[],
    )

    debug(server_info)

    return Response(
        content=server_info.to_graph().serialize(
            format="json-ld",
            context={
                "api": "https://onerecord.iata.org/ns/api#",
                "cargo": "https://onerecord.iata.org/ns/cargo#",
            },
        ),
        media_type="application/ld+json",
    )


@app.get(
    "/subscriptions",
    # response_class=Response,
    response_model=Subscription,
)
def get_subscription(request: Request, topicType: TopicType, topic: AnyUrl):
    base_url = str(request.base_url).rstrip("/")
    data_holder = "/".join([base_url, "logistics-objects", "_data-holder"])

    organization = Organization(
        subject=URIRef(data_holder),
        name="TEST ORG",
    )

    subscription = Subscription(
        hasSubscriber=organization,
        hasTopicType=topicType,
        hasTopic=topic,
        includeSubscriptionEventType=[
            SubscriptionEventType.LOGISTICS_OBJECT_UPDATED,
            SubscriptionEventType.LOGISTICS_OBJECT_CREATED,
            SubscriptionEventType.LOGISTICS_EVENT_RECEIVED,
        ],
    )

    return Response(
        content=subscription.to_graph().serialize(
            format="json-ld",
            context={
                "api": "https://onerecord.iata.org/ns/api#",
                "cargo": "https://onerecord.iata.org/ns/cargo#",
            },
        ),
        media_type="application/ld+json",
    )
