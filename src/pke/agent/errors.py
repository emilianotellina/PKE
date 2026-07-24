from dataclasses import dataclass
import json



@dataclass
class AgentError:

    code: str

    message: str



@dataclass
class AgentErrorResponse:


    error: AgentError

    protocol_version: str = "1.0"

    success: bool = False



    def to_dict(
        self
    ):

        return {

            "protocol_version":
                self.protocol_version,

            "success":
                self.success,

            "error":
                {

                    "code":
                        self.error.code,

                    "message":
                        self.error.message

                }

        }



    def to_json(
        self
    ):

        return json.dumps(

            self.to_dict(),

            indent=2

        )