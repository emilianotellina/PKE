from pke.csr.semantic_visitor import SemanticVisitor
from pke.csr.query import CSRQuery
from pke.csr.expression_resolver import ExpressionResolver

from .project import Project
from .package import Package
from .file import SourceFile
from .function import Function, Parameter


class KnowledgeCSRVisitor(SemanticVisitor):


    def __init__(
        self,
        graph=None
    ):

        self.project = None

        self.current_package = None

        self.current_file = None

        self.current_function = None


        if graph is not None:

            self.query = CSRQuery(
                graph
            )

            self.resolver = ExpressionResolver(
                self.query
            )

        else:

            self.query = None

            self.resolver = None



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

        if self.current_function is None:
            return


        if self.query is None:
            return


        if node.type == "assignment":

            left = self.query.left(
                node
            )


            right = self.query.right(
                node
            )


            if left is not None:

                variable = self.resolver.resolve(
                    left
                )

                if variable not in self.current_function.variables:

                    self.current_function.variables.append(
                        variable
                    )


                if right is not None:

                    expression = self.resolver.resolve(
                        right
                    )


                    if right.type == "call":

                        if expression not in self.current_function.calls:

                            self.current_function.calls.append(
                                expression
                            )


                        target = self.query.target(
                            right
                        )


                        if target is not None:

                            target_name = self.resolver.resolve(
                                target
                            )


                            if (
                                target_name
                                not in self.current_function.call_targets
                            ):

                                self.current_function.call_targets.append(
                                    target_name
                                )



        elif node.type == "return":

            value = self.query.value(
                node
            )


            if value is not None:

                expression = self.resolver.resolve(
                    value
                )


                if expression not in self.current_function.returns:

                    self.current_function.returns.append(
                        expression
                    )