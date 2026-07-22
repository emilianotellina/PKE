from dataclasses import dataclass, field



@dataclass
class PackageMetrics:


    name: str


    dependencies: list[str] = field(
        default_factory=list
    )


    dependents: list[str] = field(
        default_factory=list
    )


    fan_in: int = 0


    fan_out: int = 0


    instability: float = 0.0