from pke.context.context_selector import ContextSelector
from pke.context.context import SymbolContext



def test_context_selector_limit():


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
        ),

        (
            SymbolContext(
                name="validate"
            ),
            50
        )

    ]



    result = ContextSelector().select(
        ranked,
        limit=2
    )


    assert len(result) == 2

    assert result[0][0].name == "login"

    assert result[1][0].name == "authenticate"




def test_context_selector_min_score():


    ranked = [

        (
            SymbolContext(
                name="login"
            ),
            100
        ),

        (
            SymbolContext(
                name="validate"
            ),
            40
        )

    ]



    result = ContextSelector().select(
        ranked,
        min_score=50
    )


    assert len(result) == 1

    assert result[0][0].name == "login"