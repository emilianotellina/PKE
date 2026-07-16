from pke.csr import (
    FunctionNode,
    BodyNode,
    StatementNode,
    CSRGraph
)

from pke.csr.relation import RelationType


def test_function_body():

    fn = FunctionNode(
        "login"
    )

    body = BodyNode()

    stmt = StatementNode(
        "return"
    )


    graph = CSRGraph()


    graph.add(fn)

    graph.add(body)

    graph.add(stmt)


    graph.link(
        fn,
        body,
        RelationType.BODY
    )


    graph.link(
        body,
        stmt,
        RelationType.CONTAINS
    )


    result = graph.children(
        body,
        RelationType.CONTAINS
    )


    assert len(result) == 1

    assert result[0].type == "return"