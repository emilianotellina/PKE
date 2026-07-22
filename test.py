from pathlib import Path
import shutil


from pke.parser import PythonAdapter

from pke.csr.semantic_walker import SemanticWalker

from pke.knowledge import (
    KnowledgeCSRVisitor,
    SemanticCallGraphBuilder,
    SemanticCallAnalyzer,
    KnowledgeGenerator,
)



output = Path(
    "knowledge_output"
)


if output.exists():

    shutil.rmtree(
        output
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



call_graph = SemanticCallGraphBuilder().build(
    visitor.project
)



SemanticCallAnalyzer(
    call_graph
).propagate_effects()



KnowledgeGenerator(
    output
).generate(
    visitor.project,
    call_graph
)



for file in output.rglob(
    "*.md"
):

    print(
        file
    )