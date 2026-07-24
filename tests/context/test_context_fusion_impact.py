from pke.context.context_fusion import ContextFusion
from pke.context.context import AIContext, SymbolContext



def test_context_fusion_calculates_impact_score():


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

        impact={

            "target": "login",

            "affected": [

                "controller",

                "service",

                "database",

                "cache"

            ],

            "risk_level": "medium"

        }

    )



    item = items[0]


    assert item.impact_score == 30

    assert item.score == item.impact_score