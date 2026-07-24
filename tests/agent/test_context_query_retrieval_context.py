from pathlib import Path

from pke.agent.context_query import ContextQuery
from pke.knowledge.repository import KnowledgeRepository



class FakeCSR:

    name = "test_project"

    nodes = {}



def test_context_query_returns_retrieval_context(
    tmp_path
):


    project_path = (
        Path(tmp_path)
        /
        "test_project"
    )


    project_path.mkdir()



    project_file = (
        project_path
        /
        "Project.md"
    )


    project_file.write_text(

        """
# Project: test_project

## Packages

- core

## Files

- login.py

## Functions

- login
""",

        encoding="utf-8"

    )



    knowledge_file = (
        project_path
        /
        "Function.md"
    )


    knowledge_file.write_text(

        """
# Function: login

## Calls

- authenticate
""",

        encoding="utf-8"

    )



    repository = KnowledgeRepository(
        tmp_path
    )



    query = ContextQuery(

        FakeCSR(),

        repository=repository

    )



    result = query.execute(

        task="login",

        target="login"

    )



    assert result.retrieval_context is not None



    assert result.retrieval_context.query == "login"



    assert len(
        result.retrieval_context.documents
    ) > 0



    data = result.to_dict()



    assert "retrieval" in data



    assert data["retrieval"]["documents"]