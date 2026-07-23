from dataclasses import dataclass, field
import json



@dataclass
class AgentPayload:


    protocol_version: str = "1.0"

    task: str | None = None

    target: str | None = None

    context: object | None = None

    prompt: str | None = None

    metadata: dict = field(
        default_factory=dict
    )



    def to_dict(
        self
    ):


        context = self.context


        if hasattr(
            context,
            "to_dict"
        ):

            context = context.to_dict()



        return {

            "protocol_version":
                self.protocol_version,

            "task":
                self.task,

            "target":
                self.target,

            "context":
                context,

            "prompt":
                self.prompt,

            "metadata":
                self.metadata

        }



    def to_json(
        self
    ):


        return json.dumps(

            self.to_dict(),

            indent=2,

            default=str

        )



    @classmethod
    def from_response(
        cls,
        response
    ):


        prompt = None


        context = response.context


        if hasattr(
            context,
            "llm_context"
        ):

            prompt = context.llm_context



        return cls(

            protocol_version=
                response.protocol_version,

            task=
                response.task,

            target=
                response.target,

            context=
                context,

            prompt=
                prompt

        )