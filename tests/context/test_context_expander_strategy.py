from pke.context.context import AIContext
from pke.context.context import SymbolContext
from pke.context.context_expander import ContextExpander
from pke.context.context_strategy import ContextStrategy



def build_context():

    context = AIContext(
        project="test"
    )

    context.symbols = [

        SymbolContext(

            name="login",

            calls=["authenticate"],

            called_by=["controller"],

            dependencies=["database"],

            side_effects=["write db"]

        )

    ]

    return context



def test_strategy_disables_callers():

    strategy = ContextStrategy(

        expand_callers=False,

        expand_dependencies=True,

        include_side_effects=True

    )

    graph = ContextExpander().expand(

        build_context(),

        strategy

    )

    relations = graph.nodes["login"].relations

    assert "called_by" not in relations



def test_strategy_disables_dependencies():

    strategy = ContextStrategy(

        expand_callers=True,

        expand_dependencies=False,

        include_side_effects=True

    )

    graph = ContextExpander().expand(

        build_context(),

        strategy

    )

    relations = graph.nodes["login"].relations

    assert "depends_on" not in relations



def test_strategy_disables_side_effects():

    strategy = ContextStrategy(

        expand_callers=True,

        expand_dependencies=True,

        include_side_effects=False

    )

    graph = ContextExpander().expand(

        build_context(),

        strategy

    )

    relations = graph.nodes["login"].relations

    assert "side_effect" not in relations