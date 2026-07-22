from dataclasses import dataclass, field



@dataclass
class ArchitectureNode:

    name: str

    type: str

    metadata: dict = field(
        default_factory=dict
    )



@dataclass
class ArchitectureEdge:

    source: str

    target: str

    relation: str



@dataclass
class ArchitectureGraph:


    nodes: dict[str, ArchitectureNode] = field(
        default_factory=dict
    )


    edges: list[ArchitectureEdge] = field(
        default_factory=list
    )



    def add_node(
        self,
        name,
        node_type,
        metadata=None
    ):

        if name not in self.nodes:

            self.nodes[name] = ArchitectureNode(
                name=name,
                type=node_type,
                metadata=metadata or {}
            )


        return self.nodes[name]



    def add_edge(
        self,
        source,
        target,
        relation
    ):

        edge = ArchitectureEdge(
            source=source,
            target=target,
            relation=relation
        )


        if edge not in self.edges:

            self.edges.append(
                edge
            )



    def outgoing(
        self,
        node
    ):

        return [
            edge
            for edge in self.edges
            if edge.source == node
        ]



    def incoming(
        self,
        node
    ):

        return [
            edge
            for edge in self.edges
            if edge.target == node
        ]