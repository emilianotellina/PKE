from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class CSRNode:

    type: str

    name: str

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    attributes: dict = field(
        default_factory=dict
    )

    children: list = field(
        default_factory=list
    )


    def add_child(
        self,
        node
    ):

        self.children.append(
            node
        )