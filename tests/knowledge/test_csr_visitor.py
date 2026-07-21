from pke.parser.python_adapter import PythonAdapter

from pke.csr import SemanticWalker

from pke.knowledge import KnowledgeCSRVisitor



def test_csr_to_knowledge():


    graph = PythonAdapter().parse(
        """
def login(user):
    return user
"""
    )


    visitor = KnowledgeCSRVisitor()


    walker = SemanticWalker(
        graph,
        visitor
    )


    walker.walk()


    project = visitor.project


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

    assert (
        function.parameters[0].name
        ==
        "user"
    )