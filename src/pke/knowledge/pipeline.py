from pke.languages import (
    LanguageAnalyzer,
)


class KnowledgePipeline:


    def __init__(
        self,
        analyzer,
        generator
    ):

        self.analyzer = analyzer

        self.generator = generator



    def execute(
        self,
        project
    ):


        for package in project.packages:

            for file in package.files:

                self.analyzer.analyze_file(
                    file
                )


        self.generator.generate(
            project
        )


        return project