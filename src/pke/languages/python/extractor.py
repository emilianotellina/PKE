import ast

from pke.knowledge import (
    Function,
    Parameter,
    Symbol
)


class PythonExtractor:


    def extract(self, tree):

        symbols = []


        for node in ast.walk(tree):


            if isinstance(
                node,
                ast.FunctionDef
            ):

                symbols.append(
                    self._function(node)
                )


            elif isinstance(
                node,
                ast.ClassDef
            ):

                symbols.append(
                    Symbol(
                        name=node.name,
                        type="CLASS"
                    )
                )


        return symbols



    def _function(self, node):

        parameters = []


        for arg in node.args.args:

            parameters.append(
                Parameter(
                    name=arg.arg
                )
            )


        return Function(
            name=node.name,
            type="FUNCTION",
            parameters=parameters
        )