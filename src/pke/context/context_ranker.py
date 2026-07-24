import heapq

from .graph_traversal import GraphTraversal
from .retrieval_matcher import RetrievalMatcher



class ContextRanker:



    def __init__(self):

        self.traversal = GraphTraversal()

        self.matcher = RetrievalMatcher()



    def rank(
        self,
        context,
        target,
        graph=None,
        risks=None,
        retrieved_documents=None,
        profile=None
    ):


        if graph is not None:

            return self._rank_graph(

                context,

                target,

                graph,

                risks,

                retrieved_documents,

                profile

            )


        return self._rank_legacy(

            context,

            target,

            risks,

            retrieved_documents,

            profile

        )



    def _rank_graph(
        self,
        context,
        target,
        graph,
        risks=None,
        retrieved_documents=None,
        profile=None
    ):


        costs = self._calculate_costs(
            graph,
            target
        )


        result = []



        for symbol in context.symbols:


            if symbol.name in costs:


                score = self._score(
                    costs[symbol.name]
                )


                score = self._apply_risk_bonus(
                    symbol,
                    score,
                    risks,
                    profile
                )


                score = self._apply_retrieval_bonus(
                    symbol,
                    score,
                    retrieved_documents
                )


                result.append(
                    (
                        symbol,
                        score
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



        return max(

            10,

            int(
                100 / (1 + cost)
            )

        )



    def _rank_legacy(
        self,
        context,
        target,
        risks=None,
        retrieved_documents=None,
        profile=None
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

                self._apply_retrieval_bonus(

                    target_symbol,

                    self._apply_risk_bonus(

                        target_symbol,

                        100,

                        risks,

                        profile

                    ),

                    retrieved_documents

                )

            )

        )



        for symbol in context.symbols:


            for call in symbol.calls:


                called_name = call.split("(")[0]


                if called_name == target:


                    score = self._apply_risk_bonus(

                        symbol,

                        80,

                        risks,

                        profile

                    )


                    score = self._apply_retrieval_bonus(

                        symbol,

                        score,

                        retrieved_documents

                    )


                    result.append(

                        (
                            symbol,
                            score
                        )

                    )



        return self._remove_duplicates(
            result
        )



    def _apply_risk_bonus(
        self,
        symbol,
        score,
        risks,
        profile=None
    ):


        if not risks:

            return score



        name = getattr(
            symbol,
            "name",
            str(symbol)
        )



        bonus = 0



        for risk in risks:


            if name in risk:


                if "critical" in risk:

                    bonus = 20


                elif "side effect" in risk:

                    bonus = 10


                elif "dependency" in risk:

                    bonus = 5


                else:

                    bonus = 5



        if profile is not None and getattr(
            profile,
            "prioritize_risks",
            False
        ):


            weight = getattr(
                profile,
                "risk_weight",
                1.0
            )


            bonus = int(
                bonus * weight
            )



        return score + bonus



    def _apply_retrieval_bonus(
        self,
        symbol,
        score,
        retrieved_documents
    ):


        if not retrieved_documents:

            return score



        retrieval_score = self.matcher.score(

            symbol,

            retrieved_documents

        )



        if retrieval_score <= 0:

            return score



        return score + min(

            50,

            retrieval_score * 5

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