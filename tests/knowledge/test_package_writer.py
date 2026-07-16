from pke.knowledge import MarkdownWriter
from pke.knowledge.model import (
    KnowledgePackage,
    KnowledgeFile,
)


def test_write_package(tmp_path):

    package = KnowledgePackage(
        name="auth",
        path="src/auth"
    )


    file = KnowledgeFile(
        name="login.py",
        path="src/auth/login.py"
    )


    package.files.append(
        file
    )


    writer = MarkdownWriter(
        tmp_path
    )


    writer.write_package(
        package
    )


    result = (
        tmp_path /
        "packages" /
        "auth" /
        "Package.md"
    )


    assert result.exists()