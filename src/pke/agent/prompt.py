from dataclasses import dataclass

from pke.context.prompt_document import PromptDocument



@dataclass
class AgentPrompt:


    task: str

    target: str | None

    document: PromptDocument



    def __init__(
        self,
        task,
        target=None,
        document=None,
        context=None
    ):

        self.task = task

        self.target = target


        if document is not None:

            self.document = document


        else:

            self.document = PromptDocument()


            self.document.add_section(
                "Task",
                task
            )


            if target:

                self.document.add_section(
                    "Target",
                    target
                )


            if context is not None:

                self.document.add_section(
                    "Context",
                    context
                )



    def to_text(
        self
    ):

        return self.document.render()



    def render(
        self
    ):

        return self.to_text()




class PromptBuilder:


    def build(
        self,
        response
    ):

        document = PromptDocument()


        document.add_section(
            "Task",
            response.task
        )


        if response.target:

            document.add_section(
                "Target",
                response.target
            )


        document.add_section(
            "Context",
            response.context
        )


        return AgentPrompt(

            task=response.task,

            target=response.target,

            document=document

        )



    def build_from_context(
        self,
        task,
        target,
        context
    ):


        document = PromptDocument()


        document.add_section(
            "Task",
            task
        )


        if target:

            document.add_section(
                "Target",
                target
            )


        document.add_section(
            "Context",
            context
        )


        return AgentPrompt(

            task=task,

            target=target,

            document=document

        )