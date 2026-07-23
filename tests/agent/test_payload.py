from pke.agent.payload import AgentPayload



class DummyContext:


    def to_dict(
        self
    ):

        return {

            "functions":
                [
                    "login"
                ]

        }



class DummyResponse:


    protocol_version = "1.0"

    task = "modifica login"

    target = "login"

    context = DummyContext()



def test_payload_dict():


    payload = AgentPayload.from_response(
        DummyResponse()
    )


    data = payload.to_dict()


    assert data["protocol_version"] == "1.0"

    assert data["task"] == "modifica login"

    assert data["target"] == "login"

    assert data["context"]["functions"] == [
        "login"
    ]



def test_payload_json():


    payload = AgentPayload(

        task="analizza login",

        target="login",

        prompt="test prompt"

    )


    result = payload.to_json()


    assert "analizza login" in result

    assert "test prompt" in result



def test_payload_default_protocol():


    payload = AgentPayload()


    assert payload.protocol_version == "1.0"