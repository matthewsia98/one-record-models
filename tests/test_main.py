from pathlib import Path

import pytest
from rdflib import Graph
from rdflib.compare import graph_diff

from one_record_ontology.models.base_model import OneRecordBaseModel
from one_record_ontology.models.generated.api import (
    Notification,
    ServerInformation,
    Subscription,
)
from one_record_ontology.models.generated.cargo import Piece, Waybill

TEST_DIR = Path(__file__).parent.resolve()


@pytest.mark.parametrize(
    "model_cls, filename",
    [
        (ServerInformation, "ServerInformation.json"),
        (Subscription, "Subscription.json"),
        (Notification, "Notification.json"),
        (Piece, "Piece.json"),
        (Waybill, "Waybill.json"),
    ],
)
def test_jsonld_roundtrip(model_cls: OneRecordBaseModel, filename):
    filepath = TEST_DIR / "resources" / filename
    data = filepath.read_text()

    g1 = Graph()
    g1.parse(data=data, format="json-ld")

    obj = model_cls.from_graph(g1)

    g2 = obj.to_graph()

    _, in_first, _ = graph_diff(g1, g2)

    assert len(in_first) == 0, "\n".join(
        [
            "==== g1 ====",
            g1.serialize(format="json-ld"),
            "==== g2 ====",
            g2.serialize(format="json-ld"),
            "==== in_first ====",
            "".join([f"\n{str(x)}" for x in in_first]),
        ]
    )
