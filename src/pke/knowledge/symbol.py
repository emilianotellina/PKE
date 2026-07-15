from dataclasses import dataclass

from .base import KnowledgeEntity


@dataclass
class Symbol(KnowledgeEntity):

    type: str = ""

    visibility: str = ""

    location: str = ""

    documentation: str = ""