from pke.csr.node import CSRNode


class ProjectNode(CSRNode):

    def __init__(
        self,
        name
    ):

        super().__init__(
            "project",
            name
        )


class PackageNode(CSRNode):

    def __init__(
        self,
        name
    ):

        super().__init__(
            "package",
            name
        )


class FileNode(CSRNode):

    def __init__(
        self,
        name
    ):

        super().__init__(
            "file",
            name
        )