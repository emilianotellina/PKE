from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class CSREdge:

    source: str

    target: str

    relation: str

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    attributes: dict = field(
        default_factory=dict
    )