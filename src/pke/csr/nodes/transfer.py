from .statement import StatementNode


class TransferNode(StatementNode):

    def __init__(self, node_type):

        super().__init__(node_type)

class ReturnNode(TransferNode):

    def __init__(self):

        super().__init__("return")

        self.value = None

class BreakNode(TransferNode):

    def __init__(self):

        super().__init__("break")

class ContinueNode(TransferNode):

    def __init__(self):

        super().__init__("continue")

class ThrowNode(TransferNode):

    def __init__(self):

        super().__init__("throw")

        self.exception = None