from unittest.mock import Mock

from pke.knowledge.retriever import KnowledgeRetriever
from pke.knowledge.retrieval_context import RetrievalContext



def test_retriever_returns_retrieval_context():


    repository = Mock()


    repository.search.return_value = [

        {
            "name": "Function.md",
            "content": "login",
            "score": 20,
            "source": "knowledge"
        }

    ]


    retriever = KnowledgeRetriever(
        repository
    )


    result = retriever.retrieve(
        "login"
    )


    assert isinstance(
        result,
        RetrievalContext
    )


    assert result.query == "login"


    assert result.names() == [

        "Function.md"

    ]