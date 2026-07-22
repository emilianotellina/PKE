from dataclasses import dataclass, field



@dataclass
class CallGraphNode:

    name: str

    calls: list[str] = field(
        default_factory=list
    )



@dataclass
class CallGraph:


    nodes: dict[str, CallGraphNode] = field(
        default_factory=dict
    )


    def add_function(
        self,
        name
    ):

        if name not in self.nodes:

            self.nodes[name] = CallGraphNode(
                name=name
            )


        return self.nodes[name]


    def add_call(
        self,
        source,
        target
    ):

        source_node = self.add_function(
            source
        )


        self.add_function(
            target
        )


        if target not in source_node.calls:

            source_node.calls.append(
                target
            )