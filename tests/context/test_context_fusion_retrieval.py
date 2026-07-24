from pke.context.context_fusion import ContextFusion
from pke.context.context import AIContext, SymbolContext
from pke.knowledge.retrieval_context import RetrievalContext



def test_context_fusion_calculates_retrieval_score():


    context = AIContext(
        project="test"
    )


    context.symbols = [

        SymbolContext(

            name="login"

        )

    ]



    retrieval = RetrievalContext(

        query="login"

    )


    retrieval.add(

        {
            "content": "# Function: login"

        }

    )



    fusion = ContextFusion()



    items = fusion.fuse(

        context,

        retrieval_context=retrieval

    )



    item = items[0]



    assert item.retrieval_score > 0

    assert item.score == item.retrieval_score