from pke.parser import PythonAdapter

from pke.knowledge import (
    KnowledgeCSRVisitor,
    CallGraphBuilder,
    CallGraphAnalyzer
)

from pke.csr.semantic_walker import SemanticWalker



source = """

def create_user(user):

    db.save(user)

    send_email(user)



def send_email(user):

    print(user)

"""


graph = PythonAdapter().parse(
    source
)


visitor = KnowledgeCSRVisitor(
    graph
)


walker = SemanticWalker(
    graph,
    visitor
)

walker.walk()



call_graph = CallGraphBuilder().build(
    visitor.project
)



metrics = CallGraphAnalyzer(
    call_graph
).analyze()



print(
    "ENTRY POINTS:"
)

for item in metrics.entry_points:

    print(
        " -",
        item
    )



print(
    "\nLEAF FUNCTIONS:"
)

for item in metrics.leaf_functions:

    print(
        " -",
        item
    )



print(
    "\nFAN OUT:"
)

for name,value in metrics.fan_out.items():

    print(
        name,
        value
    )


print(
    "\nFAN IN:"
)

for name,value in metrics.fan_in.items():

    print(
        name,
        value
    )