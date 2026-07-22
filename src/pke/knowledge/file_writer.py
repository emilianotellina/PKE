from pathlib import Path



class FileWriter:


    def __init__(
        self,
        output_path
    ):

        self.output_path = Path(
            output_path
        )



    def write(
        self,
        file
    ):

        path = (
            self.output_path
            /
            "File.md"
        )


        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        functions = []

        calls = set()

        side_effects = set()

        complexity = 0



        for symbol in file.symbols:

            functions.append(
                symbol.name
            )


            for call in symbol.calls:

                calls.add(
                    call
                )


            for effect in symbol.side_effects:

                side_effects.add(
                    effect.type
                )


            complexity += (
                symbol.complexity
            )



        content = []


        content.append(
            f"# File: {file.name}\n"
        )


        content.append(
            "\n## Functions\n"
        )


        if functions:

            for function in functions:

                content.append(
                    f"- {function}\n"
                )

        else:

            content.append(
                "- None\n"
            )



        content.append(
            "\n## Calls\n"
        )


        if calls:

            for call in sorted(calls):

                content.append(
                    f"- {call}\n"
                )

        else:

            content.append(
                "- None\n"
            )



        content.append(
            "\n## Side Effects\n"
        )


        if side_effects:

            for effect in sorted(side_effects):

                content.append(
                    f"- {effect}\n"
                )

        else:

            content.append(
                "- None\n"
            )



        content.append(
            "\n## Metrics\n"
        )


        content.append(
            f"""
Functions:
{len(functions)}

Total Complexity:
{complexity}
"""
        )


        path.write_text(
            "".join(content),
            encoding="utf-8"
        )


        return path