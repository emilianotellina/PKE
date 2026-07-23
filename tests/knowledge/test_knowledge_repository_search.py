from pathlib import Path

from pke.knowledge.repository import KnowledgeRepository



def test_repository_search_finds_function_reference(
    tmp_path
):


    project_path = (
        Path(tmp_path)
        /
        "test_project"
    )


    project_path.mkdir()



    function_path = (
        project_path
        /
        "Function.md"
    )


    function_path.write_text(

        """
# Function: login

## Calls

- authenticate

## Side Effects

- database access
""",

        encoding="utf-8"

    )



    repository = KnowledgeRepository(
        tmp_path
    )



    results = repository.search(
        "authenticate"
    )



    assert len(results) == 1

    assert (
        "Function.md"
        in
        results[0]["file"]
    )

    assert results[0]["score"] > 0