from .producers import (
    PackageProducer,
    FileProducer,
    FunctionProducer,
)

from .writer import KnowledgeWriter


class KnowledgeGenerator:


    def __init__(
        self,
        output_dir="knowledge"
    ):

        self.writer = KnowledgeWriter(
            output_dir
        )

        self.package = PackageProducer()

        self.file = FileProducer()

        self.function = FunctionProducer()



    def generate(
        self,
        project
    ):

        for package in project.packages:

            package_name = (
                package.name
                if package.name != "."
                else "root"
            )


            self.writer.write(
                f"packages/{package_name}/Package.md",
                self.package.generate(package)
            )


            for file in package.files:

                file_name = file.name


                self.writer.write(
                    f"files/{file_name}/File.md",
                    self.file.generate(file)
                )


                for symbol in file.symbols:

                    if symbol.type == "FUNCTION":

                        self.writer.write(
                            f"functions/{symbol.name}/Function.md",
                            self.function.generate(symbol)
                        )