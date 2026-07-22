from dataclasses import dataclass, field



@dataclass
class SymbolContext:


    name: str


    type: str = "function"



    calls: list[str] = field(
        default_factory=list
    )


    called_by: list[str] = field(
        default_factory=list
    )


    dependencies: list[str] = field(
        default_factory=list
    )


    side_effects: list[str] = field(
        default_factory=list
    )


    metrics: dict = field(
        default_factory=dict
    )



@dataclass
class AIContext:


    project: str


    symbols: list[SymbolContext] = field(
        default_factory=list
    )


    architecture: dict = field(
        default_factory=dict
    )