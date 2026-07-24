from pke.context.retrieval_matcher import RetrievalMatcher
from pke.context.context import SymbolContext
from pke.knowledge.retrieval_context import RetrievalContext



def test_retrieval_symbols_boost_ranking():


    matcher = RetrievalMatcher()



    symbol = SymbolContext(
        name="UserRepository"
    )



    context = RetrievalContext(
        query="user"
    )



    context.documents = [

        {
            "content":
                "handles database access"
        }

    ]



    context.symbols = [

        "UserRepository"

    ]



    score = matcher.score(
        symbol,
        context
    )



    assert score > 0