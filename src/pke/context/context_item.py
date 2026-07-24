from dataclasses import dataclass
from dataclasses import field



@dataclass
class ContextItem:


    symbol: object


    graph_score: int = 0

    retrieval_score: int = 0

    risk_score: int = 0

    impact_score: int = 0

    metric_score: int = 0


    score: int = 0


    metadata: dict = field(
        default_factory=dict
    )



    def total_score(
        self
    ):

        return (

            self.graph_score

            + self.retrieval_score

            + self.risk_score

            + self.impact_score

            + self.metric_score

        )



    def update_score(
        self
    ):

        self.score = self.total_score()

        return self.score



    def add_score(
        self,
        category,
        value
    ):


        if not hasattr(
            self,
            f"{category}_score"
        ):

            raise ValueError(

                f"Unknown score category: {category}"

            )


        current = getattr(

            self,

            f"{category}_score"

        )


        setattr(

            self,

            f"{category}_score",

            current + value

        )


        return self.update_score()



    @property
    def name(
        self
    ):

        return getattr(

            self.symbol,

            "name",

            str(self.symbol)

        )



    @property
    def type(
        self
    ):

        return getattr(

            self.symbol,

            "type",

            "unknown"

        )



    def to_dict(
        self
    ):

        return {


            "symbol":

                self.name,


            "type":

                self.type,


            "graph_score":

                self.graph_score,


            "retrieval_score":

                self.retrieval_score,


            "risk_score":

                self.risk_score,


            "impact_score":

                self.impact_score,


            "metric_score":

                self.metric_score,


            "score":

                self.score,


            "metadata":

                self.metadata

        }



    def __repr__(
        self
    ):

        return (

            f"ContextItem("

            f"{self.name}, "

            f"score={self.score}"

            f")"

        )