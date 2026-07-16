import json


class CSRSerializer:


    def serialize(
        self,
        graph
    ):

        return json.dumps(
            {
                "nodes": [
                    self._node(n)
                    for n in graph.nodes.values()
                ],
                "edges": [
                    self._edge(e)
                    for e in graph.edges
                ]
            },
            indent=2
        )



    def _node(
        self,
        node
    ):

        return {
            "id": node.id,
            "type": node.type,
            "name": node.name,
            "attributes": node.attributes
        }



    def _edge(
        self,
        edge
    ):

        return {
            "id": edge.id,
            "source": edge.source,
            "target": edge.target,
            "relation": edge.relation,
            "attributes": edge.attributes
        }