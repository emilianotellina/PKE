class KnowledgeGraph:


    def __init__(self):

        self.nodes = {}

        self.edges = []


    def add_node(self, entity):

        self.nodes[
            entity.id
        ] = entity


    def add_edge(
        self,
        source,
        target,
        relation
    ):

        self.edges.append(
            {
                "source": source.id,
                "target": target.id,
                "relation": relation
            }
        )


    def find(self, entity_id):

        return self.nodes.get(entity_id)