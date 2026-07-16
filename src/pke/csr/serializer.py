import json


class CSRSerializer:


    def serialize(
        self,
        node
    ):

        return json.dumps(
            self._convert(node),
            indent=2
        )


    def _convert(
        self,
        node
    ):

        return {
            "id": node.id,
            "type": node.type,
            "name": node.name,
            "attributes": node.attributes,
            "children": [
                self._convert(c)
                for c in node.children
            ]
        }