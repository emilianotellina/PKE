class CSRGraph:


    def __init__(self):

        self.nodes = {}



    def add(
        self,
        node
    ):

        self.nodes[node.id] = node



    def find(
        self,
        name
    ):

        return [
            n
            for n in self.nodes.values()
            if n.name == name
        ]