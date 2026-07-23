from pke.context.context_expander import ContextExpander
from pke.context.context import AIContext, SymbolContext



def test_context_expander_creates_called_by_relation():


    context = AIContext()



    context.symbols.append(

        SymbolContext(

            name="login",

            calls=[

                "authenticate"

            ]

        )

    )



    graph = ContextExpander().expand(
        context
    )



    assert graph.contains(
        "login"
    )


    assert graph.contains(
        "authenticate"
    )


    assert "authenticate" in graph.get_relations(
        "login"
    )


    assert "login" in graph.get_relations(
        "authenticate"
    )