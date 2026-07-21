from pke.parser.python_adapter import PythonAdapter
from pke.csr.query import CSRQuery


def test_query_function():

    graph = PythonAdapter().parse(
        """
def login(user):
    return user
"""
    )


    query = CSRQuery(graph)


    projects = query.projects()

    assert len(projects) == 1


    packages = query.packages(
        projects[0]
    )

    assert len(packages) == 1


    files = query.files(
        packages[0]
    )

    assert len(files) == 1


    functions = query.functions(
        files[0]
    )

    assert len(functions) == 1


    function = functions[0]

    assert function.name == "login"


    parameters = query.parameters(
        function
    )

    assert len(parameters) == 1

    assert parameters[0].name == "user"
    
def test_assignment_query():

    graph = PythonAdapter().parse(
        """
def login(user):
    token = authenticate(user)
"""
    )

    query = CSRQuery(graph)

    assignment = graph.find(
        node_type="assignment"
    )[0]

    target = query.target(
        assignment
    )

    value = query.value(
        assignment
    )

    assert target.name == "token"
    assert value.type == "call"


def test_call_query():

    graph = PythonAdapter().parse(
        """
def login(user):
    token = authenticate(user)
"""
    )

    query = CSRQuery(graph)

    call = graph.find(
        node_type="call"
    )[0]

    target = query.target(
        call
    )

    arguments = query.arguments(
        call
    )

    assert target.name == "authenticate"

    assert len(arguments) == 1

    assert arguments[0].name == "user"
    
def test_statement_queries():

    graph = PythonAdapter().parse(
        """
def test():

    x = 1

    return x
"""
    )

    query = CSRQuery(
        graph
    )

    function = query.functions(
        query.files(
            query.packages(
                query.projects()[0]
            )[0]
        )[0]
    )[0]

    body = query.body(
        function
    )

    assignments = query.assignments(
        body
    )

    returns = query.returns(
        body
    )

    assert len(assignments) == 1

    assert len(returns) == 1