from dataclasses import dataclass, field

from .symbol import Symbol
from .variable import VariableKnowledge
from .side_effect import SideEffectKnowledge
from .call import CallKnowledge
from .property_access import PropertyAccessKnowledge
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


    call_details: list[CallKnowledge] = field(
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


    # Compatibilità con API esistente
    variables: list[str] = field(
        default_factory=list
    )


    # Analisi semantica avanzata delle variabili
    variable_details: list[VariableKnowledge] = field(
        default_factory=list
    )

    property_accesses: list[PropertyAccessKnowledge] = field(
        default_factory=list
    )

    # Effetti collaterali della funzione
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


    complexity: int = 0