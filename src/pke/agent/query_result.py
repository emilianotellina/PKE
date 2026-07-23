from dataclasses import dataclass, field



@dataclass
class QueryResult:


    task: str

    target: str | None

    context: object


    functions: list = field(
        default_factory=list
    )


    files: list = field(
        default_factory=list
    )


    packages: list = field(
        default_factory=list
    )


    dependencies: list = field(
        default_factory=list
    )


    side_effects: list = field(
        default_factory=list
    )


    risks: list = field(
        default_factory=list
    )


    impact: object | None = None



    def agent_context(
        self
    ):

        return self.context



    def to_dict(
        self
    ):

        return {

            "task":
                self.task,

            "target":
                self.target,

            "impact":
                (
                    self.impact.to_dict()

                    if self.impact

                    else None
                )

        }