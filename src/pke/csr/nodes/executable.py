from .declaration import DeclarationNode


class ExecutableNode(DeclarationNode):

    def __init__(
        self,
        node_type,
        name,
        attributes=None
    ):

        super().__init__(
            node_type=node_type,
            name=name,
            attributes=attributes
        )

        self.body = None


    def set_body(
        self,
        body
    ):

        self.body = body