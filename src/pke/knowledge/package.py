from dataclasses import dataclass, field

from .base import KnowledgeEntity


@dataclass
class Package(KnowledgeEntity):

    path: str = ""

    description: str = ""

    files: list = field(
        default_factory=list
    )