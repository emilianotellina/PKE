from pke.agent.api import AgentAPI
from pke.parser.python_adapter import PythonAdapter



def test_agent_api_shared_cache():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)
"""
    )


    api = AgentAPI(
        project
    )


    first = api.query(
        "analizza login",
        "login"
    )


    second = api.query(
        "analizza login",
        "login"
    )


    assert first.context is second.context