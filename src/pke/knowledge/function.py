from dataclasses import dataclass, field

from .symbol import Symbol
from .variable import VariableKnowledge
from .side_effect import SideEffectKnowledge
from .dependency import DependencyKnowledge



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


    call_details: list = field(
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



    variables: list[str] = field(
        default_factory=list
    )



    variable_details: list[VariableKnowledge] = field(
        default_factory=list
    )



    side_effects: list[SideEffectKnowledge] = field(
        default_factory=list
    )



    returns: list = field(
        default_factory=list
    )



    statements: list = field(
        default_factory=list
    )



    dependencies: list[DependencyKnowledge] = field(
        default_factory=list
    )



    references: list[str] = field(
        default_factory=list
    )



    complexity: int = 0