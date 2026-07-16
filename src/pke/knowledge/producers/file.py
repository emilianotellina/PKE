from .base import KnowledgeProducer


class FileProducer(KnowledgeProducer):


    def generate(self, file):

        content = []


        content.append(
            f"# File {file.name}\n"
        )


        content.append(
            f"Language: {file.language}\n"
        )


        content.append(
            "## Symbols\n"
        )


        for symbol in file.symbols:

            content.append(
                f"- {symbol.type}: {symbol.name}"
            )


        return "\n".join(content)