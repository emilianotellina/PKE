from pke.context.context_engine import ContextEngine
from pke.context.context import AIContext, SymbolContext
from pke.context.impact_builder import ImpactBuilder
from pke.context.impact_analyzer import ImpactAnalyzer

from pke.csr.semantic_walker import SemanticWalker
from pke.knowledge.csr_visitor import KnowledgeCSRVisitor

from .query_analyzer import QueryAnalyzer
from .risk_analyzer import RiskAnalyzer
from .query_result import QueryResult
from .context_cache import ContextCache
from .project_fingerprint import ProjectFingerprint


class ContextQuery:


    def __init__(
        self,
        project,
        cache=None
    ):

        self.csr = project

        self.engine = ContextEngine()

        self.analyzer = QueryAnalyzer()

        self.risk_analyzer = RiskAnalyzer()

        self.impact_builder = ImpactBuilder()

        self.impact_analyzer = ImpactAnalyzer()

        self.cache = cache or ContextCache()

        self.fingerprint = ProjectFingerprint()



    def execute(
        self,
        task,
        target=None,
        options=None
    ):


        if options is None:

            options = {}



        fingerprint = self.fingerprint.calculate(
            self.csr
        )



        cached = self.cache.get(
            fingerprint,
            task,
            target,
            options
        )


        if cached is not None:

            return cached



        visitor = KnowledgeCSRVisitor(
            self.csr
        )


        walker = SemanticWalker(
            self.csr,
            visitor
        )


        walker.walk()


        knowledge_project = visitor.project



        engine_context = self.engine.build(

            project=knowledge_project,

            target=target,

            budget=options.get(
                "max_tokens",
                300
            )

        )



        analysis = self.analyzer.analyze(
            knowledge_project,
            target
        )



        risks = []


        if options.get(
            "include_risks",
            True
        ):

            risks = self.risk_analyzer.analyze(
                knowledge_project,
                target
            )



        symbols = []


        for function in analysis["functions"]:


            if hasattr(
                function,
                "name"
            ):

                symbols.append(

                    SymbolContext(

                        name=function.name,

                        calls=function.calls,

                        dependencies=[

                            item.name

                            for item

                            in function.dependencies

                        ],

                        side_effects=[

                            item.expression

                            for item

                            in function.side_effects

                        ]

                    )

                )


            else:

                symbols.append(

                    SymbolContext(

                        name=function

                    )

                )



        context = AIContext(

            project=knowledge_project.name,

            functions=analysis["functions"],

            files=analysis["files"],

            packages=analysis["packages"],

            dependencies=analysis["dependencies"],

            side_effects=analysis["side_effects"],

            risks=risks,

            symbols=symbols,

            architecture={

                "task":

                    task,

                "target":

                    target,

                "llm_context":

                    engine_context

            }

        )



        #
        # Il prompt finale è quello prodotto dal ContextEngine
        #

        context.llm_context = engine_context["prompt"]



        impact_graph = self.impact_builder.build(
            knowledge_project
        )


        impact = self.impact_analyzer.analyze(
            impact_graph,
            target
        )



        result = QueryResult(

            task=task,

            target=target,

            context=context,

            engine_context=engine_context,

            functions=analysis["functions"],

            files=analysis["files"],

            packages=analysis["packages"],

            dependencies=analysis["dependencies"],

            side_effects=analysis["side_effects"],

            risks=risks,

            impact=impact

        )



        self.cache.put(

            fingerprint,

            task,

            target,

            options,

            result

        )


        return result