from dataclasses import dataclass, field



@dataclass
class SemanticCallNode:

    name: str


    calls: list[str] = field(
        default_factory=list
    )


    callers: list[str] = field(
        default_factory=list
    )


    kind: str = "internal"


    side_effects: list[str] = field(
        default_factory=list
    )



@dataclass
class SemanticCallEdge:

    source: str

    target: str

    kind: str

    receiver: str = ""



class SemanticCallGraph:


    def __init__(self):

        self.nodes = {}

        self.edges = []



    def add_function(
        self,
        name
    ):

        if name not in self.nodes:

            self.nodes[name] = SemanticCallNode(
                name=name
            )


        return self.nodes[name]



    def add_call(
        self,
        source,
        target,
        kind,
        receiver=""
    ):

        source_node = self.add_function(
            source
        )


        target_node = self.add_function(
            target
        )


        edge = SemanticCallEdge(
            source=source,
            target=target,
            kind=kind,
            receiver=receiver
        )


        self.edges.append(
            edge
        )


        if target not in source_node.calls:

            source_node.calls.append(
                target
            )


        if source not in target_node.callers:

            target_node.callers.append(
                source
            )


        target_node.kind = kind


        return target_node



#
# compatibilità vecchia API
#

CallGraphNode = SemanticCallNode

CallGraph = SemanticCallGraph