from pathlib import Path

from rdflib import Graph

from one_record_ontology.models.generated.api import ServerInformation

TEST_DIR = Path(__file__).parent.resolve()


def test_ServerInformation():
    filepath = TEST_DIR / "resources" / "ServerInformation.json"

    data = Path(filepath).read_text()

    g = Graph()
    g.parse(data=data, format="json-ld")

    obj = ServerInformation.from_graph(g)
    obj.to_graph()
