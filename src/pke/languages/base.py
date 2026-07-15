from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class ParseResult:

    language: str

    ast: object = None

    symbols: list = field(
        default_factory=list
    )



class LanguagePlugin(ABC):

    name: str = ""

    extensions: list[str] = []


    @abstractmethod
    def detect(self, file):
        pass


    @abstractmethod
    def parse(self, file):
        pass


    @abstractmethod
    def extract_symbols(self, ast):
        pass