from pke.parser.python_adapter import PythonAdapter
from pke.csr import SemanticWalker
from pke.csr import SemanticVisitor


class DummyVisitor(SemanticVisitor):

    def __init__(self):

        self.events = []


    def visit_project(self, node):

        self.events.append(
            ("project", node.name)
        )


    def visit_package(self, node):

        self.events.append(
            ("package", node.name)
        )


    def visit_file(self, node):

        self.events.append(
            ("file", node.name)
        )


    def visit_function(self, node):

        self.events.append(
            ("function", node.name)
        )


def test_semantic_walker():

    graph = PythonAdapter().parse(
        """
def login(user):
    return user
"""
    )

    visitor = DummyVisitor()

    walker = SemanticWalker(
        graph,
        visitor
    )

    walker.walk()

    assert (
        "project",
        "python_project"
    ) in visitor.events

    assert (
        "package",
        "root"
    ) in visitor.events

    assert (
        "file",
        "module.py"
    ) in visitor.events

    assert (
        "function",
        "login"
    ) in visitor.events