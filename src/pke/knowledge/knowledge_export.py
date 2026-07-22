from dataclasses import dataclass, field



@dataclass
class KnowledgeExport:


    nodes: list = field(
        default_factory=list
    )


    edges: list = field(
        default_factory=list
    )


    def add_node(
        self,
        node
    ):

        self.nodes.append(
            node
        )


    def add_edge(
        self,
        edge
    ):

        self.edges.append(
            edge
        )