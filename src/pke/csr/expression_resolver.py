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

        if hasattr(
            node,
            "attributes"
        ):

            return str(
                node.attributes["value"]
            )


        return str(
            node.value
        )


    def _resolve_call(self, node):

        target = self.query.target(node)

        function_name = self.resolve(
            target
        )


        arguments = self.query.arguments(
            node
        )


        arguments_text = ", ".join(
            self.resolve(argument)
            for argument in arguments
        )


        return (
            f"{function_name}"
            f"({arguments_text})"
        )


    def _resolve_assignment(self, node):

        target = self.query.target(node)

        value = self.query.value(node)


        target_text = self.resolve(
            target
        )

        value_text = self.resolve(
            value
        )


        return (
            f"{target_text}"
            f" = "
            f"{value_text}"
        )


    def _resolve_return(self, node):

        value = self.query.value(
            node
        )


        value_text = self.resolve(
            value
        )


        return (
            f"return "
            f"{value_text}"
        )


    def _resolve_unknown(self, node):

        raise NotImplementedError(
            f"Unsupported node type: {node.type}"
        )
        
    def _resolve_binary_operation(
        self,
        node
    ):

        left = self.query.left(
            node
        )

        right = self.query.right(
            node
        )


        left_text = self.resolve(
            left
        )

        right_text = self.resolve(
            right
        )


        operator = node.attributes["operator"]


        return (
            f"{left_text} "
            f"{operator} "
            f"{right_text}"
        )

    def _resolve_attribute_access(
        self,
        node
    ):

        obj = self.query.object(
            node
        )


        obj_text = self.resolve(
            obj
        )


        return (
            f"{obj_text}."
            f"{node.name}"
        )
        
    def _resolve_index_access(
        self,
        node
    ):

        target = self.query.target(
            node
        )

        index = self.query.index(
            node
        )


        target_text = self.resolve(
            target
        )

        index_text = self.resolve(
            index
        )


        return (
            f"{target_text}"
            f"[{index_text}]"
        )