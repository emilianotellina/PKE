from pke.agent.query_result import QueryResult



def test_query_result_contains_retrieved_documents():

    result = QueryResult(

        task="explain",

        target="login",

        context=None,

        retrieved_documents=[

            "Function.md",

            "File.md"

        ]

    )


    assert result.retrieved_documents == [

        "Function.md",

        "File.md"

    ]


    assert result.retrieved_context() == [

        "Function.md",

        "File.md"

    ]


    data = result.to_dict()


    assert data["retrieved_documents"] == [

        "Function.md",

        "File.md"

    ]