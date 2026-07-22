from pathlib import Path



class ProjectWriter:


    def __init__(
        self,
        output_path
    ):

        self.output_path = Path(
            output_path
        )



    def write(
        self,
        project,
        call_graph=None
    ):

        path = (
            self.output_path
            /
            "Project.md"
        )


        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        packages = []

        files = []

        functions = []

        side_effects = set()

        dependencies = set()



        for package in project.packages:

            packages.append(
                package.name
            )


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

                        dependencies.add(
                            dependency.type
                        )



        entries = []

        leaves = []



        #
        # SemanticCallGraph attuale
        #
        # Le metriche vengono calcolate
        # dall'analyzer, quindi leggiamo
        # i nodi già arricchiti
        #

        if call_graph is not None:

            for name, node in call_graph.nodes.items():

                if not node.callers:

                    entries.append(
                        name
                    )


                if not node.calls:

                    leaves.append(
                        name
                    )



        content = []



        content.append(
            f"# Project: {project.name}\n"
        )



        content.append(
            "\n## Packages\n"
        )


        for package in packages:

            content.append(
                f"- {package}\n"
            )



        content.append(
            "\n## Files\n"
        )


        for file in files:

            content.append(
                f"- {file}\n"
            )



        content.append(
            "\n## Functions\n"
        )


        for function in functions:

            content.append(
                f"- {function}\n"
            )



        content.append(
            "\n## Architecture\n"
        )


        content.append(
            "\nEntry Points:\n"
        )


        if entries:

            for entry in entries:

                content.append(
                    f"- {entry}\n"
                )

        else:

            content.append(
                "- None\n"
            )



        content.append(
            "\nLeaf Functions:\n"
        )


        if leaves:

            for leaf in leaves:

                content.append(
                    f"- {leaf}\n"
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
Packages:
{len(packages)}

Files:
{len(files)}

Functions:
{len(functions)}

Dependencies:
{len(dependencies)}
"""
        )



        path.write_text(
            "".join(content),
            encoding="utf-8"
        )


        return path