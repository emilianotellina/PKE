from __future__ import annotations


class ExpressionResolver:
    """
    Resolves CSR expression nodes into textual representation.

    The resolver depends only on CSRQuery.
    """

    def __init__(self, query):
        self.query = query

    def resolve(self, node):

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

        return node.name

    def _resolve_literal(self, node):

        return str(node.value)

    def _resolve_call(self, node):
        """
        Resolve function calls.

        Example:

            authenticate(user)

        """

        target = self.query.target(node)

        function_name = self.resolve(target)

        arguments = self.query.arguments(node)

        arguments_text = ", ".join(
            self.resolve(argument)
            for argument in arguments
        )

        return f"{function_name}({arguments_text})"

    def _resolve_unknown(self, node):

        raise NotImplementedError(
            f"Unsupported node type: {node.type}"
        )