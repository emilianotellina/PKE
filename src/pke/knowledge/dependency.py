from dataclasses import dataclass


@dataclass
class DependencyKnowledge:

    type: str

    name: str

    source: str = ""