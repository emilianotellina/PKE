from dataclasses import dataclass, field

from .symbol import Symbol


@dataclass
class Parameter:

    name: str

    type: str = ""

    default_value: str = ""


@dataclass
class Function(Symbol):

    signature: str = ""

    return_type: str = ""

    parameters: list[Parameter] = field(
        default_factory=list
    )

    calls: list = field(
        default_factory=list
    )

    called_by: list = field(
        default_factory=list
    )

    complexity: int = 0