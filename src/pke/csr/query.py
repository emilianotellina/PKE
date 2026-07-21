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
        
    def arguments(
        self,
        node
    ):

        return self.graph.children(
            node,
            RelationType.ARGUMENT
        )


    def target(
        self,
        node
    ):

        targets = self.graph.children(
            node,
            RelationType.TARGET
        )

        if not targets:
            return None

        return targets[0]


    def value(
        self,
        node
    ):

        values = self.graph.children(
            node,
            RelationType.VALUE
        )

        if not values:
            return None

        return values[0]
    
    def left(
        self,
        node
    ):

        nodes = self.graph.children(
            node,
            RelationType.LEFT
        )

        return nodes[0] if nodes else None


    def right(
        self,
        node
    ):

        nodes = self.graph.children(
            node,
            RelationType.RIGHT
        )

        return nodes[0] if nodes else None


    def object(
        self,
        node
    ):

        nodes = self.graph.children(
            node,
            RelationType.OBJECT
        )

        return nodes[0] if nodes else None


    def index(
        self,
        node
    ):

        nodes = self.graph.children(
            node,
            RelationType.INDEX
        )

        return nodes[0] if nodes else None


    def condition(
        self,
        node
    ):

        nodes = self.graph.children(
            node,
            RelationType.CONDITION
        )

        return nodes[0] if nodes else None


    def iterable(
        self,
        node
    ):

        nodes = self.graph.children(
            node,
            RelationType.ITERABLE
        )

        return nodes[0] if nodes else None

    def assignments(
        self,
        body
    ):

        return [
            statement
            for statement in self.statements(body)
            if statement.type == "assignment"
        ]


    def returns(
        self,
        body
    ):

        return [
            statement
            for statement in self.statements(body)
            if statement.type == "return"
        ]


    def ifs(
        self,
        body
    ):

        return [
            statement
            for statement in self.statements(body)
            if statement.type == "if"
        ]


    def fors(
        self,
        body
    ):

        return [
            statement
            for statement in self.statements(body)
            if statement.type == "for"
        ]
    
    def left(
        self,
        node
    ):

        values = self.related(
            node,
            RelationType.LEFT
        )

        if not values:
            return None

        return values[0]


    def right(
        self,
        node
    ):

        values = self.related(
            node,
            RelationType.RIGHT
        )

        if not values:
            return None

        return values[0]

    def value(
        self,
        node
    ):

        values = self.related(
            node,
            RelationType.VALUE
        )

        if not values:
            return None

        return values[0]
    
    def related(
        self,
        node,
        relation
    ):

        return self.graph.children(
            node,
            relation
        )