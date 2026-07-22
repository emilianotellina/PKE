from .call_graph import CallGraph



class CallGraphBuilder:


    def __init__(self):

        self.graph = CallGraph()



    def build(
        self,
        project
    ):

        for package in project.packages:

            for file in package.files:

                for symbol in file.symbols:

                    self._process_function(
                        symbol
                    )


        return self.graph



    def _process_function(
        self,
        function
    ):

        self.graph.add_function(
            function.name
        )


        for call in function.call_details:

            target = self._resolve_target(
                call
            )


            graph.add_call(
                call.caller,
                call.target
            )



    def _resolve_target(
        self,
        call
    ):

        if call.receiver:

            return (
                call.receiver
                +
                "."
                +
                call.target
            )


        return call.target