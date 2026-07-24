from pke.agent.query_result import QueryResult
from pke.knowledge.retrieval_context import RetrievalContext



def test_query_result_contains_retrieval_context():


    retrieval = RetrievalContext(
        query="login"
    )


    retrieval.add(
        "Function.md",
        score=10
    )


    result = QueryResult(

        task="explain",

        target="login",

        context=None,

        retrieval_context=retrieval

    )


    assert result.retrieved_documents == [

        "Function.md"

    ]


    data = result.to_dict()


    assert data["retrieval"]["query"] == "login"


    assert data["retrieval"]["documents"] == [

        "Function.md"

    ]