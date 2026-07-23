from pke.agent.context_query import ContextQuery
from pke.knowledge.repository import KnowledgeRepository



class FakeRepository:


    def load(
        self,
        name
    ):

        return {

            "name":
                "test_project",

            "functions":
                [
                    "login"
                ],

            "files":
                [],

            "packages":
                []

        }



def test_context_query_uses_repository_when_available(
    monkeypatch
):


    query = ContextQuery(
        None
    )


    query.repository = FakeRepository()



    result = query.repository.load(
        "test_project"
    )



    assert result["name"] == "test_project"

    assert "login" in result["functions"]