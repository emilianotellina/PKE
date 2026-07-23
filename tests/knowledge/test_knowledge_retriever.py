from pathlib import Path

from pke.knowledge.repository import KnowledgeRepository
from pke.knowledge.retriever import KnowledgeRetriever



def test_retriever_returns_relevant_documents(
    tmp_path
):


    project_path = (
        Path(tmp_path)
        /
        "test_project"
    )


    project_path.mkdir()



    function_file = (
        project_path
        /
        "Function.md"
    )


    function_file.write_text(

        """
# Function: login

## Calls

- authenticate
""",

        encoding="utf-8"

    )



    other_file = (
        project_path
        /
        "Other.md"
    )


    other_file.write_text(

        """
# Function: logout

## Calls

- cleanup
""",

        encoding="utf-8"

    )



    repository = KnowledgeRepository(
        tmp_path
    )


    retriever = KnowledgeRetriever(
        repository
    )



    results = retriever.retrieve(
        "authenticate"
    )



    assert len(results) == 1

    assert (
        "Function.md"
        in
        results[0]["file"]
    )



def test_retriever_returns_content_only(
    tmp_path
):


    project_path = (
        Path(tmp_path)
        /
        "test_project"
    )


    project_path.mkdir()



    file = (
        project_path
        /
        "Function.md"
    )


    file.write_text(

        "login authenticate",

        encoding="utf-8"

    )



    repository = KnowledgeRepository(
        tmp_path
    )


    retriever = KnowledgeRetriever(
        repository
    )



    content = retriever.retrieve_content(
        "login"
    )


    assert content == [

        "login authenticate"

    ]