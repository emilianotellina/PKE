from dataclasses import dataclass, field



@dataclass
class CallGraphMetrics:


    fan_in: dict[str, int] = field(
        default_factory=dict
    )


    fan_out: dict[str, int] = field(
        default_factory=dict
    )


    entry_points: list[str] = field(
        default_factory=list
    )


    leaf_functions: list[str] = field(
        default_factory=list
    )


    cycles: list[list[str]] = field(
        default_factory=list
    )



class CallGraphAnalyzer:



    def __init__(
        self,
        graph
    ):

        self.graph = graph



    def analyze(
        self
    ):

        metrics = CallGraphMetrics()


        self._calculate_fan_out(
            metrics
        )


        self._calculate_fan_in(
            metrics
        )


        self._find_entry_points(
            metrics
        )


        self._find_leaf_functions(
            metrics
        )


        self._find_cycles(
            metrics
        )


        return metrics



    def _calculate_fan_out(
        self,
        metrics
    ):

        for name,node in self.graph.nodes.items():

            metrics.fan_out[name] = len(
                node.calls
            )



    def _calculate_fan_in(
        self,
        metrics
    ):

        for name in self.graph.nodes:

            metrics.fan_in[name] = 0



        for node in self.graph.nodes.values():

            for target in node.calls:

                if target in metrics.fan_in:

                    metrics.fan_in[target] += 1



    def _find_entry_points(
        self,
        metrics
    ):

        for name,value in metrics.fan_in.items():

            if value == 0:

                metrics.entry_points.append(
                    name
                )



    def _find_leaf_functions(
        self,
        metrics
    ):

        for name,value in metrics.fan_out.items():

            if value == 0:

                metrics.leaf_functions.append(
                    name
                )



    def _find_cycles(
        self,
        metrics
    ):

        visited = set()

        stack = []


        for node in self.graph.nodes:

            self._visit_cycle(
                node,
                visited,
                stack,
                metrics
            )



    def _visit_cycle(
        self,
        node,
        visited,
        stack,
        metrics
    ):

        if node in stack:

            index = stack.index(
                node
            )

            cycle = stack[index:] + [node]


            if cycle not in metrics.cycles:

                metrics.cycles.append(
                    cycle
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


        current = self.graph.nodes.get(
            node
        )


        if current:

            for target in current.calls:

                self._visit_cycle(
                    target,
                    visited,
                    stack,
                    metrics
                )


        stack.pop()