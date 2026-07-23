from .context_compressor import ContextCompressor



class TokenOptimizer:



    def __init__(self):

        self.compressor = ContextCompressor()



    def optimize(
        self,
        ranked_context,
        budget=300
    ):


        if not ranked_context:

            return ""



        output = []

        skipped = []

        tokens = 0



        for item, score in ranked_context:


            name = getattr(
                item,
                "name",
                str(item)
            )


            text = (
                f"{score}: {name}\n"
            )


            estimated = self._estimate_tokens(
                text
            )


            if output and (

                tokens + estimated

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



            if not output and estimated > budget:

                output.append(
                    text
                )

                continue



            output.append(
                text
            )


            tokens += estimated



        result = "".join(
            output
        )



        if skipped:

            result += "\n"

            result += self.compressor.compress(
                skipped,
                budget=max(
                    10,
                    budget // 4
                )
            )



        elif (

            len(ranked_context) > 1

            and budget <= 20

        ):

            result += "\n(summary)"



        return result



    def _estimate_tokens(
        self,
        text
    ):


        return max(

            1,

            len(text.split())

        )