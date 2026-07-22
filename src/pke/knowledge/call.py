from dataclasses import dataclass, field


@dataclass
class CallKnowledge:

    """
    Rappresenta una chiamata di funzione/metodo
    estratta dal CSR.
    """

    target: str

    receiver: str = ""

    arguments: list[str] = field(
        default_factory=list
    )

    kind: str = "function_call"

    side_effect: str = ""