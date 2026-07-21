from pke.csr.semantic_visitor import SemanticVisitor

from .project import Project
from .package import Package
from .file import SourceFile
from .function import Function, Parameter


class KnowledgeCSRVisitor(SemanticVisitor):


    def __init__(self):

        self.project = None

        self.current_package = None

        self.current_file = None

        self.current_function = None



    def visit_project(
        self,
        node
    ):

        self.project = Project(
            name=node.name
        )


    def visit_package(
        self,
        node
    ):

        package = Package(
            name=node.name
        )

        self.project.packages.append(
            package
        )

        self.current_package = package



    def visit_file(
        self,
        node
    ):

        file = SourceFile(
            name=node.name
        )

        self.current_package.files.append(
            file
        )

        self.current_file = file



    def visit_function(
        self,
        node
    ):

        function = Function(
            name=node.name
        )

        self.current_file.symbols.append(
            function
        )

        self.current_function = function



    def visit_parameter(
        self,
        node
    ):

        parameter = Parameter(
            name=node.name
        )

        self.current_function.parameters.append(
            parameter
        )

    def visit_statement(
        self,
        node
    ):

        if node.type == "assignment":

            self.current_function.variables.append(
                node.type
            )


        if node.type == "return":

            self.current_function.returns.append(
                node.type
            )