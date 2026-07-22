class FunctionProducer:


    def generate(
        self,
        function
    ):

        lines = []


        lines.append(
            f"# {function.name}"
        )


        lines.append("")


        if function.signature:

            lines.append(
                "## Signature"
            )

            lines.append("")

            lines.append(
                function.signature
            )

            lines.append("")



        if function.parameters:

            lines.append(
                "## Parameters"
            )

            lines.append("")


            for parameter in function.parameters:

                lines.append(
                    f"- {parameter.name}"
                )


            lines.append("")



        if function.variables:

            lines.append(
                "## Variables"
            )

            lines.append("")


            for variable in function.variables:

                lines.append(
                    f"- {variable}"
                )


            lines.append("")



        if function.calls:

            lines.append(
                "## Calls"
            )

            lines.append("")


            for call in function.calls:

                lines.append(
                    f"- {call}"
                )


            lines.append("")



        if function.returns:

            lines.append(
                "## Returns"
            )

            lines.append("")


            for value in function.returns:

                lines.append(
                    f"- {value}"
                )


        return "\n".join(
            lines
        )