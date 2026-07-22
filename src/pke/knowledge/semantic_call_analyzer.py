class SemanticCallAnalyzer:


    def __init__(
        self,
        call_graph
    ):

        self.graph = call_graph



    def propagate_effects(
        self
    ):

        changed = True


        while changed:

            changed = False


            for node in self.graph.nodes.values():

                effects = set(
                    node.side_effects
                )


                for call in node.calls:

                    target = self.graph.nodes.get(
                        call
                    )


                    if target is None:
                        continue


                    for effect in target.side_effects:

                        if effect not in effects:

                            effects.add(
                                effect
                            )

                            changed = True



                node.side_effects = list(
                    effects
                )



        return self.graph



    def entry_points(
        self
    ):

        result = []


        for node in self.graph.nodes.values():

            if not node.callers:

                result.append(
                    node.name
                )


        return result



    def leaf_functions(
        self
    ):

        result = []


        for node in self.graph.nodes.values():

            if not node.calls:

                result.append(
                    node.name
                )


        return result



    def fan_out(
        self
    ):

        return {
            node.name: len(node.calls)
            for node in self.graph.nodes.values()
        }



    def fan_in(
        self
    ):

        return {
            node.name: len(node.callers)
            for node in self.graph.nodes.values()
        }