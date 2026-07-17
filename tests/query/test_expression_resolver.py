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