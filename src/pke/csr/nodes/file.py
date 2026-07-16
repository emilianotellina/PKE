from pke.csr.node import CSRNode


class FileNode(CSRNode):

    def __init__(
        self,
        name,
        language=None
    ):

        super().__init__(
            type="file",
            name=name,
            attributes={
                "language": language
            }
        )