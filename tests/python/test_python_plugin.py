from pathlib import Path

from pke.languages.python import (
    PythonLanguagePlugin
)


def test_python_detection():

    plugin = PythonLanguagePlugin()

    assert plugin.detect(
        Path("test.py")
    )



def test_python_parse(tmp_path):


    file = tmp_path / "test.py"


    file.write_text(
        """
class User:

    def load(self, id):
        pass
"""
    )


    plugin = PythonLanguagePlugin()


    result = plugin.parse(
        file
    )


    symbols = plugin.extract_symbols(
        result.ast
    )


    names = [
        s.name
        for s in symbols
    ]


    assert "User" in names

    assert "load" in names