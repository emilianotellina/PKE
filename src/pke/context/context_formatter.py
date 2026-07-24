from .context import AIContext
from .prompt_document import PromptDocument



class ContextFormatter:



    def format(
        self,
        context: AIContext,
        target=None,
        budget=300,
        ranked=None
    ):


        document = PromptDocument()



        if target:

            document.add_section(
                "Target",
                target
            )



        architecture_lines = []



        for key, value in context.architecture.items():

            architecture_lines.append(
                f"- {key}: {value}"
            )



        document.add_section(

            "Architecture",

            "\n".join(
                architecture_lines
            )

        )



        symbols = context.symbols



        if ranked is not None:


            symbols = [

                item

                for item,score

                in ranked

            ]



        function_lines = []



        for symbol in symbols:


            function_lines.append(
                symbol.name
            )



            if symbol.calls:

                function_lines.append(
                    "  Calls:"
                )


                for call in symbol.calls:

                    function_lines.append(
                        f"  - {call}"
                    )



            if symbol.called_by:

                function_lines.append(
                    "  Called by:"
                )


                for caller in symbol.called_by:

                    function_lines.append(
                        f"  - {caller}"
                    )



            if symbol.dependencies:

                function_lines.append(
                    "  Dependencies:"
                )


                for dependency in symbol.dependencies:

                    function_lines.append(
                        f"  - {dependency}"
                    )



            if symbol.side_effects:

                function_lines.append(
                    "  Side effects:"
                )


                for effect in symbol.side_effects:

                    function_lines.append(
                        f"  - {effect}"
                    )



            if symbol.metrics:

                function_lines.append(
                    "  Metrics:"
                )


                for key,value in symbol.metrics.items():

                    function_lines.append(
                        f"  - {key}: {value}"
                    )



            function_lines.append(
                ""
            )



        document.add_section(

            "Functions",

            "\n".join(
                function_lines
            )

        )



        document.add_section(

            "Dependencies",

            "\n".join(

                str(item)

                for item

                in context.dependencies

            )

        )



        document.add_section(

            "Side Effects",

            "\n".join(

                str(item)

                for item

                in context.side_effects

            )

        )



        document.add_section(

            "Risks",

            "\n".join(

                str(item)

                for item

                in context.risks

            )

        )



        return document



    def format_optimized(
        self,
        optimized,
        profile=None
    ):


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



        if profile is not None:


            detail_level = getattr(

                profile,

                "detail_level",

                "normal"

            )



            if detail_level == "high":


                document.add_section(

                    "Metrics",

                    "\n".join(

                        [

                            f"Token count: {optimized.token_count}",

                            f"Symbols count: {len(optimized.symbols)}"

                        ]

                    )

                )



        return document.render()