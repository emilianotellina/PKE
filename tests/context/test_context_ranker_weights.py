from pke.context.context_ranker import ContextRanker
from pke.context.context_graph import ContextGraph
from pke.context.context import AIContext, SymbolContext



def test_context_ranker_respects_relation_weights():


    context = AIContext()



    symbols = [

        SymbolContext(
            name="login"
        ),

        SymbolContext(
            name="authenticate"
        ),

        SymbolContext(
            name="database"
        ),

        SymbolContext(
            name="logger"
        )

    ]



    context.symbols.extend(
        symbols
    )



    graph = ContextGraph()



    graph.add_relation(

        "login",

        "calls",

        "authenticate"

    )


    graph.add_relation(

        "login",

        "depends_on",

        "database"

    )


    graph.add_relation(

        "login",

        "side_effect",

        "logger"

    )



    ranked = ContextRanker().rank(

        context,

        target="login",

        graph=graph

    )



    scores = {

        item.name: score

        for item,score

        in ranked

    }



    assert scores["login"] == 100


    assert scores["authenticate"] > scores["database"]


    assert scores["database"] > scores["logger"]