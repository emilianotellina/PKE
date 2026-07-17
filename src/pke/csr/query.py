from .relation import RelationType


class CSRQuery:

    def __init__(
        self,
        graph
    ):
        self.graph = graph


    def projects(self):

        return [
            node
            for node in self.graph.nodes.values()
            if node.type == "project"
        ]


    def packages(
        self,
        project
    ):

        return self.graph.children(
            project,
            RelationType.PACKAGE
        )


    def files(
        self,
        package
    ):

        return self.graph.children(
            package,
            RelationType.FILE
        )


    def functions(
        self,
        parent
    ):

        return self.graph.children(
            parent,
            RelationType.FUNCTION
        )


    def parameters(
        self,
        function
    ):

        return self.graph.children(
            function,
            RelationType.PARAMETER
        )


    def body(
        self,
        executable
    ):

        bodies = self.graph.children(
            executable,
            RelationType.BODY
        )

        if not bodies:
            return None

        return bodies[0]


    def statements(
        self,
        body
    ):

        return self.graph.children(
            body,
            RelationType.CONTAINS
        )


    def calls(
        self,
        node
    ):

        return self.graph.children(
            node,
            RelationType.CALLS
        )
        
    def arguments(self, node):
        return self.related(
            node,
            Relation.ARGUMENT
        )
        
    def target(self, node):
        return self.related(
            node,
            Relation.TARGET
        )
        
    def value(self, node):
        return self.related(
            node,
            Relation.VALUE
        )