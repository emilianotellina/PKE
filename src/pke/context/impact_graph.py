from dataclasses import dataclass, field



@dataclass
class ImpactNode:


    name: str

    type: str = "symbol"

    relations: dict = field(
        default_factory=dict
    )



    def add_relation(
        self,
        relation,
        target
    ):

        if relation not in self.relations:

            self.relations[relation] = []


        if target not in self.relations[relation]:

            self.relations[relation].append(
                target
            )



    def get_relation(
        self,
        relation
    ):

        return self.relations.get(
            relation,
            []
        )



    def get_all_relations(
        self
    ):

        result = []


        for targets in self.relations.values():

            result.extend(
                targets
            )


        return result



@dataclass
class ImpactGraph:


    nodes: dict[str, ImpactNode] = field(
        default_factory=dict
    )



    def get_or_create(
        self,
        name,
        type="symbol"
    ):


        if name not in self.nodes:

            self.nodes[name] = ImpactNode(

                name=name,

                type=type

            )


        return self.nodes[name]



    def add_relation(
        self,
        source,
        relation,
        target
    ):


        source_node = self.get_or_create(
            source
        )


        self.get_or_create(
            target
        )


        source_node.add_relation(
            relation,
            target
        )



    def contains(
        self,
        name
    ):

        return name in self.nodes



    def get_node(
        self,
        name
    ):

        return self.nodes.get(
            name
        )



    def get_relations(
        self,
        name,
        relation=None
    ):


        node = self.get_node(
            name
        )


        if node is None:

            return []



        if relation is None:

            return node.get_all_relations()



        return node.get_relation(
            relation
        )



    def to_dict(
        self
    ):

        return {

            name: {

                "type":

                    node.type,

                "relations":

                    node.relations

            }

            for name,node

            in self.nodes.items()

        }