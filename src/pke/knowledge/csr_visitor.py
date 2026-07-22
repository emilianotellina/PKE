from pke.csr.semantic_visitor import SemanticVisitor
from pke.csr.query import CSRQuery
from pke.csr.expression_resolver import ExpressionResolver

from .project import Project
from .package import Package
from .file import SourceFile
from .function import Function, Parameter
from .variable import VariableKnowledge
from .side_effect import SideEffectKnowledge
from .call import CallKnowledge
from .dependency import DependencyKnowledge


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



    #
    # VARIABLES
    #

    def _is_parameter(
        self,
        name
    ):

        for parameter in self.current_function.parameters:

            if parameter.name == name:
                return True


        return False



    def _get_variable(
        self,
        name
    ):

        for variable in self.current_function.variable_details:

            if variable.name == name:
                return variable


        variable = VariableKnowledge(
            name=name
        )


        self.current_function.variable_details.append(
            variable
        )


        if name not in self.current_function.variables:

            self.current_function.variables.append(
                name
            )


        return variable



    def _register_variable_read(
        self,
        name,
        consumer
    ):

        if self._is_parameter(name):

            return


        variable = self._get_variable(
            name
        )


        if consumer not in variable.consumers:

            variable.consumers.append(
                consumer
            )



    #
    # CALL ANALYSIS
    #

    def _analyze_call_arguments(
        self,
        call,
        expression
    ):

        arguments = self.query.arguments(
            call
        )


        for argument in arguments:

            argument_name = self.resolver.resolve(
                argument
            )


            if argument_name is None:
                continue


            self._register_variable_read(
                argument_name,
                expression
            )



    def _extract_call_knowledge(
        self,
        call
    ):

        target = self.query.target(
            call
        )


        if target is None:

            return None


        target_name = ""
        receiver = ""


        if target.type == "attribute_access":

            target_name = getattr(
                target,
                "name",
                ""
            )


            obj = self.query.object(
                target
            )


            if obj is not None:

                receiver = self.resolver.resolve(
                    obj
                )


        else:

            target_name = self.resolver.resolve(
                target
            )


        arguments = []


        for argument in self.query.arguments(call):

            value = self.resolver.resolve(
                argument
            )


            if value is not None:

                arguments.append(
                    value
                )


        kind = (
            "method_call"
            if receiver
            else "function_call"
        )


        return CallKnowledge(
            target=target_name,
            receiver=receiver,
            arguments=arguments,
            kind=kind
        )



    def _register_call_detail(
        self,
        call
    ):

        detail = self._extract_call_knowledge(
            call
        )


        if detail is None:
            return


        for existing in self.current_function.call_details:

            if (
                existing.target == detail.target
                and existing.receiver == detail.receiver
                and existing.arguments == detail.arguments
            ):

                return


        self.current_function.call_details.append(
            detail
        )



    #
    # SIDE EFFECTS
    #

    def _classify_side_effect(
        self,
        expression
    ):

        lower = expression.lower()


        if (
            ".save(" in lower
            or ".insert(" in lower
            or ".update(" in lower
            or ".delete(" in lower
            or ".execute(" in lower
        ):

            return "DATABASE_WRITE"


        if (
            ".write(" in lower
            or ".write_text(" in lower
            or "open(" in lower
        ):

            return "FILE_WRITE"


        if (
            "requests." in lower
            or "http." in lower
            or "client." in lower
            or "send(" in lower
            or "post(" in lower
            or "get(" in lower
        ):

            return "NETWORK_CALL"


        if (
            "cache.set(" in lower
            or "cache.delete(" in lower
            or "cache.invalidate(" in lower
        ):

            return "CACHE_MUTATION"


        return None



    def _register_side_effect(
        self,
        expression
    ):

        effect_type = self._classify_side_effect(
            expression
        )


        if effect_type is None:
            return


        effect = SideEffectKnowledge(
            type=effect_type,
            expression=expression
        )


        for existing in self.current_function.side_effects:

            if (
                existing.type == effect.type
                and existing.expression == effect.expression
            ):

                return


        self.current_function.side_effects.append(
            effect
        )



    #
    # DEPENDENCIES
    #

    def _classify_dependency(
        self,
        expression
    ):

        lower = expression.lower()


        if (
            "db." in lower
            or ".save(" in lower
            or ".insert(" in lower
            or ".update(" in lower
        ):

            return "DATABASE"


        if (
            "cache." in lower
        ):

            return "CACHE"


        if (
            "send_email" in lower
            or "mail" in lower
        ):

            return "EMAIL"


        if (
            "http" in lower
            or "request" in lower
        ):

            return "NETWORK"


        return None



    def _register_dependency(
        self,
        expression
    ):

        dependency_type = self._classify_dependency(
            expression
        )


        if dependency_type is None:
            return


        dependency = DependencyKnowledge(
            type=dependency_type,
            name=expression
        )


        for existing in self.current_function.dependencies:

            if (
                existing.type == dependency.type
                and existing.name == dependency.name
            ):

                return


        self.current_function.dependencies.append(
            dependency
        )



    def _register_call(
        self,
        call
    ):

        expression = self.resolver.resolve(
            call
        )


        if expression is None:
            return


        if expression not in self.current_function.calls:

            self.current_function.calls.append(
                expression
            )


        self._register_call_detail(
            call
        )


        self._analyze_call_arguments(
            call,
            expression
        )


        self._register_side_effect(
            expression
        )


        self._register_dependency(
            expression
        )


        target = self.query.target(
            call
        )


        if target is not None:

            target_name = self.resolver.resolve(
                target
            )


            if (
                target_name
                and target_name not in self.current_function.call_targets
            ):

                self.current_function.call_targets.append(
                    target_name
                )



    #
    # STATEMENTS
    #

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

                variable_name = self.resolver.resolve(
                    left
                )


                variable = self._get_variable(
                    variable_name
                )


                if node not in variable.writes:

                    variable.writes.append(
                        node
                    )


                if right is not None:

                    if right.type == "call":

                        expression = self.resolver.resolve(
                            right
                        )


                        if expression not in variable.producers:

                            variable.producers.append(
                                expression
                            )


                        self._register_call(
                            right
                        )



        elif node.type == "call":

            self._register_call(
                node
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


                self._register_variable_read(
                    expression,
                    "return"
                )