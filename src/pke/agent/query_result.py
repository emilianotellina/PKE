from dataclasses import dataclass, field



@dataclass
class QueryResult:


    task: str

    target: str | None

    context: object


    engine_context: dict | None = None


    retrieval_context: object | None = None


    retrieved_documents: list = field(
        default_factory=list
    )


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



    def __post_init__(
        self
    ):


        if (

            self.retrieval_context is not None

            and

            not self.retrieved_documents

        ):

            self.retrieved_documents = (

                self.retrieval_context.documents

            )



        elif (

            self.retrieval_context is None

            and

            self.retrieved_documents

        ):

            self.retrieval_context = None

    def retrieved_context(
        self
    ):
        
        if self.retrieval_context is not None:

            return self.retrieval_context


        return self.retrieved_documents

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


        retrieval = None


        if self.retrieval_context is not None:


            if hasattr(
                self.retrieval_context,
                "to_dict"
            ):

                retrieval = self.retrieval_context.to_dict()



        elif self.retrieved_documents:


            retrieval = {

                "documents":
                    self.retrieved_documents

            }



        return {


            "task":

                self.task,


            "target":

                self.target,


            "impact":

                (
                    self.impact.to_dict()

                    if hasattr(
                        self.impact,
                        "to_dict"
                    )

                    else self.impact

                    if self.impact

                    else None
                ),


            "retrieved_documents":

                self.retrieved_documents,


            "retrieval":

                retrieval,


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