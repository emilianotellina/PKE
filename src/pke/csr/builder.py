from .graph import CSRGraph
from .relation import RelationType
from .builder_context import BuilderContext

from .nodes import (
    FunctionNode,
    ParameterNode,
    BodyNode,
    BlockNode,
    ReturnNode,
    IfNode,
    ForNode,
    WhileNode,
    TryNode,
    AttributeAccessNode,
    IndexAccessNode,
    IdentifierNode,
    LiteralNode,
    BinaryOperationNode,
    CallNode,
    AssignmentNode,
    ProjectNode,
    PackageNode,
    FileNode,
)


class CSRBuilder:


    def __init__(self):

        self.graph = CSRGraph()

        self.context_stack = []


    def add_node(
        self,
        node
    ):

        self.graph.add(node)

        return node


    def add_expression_node(
        self,
        node
    ):

        self.graph.add(node)

        return node


    def identifier(
        self,
        name
    ):

        node = IdentifierNode(name)

        return self.add_expression_node(node)


    def literal(
        self,
        value
    ):

        node = LiteralNode(value)

        return self.add_expression_node(node)


    def binary(
        self,
        operator,
        left,
        right
    ):

        node = BinaryOperationNode(operator)

        self.add_expression_node(node)

        self.graph.link(
            node,
            left,
            RelationType.LEFT
        )

        self.graph.link(
            node,
            right,
            RelationType.RIGHT
        )

        return node


    def call(
        self,
        target,
        arguments=None
    ):

        node = CallNode()

        self.add_expression_node(node)

        self.graph.link(
            node,
            target,
            RelationType.TARGET
        )

        for argument in arguments or []:

            self.graph.link(
                node,
                argument,
                RelationType.ARGUMENT
            )

        return node


    def assignment(
        self,
        left,
        right
    ):

        node = AssignmentNode()

        self.add_node(
            node
        )


        #
        # Relazioni storiche CSR
        #
        self.graph.link(
            node,
            left,
            RelationType.LEFT
        )

        self.graph.link(
            node,
            right,
            RelationType.RIGHT
        )


        #
        # Relazioni semantiche usate dal knowledge layer
        #
        self.graph.link(
            node,
            left,
            RelationType.TARGET
        )

        self.graph.link(
            node,
            right,
            RelationType.VALUE
        )


        self.add_to_current_body(
            node
        )


        return node


    def link(
        self,
        source,
        target,
        relation
    ):

        self.graph.link(
            source,
            target,
            relation
        )


    def find_context(
        self,
        allowed_types
    ):

        for context in reversed(self.context_stack):

            if context.type in allowed_types:

                return context.node

        return None


    def begin_function(
        self,
        name,
        signature=""
    ):

        function = FunctionNode(
            name,
            signature
        )

        body = BodyNode()

        self.add_node(function)
        self.add_node(body)

        parent = self.find_context(
            [
                "file",
                "class"
            ]
        )

        if parent is not None:

            self.link(
                parent,
                function,
                RelationType.FUNCTION
            )


        self.link(
            function,
            body,
            RelationType.BODY
        )


        self.push_context(function)
        self.push_context(body)

        return function


    def add_parameter(
        self,
        name,
        data_type=None
    ):

        parameter = ParameterNode(
            name,
            data_type
        )

        self.add_node(parameter)

        function = self.find_context(
            [
                "function"
            ]
        )

        self.link(
            function,
            parameter,
            RelationType.PARAMETER
        )

        return parameter


    def add_return(
        self
    ):

        node = ReturnNode()

        self.add_node(node)

        body = self.current_context()

        if body is not None:

            self.link(
                body,
                node,
                RelationType.CONTAINS
            )

        return node


    def end_function(self):

        self.pop_context()
        self.pop_context()


    def current_context(self):

        if not self.context_stack:

            return None

        return self.context_stack[-1].node


    def parent_context(self):

        if len(self.context_stack) < 2:

            return None

        return self.context_stack[-2].node


    def add_to_current_body(
        self,
        node
    ):

        parent = self.current_context()

        if parent is None:

            return

        self.link(
            parent,
            node,
            RelationType.CONTAINS
        )


    def push_context(
        self,
        node
    ):

        self.context_stack.append(
            BuilderContext(
                node,
                node.type
            )
        )


    def pop_context(self):

        return self.context_stack.pop()


    def begin_block(
        self
    ):

        block = BlockNode()

        self.add_node(block)

        parent = self.current_context()

        self.link(
            parent,
            block,
            RelationType.BODY
        )

        self.push_context(block)

        return block


    def end_block(
        self
    ):

        self.pop_context()


    def begin_if(
        self,
        condition
    ):

        node = IfNode()

        self.add_node(node)

        parent = self.current_context()

        self.link(
            parent,
            node,
            RelationType.CONTAINS
        )

        self.link(
            node,
            condition,
            RelationType.CONDITION
        )

        self.push_context(node)

        return node


    def begin_for(
        self,
        iterable
    ):

        node = ForNode()

        self.add_node(node)

        parent = self.current_context()

        self.link(
            parent,
            node,
            RelationType.CONTAINS
        )

        self.link(
            node,
            iterable,
            RelationType.ITERABLE
        )

        self.push_context(node)

        return node


    def attribute(
        self,
        obj,
        name
    ):

        node = AttributeAccessNode(name)

        self.add_expression_node(node)

        self.graph.link(
            node,
            obj,
            RelationType.OBJECT
        )

        return node


    def index(
        self,
        target,
        index
    ):

        node = IndexAccessNode()

        self.add_expression_node(node)

        self.graph.link(
            node,
            target,
            RelationType.TARGET
        )

        self.graph.link(
            node,
            index,
            RelationType.INDEX
        )

        return node


    def begin_project(
        self,
        name
    ):

        node = ProjectNode(name)

        self.add_node(node)

        self.push_context(node)

        return node


    def begin_package(
        self,
        name
    ):

        node = PackageNode(name)

        self.add_node(node)

        parent = self.current_context()

        self.link(
            parent,
            node,
            RelationType.PACKAGE
        )

        self.push_context(node)

        return node


    def begin_file(
        self,
        name
    ):

        node = FileNode(name)

        self.add_node(node)

        parent = self.current_context()

        self.link(
            parent,
            node,
            RelationType.FILE
        )

        self.push_context(node)

        return node


    def end_source_context(
        self
    ):

        self.pop_context()


    def end_if(self):

        self.pop_context()


    def end_for(self):

        self.pop_context()