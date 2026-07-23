from pke.agent.adapter import PKEAgentAdapter
from pke.parser.python_adapter import PythonAdapter



def test_agent_adapter():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    adapter = PKEAgentAdapter(
        project
    )


    response = adapter.handle(
        {
            "task": "modifica login",
            "target": "login"
        }
    )


    assert response.target == "login"



def test_agent_adapter_json():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    adapter = PKEAgentAdapter(
        project
    )


    response = adapter.handle_json(
        {
            "task": "analizza login",
            "target": "login"
        }
    )


    assert isinstance(
        response,
        str
    )


    assert "protocol_version" in response



def test_invalid_request():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    adapter = PKEAgentAdapter(
        project
    )


    response = adapter.handle(
        None
    )


    assert response.error.code == (
        "INVALID_REQUEST"
    )