from pke.context.context_ranker import ContextRanker
from pke.context.context import AIContext, SymbolContext



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
                    "calls"

                )

            ]


        return []



def test_context_ranker_applies_retrieval_bonus():


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



    ranker = ContextRanker()



    result = ranker.rank(

        context,

        target="login",

        graph=FakeGraph(),

        retrieved_documents=[

            "UserRepository.md"

        ]

    )



    scores = {

        item.name: score

        for item, score

        in result

    }



    assert "UserRepository" in scores

    assert scores["UserRepository"] > 50