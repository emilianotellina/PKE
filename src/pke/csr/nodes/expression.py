from pke.csr.node import CSRNode


class ExpressionNode(CSRNode):

    def __init__(
        self,
        expression_type,
        name=""
    ):

        super().__init__(
            type=expression_type,
            name=name or expression_type
        )

class IdentifierNode(ExpressionNode):

    def __init__(
        self,
        name
    ):

        super().__init__(
            "identifier",
            name
        )

class LiteralNode(ExpressionNode):

    def __init__(
        self,
        value
    ):

        super().__init__(
            "literal",
            str(value)
        )

        self.attributes["value"] = value

class BinaryOperationNode(ExpressionNode):

    def __init__(
        self,
        operator
    ):

        super().__init__(
            "binary_operation",
            operator
        )

        self.attributes["operator"] = operator

class CallNode(ExpressionNode):

    def __init__(self):

        super().__init__(
            "call"
        )

class AssignmentNode(ExpressionNode):

    def __init__(self):

        super().__init__(
            "assignment"
        )

class AttributeAccessNode(ExpressionNode):

    def __init__(
        self,
        attribute
    ):

        super().__init__(
            "attribute_access",
            attribute
        )

class IndexAccessNode(ExpressionNode):

    def __init__(self):

        super().__init__(
            "index_access"
        )

class AwaitNode(ExpressionNode):

    def __init__(self):

        super().__init__(
            "await"
        )