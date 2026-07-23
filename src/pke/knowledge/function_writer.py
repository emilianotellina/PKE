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
        metric=None,
        risk=None,
        impact=None
    ):


        path = (
            self.output_path
            /
            f"{function.name}.md"
        )


        self.output_path.mkdir(
            parents=True,
            exist_ok=True
        )


        content = []



        content.append(
            f"# Function: {function.name}\n"
        )



        content.append(
            "\n## Calls\n"
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
            "\n## Called By\n"
        )


        if function.called_by:

            for caller in function.called_by:

                content.append(
                    f"- {caller}\n"
                )

        else:

            content.append(
                "- None\n"
            )



        content.append(
            "\n## References\n"
        )


        if function.references:

            for reference in function.references:

                content.append(
                    f"- {reference}\n"
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
                    f"- {dependency.name}\n"
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



        if metric:


            content.append(
                "\n## Metrics\n"
            )


            for key, value in metric.items():

                content.append(
                    f"\n{key}:\n{value}\n"
                )



        if risk:


            content.append(
                "\n## Risk\n"
            )


            if isinstance(risk, list):

                for item in risk:

                    content.append(
                        f"- {item}\n"
                    )

            else:

                content.append(
                    f"- {risk}\n"
                )



        if impact:


            content.append(
                "\n## Impact\n"
            )


            if isinstance(impact, dict):

                affected = impact.get(
                    "affected",
                    []
                )

                if affected:

                    content.append(
                        "\nAffected Functions:\n"
                    )

                    for item in affected:

                        content.append(
                            f"- {item}\n"
                        )

                else:

                    content.append(
                        "- None\n"
                    )

            else:

                content.append(
                    f"- {impact}\n"
                )



        path.write_text(
            "".join(content),
            encoding="utf-8"
        )


        return path