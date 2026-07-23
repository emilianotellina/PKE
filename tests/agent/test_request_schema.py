from pke.agent.request import AgentRequest



def test_request_defaults():


    request = AgentRequest.from_dict(
        {
            "task": "modifica login"
        }
    )


    assert request.task == (
        "modifica login"
    )


    assert request.max_tokens == 4000


    assert request.include_risks is True



def test_request_options():


    request = AgentRequest.from_dict(

        {
            "task": "analizza",

            "target": "login",

            "options":
                {
                    "max_tokens": 2000,

                    "include_risks": False
                }
        }

    )


    assert request.target == "login"

    assert request.max_tokens == 2000

    assert request.include_risks is False