from pke.context.context import AIContext, SymbolContext
from pke.context.context_formatter import ContextFormatter



def test_formatter_uses_ranked_symbols():


    context = AIContext(
        project="test"
    )


    context.symbols.append(
        SymbolContext(
            name="login"
        )
    )


    context.symbols.append(
        SymbolContext(
            name="unused"
        )
    )


    ranked = [

        (
            context.symbols[0],
            100
        )

    ]


    document = ContextFormatter().format(

        context,

        target="login",

        ranked=ranked

    )


    text = document.render()


    assert "login" in text

    assert "unused" not in text