from dataclasses import dataclass, field


@dataclass
class VariableKnowledge:

    name: str


    assignments: list = field(
        default_factory=list
    )


    reads: list = field(
        default_factory=list
    )


    writes: list = field(
        default_factory=list
    )


    producers: list = field(
        default_factory=list
    )


    consumers: list = field(
        default_factory=list
    )