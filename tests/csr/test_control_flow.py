from pke.csr import (
    IfNode,
    ReturnNode,
)


def test_if_node():

    node = IfNode()

    assert node.type == "if"

    assert node.then_block is not None


def test_return_node():

    node = ReturnNode()

    node.value = "x"

    assert node.type == "return"

    assert node.value == "x"