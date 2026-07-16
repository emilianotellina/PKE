from pke.csr import CSRBuilder
from pke.csr.relation import RelationType



def test_create_literal():

    builder = CSRBuilder()


    node = builder.literal(
        10
    )


    assert node.type == "literal"

    assert node.attributes["value"] == 10



def test_create_binary():

    builder = CSRBuilder()


    left = builder.literal(1)

    right = builder.literal(2)


    operation = builder.binary(
        "+",
        left,
        right
    )


    assert operation.type == "binary_operation"


    operands = builder.graph.children(
        operation
    )


    assert len(operands) == 2



def test_create_call():

    builder = CSRBuilder()


    target = builder.identifier(
        "login"
    )


    user = builder.identifier(
        "user"
    )


    call = builder.call(
        target,
        [
            user
        ]
    )


    assert call.type == "call"


    target_nodes = builder.graph.children(
        call,
        RelationType.TARGET
    )


    assert target_nodes[0].name == "login"



def test_assignment():

    builder = CSRBuilder()


    variable = builder.identifier(
        "result"
    )


    value = builder.literal(
        10
    )


    assignment = builder.assignment(
        variable,
        value
    )


    assert assignment.type == "assignment"