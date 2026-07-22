from pke.parser.python_adapter import PythonAdapter
from pke.knowledge.csr_visitor import KnowledgeCSRVisitor
from pke.csr.semantic_walker import SemanticWalker



def test_function_call_target():

    graph = PythonAdapter().parse(
        """
def login(user):
    token = authenticate(user)
    return token
"""
    )


    visitor = KnowledgeCSRVisitor(
        graph
    )


    walker = SemanticWalker(
        graph,
        visitor
    )


    walker.walk()


    function = (
        visitor.project
        .packages[0]
        .files[0]
        .symbols[0]
    )


    assert (
        "authenticate"
        in function.call_targets
    )