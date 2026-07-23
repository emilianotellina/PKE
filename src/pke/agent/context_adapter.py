from pke.context.optimized_context import OptimizedContext
from pke.context.prompt_document import PromptDocument



class ContextAdapter:



    def to_document(
        self,
        optimized
    ):


        if isinstance(
            optimized,
            str
        ):

            document = PromptDocument()

            document.add_section(
                "Context",
                optimized
            )

            return document



        document = PromptDocument()



        document.add_section(
            "Target",
            optimized.target
        )



        lines = []



        for item in optimized.symbols:


            lines.append(

                f"{item['score']}: {item['symbol']}"

            )



        document.add_section(

            "Selected Context",

            "\n".join(
                lines
            )

        )



        if optimized.summary:


            document.add_section(

                "Summary",

                optimized.summary

            )



        return document