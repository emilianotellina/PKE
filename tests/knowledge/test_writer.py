from pathlib import Path

from pke.knowledge import (
    KnowledgeWriter,
)



def test_writer(tmp_path):


    writer = KnowledgeWriter(
        tmp_path
    )


    file = writer.write(
        "test/Test.md",
        "# Test"
    )


    assert file.exists()

    assert file.read_text() == "# Test"