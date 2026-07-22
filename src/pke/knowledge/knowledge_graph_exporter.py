import json

from pathlib import Path

from .knowledge_export import KnowledgeExport



class KnowledgeGraphExporter:



    def export(
        self,
        project,
        output
    ):


        export = KnowledgeExport()


        node_ids = {}

        counter = 0



        def register_node(
            node_type,
            name
        ):

            nonlocal counter


            if name in node_ids:

                return node_ids[name]


            counter += 1


            node_ids[name] = counter


            export.add_node(
                {
                    "id": counter,
                    "type": node_type,
                    "name": name
                }
            )


            return counter



        #
        # Prima fase:
        # registriamo tutti i simboli interni
        #

        register_node(
            "project",
            project.name
        )



        for package in project.packages:


            register_node(
                "package",
                package.name
            )


            for file in package.files:


                register_node(
                    "file",
                    file.name
                )


                for function in file.symbols:


                    register_node(
                        "function",
                        function.name
                    )



        #
        # Seconda fase:
        # costruzione struttura
        #

        for package in project.packages:


            package_id = node_ids[
                package.name
            ]


            export.add_edge(
                {
                    "source": node_ids[project.name],
                    "target": package_id,
                    "relation": "CONTAINS"
                }
            )



            for file in package.files:


                file_id = node_ids[
                    file.name
                ]


                export.add_edge(
                    {
                        "source": package_id,
                        "target": file_id,
                        "relation": "CONTAINS"
                    }
                )



                for function in file.symbols:


                    function_id = node_ids[
                        function.name
                    ]


                    export.add_edge(
                        {
                            "source": file_id,
                            "target": function_id,
                            "relation": "CONTAINS"
                        }
                    )



                    for call in function.calls:


                        target = call.split("(")[0]



                        if target in node_ids:

                            target_id = node_ids[target]


                        else:

                            target_id = register_node(
                                "external",
                                target
                            )



                        export.add_edge(
                            {
                                "source": function_id,
                                "target": target_id,
                                "relation": "CALLS"
                            }
                        )



        path = Path(
            output
        )


        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        path.write_text(
            json.dumps(
                {
                    "nodes": export.nodes,
                    "edges": export.edges
                },
                indent=2
            ),
            encoding="utf-8"
        )


        return path