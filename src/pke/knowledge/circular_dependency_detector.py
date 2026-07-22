from .circular_dependency import DependencyCycle



class CircularDependencyDetector:



    def detect(
        self,
        package_metrics
    ):


        cycles = []

        visited = set()

        stack = []



        for name in package_metrics.keys():

            self._visit(
                name,
                package_metrics,
                visited,
                stack,
                cycles
            )



        return cycles



    def _visit(
        self,
        node,
        graph,
        visited,
        stack,
        cycles
    ):


        if node in stack:


            index = stack.index(
                node
            )


            cycle = stack[index:] + [
                node
            ]


            if cycle not in [
                c.nodes for c in cycles
            ]:

                cycles.append(
                    DependencyCycle(
                        cycle
                    )
                )


            return



        if node in visited:

            return



        visited.add(
            node
        )


        stack.append(
            node
        )



        current = graph.get(
            node
        )


        if current:


            for dependency in current.dependencies:


                self._visit(
                    dependency,
                    graph,
                    visited,
                    stack,
                    cycles
                )



        stack.pop()