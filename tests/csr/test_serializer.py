from pke.csr import (
    CSRGraph,
    ProjectNode,
    CSRSerializer
)


def test_serializer():

    graph = CSRGraph()

    node = ProjectNode(
        "demo"
    )

    graph.add(node)


    result = CSRSerializer().serialize(
        graph
    )


    assert "demo" in result