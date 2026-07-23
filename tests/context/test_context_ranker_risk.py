from pke.context.context_ranker import ContextRanker
from pke.context.context import AIContext, SymbolContext



def test_ranker_promotes_risky_symbol():


    context = AIContext(

        project="test",

        symbols=[

            SymbolContext(
                name="login"
            )

        ]

    )


    ranked = ContextRanker().rank(

        context,

        target="login",

        risks=[

            "login critical function"

        ]

    )


    assert ranked[0][1] == 120