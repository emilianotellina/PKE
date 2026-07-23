from pke.agent.agent_context import AgentContext



def test_agent_context_to_dict():


    context = AgentContext(

        task="modifica login",

        target="login",

        functions=[
            "login"
        ],

        files=[
            "auth.py"
        ]

    )


    data = context.to_dict()


    assert data["task"] == "modifica login"

    assert data["summary"] == (
        "login coinvolge 1 funzioni e 1 file"
    )

    assert "login" in data["impact"]["functions"]



def test_agent_context_json():


    context = AgentContext(

        task="test",

        target="login"

    )


    value = context.to_json()


    assert isinstance(
        value,
        str
    )

    assert "login" in value