from pke.csr import (
    CSRGraph,
    ProjectNode,
    PackageNode,
)
from pke.csr.relation import RelationType


def test_relation():

    graph = CSRGraph()

    project = graph.add(
        ProjectNode("demo")
    )

    package = graph.add(
        PackageNode("core")
    )

    graph.link(
        project,
        package,
        RelationType.CONTAINS
    )

    children = graph.children(
        project,
        RelationType.CONTAINS
    )

    assert len(children) == 1

    assert children[0].name == "core"