from .context import SymbolContext



class ContextCompressor:



    def compress(
        self,
        items,
        budget=50
    ):


        if not items:

            return ""



        lines = [

            "(summary)"

        ]



        tokens = 1



        for item, score in items:


            name = getattr(
                item,
                "name",
                str(item)
            )


            line = (
                f"- {name} ({score})"
            )


            estimated = self._estimate_tokens(
                line
            )


            if (

                tokens + estimated

                >

                budget

            ):

                break



            lines.append(
                line
            )


            tokens += estimated



        if len(lines) == 1:

            return "(summary)"



        return "\n".join(
            lines
        )



    def _estimate_tokens(
        self,
        text
    ):


        return max(

            1,

            len(text.split())

        )