from pke.knowledge import (
    Project,
    Package,
    SourceFile,
    Function,
    Parameter,
    KnowledgeGraph
)


def test_project_model():

    project = Project(
        name="demo",
        path="/tmp/demo"
    )

    assert project.name == "demo"



def test_function_model():

    function = Function(
        name="load",
        return_type="User",
        parameters=[
            Parameter(
                name="id",
                type="int"
            )
        ]
    )

    assert function.parameters[0].name == "id"



def test_graph():

    graph = KnowledgeGraph()

    project = Project(
        name="demo"
    )

    graph.add_node(project)

    assert graph.find(
        project.id
    ) == project