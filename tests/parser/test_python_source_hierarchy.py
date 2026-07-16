from pke.parser import PythonAdapter
from pke.csr.relation import RelationType


def test_source_hierarchy():

    graph = PythonAdapter().parse(
        """
def login():
    return 1
"""
    )


    projects = graph.find(
        node_type="project"
    )

    assert len(projects) == 1


    packages = graph.children(
        projects[0],
        RelationType.PACKAGE
    )

    assert len(packages) == 1


    files = graph.children(
        packages[0],
        RelationType.FILE
    )

    assert len(files) == 1


    functions = graph.children(
        files[0],
        RelationType.FUNCTION
    )

    assert len(functions) == 1