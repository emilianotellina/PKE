from collections import defaultdict

from .edge import CSREdge
from .relation import RelationType


class CSRGraph:

    def __init__(self):

        self.nodes = {}

        self.edges = []

        self._outgoing = defaultdict(list)

        self._incoming = defaultdict(list)


    def add(self, node):

        self.nodes[node.id] = node

        return node


    def link(
        self,
        source,
        target,
        relation,
        **attributes
    ):

        edge = CSREdge(
            source.id,
            target.id,
            relation,
            attributes=attributes
        )

        self.edges.append(edge)

        self._outgoing[source.id].append(edge)

        self._incoming[target.id].append(edge)

        return edge


    def children(
        self,
        node,
        relation=None
    ):

        result = []

        for edge in self._outgoing[node.id]:

            if relation and edge.relation != relation:

                continue

            result.append(
                self.nodes[edge.target]
            )

        return result


    def parents(
        self,
        node,
        relation=None
    ):

        result = []

        for edge in self._incoming[node.id]:

            if relation and edge.relation != relation:

                continue

            result.append(
                self.nodes[edge.source]
            )

        return result


    def find(
        self,
        node_type=None,
        name=None
    ):

        result = []

        for node in self.nodes.values():

            if node_type and node.type != node_type:

                continue

            if name and node.name != name:

                continue

            result.append(node)

        return result