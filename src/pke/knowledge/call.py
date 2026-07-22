from dataclasses import dataclass, field


@dataclass
class CallKnowledge:
    """
    Rappresenta una chiamata estratta dal CSR.
    """

    caller: str

    target: str

    receiver: str = ""

    arguments: list[str] = field(
        default_factory=list
    )

    kind: str = "function_call"

    resolved_type: str = ""

    module: str = ""

    side_effect: str = ""