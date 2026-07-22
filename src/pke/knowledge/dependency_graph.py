from dataclasses import dataclass, field



@dataclass
class DependencyNode:

    name: str

    dependencies: list[str] = field(
        default_factory=list
    )

    dependents: list[str] = field(
        default_factory=list
    )



@dataclass
class DependencyGraph:


    nodes: dict[str, DependencyNode] = field(
        default_factory=dict
    )



    def add_node(
        self,
        name
    ):

        if name not in self.nodes:

            self.nodes[name] = DependencyNode(
                name=name
            )


        return self.nodes[name]



    def add_dependency(
        self,
        source,
        target
    ):

        source_node = self.add_node(
            source
        )


        target_node = self.add_node(
            target
        )


        if target not in source_node.dependencies:

            source_node.dependencies.append(
                target
            )


        if source not in target_node.dependents:

            target_node.dependents.append(
                source
            )