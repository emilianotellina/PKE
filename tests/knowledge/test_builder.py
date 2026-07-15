from pke.knowledge import (
    KnowledgeBuilder,
    Project
)


def test_build_graph():

    scanned = Project(
        name="demo",
        path="/tmp/demo"
    )


    builder = KnowledgeBuilder()


    result = builder.build_project(
        ".",
        scanned
    )


    assert result.name == "demo"

    assert len(
        builder.graph.nodes
    ) > 0