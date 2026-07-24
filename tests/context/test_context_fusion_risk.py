from pke.context.context_fusion import ContextFusion
from pke.context.context import AIContext, SymbolContext



def test_context_fusion_calculates_risk_score():


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

        risks=[

            "critical function",

            "function has side effects",

            "many dependencies"

        ]

    )



    item = items[0]


    assert item.risk_score > 0

    assert item.score == item.risk_score