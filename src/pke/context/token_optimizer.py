class TokenOptimizer:



    def optimize(
        self,
        ranked_context,
        budget=300
    ):


        output = []

        tokens = 0



        for item,score in ranked_context:


            name = getattr(
                item,
                "name",
                str(item)
            )


            text = (
                f"{score}: {name}\n"
            )


            estimated = len(
                text.split()
            )


            if (
                tokens + estimated
                >
                budget
            ):

                break



            output.append(
                text
            )


            tokens += estimated



        return "".join(
            output
        )