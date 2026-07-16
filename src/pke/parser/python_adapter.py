import ast

from pke.csr import CSRBuilder

from pke.csr.relation import RelationType


from pke.csr.nodes import (
    FunctionNode,
    ReturnNode,
)


class PythonAdapter:


    def __init__(self):

        self.builder = CSRBuilder()



    def parse(
        self,
        source
    ):

        tree = ast.parse(
            source
        )

        self.visit(
            tree
        )

        return self.builder.graph



    def visit(
        self,
        node
    ):

        method = getattr(
            self,
            f"visit_{type(node).__name__}",
            None
        )


        if method:

            return method(node)


        for child in ast.iter_child_nodes(node):

            self.visit(child)

    def visit_Module(
        self,
        node
    ):

        for statement in node.body:

            self.visit(statement)

    def visit_FunctionDef(
        self,
        node
    ):

        function = self.builder.begin_function(
            node.name
        )


        for argument in node.args.args:

            self.builder.add_parameter(
                argument.arg
            )


        for statement in node.body:

            self.visit(statement)


        self.builder.end_function()

    def visit_Return(
        self,
        node
    ):

        result = self.builder.add_return()


        if node.value:

            value = self.visit(
                node.value
            )

            self.builder.graph.link(
                result,
                value,
                RelationType.VALUE
            )


        return result

    def visit_Name(
        self,
        node
    ):

        return self.builder.identifier(
            node.id
        )

    def visit_Constant(
        self,
        node
    ):

        return self.builder.literal(
            node.value
        )

    def visit_Call(
        self,
        node
    ):

        target = self.visit(
            node.func
        )


        args = []


        for argument in node.args:

            args.append(
                self.visit(argument)
            )


        return self.builder.call(
            target,
            args
        )

    def visit_Assign(
        self,
        node
    ):

        left = self.visit(
            node.targets[0]
        )


        right = self.visit(
            node.value
        )


        assignment = self.builder.assignment(
            left,
            right
        )


        body = self.builder.current_context()


        self.builder.graph.link(
            body,
            assignment,
            RelationType.CONTAINS
        )


        return assignment

    def visit_If(
        self,
        node
    ):

        condition = self.visit(
            node.test
        )


        self.builder.begin_if(
            condition
        )


        self.builder.begin_block()


        for statement in node.body:

            self.visit(statement)


        self.builder.end_block()


        if node.orelse:

            self.builder.begin_block()


            for statement in node.orelse:

                self.visit(statement)


            self.builder.end_block()


        self.builder.pop_context()

    def visit_For(
        self,
        node
    ):

        iterable = self.visit(
            node.iter
        )


        self.builder.begin_for(
            iterable
        )


        self.builder.begin_block()


        for statement in node.body:

            self.visit(statement)


        self.builder.end_block()


        self.builder.pop_context()

    def visit_BinOp(
        self,
        node
    ):

        left = self.visit(
            node.left
        )


        right = self.visit(
            node.right
        )


        operator = type(
            node.op
        ).__name__


        return self.builder.binary(
            operator,
            left,
            right
        )

    def visit_Compare(
        self,
        node
    ):

        left = self.visit(
            node.left
        )


        right = self.visit(
            node.comparators[0]
        )


        operator = type(
            node.ops[0]
        ).__name__


        return self.builder.binary(
            operator,
            left,
            right
        )

    def visit_BoolOp(
        self,
        node
    ):

        values = [
            self.visit(v)
            for v in node.values
        ]


        result = values[0]


        operator = type(
            node.op
        ).__name__


        for value in values[1:]:

            result = self.builder.binary(
                operator,
                result,
                value
            )


        return result

    def visit_Attribute(
        self,
        node
    ):

        value = self.visit(
            node.value
        )


        return self.builder.attribute(
            value,
            node.attr
        )

    def visit_Subscript(
        self,
        node
    ):

        target = self.visit(
            node.value
        )


        index = self.visit(
            node.slice
        )


        return self.builder.index(
            target,
            index
        )