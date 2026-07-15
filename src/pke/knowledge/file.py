from dataclasses import dataclass, field

from .base import KnowledgeEntity


@dataclass
class SourceFile(KnowledgeEntity):

    path: str = ""

    language: str = ""

    hash: str = ""

    imports: list = field(
        default_factory=list
    )

    symbols: list = field(
        default_factory=list
    )