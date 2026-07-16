from .declaration import DeclarationNode


class FunctionNode(DeclarationNode):

    def __init__(
        self,
        name,
        signature="",
        return_type=None
    ):

        super().__init__(
            node_type="function",
            name=name,
            attributes={
                "signature": signature,
                "return_type": return_type
            }
        )


    @property
    def signature(self):

        return self.attributes.get(
            "signature"
        )


    @property
    def return_type(self):

        return self.attributes.get(
            "return_type"
        )