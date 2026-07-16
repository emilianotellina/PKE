from .statement import StatementNode


class BlockNode(StatementNode):

    def __init__(self):

        super().__init__("block")


    def add(self, statement):

        self.children.append(statement)