from pke.csr.node import CSRNode


class PackageNode(CSRNode):

    def __init__(
        self,
        name
    ):

        super().__init__(
            type="package",
            name=name
        )