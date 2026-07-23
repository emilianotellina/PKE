from pke.context.context_ranker import ContextRanker
from pke.context.context import AIContext, SymbolContext



def test_context_ranker_target():


    context = AIContext(
        project="test"
    )


    login = SymbolContext(
        name="login",
        calls=[
            "authenticate"
        ]
    )


    authenticate = SymbolContext(
        name="authenticate"
    )


    context.symbols.append(login)

    context.symbols.append(authenticate)



    result = ContextRanker().rank(
        context,
        "login"
    )


    assert len(result) == 1

    assert result[0][0].name == "login"

    assert result[0][1] == 100




def test_context_ranker_callers():


    context = AIContext(
        project="test"
    )


    login = SymbolContext(
        name="login"
    )


    controller = SymbolContext(
        name="controller",
        calls=[
            "login()"
        ]
    )


    context.symbols.append(controller)

    context.symbols.append(login)



    result = ContextRanker().rank(
        context,
        "login"
    )


    assert result[0][0].name == "login"

    assert result[0][1] == 100


    assert result[1][0].name == "controller"

    assert result[1][1] == 80