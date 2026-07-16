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


    edge = graph.connect(
        project,
        package,
        "CONTAINS"
    )


    assert edge.relation == "CONTAINS"

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


    graph.connect(
        project,
        package,
        "CONTAINS"
    )


    edges = graph.outgoing(
        project,
        "CONTAINS"
    )


    assert len(edges) == 1



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


    graph.connect(
        project,
        package,
        "CONTAINS"
    )


    edges = graph.incoming(
        package,
        "CONTAINS"
    )


    assert len(edges) == 1