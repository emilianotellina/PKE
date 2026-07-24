from .context_item import ContextItem
from .retrieval_matcher import RetrievalMatcher



class ContextFusion:



    def __init__(
        self
    ):

        self.matcher = RetrievalMatcher()



    def fuse(
        self,
        context,
        graph=None,
        risks=None,
        retrieval_context=None,
        impact=None,
        metrics=None
    ):


        items = []



        for symbol in context.symbols:



            item = ContextItem(
                symbol=symbol
            )



            #
            # Graph score
            #

            if graph is not None:


                if symbol.name in getattr(

                    graph,

                    "nodes",

                    {}

                ):


                    item.graph_score = 100



            #
            # Retrieval score
            #

            if retrieval_context is not None:


                item.retrieval_score = self.matcher.score(

                    symbol,

                    retrieval_context

                )


                item.metadata["retrieval"] = retrieval_context



            #
            # Risk score
            #

            if risks:


                item.risk_score = self._risk_score(

                    symbol,

                    risks

                )


                item.metadata["risks"] = risks



            #
            # Impact score
            #

            if impact:


                item.impact_score = self._impact_score(

                    symbol,

                    impact

                )


                item.metadata["impact"] = impact



            #
            # Metrics
            #

            if metrics:


                item.metadata["metrics"] = metrics



            item.update_score()



            items.append(
                item
            )



        return items



    def _risk_score(
        self,
        symbol,
        risks
    ):


        score = 0


        for risk in risks:


            value = str(
                risk
            ).lower()


            if "critical" in value:

                score += 20


            elif "side effect" in value:

                score += 10


            elif "dependency" in value:

                score += 5


            elif "fan-out" in value:

                score += 5


            elif "fan-in" in value:

                score += 5


            else:

                score += 5



        return score



    def _impact_score(
        self,
        symbol,
        impact
    ):


        if not isinstance(
            impact,
            dict
        ):

            return 0



        affected = impact.get(

            "affected",

            []

        )


        risk_level = impact.get(

            "risk_level",

            "low"

        )



        score = 0



        count = len(
            affected
        )



        if count > 10:

            score += 30


        elif count >= 4:

            score += 20


        elif count > 0:

            score += 10



        if risk_level == "high":

            score += 20


        elif risk_level == "medium":

            score += 10



        return score