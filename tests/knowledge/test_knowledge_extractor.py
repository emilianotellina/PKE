from pke.parser import PythonAdapter

from pke.knowledge import (
    KnowledgeExtractor,
    MarkdownWriter,
)



def test_extract_function(tmp_path):


    source = """

def login(user):

    return user

"""


    graph = PythonAdapter().parse(
        source
    )


    extractor = KnowledgeExtractor()


    docs = extractor.extract(
        graph
    )


    assert len(docs) == 1

    assert docs[0].name == "login"



def test_write_function(tmp_path):


    writer = MarkdownWriter(
        tmp_path
    )


    source = """

def login(user):

    return user

"""


    graph = PythonAdapter().parse(
        source
    )


    docs = KnowledgeExtractor().extract(
        graph
    )


    writer.write_function(
        docs[0]
    )


    assert (
        tmp_path /
        "Function-login.md"
    ).exists()