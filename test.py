from pke.parser import PythonAdapter

from pke.csr.semantic_walker import SemanticWalker

from pke.knowledge import (
    KnowledgeCSRVisitor,
    KnowledgeGraphExporter,
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



visitor = KnowledgeCSRVisitor()



SemanticWalker(
    graph,
    visitor
).walk()



file = KnowledgeGraphExporter().export(
    visitor.project,
    "out/knowledge.json"
)



print(
    file
)