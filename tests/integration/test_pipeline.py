from pke.scanner import ProjectScanner

from pke.languages import (
    LanguageManager,
    LanguageAnalyzer,
    create_default_registry
)

from pke.knowledge import (
    KnowledgeGenerator,
    KnowledgePipeline,
)



def test_full_pipeline(tmp_path):


    source = tmp_path / "demo.py"


    source.write_text(
        """
def hello(name):
    pass
"""
    )


    scanner = ProjectScanner()


    project = scanner.scan(
        tmp_path
    )


    analyzer = LanguageAnalyzer(
        LanguageManager(
            create_default_registry()
        )
    )


    generator = KnowledgeGenerator(
        tmp_path / "knowledge"
    )


    pipeline = KnowledgePipeline(
        analyzer,
        generator
    )


    pipeline.execute(
        project
    )


    files = list(
        (
            tmp_path /
            "knowledge"
        ).rglob(
            "*.md"
        )
    )


    assert len(files) > 0