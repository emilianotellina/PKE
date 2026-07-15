import ast


class PythonParser:


    def parse(self, file):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            source = f.read()


        return ast.parse(source)