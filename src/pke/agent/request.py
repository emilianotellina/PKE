from dataclasses import dataclass, field
from typing import Any


REQUEST_PROTOCOL_VERSION = "1.0"



@dataclass
class AgentRequest:


    task: str | None = None

    target: str | None = None


    options: dict[str, Any] = field(
        default_factory=dict
    )


    protocol_version: str = (
        REQUEST_PROTOCOL_VERSION
    )



    @property
    def max_tokens(self):

        return self.options.get(
            "max_tokens",
            4000
        )



    @property
    def include_risks(self):

        return self.options.get(
            "include_risks",
            True
        )



    @classmethod
    def from_dict(
        cls,
        data: dict
    ):

        return cls(

            task=data.get(
                "task"
            ),

            target=data.get(
                "target"
            ),

            options=data.get(
                "options",
                {}
            ),

            protocol_version=data.get(
                "protocol_version",
                REQUEST_PROTOCOL_VERSION
            )

        )