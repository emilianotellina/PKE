from dataclasses import dataclass, field



@dataclass
class KnowledgeDocument:

    title: str

    content: str



@dataclass
class KnowledgePackage:

    name: str

    path: str

    files: list = field(
        default_factory=list
    )



@dataclass
class KnowledgeFile:

    name: str

    path: str

    functions: list = field(
        default_factory=list
    )



@dataclass
class KnowledgeFunction:

    name: str

    signature: str

    pseudocode: str