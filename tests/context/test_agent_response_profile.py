from pke.agent.protocol import AgentResponse



def test_agent_response_contains_agent():


    response = AgentResponse(

        task="fix login",

        target="login",

        context={},

        agent="debug",

        profile="debug"

    )


    data = response.to_dict()


    assert data["agent"] == "debug"

    assert data["profile"] == "debug"



def test_agent_response_backward_compatible():


    response = AgentResponse(

        task="test",

        target=None,

        context={}

    )


    data = response.to_dict()


    assert data["agent"] is None

    assert data["profile"] is None