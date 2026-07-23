from dataclasses import dataclass, field



@dataclass
class PromptDocument:


    sections: dict[str, str] = field(
        default_factory=dict
    )


    metadata: dict = field(
        default_factory=dict
    )



    def add_section(
        self,
        name,
        content
    ):

        self.sections[name] = content



    def add_metadata(
        self,
        key,
        value
    ):

        self.metadata[key] = value



    def render(
        self
    ):

        lines = []


        for name, content in self.sections.items():

            lines.append(
                f"# {name}"
            )


            if content:

                lines.append(
                    str(content)
                )


            lines.append(
                ""
            )



        return "\n".join(
            lines
        ).strip()



    def to_dict(
        self
    ):

        return {

            "sections": self.sections,

            "metadata": self.metadata

        }