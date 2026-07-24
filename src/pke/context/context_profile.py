from dataclasses import dataclass, field



@dataclass
class ContextProfile:


    name: str = "default"



    #
    # Agent metadata
    #

    description: str = ""



    #
    # Expansion
    #

    expand_callers: bool = False

    expand_dependencies: bool = False

    include_tests: bool = False

    include_docs: bool = False

    include_side_effects: bool = False

    max_depth: int = 1



    #
    # Ranking
    #

    prioritize_risks: bool = False

    prioritize_dependencies: bool = False

    prioritize_callers: bool = False



    #
    # Ranking weights
    #

    risk_weight: float = 1.0

    dependency_weight: float = 1.0

    caller_weight: float = 1.0



    #
    # Compression
    #

    compression_mode: str = "balanced"



    #
    # Formatting
    #

    detail_level: str = "normal"



    metadata: dict = field(
        default_factory=dict
    )



    def to_dict(
        self
    ):

        return {

            "name":
                self.name,

            "description":
                self.description,

            "expand_callers":
                self.expand_callers,

            "expand_dependencies":
                self.expand_dependencies,

            "include_tests":
                self.include_tests,

            "include_docs":
                self.include_docs,

            "include_side_effects":
                self.include_side_effects,

            "max_depth":
                self.max_depth,

            "prioritize_risks":
                self.prioritize_risks,

            "prioritize_dependencies":
                self.prioritize_dependencies,

            "prioritize_callers":
                self.prioritize_callers,

            "risk_weight":
                self.risk_weight,

            "dependency_weight":
                self.dependency_weight,

            "caller_weight":
                self.caller_weight,

            "compression_mode":
                self.compression_mode,

            "detail_level":
                self.detail_level,

            "metadata":
                self.metadata

        }