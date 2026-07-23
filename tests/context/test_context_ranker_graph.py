from pke.context.context_ranker import ContextRanker
from pke.context.context_graph import ContextGraph
from pke.context.context import AIContext, SymbolContext



def test_context_ranker_uses_graph_relations():


    context = AIContext()



    login = SymbolContext(
        name="login",
        calls=[
            "authenticate"
        ]
    )


    authenticate = SymbolContext(
        name="authenticate"
    )



    context.symbols.append(
        login
    )


    context.symbols.append(
        authenticate
    )



    graph = ContextGraph()



    graph.add_relation(

        "login",

        "calls",

        "authenticate"

    )


    graph.add_relation(

        "authenticate",

        "called_by",

        "login"

    )



    ranked = ContextRanker().rank(

        context,

        target="authenticate",

        graph=graph

    )



    names = [

        item.name

        for item,score

        in ranked

    ]



    scores = {

        item.name: score

        for item,score

        in ranked

    }



    assert names[0] == "authenticate"


    assert "login" in names


    assert scores["authenticate"] == 100


    assert scores["login"] < 100