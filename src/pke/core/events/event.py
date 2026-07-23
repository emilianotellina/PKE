from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import uuid4



@dataclass(slots=True)
class Event:

    type: str

    source: str

    payload: dict = field(
        default_factory=dict
    )

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )