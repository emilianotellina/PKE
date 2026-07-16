from .declaration import DeclarationNode


class ClassNode(DeclarationNode):

    def __init__(
        self,
        name,
        base_classes=None
    ):

        super().__init__(
            node_type="class",
            name=name,
            attributes={
                "base_classes": base_classes or []
            }
        )