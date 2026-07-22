from dataclasses import dataclass


@dataclass
class SideEffectKnowledge:

    type: str

    target: str = ""

    expression: str = ""