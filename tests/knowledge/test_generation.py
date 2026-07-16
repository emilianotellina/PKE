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
        output_dir=tmp_path
    )


    generator.generate(
        project
    )


    assert (
        tmp_path /
        "packages/core/Package.md"
    ).exists()