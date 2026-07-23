from pke.context.context import AIContext, SymbolContext
from pke.context.context_expander import ContextExpander



def test_context_expander_builds_graph():


    context = AIContext()


    context.symbols.append(

        SymbolContext(

            name="login",

            calls=[
                "authenticate"
            ],

            dependencies=[
                "UserRepository"
            ]

        )

    )



    graph = ContextExpander().expand(
        context
    )



    assert "login" in graph.nodes


    assert (

        "authenticate"

        in graph.nodes["login"].relations["calls"]

    )


    assert (

        "UserRepository"

        in graph.nodes["login"].relations["depends_on"]

    )