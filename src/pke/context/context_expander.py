from .context_graph import ContextGraph



class ContextExpander:



    def expand(
        self,
        context,
        strategy=None
    ):


        graph = ContextGraph()



        max_depth = None

        expand_callers = True

        expand_dependencies = True

        include_side_effects = True



        if strategy is not None:


            max_depth = getattr(
                strategy,
                "max_depth",
                None
            )


            expand_callers = getattr(
                strategy,
                "expand_callers",
                True
            )


            expand_dependencies = getattr(
                strategy,
                "expand_dependencies",
                True
            )


            include_side_effects = getattr(
                strategy,
                "include_side_effects",
                True
            )



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

                if expand_callers:


                    graph.add_relation(

                        call,

                        "called_by",

                        symbol.name

                    )



            #
            # Existing called_by
            #

            if expand_callers:


                for caller in symbol.called_by:


                    graph.add_relation(

                        symbol.name,

                        "called_by",

                        caller

                    )



            #
            # Dependencies
            #

            if expand_dependencies:


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

            if include_side_effects:


                for effect in symbol.side_effects:


                    graph.add_relation(

                        symbol.name,

                        "side_effect",

                        effect

                    )



        return graph