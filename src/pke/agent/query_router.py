from pke.csr.semantic_walker import SemanticWalker
from pke.knowledge.csr_visitor import KnowledgeCSRVisitor

from .intent import TaskIntentAnalyzer



class QueryRouter:


    def __init__(
        self
    ):

        self.intent_analyzer = TaskIntentAnalyzer()



    def _build_knowledge(
        self,
        graph
    ):

        visitor = KnowledgeCSRVisitor(
            graph
        )


        walker = SemanticWalker(
            graph,
            visitor
        )


        walker.walk()


        return visitor.project



    def find_symbol(
        self,
        graph,
        name
    ):

        project = self._build_knowledge(
            graph
        )


        result = []


        for package in project.packages:

            for file in package.files:

                for symbol in file.symbols:

                    if symbol.name == name:

                        result.append(
                            symbol
                        )


        return result



    def route(
        self,
        graph,
        task
    ):


        project = self._build_knowledge(
            graph
        )


        intent = self.intent_analyzer.analyze(
            task
        )


        candidates = []


        for package in project.packages:

            for file in package.files:

                for symbol in file.symbols:


                    name = symbol.name.lower()


                    score = 0


                    for keyword in intent.keywords:

                        if keyword in name:

                            score += 1



                    if intent.domain:

                        if intent.domain in name:

                            score += 1



                    if score > 0:

                        candidates.append(

                            {
                                "symbol":
                                    symbol.name,

                                "score":
                                    score /
                                    max(
                                        len(intent.keywords),
                                        1
                                    ),

                                "intent":
                                    intent.action

                            }

                        )


        candidates.sort(

            key=lambda item:
                item["score"],

            reverse=True

        )


        return candidates