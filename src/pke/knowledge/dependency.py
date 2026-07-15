from dataclasses import dataclass


@dataclass
class Dependency:

    source: str

    target: str

    type: str