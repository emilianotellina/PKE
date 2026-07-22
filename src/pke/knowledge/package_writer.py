from pathlib import Path



class PackageWriter:


    def __init__(
        self,
        output_path
    ):

        self.output_path = Path(
            output_path
        )



    def write(
        self,
        package
    ):

        path = (
            self.output_path
            /
            "Package.md"
        )


        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        files = []

        functions = []

        side_effects = set()

        external_dependencies = set()



        for file in package.files:

            files.append(
                file.name
            )


            for symbol in file.symbols:

                functions.append(
                    symbol.name
                )


                for effect in symbol.side_effects:

                    side_effects.add(
                        effect.type
                    )


                for dependency in symbol.dependencies:

                    external_dependencies.add(
                        dependency.type
                    )



        content = []


        content.append(
            f"# Package: {package.name}\n"
        )


        content.append(
            "\n## Files\n"
        )


        if files:

            for file in files:

                content.append(
                    f"- {file}\n"
                )

        else:

            content.append(
                "- None\n"
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
Files:
{len(files)}

Functions:
{len(functions)}

External Dependencies:
{len(external_dependencies)}
"""
        )


        path.write_text(
            "".join(content),
            encoding="utf-8"
        )


        return path