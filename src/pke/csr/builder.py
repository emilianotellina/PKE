from .graph import CSRGraph
from .relation import RelationType
from .builder_context import BuilderContext

from .nodes import (
    FunctionNode,
    ParameterNode,
    BodyNode,
    BlockNode,
    ReturnNode,
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


        self.add_node(
            parameter
        )


        function = self.stack[-2]


        self.link(
            function,
            parameter,
            RelationType.ARGUMENT
        )


        return parameter



    def add_return(
        self
    ):

        node = ReturnNode()


        self.add_node(
            node
        )


        body = self.current_context()


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