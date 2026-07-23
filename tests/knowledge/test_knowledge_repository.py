from pathlib import Path

from pke.knowledge.repository import KnowledgeRepository



def test_repository_loads_project_knowledge(
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

## Functions

- login
- authenticate
""",

        encoding="utf-8"

    )



    repository = KnowledgeRepository(
        tmp_path
    )


    knowledge = repository.load(
        "test_project"
    )



    assert knowledge is not None

    assert knowledge["name"] == "test_project"

    assert "login" in knowledge["functions"]



def test_repository_returns_none_for_missing_project(
    tmp_path
):


    repository = KnowledgeRepository(
        tmp_path
    )


    result = repository.load(
        "missing"
    )


    assert result is None