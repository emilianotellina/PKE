from pathlib import Path


class Paths:


    def __init__(
        self,
        root="."
    ):

        self.root = Path(root)


    @property
    def docs(self):

        return self.root / "docs"


    @property
    def database(self):

        return self.root / ".pke" / "pke.db"



    def initialize(self):

        (
            self.root / ".pke"
        ).mkdir(
            exist_ok=True
        )