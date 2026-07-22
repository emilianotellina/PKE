from .context_builder import ContextBuilder
from .context_ranker import ContextRanker
from .token_optimizer import TokenOptimizer



class ContextEngine:


    def __init__(self):

        self.builder = ContextBuilder()

        self.ranker = ContextRanker()

        self.optimizer = TokenOptimizer()



    def build(
        self,
        project,
        target,
        call_graph=None,
        dependency_graph=None,
        metrics=None,
        budget=300
    ):


        context = self.builder.build(
            project,
            call_graph,
            dependency_graph,
            metrics
        )



        ranked = self.ranker.rank(
            context,
            target
        )



        optimized = self.optimizer.optimize(
            ranked,
            budget
        )



        return {

            "target":
                target,

            "context":
                optimized,

            "ranking":
                [
                    {

                        "symbol":
                            getattr(
                                item,
                                "name",
                                str(item)
                            ),

                        "score":
                            score

                    }

                    for item,score in ranked
                ]

        }