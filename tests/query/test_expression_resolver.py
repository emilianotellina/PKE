import pytest

from pke.csr.expression_resolver import ExpressionResolver


class DummyNode:

    def __init__(
        self,
        node_type,
        name=None,
        value=None,
    ):
        self.type = node_type
        self.name = name
        self.value = value


def test_resolve_none():

    resolver = ExpressionResolver(None)

    assert resolver.resolve(None) is None


def test_resolve_identifier():

    resolver = ExpressionResolver(None)

    node = DummyNode(
        "identifier",
        name="token",
    )

    assert resolver.resolve(node) == "token"


def test_resolve_literal():

    resolver = ExpressionResolver(None)

    node = DummyNode(
        "literal",
        value=5,
    )

    assert resolver.resolve(node) == "5"


def test_unknown_node():

    resolver = ExpressionResolver(None)

    node = DummyNode(
        "unknown",
    )

    with pytest.raises(NotImplementedError):

        resolver.resolve(node)

def test_resolve_call():

    class FakeQuery:

        def target(self, node):
            return node.target


        def arguments(self, node):
            return node.arguments


    resolver = ExpressionResolver(
        FakeQuery()
    )


    function = DummyNode(
        "identifier",
        name="authenticate",
    )

    argument = DummyNode(
        "identifier",
        name="user",
    )


    call = DummyNode(
        "call",
    )

    call.target = function
    call.arguments = [
        argument
    ]


    assert (
        resolver.resolve(call)
        ==
        "authenticate(user)"
    )
    
    def test_resolve_assignment():


        class FakeQuery:


            def target(self, node):
                return node.target


            def value(self, node):
                return node.value



        resolver = ExpressionResolver(
            FakeQuery()
        )


        target = DummyNode(
            "identifier",
            name="token",
        )


        value = DummyNode(
            "identifier",
            name="value",
        )


        assignment = DummyNode(
            "assignment"
        )


        assignment.target = target
        assignment.value = value


        assert (
            resolver.resolve(
                assignment
            )
            ==
            "token = value"
        )
        
    def test_resolve_return():


        class FakeQuery:


            def value(self, node):
                return node.value



        resolver = ExpressionResolver(
            FakeQuery()
        )


        value = DummyNode(
            "identifier",
            name="token",
        )


        return_node = DummyNode(
            "return"
        )


        return_node.value = value


        assert (
            resolver.resolve(
                return_node
            )
            ==
            "return token"
        )