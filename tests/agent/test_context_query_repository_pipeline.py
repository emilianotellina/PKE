from pathlib import Path

from pke.agent.context_query import ContextQuery
from pke.knowledge.repository import KnowledgeRepository



class FakeCSR:


    name = "test_project"



def test_context_query_uses_repository_knowledge(
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
        task="explain login",
        target="login"
    )



    assert result is not None

    assert result.context.project == "test_project"

    assert "login" in [

        symbol.name

        for symbol

        in result.context.symbols

    ]