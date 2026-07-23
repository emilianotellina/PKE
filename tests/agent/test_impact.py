from pke.agent.impact import ImpactAnalyzer
from pke.parser.python_adapter import PythonAdapter
from pke.knowledge.csr_visitor import KnowledgeCSRVisitor
from pke.csr.semantic_walker import SemanticWalker



def test_impact_analysis():


    graph = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)


def authenticate(user):

    return True
"""
    )


    visitor = KnowledgeCSRVisitor(
        graph
    )


    walker = SemanticWalker(
        graph,
        visitor
    )


    walker.walk()


    analyzer = ImpactAnalyzer()


    report = analyzer.analyze(

        visitor.project,

        "login"

    )


    assert report.target == "login"

    assert "authenticate" in report.calls