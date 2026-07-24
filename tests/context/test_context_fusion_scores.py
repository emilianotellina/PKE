from pke.context.context_fusion import ContextFusion
from pke.context.context import AIContext, SymbolContext


def test_context_fusion_calculates_graph_score():

    context = AIContext(
        project="test"
    )


    context.symbols = [

        SymbolContext(
            name="login"
        )

    ]


    class Graph:

        nodes = {

            "login": object()

        }


    fusion = ContextFusion()


    items = fusion.fuse(

        context,

        graph=Graph()

    )


    item = items[0]


    assert item.symbol.name == "login"

    assert item.graph_score == 100

    assert item.score == 100