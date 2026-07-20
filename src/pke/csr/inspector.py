from pke.csr.query import CSRQuery
from pke.csr.expression_resolver import ExpressionResolver


class CSRInspector:

    def __init__(self, graph):

        self.graph = graph

        self.query = CSRQuery(
            graph
        )

        self.resolver = ExpressionResolver(
            self.query
        )


    def inspect(self):

        lines = []

        projects = self.query.projects()

        for project in projects:

            lines.append(
                f"Project: {project.name}"
            )

            for package in self.query.packages(project):

                lines.append(
                    f"  Package: {package.name}"
                )

                for file in self.query.files(package):

                    lines.append(
                        f"    File: {file.name}"
                    )

                    for function in self.query.functions(file):

                        lines.append(
                            f"      Function: {function.name}"
                        )

                        parameters = self.query.parameters(function)

                        for parameter in parameters:

                            lines.append(
                                f"        Parameter: {parameter.name}"
                            )

                        body = self.query.body(function)

                        if body:

                            lines.append(
                                "        Body:"
                            )

                            for statement in self.query.statements(body):

                                resolved = self.resolver.resolve(
                                    statement
                                )

                                if resolved:

                                    lines.append(
                                        f"          {resolved}"
                                    )

                                else:

                                    lines.append(
                                        f"          {statement.type}"
                                    )

        return "\n".join(lines)