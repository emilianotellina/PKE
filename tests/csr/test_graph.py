from pke.csr import (
    CSRGraph,
    ProjectNode,
    PackageNode,
)


def test_graph_add_node():

    graph = CSRGraph()


    project = ProjectNode(
        "demo"
    )


    graph.add(
        project
    )


    assert project.id in graph.nodes

    assert graph.nodes[project.id] == project



def test_graph_find_node():

    graph = CSRGraph()


    project = ProjectNode(
        "demo"
    )

    package = PackageNode(
        "core"
    )


    graph.add(
        project
    )

    graph.add(
        package
    )


    result = graph.find(
        name="core"
    )


    assert len(result) == 1

    assert result[0].name == "core"