from pke.csr import (
    FunctionNode,
    BodyNode,
    StatementNode,
)


def test_function_body():

    fn = FunctionNode(
        "login"
    )


    body = BodyNode()

    stmt = StatementNode(
        "return"
    )


    body.add_statement(
        stmt
    )


    fn.set_body(
        body
    )


    assert fn.body is body

    assert len(fn.body.children) == 1

    assert fn.body.children[0].type == "return"