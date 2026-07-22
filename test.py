from pke.parser import PythonAdapter

from pke.csr.semantic_walker import SemanticWalker

from pke.knowledge import (
    KnowledgeCSRVisitor,
    SemanticCallGraphBuilder,
    ArchitectureMetrics,
)

from pke.context import (
    ContextEngine,
)



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



visitor = KnowledgeCSRVisitor(
    graph
)



SemanticWalker(
    graph,
    visitor
).walk()



call_graph = SemanticCallGraphBuilder().build(
    visitor.project
)



metrics = ArchitectureMetrics(
    call_graph
).calculate()



result = ContextEngine().build(
    visitor.project,
    "save_user",
    call_graph,
    None,
    metrics,
    100
)



print(
    "TARGET:"
)

print(
    result["target"]
)


print()


print(
    "RANKING:"
)


for item in result["ranking"]:

    print(
        item
    )


print()


print(
    "CONTEXT:"
)


print(
    result["context"]
)