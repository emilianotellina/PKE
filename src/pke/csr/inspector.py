from .query import CSRQuery


class CSRInspector:


    def __init__(
        self,
        graph
    ):

        self.query = CSRQuery(graph)


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

                                lines.append(
                                    f"          {statement.type}"
                                )

        return "\n".join(lines)