from dataclasses import dataclass, field



RELATION_WEIGHTS = {

    "calls": 1.0,

    "depends_on": 1.5,

    "called_by": 2.0,

    "side_effect": 2.5

}



@dataclass
class ContextNode:


    name: str

    type: str = "symbol"

    score: int = 0

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



    def get_relations(
        self
    ):

        result = []


        for targets in self.relations.values():

            result.extend(
                targets
            )


        return result



    def get_weighted_relations(
        self
    ):

        result = []


        for relation, targets in self.relations.items():


            weight = RELATION_WEIGHTS.get(
                relation,
                1.0
            )


            for target in targets:


                result.append(

                    (
                        target,
                        weight,
                        relation

                    )

                )



        return result



    def to_dict(
        self
    ):

        return {

            "name":
                self.name,

            "type":
                self.type,

            "score":
                self.score,

            "relations":
                self.relations

        }





@dataclass
class ContextGraph:


    nodes: dict[str, ContextNode] = field(
        default_factory=dict
    )



    def get_or_create(
        self,
        name,
        type="symbol"
    ):


        if name not in self.nodes:

            self.nodes[name] = ContextNode(

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



    def get_relations(
        self,
        node
    ):


        if node not in self.nodes:

            return []


        return self.nodes[node].get_relations()



    def get_weighted_relations(
        self,
        node
    ):


        if node not in self.nodes:

            return []


        return self.nodes[node].get_weighted_relations()



    def contains(
        self,
        name
    ):

        return name in self.nodes



    def to_dict(
        self
    ):

        return {

            name:

                node.to_dict()

            for name, node

            in self.nodes.items()

        }