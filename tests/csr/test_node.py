from pke.csr import ProjectNode


def test_project_node():

    node = ProjectNode(
        "demo"
    )

    assert node.type == "project"

    assert node.name == "demo"