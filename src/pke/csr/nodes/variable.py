from .declaration import DeclarationNode


class VariableNode(DeclarationNode):

    def __init__(
        self,
        name,
        data_type=None
    ):

        super().__init__(
            node_type="variable",
            name=name,
            attributes={
                "data_type": data_type
            }
        )

class ParameterNode(DeclarationNode):

    def __init__(
        self,
        name,
        data_type=None
    ):

        super().__init__(
            node_type="parameter",
            name=name,
            attributes={
                "data_type": data_type
            }
        )