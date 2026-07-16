from .statement import StatementNode


class ControlFlowNode(StatementNode):

    def __init__(self, node_type):

        super().__init__(node_type)

class IfNode(ControlFlowNode):

    def __init__(self):

        super().__init__("if")

        self.condition = None

        self.then_block = BlockNode()

        self.else_block = None

class LoopNode(ControlFlowNode):

    def __init__(self, loop_type):

        super().__init__(loop_type)

        self.condition = None

        self.body = BlockNode()

class TryNode(ControlFlowNode):

    def __init__(self):

        super().__init__("try")

        self.try_block = BlockNode()

        self.catch_blocks = []

        self.finally_block = None