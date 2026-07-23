from pke.agent.api import AgentAPI
from pke.parser.python_adapter import PythonAdapter



def test_agent_api():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)
"""
    )


    api = AgentAPI(
        project
    )


    context = api.query(
        task="modifica login",
        target="login"
    )


    assert context.protocol_version == "1.0"

    assert context.target == "login"

    assert "login" in context.context.functions



def test_agent_api_json():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    api = AgentAPI(
        project
    )


    result = api.query_json(
        task="analizza login",
        target="login"
    )


    assert isinstance(
        result,
        str
    )

    assert "protocol_version" in result

    assert "login" in result