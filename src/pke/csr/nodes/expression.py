from pke.csr.node import CSRNode


class ExpressionNode(CSRNode):

    def __init__(
        self,
        expression_type
    ):

        super().__init__(
            type=expression_type,
            name=expression_type
        )