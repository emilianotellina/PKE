from pke.csr.node import CSRNode


class DeclarationNode(CSRNode):

    def __init__(
        self,
        node_type,
        name,
        attributes=None
    ):

        super().__init__(
            type=node_type,
            name=name,
            attributes=attributes or {}
        )