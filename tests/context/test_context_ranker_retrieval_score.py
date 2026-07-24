from pke.context.context_ranker import ContextRanker
from pke.context.context import AIContext, SymbolContext
from pke.knowledge.retrieval_context import RetrievalContext



class FakeGraph:


    def get_weighted_relations(
        self,
        node
    ):

        if node == "login":

            return [

                (
                    "UserRepository",
                    1,
                    "call"

                )

            ]

        return []



def test_context_ranker_retrieval_score_increases_priority():


    context = AIContext(
        project="test"
    )


    login = SymbolContext(
        name="login"
    )


    repository = SymbolContext(
        name="UserRepository"
    )


    context.symbols = [

        login,

        repository

    ]


    retrieval = RetrievalContext(
        query="repository"
    )


    retrieval.add(
        "src/user_repository.py",
        score=10
    )


    ranker = ContextRanker()


    result = ranker.rank(

        context,

        "login",

        graph=FakeGraph(),

        retrieved_documents=retrieval

    )


    scores = {

        item.name: score

        for item,score

        in result

    }


    assert scores["UserRepository"] > 0