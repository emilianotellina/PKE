from pke.csr.expression_resolver import ExpressionResolver
from pke.csr.query import CSRQuery
from pke.parser.python_adapter import PythonAdapter


def test_python_identifier_resolution():

    graph = PythonAdapter().parse(
        """
def login(user):
    return user
"""
    )

    query = CSRQuery(graph)

    resolver = ExpressionResolver(query)

    identifiers = graph.find(
        node_type="identifier"
    )

    assert len(identifiers) > 0

    result = resolver.resolve(
        identifiers[0]
    )

    assert result is not None
    
    def test_python_call_resolution():

        graph = PythonAdapter().parse(
            """
    def login(user):
        token = authenticate(user)
        return token
    """
        )


        query = CSRQuery(graph)

        resolver = ExpressionResolver(
            query
        )


        calls = graph.find(
            node_type="call"
        )


        assert len(calls) == 1


        result = resolver.resolve(
            calls[0]
        )


        assert result == "authenticate(user)"
        
    def test_python_assignment_resolution():


        graph = PythonAdapter().parse(
            """
    def login(user):
        token = authenticate(user)
        return token
    """
        )


        query = CSRQuery(
            graph
        )


        resolver = ExpressionResolver(
            query
        )


        assignments = graph.find(
            node_type="assignment"
        )


        assert len(assignments) == 1


        result = resolver.resolve(
            assignments[0]
        )


        assert (
            result
            ==
            "token = authenticate(user)"
        )