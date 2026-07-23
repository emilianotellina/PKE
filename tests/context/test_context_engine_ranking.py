from pke.context.context_engine import ContextEngine
from pke.context.context import AIContext, SymbolContext



def test_context_engine_structured_symbols_follow_ranking():


    context = AIContext(
        project="test"
    )


    login = SymbolContext(
        name="login",
        calls=[
            "authenticate"
        ]
    )


    helper = SymbolContext(
        name="helper"
    )


    context.symbols.append(helper)

    context.symbols.append(login)



    engine = ContextEngine()


    ranked = engine.ranker.rank(
        context,
        "login"
    )


    assert ranked[0][0].name == "login"

    assert ranked[0][1] == 100