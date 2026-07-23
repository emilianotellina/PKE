from pke.context.context_retriever import ContextRetriever



def test_context_retriever_limit():


    ranked = [

        ("a",100),
        ("b",80),
        ("c",70)

    ]


    result = ContextRetriever().retrieve(
        ranked,
        max_items=2
    )


    assert len(result) == 2

    assert result[0][0] == "a"

    assert result[1][0] == "b"