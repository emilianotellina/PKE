from .context_graph import ContextGraph



class ContextExpander:


    def expand(
        self,
        context
    ):


        graph = ContextGraph()



        for symbol in context.symbols:


            graph.get_or_create(
                symbol.name,
                symbol.type
            )



        for symbol in context.symbols:



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
                # Reverse relation
                #

                graph.add_relation(

                    call,

                    "called_by",

                    symbol.name

                )



            #
            # Existing called_by
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


                dependency_name = getattr(

                    dependency,

                    "name",

                    str(dependency)

                )


                graph.add_relation(

                    symbol.name,

                    "depends_on",

                    dependency_name

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