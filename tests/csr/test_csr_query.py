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