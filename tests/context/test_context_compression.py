from pke.context.token_optimizer import TokenOptimizer
from pke.context.context import SymbolContext



def test_context_compression_keeps_priority():


    ranked = [

        (
            SymbolContext(
                name="login"
            ),
            100
        ),

        (
            SymbolContext(
                name="authenticate"
            ),
            80
        )

    ]


    result = TokenOptimizer().optimize(
        ranked,
        budget=10
    )


    assert "100: login" in result

    assert "80: authenticate" in result



def test_context_compression_marks_summary():


    ranked = [

        (
            SymbolContext(
                name="login"
            ),
            100
        ),

        (
            SymbolContext(
                name="database"
            ),
            50
        )

    ]


    result = TokenOptimizer().optimize(
        ranked,
        budget=20
    )


    assert "100: login" in result

    assert "(summary)" in result