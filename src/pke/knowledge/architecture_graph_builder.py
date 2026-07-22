from .architecture_graph import ArchitectureGraph



class ArchitectureGraphBuilder:


    def __init__(self):

        self.graph = ArchitectureGraph()



    def build(
        self,
        functions
    ):

        #
        # creo nodi funzione
        #

        for function in functions:

            self.graph.add_node(
                function.name,
                "FUNCTION"
            )


        #
        # creo archi chiamate
        #

        for function in functions:


            for call in function.call_details:


                if call.resolved_type == "internal":

                    target_type = "FUNCTION"


                elif call.resolved_type == "builtin":

                    target_type = "BUILTIN"


                else:

                    target_type = "EXTERNAL"



                target_name = call.target


                if call.receiver:

                    target_name = (
                        call.receiver
                        + "."
                        + call.target
                    )



                self.graph.add_node(
                    target_name,
                    target_type,
                    {
                        "module": call.module
                    }
                )


                self.graph.add_edge(
                    function.name,
                    target_name,
                    "CALLS"
                )


        return self.graph