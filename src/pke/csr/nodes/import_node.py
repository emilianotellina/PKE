from .declaration import DeclarationNode


class ImportNode(DeclarationNode):

    def __init__(
        self,
        module
    ):

        super().__init__(
            node_type="import",
            name=module
        )