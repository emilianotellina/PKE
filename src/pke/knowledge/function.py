from dataclasses import dataclass, field

from .symbol import Symbol
from .variable import VariableKnowledge



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


    call_targets: list = field(
        default_factory=list
    )


    callers: list = field(
        default_factory=list
    )


    variables: list[VariableKnowledge] = field(
        default_factory=list
    )


    returns: list = field(
        default_factory=list
    )


    statements: list = field(
        default_factory=list
    )


    dependencies: list = field(
        default_factory=list
    )


    complexity: int = 0