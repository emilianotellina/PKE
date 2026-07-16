from .base import KnowledgeProducer


class PackageProducer(KnowledgeProducer):


    def generate(self, package):

        content = []

        content.append(
            f"# Package {package.name}\n"
        )


        if package.description:

            content.append(
                package.description
            )

        else:

            content.append(
                "No description available."
            )


        content.append(
            "\n## Files\n"
        )


        for file in package.files:

            content.append(
                f"- {file.name}"
            )


        return "\n".join(content)