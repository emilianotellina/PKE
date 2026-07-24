from dataclasses import dataclass, field
from typing import Any
import json


PROTOCOL_VERSION = "1.0"



@dataclass
class AgentResponse:


    task: str

    target: str | None

    context: Any


    agent: str | None = None

    profile: str | None = None



    candidates: list[Any] = field(
        default_factory=list
    )


    functions: list = field(
        default_factory=list
    )


    files: list = field(
        default_factory=list
    )


    packages: list = field(
        default_factory=list
    )


    dependencies: list = field(
        default_factory=list
    )


    side_effects: list = field(
        default_factory=list
    )


    risks: list = field(
        default_factory=list
    )


    impact: Any = None


    protocol_version: str = PROTOCOL_VERSION



    def _serialize(
        self,
        value
    ):

        if hasattr(
            value,
            "to_dict"
        ):

            return value.to_dict()


        if isinstance(
            value,
            list
        ):

            return [

                self._serialize(
                    item
                )

                for item in value

            ]


        if isinstance(
            value,
            dict
        ):

            return {

                key:
                    self._serialize(item)

                for key,item in value.items()

            }


        return value



    def to_dict(
        self
    ):

        return {

            "protocol_version":
                self.protocol_version,

            "task":
                self.task,

            "target":
                self.target,


            "agent":
                self.agent,


            "profile":
                self.profile,


            "candidates":
                self._serialize(
                    self.candidates
                ),


            "context":
                self._serialize(
                    self.context
                ),


            "functions":
                self._serialize(
                    self.functions
                ),


            "files":
                self._serialize(
                    self.files
                ),


            "packages":
                self._serialize(
                    self.packages
                ),


            "dependencies":
                self._serialize(
                    self.dependencies
                ),


            "side_effects":
                self._serialize(
                    self.side_effects
                ),


            "risks":
                self._serialize(
                    self.risks
                ),


            "impact":
                self._serialize(
                    self.impact
                )

        }



    def to_json(
        self
    ):

        return json.dumps(

            self.to_dict(),

            indent=2,

            default=str

        )