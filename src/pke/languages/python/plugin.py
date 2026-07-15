from pathlib import Path


from pke.languages import (
    LanguagePlugin,
    ParseResult
)


from .parser import PythonParser
from .extractor import PythonExtractor



class PythonLanguagePlugin(
    LanguagePlugin
):


    name = "python"


    extensions = [
        ".py"
    ]


    def __init__(self):

        self.parser = PythonParser()

        self.extractor = PythonExtractor()



    def detect(self, file):

        return (
            Path(file).suffix
            == ".py"
        )



    def parse(self, file):

        tree = self.parser.parse(file)


        return ParseResult(
            language="python",
            ast=tree
        )



    def extract_symbols(self, ast):

        return self.extractor.extract(
            ast
        )