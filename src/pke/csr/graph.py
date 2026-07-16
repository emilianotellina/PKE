from .edge import CSREdge


class CSRGraph:


    def __init__(self):

        self.nodes = {}

        self.edges = []



    def add(
        self,
        node
    ):

        self.nodes[node.id] = node



    def connect(
        self,
        source,
        target,
        relation,
        attributes=None
    ):

        edge = CSREdge(
            source=source.id,
            target=target.id,
            relation=relation,
            attributes=attributes or {}
        )


        self.edges.append(
            edge
        )


        return edge



    def find(
        self,
        name
    ):

        return [
            n
            for n in self.nodes.values()
            if n.name == name
        ]



    def outgoing(
        self,
        node,
        relation=None
    ):

        return [
            e
            for e in self.edges
            if e.source == node.id
            and (
                relation is None
                or e.relation == relation
            )
        ]



    def incoming(
        self,
        node,
        relation=None
    ):

        return [
            e
            for e in self.edges
            if e.target == node.id
            and (
                relation is None
                or e.relation == relation
            )
        ]