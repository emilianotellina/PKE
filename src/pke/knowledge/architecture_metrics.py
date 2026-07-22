from dataclasses import dataclass, field



@dataclass
class FunctionMetrics:

    name: str

    fan_in: int = 0

    fan_out: int = 0

    instability: float = 0.0

    complexity: int = 0

    criticality: float = 0.0



class ArchitectureMetrics:


    def __init__(
        self,
        call_graph
    ):

        self.graph = call_graph



    def calculate(
        self
    ):

        result = {}


        fan_in = self._fan_in()

        fan_out = self._fan_out()


        for name,node in self.graph.nodes.items():


            metrics = FunctionMetrics(
                name=name
            )


            metrics.fan_in = fan_in[name]

            metrics.fan_out = fan_out[name]


            total = (
                metrics.fan_in
                +
                metrics.fan_out
            )


            if total > 0:

                metrics.instability = (
                    metrics.fan_out
                    /
                    total
                )


            metrics.complexity = (
                metrics.fan_out
                +
                metrics.fan_in
            )


            metrics.criticality = (
                metrics.complexity
                *
                (1 + len(node.side_effects))
            )


            result[name] = metrics


        return result



    def _fan_in(
        self
    ):

        return {
            node.name: len(node.callers)
            for node in self.graph.nodes.values()
        }



    def _fan_out(
        self
    ):

        return {
            node.name: len(node.calls)
            for node in self.graph.nodes.values()
        }