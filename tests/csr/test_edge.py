from pke.csr.relation import RelationType

from pke.csr import (
    CSRGraph,
    ProjectNode,
    PackageNode,
)


def test_create_relation():

    graph = CSRGraph()


    project = ProjectNode(
        "demo"
    )


    package = PackageNode(
        "core"
    )


    graph.add(project)

    graph.add(package)


    edge = graph.link(
        project,
        package,
        RelationType.CONTAINS
    )


    assert edge.relation == RelationType.CONTAINS

    assert edge.source == project.id

    assert edge.target == package.id



def test_find_outgoing_relation():

    graph = CSRGraph()


    project = ProjectNode(
        "demo"
    )


    package = PackageNode(
        "core"
    )


    graph.add(project)

    graph.add(package)


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



def test_find_incoming_relation():

    graph = CSRGraph()


    project = ProjectNode(
        "demo"
    )


    package = PackageNode(
        "core"
    )


    graph.add(project)

    graph.add(package)


    graph.link(
        project,
        package,
        RelationType.CONTAINS
    )


    parents = graph.parents(
        package,
        RelationType.CONTAINS
    )

    assert len(parents) == 1

    assert parents[0].name == "demo"