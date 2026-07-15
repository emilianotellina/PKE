from pathlib import Path

from pke.languages import (
    LanguageRegistry,
    LanguageManager,
    LanguageAnalyzer,
)

from pke.languages.python import (
    PythonLanguagePlugin
)

from pke.knowledge import SourceFile



def test_python_analysis(tmp_path):


    file = tmp_path / "demo.py"


    file.write_text(
        """
def hello():
    pass
"""
    )


    registry = LanguageRegistry()

    registry.register(
        PythonLanguagePlugin()
    )


    manager = LanguageManager(
        registry
    )


    analyzer = LanguageAnalyzer(
        manager
    )


    source = SourceFile(
        name="demo.py",
        path=str(file)
    )


    analyzer.analyze_file(
        source
    )


    assert len(
        source.symbols
    ) == 1