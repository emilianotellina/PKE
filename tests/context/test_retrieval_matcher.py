from pke.context.retrieval_matcher import RetrievalMatcher



class FakeSymbol:


    def __init__(
        self,
        name
    ):

        self.name = name



def test_retrieval_matcher_matches_symbol_name():


    matcher = RetrievalMatcher()


    symbol = FakeSymbol(
        "UserRepository"
    )


    score = matcher.score(

        symbol,

        [

            "src/security/user_repository.py"

        ]

    )


    assert score > 0



def test_retrieval_matcher_returns_zero_without_match():


    matcher = RetrievalMatcher()


    symbol = FakeSymbol(
        "PaymentService"
    )


    score = matcher.score(

        symbol,

        [

            "src/security/user_repository.py"

        ]

    )


    assert score == 0