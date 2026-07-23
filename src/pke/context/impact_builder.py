from .impact_graph import ImpactGraph



class ImpactBuilder:



    def build(
        self,
        project
    ):


        graph = ImpactGraph()



        if project is None:

            return graph



        for function in getattr(

            project,

            "functions",

            []

        ):



            name = getattr(

                function,

                "name",

                None

            )



            if name is None:

                continue



            graph.get_or_create(
                name
            )



            for call in getattr(

                function,

                "calls",

                []

            ):


                called = call.split("(")[0]


                graph.add_relation(

                    name,

                    "calls",

                    called

                )


                graph.add_relation(

                    called,

                    "called_by",

                    name

                )



            for dependency in getattr(

                function,

                "dependencies",

                []

            ):


                dependency_name = getattr(

                    dependency,

                    "name",

                    str(dependency)

                )


                graph.add_relation(

                    name,

                    "depends_on",

                    dependency_name

                )


                graph.add_relation(

                    dependency_name,

                    "dependency_of",

                    name

                )



        return graph