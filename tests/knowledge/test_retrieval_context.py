from pke.knowledge.retrieval_context import RetrievalContext



def test_retrieval_context():

    context = RetrievalContext(
        query="login"
    )


    context.add(
        "Function.md",
        score=10,
        source="knowledge"
    )


    assert context.documents == [
        "Function.md"
    ]


    assert context.scores == [
        10
    ]


    assert context.sources == [
        "knowledge"
    ]


    assert context.names() == [
        "Function.md"
    ]



    data = context.to_dict()


    assert data["query"] == "login"