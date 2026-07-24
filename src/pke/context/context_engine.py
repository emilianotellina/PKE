from .context_builder import ContextBuilder
from .context_ranker import ContextRanker
from .token_optimizer import TokenOptimizer
from .context_formatter import ContextFormatter
from .context_expander import ContextExpander
from .context_fusion import ContextFusion
from .optimized_context import OptimizedContext



class ContextEngine:



    def __init__(self):

        self.builder = ContextBuilder()

        self.expander = ContextExpander()

        self.fusion = ContextFusion()

        self.ranker = ContextRanker()

        self.optimizer = TokenOptimizer()

        self.formatter = ContextFormatter()



    def build(
        self,
        project,
        target,
        call_graph=None,
        dependency_graph=None,
        metrics=None,
        risks=None,
        retrieved_documents=None,
        budget=300,
        strategy=None
    ):


        context = self.builder.build(
            project,
            call_graph,
            dependency_graph,
            metrics
        )



        graph = self.expander.expand(
            context,
            strategy
        )



        fused_context = self.fusion.fuse(

            context,

            graph=graph,

            risks=risks,

            retrieval_context=retrieved_documents,

            metrics=metrics

        )



        ranked = self.ranker.rank(

            fused_context,

            target

        )



        optimized = self._optimize(

            ranked,

            target,

            budget

        )



        prompt = self.formatter.format_optimized(
            optimized
        )



        if retrieved_documents:


            prompt = self._append_retrieved_documents(

                prompt,

                retrieved_documents

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

                    for item, score in ranked

                ],



            "fusion":

                [

                    item.to_dict()

                    for item in fused_context

                ],



            "structured":

                context.to_dict(),



            "prompt":

                prompt,



            "graph":

                graph.nodes,



            "retrieved_documents":

                retrieved_documents


        }


    def _append_retrieved_documents(
        self,
        prompt,
        documents
    ):

        section = [

            "\n",

            "## Retrieved Knowledge\n"

        ]


        for document in documents:


            if isinstance(
                document,
                dict
            ):


                name = document.get(

                    "name",

                    document.get(

                        "path",

                        document.get(

                            "file",

                            "unknown"

                        )

                    )

                )


            else:

                name = str(
                    document
                )



            section.append(

                f"- {name}\n"

            )



        return prompt + "".join(
            section
        )



    def _optimize(
        self,
        ranked,
        target,
        budget
    ):


        result = OptimizedContext(
            target=target
        )


        tokens = 0



        for item, score in ranked:


            name = getattr(
                item,
                "name",
                str(item)
            )


            cost = len(
                name.split()
            ) + 1



            if (

                tokens + cost

                >

                budget

            ):

                break



            result.add_symbol(
                name,
                score
            )


            tokens += cost



        result.token_count = tokens



        if len(result.symbols) < len(ranked):


            result.summary = self.optimizer.compressor.compress(

                ranked[len(result.symbols):],

                budget=max(

                    10,

                    budget // 4

                )

            )



        return result