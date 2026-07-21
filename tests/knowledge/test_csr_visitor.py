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
    
    
def test_function_semantics():


    graph = PythonAdapter().parse(
        """
def login(user):
    token = authenticate(user)
    return token
"""
    )


    visitor = KnowledgeCSRVisitor(graph)


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


    assert len(
        function.variables
    ) == 1


    assert len(
        function.returns
    ) == 1
    
def test_expression_information():


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
        "token"
        in function.variables
    )


    assert (
        "authenticate(user)"
        in function.calls
    )


    assert (
        "token"
        in function.returns
    )