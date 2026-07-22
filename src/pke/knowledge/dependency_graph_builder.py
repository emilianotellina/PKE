from .dependency_graph import DependencyGraph



class DependencyGraphBuilder:



    def build(
        self,
        project
    ):

        graph = DependencyGraph()



        for package in project.packages:

            for file in package.files:

                for function in file.symbols:


                    graph.add_node(
                        function.name
                    )



                    for call in function.calls:


                        target = self._extract_target(
                            call
                        )


                        graph.add_dependency(
                            function.name,
                            target
                        )



        return graph



    def _extract_target(
        self,
        call
    ):

        if "(" in call:

            return call.split(
                "("
            )[0]


        return call