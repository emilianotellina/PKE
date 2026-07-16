from pke.csr.node import CSRNode


class ProjectNode(CSRNode):

    def __init__(
        self,
        name
    ):

        super().__init__(
            type="project",
            name=name
        )