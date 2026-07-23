from pke.context.context_formatter import ContextFormatter
from pke.context.context import AIContext, SymbolContext



def test_context_formatter():


    context = AIContext(
        project="test"
    )


    context.symbols.append(

        SymbolContext(
            name="login",
            calls=[
                "authenticate"
            ]
        )

    )


    document = ContextFormatter().format(
        context,
        target="login"
    )


    text = document.render()



    assert "# Target" in text

    assert "login" in text

    assert "# Functions" in text

    assert "authenticate" in text