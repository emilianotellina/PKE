from pke.csr.node import CSRNode


class BodyNode(CSRNode):

    def __init__(self):

        super().__init__(
            type="body",
            name="body"
        )


    def add_statement(
        self,
        statement
    ):

        self.children.append(
            statement
        )