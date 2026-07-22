from dataclasses import dataclass



@dataclass
class DependencyCycle:


    nodes: list[str]



    def __str__(
        self
    ):

        return " -> ".join(
            self.nodes
        )