from pke.csr.node import CSRNode


class SymbolNode(CSRNode):

    def __init__(
        self,
        name,
        symbol_type
    ):

        super().__init__(
            type=symbol_type,
            name=name
        )