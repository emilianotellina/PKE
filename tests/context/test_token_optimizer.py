from pke.context.token_optimizer import TokenOptimizer
from pke.context.context import SymbolContext



def test_token_optimizer_respects_ranking_order():


    login = SymbolContext(
        name="login"
    )


    authenticate = SymbolContext(
        name="authenticate"
    )


    ranked = [

        (
            login,
            100
        ),

        (
            authenticate,
            80
        )

    ]


    result = TokenOptimizer().optimize(
        ranked,
        budget=10
    )


    assert "100: login" in result

    assert "80: authenticate" in result



def test_token_optimizer_stops_when_budget_exceeded():


    login = SymbolContext(
        name="login"
    )


    authenticate = SymbolContext(
        name="authenticate"
    )


    ranked = [

        (
            login,
            100
        ),

        (
            authenticate,
            80
        )

    ]


    result = TokenOptimizer().optimize(
        ranked,
        budget=2
    )


    assert "100: login" in result

    assert "80: authenticate" not in result