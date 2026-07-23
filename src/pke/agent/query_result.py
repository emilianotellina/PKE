from dataclasses import dataclass, field



@dataclass
class QueryResult:


    task: str

    target: str | None

    context: object


    engine_context: dict | None = None



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



    def optimized_context(
        self
    ):

        if self.engine_context is None:

            return None


        return self.engine_context.get(
            "context"
        )



    def prompt(
        self
    ):

        if self.engine_context is None:

            return None


        return self.engine_context.get(
            "prompt"
        )



    def ranking(
        self
    ):

        if self.engine_context is None:

            return []


        return self.engine_context.get(
            "ranking",
            []
        )



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
                ),


            "engine_context":

                {

                    "prompt":

                        self.prompt(),


                    "ranking":

                        self.ranking(),


                    "context":

                        (

                            self.optimized_context().to_dict()

                            if self.optimized_context()

                            else None

                        )

                }

        }