from pke.agent.context_query import ContextQuery
from pke.context.context_engine import ContextEngine
from pke.knowledge.project import Project



class FakeEngine(ContextEngine):


    def build(
        self,
        *args,
        **kwargs
    ):

        return {

            "target": "login",

            "context": None,

            "ranking": [],

            "structured": {},

            "prompt": "OPTIMIZED_CONTEXT_PROMPT",

            "graph": {}

        }



class FakeVisitor:


    def __init__(self):

        self.project = Project(
            name="test_project"
        )



class FakeWalker:


    def __init__(
        self,
        *args,
        **kwargs
    ):

        self.visitor = args[1]



    def walk(
        self
    ):

        self.visitor.project = Project(
            name="test_project"
        )



def test_context_query_uses_optimized_context(
    monkeypatch
):


    monkeypatch.setattr(

        "pke.agent.context_query.KnowledgeCSRVisitor",

        lambda csr: FakeVisitor()

    )


    monkeypatch.setattr(

        "pke.agent.context_query.SemanticWalker",

        FakeWalker

    )



    query = ContextQuery(
        None
    )


    query.engine = FakeEngine()



    query.analyzer.analyze = lambda *args, **kwargs: {

        "functions": [],

        "files": [],

        "packages": [],

        "dependencies": [],

        "side_effects": []

    }



    query.risk_analyzer.analyze = lambda *args, **kwargs: []



    result = query.execute(

        task="explain login",

        target="login"

    )



    assert (

        result.context.llm_context

        ==

        "OPTIMIZED_CONTEXT_PROMPT"

    )