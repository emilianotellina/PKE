from pke.csr.relation import RelationType

from .model import (
    KnowledgePackage,
    KnowledgeFile,
    KnowledgeFunction,
)



class KnowledgeExtractor:


    def extract(
        self,
        graph
    ):

        result = []


        functions = graph.find(
            node_type="function"
        )


        for function in functions:

            result.append(
                self.extract_function(
                    graph,
                    function
                )
            )


        return result



    def extract_function(
        self,
        graph,
        node
    ):

        return KnowledgeFunction(

            name=node.name,

            signature=node.attributes.get(
                "signature",
                ""
            ),

            pseudocode=self.generate_pseudocode(
                graph,
                node
            )
        )



    def generate_pseudocode(
        self,
        graph,
        node
    ):

        lines = []


        body = graph.children(
            node,
            RelationType.BODY
        )


        if body:

            statements = graph.children(
                body[0]
            )


            for statement in statements:

                lines.append(
                    statement.type
                )


        return "\n".join(
            lines
        )