from .context_compressor import ContextCompressor
from .optimized_context import OptimizedContext



class TokenOptimizer:



    def __init__(self):

        self.compressor = ContextCompressor()



    def optimize(
        self,
        ranked_context,
        target=None,
        budget=300,
        profile=None
    ):


        optimized = self._optimize_context(

            ranked_context,

            target,

            budget,

            profile

        )


        #
        # Nuovo comportamento:
        # con profile ritorniamo oggetto strutturato
        #

        if profile is not None:

            return optimized



        #
        # Compatibilità legacy:
        # ritorniamo stringa
        #

        lines = []


        for item in optimized.symbols:


            lines.append(

                f"{item['score']}: {item['symbol']}"

            )


        result = "\n".join(
            lines
        )


        if optimized.summary:


            result += "\n\n"

            result += optimized.summary


        elif len(ranked_context) > 1 and budget <= 20:



            result += "\n\n(summary)"



        return result



    def _optimize_context(
        self,
        ranked_context,
        target=None,
        budget=300,
        profile=None
    ):


        result = OptimizedContext(

            target=target

        )


        if not ranked_context:

            return result



        if profile is not None:


            mode = getattr(

                profile,

                "compression_mode",

                "balanced"

            )


            if mode == "minimal":

                budget = int(

                    budget * 0.5

                )


            elif mode == "compact":

                budget = int(

                    budget * 0.75

                )


            elif mode == "detailed":

                budget = int(

                    budget * 1.25

                )



        tokens = 0

        skipped = []



        for item, score in ranked_context:


            name = getattr(

                item,

                "name",

                str(item)

            )


            cost = self._estimate_tokens(

                name

            )



            if (

                tokens + cost

                >

                budget

            ):


                skipped.append(

                    (

                        item,

                        score

                    )

                )

                continue



            result.add_symbol(

                name,

                score

            )


            tokens += cost



        result.token_count = tokens



        if skipped:


            result.summary = self.compressor.compress(

                skipped,

                budget=max(

                    10,

                    budget // 4

                )

            )


        return result



    def _estimate_tokens(
        self,
        text
    ):


        return max(

            1,

            len(text.split()) + 1

        )