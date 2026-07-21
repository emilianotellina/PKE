from pke.csr.semantic_walker import SemanticWalker

from .csr_visitor import KnowledgeCSRVisitor



class CSRKnowledgeAdapter:


    def build(
        self,
        graph
    ):

        visitor = KnowledgeCSRVisitor(
            graph
        )


        walker = SemanticWalker(
            graph,
            visitor
        )


        walker.walk()


        return visitor.project