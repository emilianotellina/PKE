from dataclasses import dataclass, field

from .base import KnowledgeEntity


@dataclass
class Project(KnowledgeEntity):

    path: str = ""

    language: str = ""

    version: str = ""

    packages: list = field(
        default_factory=list
    )