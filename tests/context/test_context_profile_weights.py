from pke.context.context_ranker import ContextRanker
from pke.context.context import AIContext, SymbolContext
from pke.context.context_strategy import ContextProfile



def test_profile_risk_weight_changes_score():


    context = AIContext(

        project="test",

        symbols=[

            SymbolContext(

                name="login"

            )

        ]

    )


    profile = ContextProfile(

        name="debug",

        prioritize_risks=True,

        risk_weight=2.0

    )


    ranked = ContextRanker().rank(

        context,

        target="login",

        risks=[

            "login critical function"

        ],

        profile=profile

    )


    assert ranked[0][1] == 140