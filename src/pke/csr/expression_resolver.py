from __future__ import annotations


class ExpressionResolver:
    """
    Resolves CSR expression nodes into a textual representation.

    The resolver operates exclusively through CSRQuery and never
    accesses the graph directly.
    """

    def __init__(self, query):
        self.query = query

    def resolve(self, node):
        """
        Resolve a CSR node.

        Returns None when the node is None.
        """

        if node is None:
            return None

        method_name = f"_resolve_{node.type}"

        method = getattr(
            self,
            method_name,
            self._resolve_unknown,
        )

        return method(node)

    def _resolve_identifier(self, node):
        """
        Temporary implementation.
        """

        return node.name

    def _resolve_unknown(self, node):
        raise NotImplementedError(
            f"Unsupported node type: {node.type}"
        )