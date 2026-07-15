from pke.knowledge import Function


class LanguageAnalyzer:


    def __init__(
        self,
        manager
    ):

        self.manager = manager



    def analyze(
        self,
        source_file
    ):


        plugin = self.manager.detect(
            source_file.path
        )


        if not plugin:

            return []


        result = plugin.parse(
            source_file.path
        )


        return plugin.extract_symbols(
            result.ast
        )
    
    def analyze_file(
        self,
        source_file
    ):

        symbols = self.analyze(
            source_file
        )

        source_file.symbols.extend(
            symbols
        )

        return source_file