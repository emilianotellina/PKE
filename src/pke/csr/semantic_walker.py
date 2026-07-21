from .query import CSRQuery


class SemanticWalker:

    def __init__(self, graph, visitor):

        self.query = CSRQuery(graph)
        self.visitor = visitor


    def walk(self):

        for project in self.query.projects():

            self.visitor.visit_project(project)

            for package in self.query.packages(project):

                self.visitor.visit_package(package)

                for file in self.query.files(package):

                    self.visitor.visit_file(file)

                    for function in self.query.functions(file):

                        self.visitor.visit_function(function)

                        for parameter in self.query.parameters(function):

                            self.visitor.visit_parameter(parameter)

                        body = self.query.body(function)

                        if body is None:
                            continue

                        self.visitor.visit_body(body)

                        for statement in self.query.statements(body):

                            self.visitor.visit_statement(statement)