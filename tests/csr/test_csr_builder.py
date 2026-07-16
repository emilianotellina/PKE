from pke.csr import CSRBuilder
from pke.csr.relation import RelationType


def test_create_function():

    builder = CSRBuilder()


    function = builder.begin_function(
        "login",
        "login(user)"
    )


    builder.add_parameter(
        "user",
        "User"
    )


    builder.add_return()


    builder.end_function()


    graph = builder.graph


    assert function.name == "login"


    body = graph.children(
        function,
        RelationType.BODY
    )


    assert len(body) == 1


    statements = graph.children(
        body[0],
        RelationType.CONTAINS
    )


    assert len(statements) == 1

    assert statements[0].type == "return"