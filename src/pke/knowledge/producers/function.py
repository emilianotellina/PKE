from .base import KnowledgeProducer


class FunctionProducer(KnowledgeProducer):


    def generate(self, function):


        content = []


        content.append(
            f"# Function {function.name}\n"
        )


        signature = (
            function.signature
            if function.signature
            else function.name
        )


        content.append(
            f"Signature: {signature}\n"
        )


        content.append(
            f"Returns: {function.return_type}\n"
        )


        content.append(
            "\n## Parameters\n"
        )


        for param in function.parameters:

            content.append(
                f"- {param.name}: {param.type}"
            )


        return "\n".join(content)