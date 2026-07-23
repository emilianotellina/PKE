from pke.knowledge import (
    Project,
    Package,
    SourceFile,
    KnowledgeGenerator,
)


def test_generate_docs(tmp_path):

    project = Project(
        name="demo"
    )

    package = Package(
        name="core"
    )

    file = SourceFile(
        name="main.py"
    )

    package.files.append(file)

    project.packages.append(package)

    generator = KnowledgeGenerator(
        output_path=tmp_path
    )

    generator.generate(
        project
    )

    assert (
        tmp_path /
        "demo/core/Package.md"
    ).exists()

    assert (
        tmp_path /
        "demo/Project.md"
    ).exists()