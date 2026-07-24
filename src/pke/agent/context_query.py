from pke.context.context_engine import ContextEngine
from pke.context.context import AIContext, SymbolContext
from pke.context.impact_builder import ImpactBuilder
from pke.context.impact_analyzer import ImpactAnalyzer
from pke.context.context_strategy import ContextStrategyAnalyzer

from pke.knowledge.retriever import KnowledgeRetriever
from pke.knowledge.semantic_retriever import SemanticRetriever

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
        cache=None,
        repository=None
    ):

        self.csr = project

        self.repository = repository

        self.engine = ContextEngine()

        self.analyzer = QueryAnalyzer()

        self.risk_analyzer = RiskAnalyzer()

        self.impact_builder = ImpactBuilder()

        self.impact_analyzer = ImpactAnalyzer()

        self.cache = cache or ContextCache()

        self.fingerprint = ProjectFingerprint()

        self.strategy_analyzer = ContextStrategyAnalyzer()

        self.retriever = None

        self.semantic_retriever = None



        if repository is not None:

            self.retriever = KnowledgeRetriever(
                repository
            )


            self.semantic_retriever = SemanticRetriever(
                repository
            )



    def execute(
        self,
        task,
        target=None,
        options=None
    ):


        if options is None:

            options = {}



        strategy = self.strategy_analyzer.analyze(
            task
        )



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



        knowledge_project = self._load_knowledge_project()



        retrieval_context = self._retrieve_documents(
            task,
            options
        )



        engine_context = self._build_engine_context(
            knowledge_project,
            target,
            options,
            retrieval_context,
            strategy
        )



        analysis = self._analyze(
            knowledge_project,
            target
        )



        risks = self._build_risks(
            knowledge_project,
            target,
            options
        )



        symbols = self._build_symbols(
            analysis
        )



        context = self._build_ai_context(
            knowledge_project,
            task,
            target,
            engine_context,
            analysis,
            risks,
            symbols
        )



        impact = self._build_impact(
            knowledge_project,
            target
        )



        result = self._build_result(
            task,
            target,
            context,
            engine_context,
            analysis,
            risks,
            impact,
            retrieval_context
        )



        self.cache.put(
            fingerprint,
            task,
            target,
            options,
            result
        )


        return result



    def _retrieve_documents(
        self,
        task,
        options
    ):


        if self.retriever is None:

            return None



        if not options.get(
            "use_retrieval",
            True
        ):

            return None



        context = self.retriever.retrieve(
            task
        )


        if self.semantic_retriever is not None:

            context = self.semantic_retriever.expand(
                context
            )


        return context



    def _build_engine_context(
        self,
        project,
        target,
        options,
        retrieval_context,
        strategy
    ):


        return self.engine.build(

            project=project,

            target=target,

            budget=options.get(
                "max_tokens",
                300
            ),

            retrieved_documents=retrieval_context,

            strategy=strategy

        )



    def _analyze(
        self,
        project,
        target
    ):

        return self.analyzer.analyze(
            project,
            target
        )



    def _build_risks(
        self,
        project,
        target,
        options
    ):


        if not options.get(
            "include_risks",
            True
        ):

            return []


        return self.risk_analyzer.analyze(
            project,
            target
        )



    def _build_symbols(
        self,
        analysis
    ):


        symbols = []


        for function in analysis["functions"]:


            if hasattr(
                function,
                "name"
            ):


                symbols.append(

                    SymbolContext(

                        name=function.name,

                        calls=getattr(
                            function,
                            "calls",
                            []
                        ),

                        dependencies=[

                            item.name

                            for item

                            in getattr(
                                function,
                                "dependencies",
                                []
                            )

                        ],

                        side_effects=[

                            item.expression

                            for item

                            in getattr(
                                function,
                                "side_effects",
                                []
                            )

                        ]

                    )

                )


            else:

                symbols.append(

                    SymbolContext(
                        name=function
                    )

                )


        return symbols



    def _build_ai_context(
        self,
        project,
        task,
        target,
        engine_context,
        analysis,
        risks,
        symbols
    ):


        context = AIContext(

            project=project.name,

            functions=analysis["functions"],

            files=analysis["files"],

            packages=analysis["packages"],

            dependencies=analysis["dependencies"],

            side_effects=analysis["side_effects"],

            risks=risks,

            symbols=symbols,

            architecture={

                "task": task,

                "target": target,

                "llm_context": engine_context

            }

        )


        context.llm_context = engine_context["prompt"]


        return context



    def _build_impact(
        self,
        project,
        target
    ):


        graph = self.impact_builder.build(
            project
        )


        return self.impact_analyzer.analyze(
            graph,
            target
        )



    def _build_result(
        self,
        task,
        target,
        context,
        engine_context,
        analysis,
        risks,
        impact,
        retrieval_context
    ):


        return QueryResult(

            task=task,

            target=target,

            context=context,

            engine_context=engine_context,

            retrieval_context=retrieval_context,

            functions=analysis["functions"],

            files=analysis["files"],

            packages=analysis["packages"],

            dependencies=analysis["dependencies"],

            side_effects=analysis["side_effects"],

            risks=risks,

            impact=impact

        )



    def _load_knowledge_project(
        self
    ):


        if self.repository is not None:


            project_name = getattr(
                self.csr,
                "name",
                None
            )


            if project_name is not None:


                knowledge_project = self.repository.load_project(
                    project_name
                )


                if knowledge_project is not None:

                    return knowledge_project



        visitor = KnowledgeCSRVisitor(
            self.csr
        )


        walker = SemanticWalker(
            self.csr,
            visitor
        )


        walker.walk()


        return visitor.project