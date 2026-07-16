from pke.csr import (
    ProjectNode,
    CSRSerializer
)


def test_serializer():

    node = ProjectNode(
        "demo"
    )


    result = CSRSerializer().serialize(
        node
    )


    assert "demo" in result

    assert "project" in result