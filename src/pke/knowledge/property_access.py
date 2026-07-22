from dataclasses import dataclass, field


@dataclass
class PropertyAccessKnowledge:

    expression: str

    object: str

    property: str


    consumers: list = field(
        default_factory=list
    )