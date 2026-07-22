from .call_graph import SemanticCallGraph
from .call_classifier import CallClassifier



class SemanticCallGraphBuilder:


    def __init__(self):

        self.classifier = CallClassifier()



    def build(
        self,
        project
    ):

        graph = SemanticCallGraph()


        functions = self._collect_functions(
            project
        )


        project_functions = {
            function.name
            for function in functions
        }


        #
        # crea nodi funzione
        #
        for function in functions:

            node = graph.add_function(
                function.name
            )


            for effect in function.side_effects:

                if effect.type not in node.side_effects:

                    node.side_effects.append(
                        effect.type
                    )



        #
        # crea relazioni
        #
        for function in functions:

            for call in function.call_details:


                kind = self.classifier.classify(
                    call,
                    project_functions
                )


                graph.add_call(
                    function.name,
                    call.target,
                    kind,
                    call.receiver
                )


        return graph



    def _collect_functions(
        self,
        project
    ):

        functions = []


        for package in project.packages:

            for file in package.files:

                for symbol in file.symbols:

                    functions.append(
                        symbol
                    )


        return functions