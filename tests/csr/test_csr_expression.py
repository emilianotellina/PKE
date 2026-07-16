from pke.csr import (
    IdentifierNode,
    LiteralNode,
    BinaryOperationNode,
    CallNode,
    AssignmentNode,
)


def test_identifier():

    node = IdentifierNode(
        "user"
    )

    assert node.type == "identifier"

    assert node.name == "user"



def test_literal():

    node = LiteralNode(
        10
    )

    assert node.type == "literal"

    assert node.attributes["value"] == 10



def test_binary():

    node = BinaryOperationNode(
        "+"
    )

    assert node.type == "binary_operation"

    assert node.attributes["operator"] == "+"



def test_call():

    node = CallNode()

    assert node.type == "call"



def test_assignment():

    node = AssignmentNode()

    assert node.type == "assignment"