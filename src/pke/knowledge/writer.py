from pathlib import Path


class KnowledgeWriter:


    def __init__(
        self,
        output_dir="knowledge"
    ):

        self.output_dir = Path(
            output_dir
        )



    def write(
        self,
        path,
        content
    ):

        path = self.output_dir / path

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        path.write_text(
            content,
            encoding="utf-8"
        )


        return path