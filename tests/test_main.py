from pathlib import Path

from devtools import debug
from rdflib import Graph

from one_record_ontology.models.generated.api import (
    Notification,
    ServerInformation,
    Subscription,
)

TEST_DIR = Path(__file__).parent.resolve()


def test_ServerInformation():
    filepath = TEST_DIR / "resources" / "ServerInformation.json"

    data = Path(filepath).read_text()

    g = Graph()
    g.parse(data=data, format="json-ld")

    obj = ServerInformation.from_graph(g)
    debug(obj)

    obj.to_graph()


def test_Subscription():
    filepath = TEST_DIR / "resources" / "Subscription.json"

    data = Path(filepath).read_text()

    g = Graph()
    g.parse(data=data, format="json-ld")

    obj = Subscription.from_graph(g)
    debug(obj)

    obj.to_graph()


def test_Notification():
    filepath = TEST_DIR / "resources" / "Notification.json"

    data = Path(filepath).read_text()

    g = Graph()
    g.parse(data=data, format="json-ld")

    obj = Notification.from_graph(g)
    debug(obj)

    obj.to_graph()
