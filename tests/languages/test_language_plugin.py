from pathlib import Path


from pke.languages import (
    LanguagePlugin,
    LanguageRegistry,
    LanguageManager
)



class PythonPlugin(LanguagePlugin):

    name = "python"

    extensions = [
        ".py"
    ]


    def detect(self, file):

        return file.suffix == ".py"


    def parse(self, file):

        return None


    def extract_symbols(self, ast):

        return []



def test_registry():


    registry = LanguageRegistry()


    plugin = PythonPlugin()


    registry.register(
        plugin
    )


    assert registry.get(
        "python"
    ) == plugin



def test_detection():


    registry = LanguageRegistry()


    registry.register(
        PythonPlugin()
    )


    manager = LanguageManager(
        registry
    )


    plugin = manager.detect(
        Path("test.py")
    )


    assert plugin.name == "python"