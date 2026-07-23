import heapq

from .graph_traversal import GraphTraversal



class ContextRanker:


    def __init__(self):

        self.traversal = GraphTraversal()



    def rank(
        self,
        context,
        target,
        graph=None
    ):


        if graph is not None:

            return self._rank_graph(
                context,
                target,
                graph
            )


        return self._rank_legacy(
            context,
            target
        )



    def _rank_graph(
        self,
        context,
        target,
        graph
    ):


        costs = self._calculate_costs(
            graph,
            target
        )


        result = []



        for symbol in context.symbols:


            if symbol.name in costs:


                result.append(

                    (

                        symbol,

                        self._score(
                            costs[symbol.name]
                        )

                    )

                )



        result.sort(

            key=lambda item: item[1],

            reverse=True

        )


        return result



    def _calculate_costs(
        self,
        graph,
        start
    ):


        queue = [

            (
                0,
                start
            )

        ]


        costs = {}



        while queue:


            cost, node = heapq.heappop(
                queue
            )



            if node in costs:

                continue



            costs[node] = cost



            for target, weight, relation in graph.get_weighted_relations(node):


                if target not in costs:


                    heapq.heappush(

                        queue,

                        (

                            cost + weight,

                            target

                        )

                    )



        return costs



    def _score(
        self,
        cost
    ):


        if cost == 0:

            return 100



        score = int(
            100 / (1 + cost)
        )



        return max(
            10,
            score
        )



    def _rank_legacy(
        self,
        context,
        target
    ):


        result = []


        target_symbol = None



        for symbol in context.symbols:


            if symbol.name == target:

                target_symbol = symbol

                break



        if target_symbol is None:

            return result



        result.append(

            (
                target_symbol,
                100
            )

        )



        for symbol in context.symbols:


            for call in symbol.calls:


                called_name = call.split("(")[0]


                if called_name == target:


                    result.append(

                        (
                            symbol,
                            80
                        )

                    )



        for dependency in target_symbol.dependencies:


            result.append(

                (
                    dependency,
                    70
                )

            )



        if target_symbol.side_effects:


            result.append(

                (
                    target_symbol,
                    60
                )

            )



        return self._remove_duplicates(
            result
        )



    def _remove_duplicates(
        self,
        items
    ):


        result = []

        seen = set()



        for item, score in items:


            key = (

                getattr(
                    item,
                    "name",
                    str(item)
                ),

                score

            )


            if key not in seen:

                seen.add(key)

                result.append(

                    (
                        item,
                        score
                    )

                )



        result.sort(

            key=lambda x: x[1],

            reverse=True

        )


        return result