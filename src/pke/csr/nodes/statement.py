from pke.csr.node import CSRNode


class StatementNode(CSRNode):

    def __init__(
        self,
        statement_type
    ):

        super().__init__(
            type=statement_type,
            name=statement_type
        )