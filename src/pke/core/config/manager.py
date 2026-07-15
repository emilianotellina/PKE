from pathlib import Path
import yaml

from .models import PKEConfig


class ConfigManager:


    def __init__(
        self,
        path: str | None = None
    ):

        self.path = (
            Path(path)
            if path
            else Path("pke.yaml")
        )


        self.config = None



    def load(self) -> PKEConfig:


        if self.path.exists():

            with open(
                self.path,
                "r"
            ) as file:

                data = yaml.safe_load(file) or {}


        else:

            data = {}


        self.config = PKEConfig(
            **data
        )


        return self.config



    def get(self) -> PKEConfig:

        if self.config is None:

            return self.load()


        return self.config