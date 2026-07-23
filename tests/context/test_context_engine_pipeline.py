from pke.context.context_engine import ContextEngine
from pke.context.context import AIContext, SymbolContext


class FakeProject:

    name = "test_project"



def test_context_engine_keeps_only_optimized_context():


    engine = ContextEngine()



    context = AIContext(

        project="test_project",

        symbols=[

            SymbolContext(
                name="login"
            ),

            SymbolContext(
                name="authenticate"
            ),

            SymbolContext(
                name="database"
            )

        ]

    )



    engine.builder.build = lambda *args, **kwargs: context



    engine.ranker.rank = lambda *args, **kwargs: [

        (
            context.symbols[0],
            100
        ),

        (
            context.symbols[1],
            80
        ),

        (
            context.symbols[2],
            50
        )

    ]



    result = engine.build(

        project=FakeProject(),

        target="login",

        budget=4

    )



    optimized = result["context"]



    names = []



    for symbol in optimized.symbols:


        if hasattr(
            symbol,
            "name"
        ):

            names.append(
                symbol.name
            )


        elif isinstance(
            symbol,
            dict
        ):

            names.append(

                symbol.get(
                    "symbol",
                    symbol.get(
                        "name"
                    )
                )

            )


        else:

            names.append(
                str(symbol)
            )



    assert "login" in names


    assert "authenticate" in names


    assert "database" not in names



    assert result["prompt"] is not None