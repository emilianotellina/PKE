from pke.parser import PythonAdapter

from pke.knowledge import (
    KnowledgeCSRVisitor,
    SemanticCallGraphBuilder,
    SemanticCallAnalyzer,
    ArchitectureMetrics,
)

from pke.csr.semantic_walker import SemanticWalker



source = """

def create_user(user):

    save_user(user)

    send_email(user)



def save_user(user):

    db.save(user)



def send_email(user):

    print(user)

"""



graph = PythonAdapter().parse(
    source
)



visitor = KnowledgeCSRVisitor()


SemanticWalker(
    graph,
    visitor
).walk()



call_graph = SemanticCallGraphBuilder().build(
    visitor.project
)



SemanticCallAnalyzer(
    call_graph
).propagate_effects()



metrics = ArchitectureMetrics(
    call_graph
)



result = metrics.calculate()



for name, value in result.items():

    print(name)

    print(
        "fan_in:",
        value.fan_in
    )

    print(
        "fan_out:",
        value.fan_out
    )

    print(
        "instability:",
        value.instability
    )

    print(
        "complexity:",
        value.complexity
    )

    print(
        "criticality:",
        value.criticality
    )

    print()