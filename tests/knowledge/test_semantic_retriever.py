from pke.knowledge.semantic_retriever import SemanticRetriever



class FakeRetrievalContext:


    def __init__(
        self,
        documents
    ):

        self.documents = documents

        self.symbols = []



class FakeRepository:

    pass



def test_semantic_retriever_extracts_symbols():


    context = FakeRetrievalContext(

        [

            {

                "content":

                    """
# Function: login

## Calls

- authenticate

- UserRepository

"""

            }

        ]

    )


    retriever = SemanticRetriever(
        FakeRepository()
    )



    result = retriever.expand(
        context
    )



    assert "login" in result.symbols

    assert "authenticate" in result.symbols

    assert "UserRepository" in result.symbols