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



    def to_dict(
        self
    ):

        return {

            "name":
                self.name,

            "type":
                self.type,

            "calls":
                self.calls,

            "called_by":
                self.called_by,

            "dependencies":
                self.dependencies,

            "side_effects":
                self.side_effects,

            "metrics":
                self.metrics

        }



@dataclass
class AIContext:


    project: str = ""


    functions: list[str] = field(
        default_factory=list
    )


    files: list[str] = field(
        default_factory=list
    )


    packages: list[str] = field(
        default_factory=list
    )


    dependencies: list[str] = field(
        default_factory=list
    )


    side_effects: list[str] = field(
        default_factory=list
    )


    risks: list[str] = field(
        default_factory=list
    )


    symbols: list[SymbolContext] = field(
        default_factory=list
    )


    llm_context: object | None = None


    architecture: dict = field(
        default_factory=dict
    )



    def to_dict(
        self
    ):

        return {

            "project":
                self.project,

            "functions":
                self.functions,

            "files":
                self.files,

            "packages":
                self.packages,

            "dependencies":
                self.dependencies,

            "side_effects":
                self.side_effects,

            "risks":
                self.risks,

            "symbols":
                [
                    symbol.to_dict()
                    for symbol in self.symbols
                ],

            "llm_context":
                self.llm_context,

            "architecture":
                self.architecture

        }