import json
from pathlib import Path



class ProtocolSchemaValidator:


    def __init__(
        self
    ):

        self.schema_path = (

            Path(__file__).parent

            / "schemas"

            / "agent_protocol_v1.json"

        )



        with open(
            self.schema_path,
            "r",
            encoding="utf-8"
        ) as file:

            self.schema = json.load(
                file
            )



    def validate(
        self,
        payload
    ):

        required = self.schema.get(
            "required",
            []
        )


        missing = [

            field

            for field in required

            if field not in payload

        ]


        if missing:

            return False



        if payload.get(
            "protocol_version"
        ) != "1.0":

            return False



        return True