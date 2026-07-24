from pke.context.context import AIContext
from pke.context.context import SymbolContext
from pke.context.context_fusion import ContextFusion


class FakeGraph:

    nodes = {

        "login": object()

    }


def test_context_fusion():

    context = AIContext(
        project="test"
    )

    context.symbols = [

        SymbolContext(
            name="login"
        )

    ]

    fusion = ContextFusion()

    items = fusion.fuse(

        context,

        graph=FakeGraph()

    )

    assert len(items) == 1

    assert items[0].name == "login"

    assert items[0].graph_score == 100