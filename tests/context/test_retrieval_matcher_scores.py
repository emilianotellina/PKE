from pke.context.retrieval_matcher import RetrievalMatcher
from pke.context.context import SymbolContext
from pke.knowledge.retrieval_context import RetrievalContext



def test_retrieval_matcher_uses_retrieval_scores():


    matcher = RetrievalMatcher()


    symbol = SymbolContext(
        name="login"
    )


    context = RetrievalContext(
        query="login"
    )


    context.add(
        {
            "name": "login.md",
            "content": "login authentication"
        },
        score=10
    )


    context.add(
        {
            "name": "login_old.md",
            "content": "login"
        },
        score=1
    )



    score = matcher.score(
        symbol,
        context
    )


    assert score > 1