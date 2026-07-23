from .context_graph import ContextGraph



class ContextExpander:



    def expand(
        self,
        context
    ):


        graph = ContextGraph()



        for symbol in context.symbols:


            node = graph.get_or_create(
                symbol.name,
                symbol.type
            )


            #
            # Calls
            #

            for call in symbol.calls:


                graph.add_relation(

                    symbol.name,

                    "calls",

                    call

                )



            #
            # Called by
            #

            for caller in symbol.called_by:


                graph.add_relation(

                    symbol.name,

                    "called_by",

                    caller

                )



            #
            # Dependencies
            #

            for dependency in symbol.dependencies:


                graph.add_relation(

                    symbol.name,

                    "depends_on",

                    dependency

                )



            #
            # Side effects
            #

            for effect in symbol.side_effects:


                graph.add_relation(

                    symbol.name,

                    "side_effect",

                    effect

                )



        return graph