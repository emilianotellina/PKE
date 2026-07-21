from pke.parser.python_adapter import PythonAdapter

from pke.knowledge import CSRKnowledgeAdapter



def test_csr_adapter():


    graph = PythonAdapter().parse(
        """
def login(user):
    return user
"""
    )


    adapter = CSRKnowledgeAdapter()


    project = adapter.build(
        graph
    )


    assert project.name == "python_project"


    assert (
        project.packages[0].name
        ==
        "root"
    )


    function = (
        project
        .packages[0]
        .files[0]
        .symbols[0]
    )


    assert function.name == "login"