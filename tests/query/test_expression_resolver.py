import pytest

from pke.csr import ExpressionResolver


class DummyNode:

    def __init__(self, node_type, name=None):
        self.type = node_type
        self.name = name


def test_resolve_none():

    resolver = ExpressionResolver(None)

    assert resolver.resolve(None) is None


def test_resolve_identifier():

    resolver = ExpressionResolver(None)

    node = DummyNode(
        "identifier",
        "token",
    )

    assert resolver.resolve(node) == "token"


def test_unknown_node():

    resolver = ExpressionResolver(None)

    node = DummyNode("unknown")

    with pytest.raises(NotImplementedError):
        resolver.resolve(node)