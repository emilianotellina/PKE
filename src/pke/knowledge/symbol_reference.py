from dataclasses import dataclass, field



@dataclass
class SymbolReference:


    name: str


    calls: list[str] = field(
        default_factory=list
    )


    called_by: list[str] = field(
        default_factory=list
    )


    references: list[str] = field(
        default_factory=list
    )