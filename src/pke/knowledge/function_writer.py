from pathlib import Path



class FunctionWriter:


    def __init__(
        self,
        output_path
    ):

        self.output_path = Path(
            output_path
        )



    def write(
        self,
        function,
        metrics=None
    ):

        path = self.output_path / (
            function.name + ".md"
        )


        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        content = []


        content.append(
            f"# Function: {function.name}\n"
        )


        content.append(
            "## Calls\n"
        )


        if function.calls:

            for call in function.calls:

                content.append(
                    f"- {call}\n"
                )

        else:

            content.append(
                "- None\n"
            )


        content.append(
            "\n## Call Targets\n"
        )


        if function.call_targets:

            for target in function.call_targets:

                content.append(
                    f"- {target}\n"
                )

        else:

            content.append(
                "- None\n"
            )


        content.append(
            "\n## Side Effects\n"
        )


        if function.side_effects:

            for effect in function.side_effects:

                content.append(
                    f"- {effect.type}\n"
                )

        else:

            content.append(
                "- None\n"
            )


        content.append(
            "\n## Dependencies\n"
        )


        if function.dependencies:

            for dependency in function.dependencies:

                content.append(
                    f"- {dependency.type}\n"
                )

        else:

            content.append(
                "- None\n"
            )


        if metrics is not None:

            content.append(
                "\n## Metrics\n"
            )


            content.append(
                f"""
Fan in:
{metrics.fan_in}

Fan out:
{metrics.fan_out}

Instability:
{metrics.instability}

Complexity:
{metrics.complexity}

Criticality:
{metrics.criticality}
"""
            )


        path.write_text(
            "".join(content),
            encoding="utf-8"
        )


        return path