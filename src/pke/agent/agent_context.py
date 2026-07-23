from dataclasses import dataclass, field
from typing import Any
import json



@dataclass
class AgentContext:


    task: str

    target: str | None


    summary: str = ""


    functions: list[Any] = field(
        default_factory=list
    )


    files: list[Any] = field(
        default_factory=list
    )


    packages: list[Any] = field(
        default_factory=list
    )


    dependencies: list[Any] = field(
        default_factory=list
    )


    side_effects: list[Any] = field(
        default_factory=list
    )


    risks: list[Any] = field(
        default_factory=list
    )


    llm_context: Any = None



    def __post_init__(self):

        if not self.summary:

            self.summary = (
                f"{self.target or 'target'} "
                f"coinvolge "
                f"{len(self.functions)} funzioni "
                f"e "
                f"{len(self.files)} file"
            )



    def to_dict(self):

        return {

            "task": self.task,

            "target": self.target,

            "summary": self.summary,

            "impact": {

                "functions": self.functions,

                "files": self.files,

                "packages": self.packages,

                "dependencies": self.dependencies,

                "side_effects": self.side_effects

            },

            "risks": self.risks,

            "llm_context": self.llm_context

        }



    def to_json(self):

        return json.dumps(
            self.to_dict(),
            indent=2,
            default=str
        )