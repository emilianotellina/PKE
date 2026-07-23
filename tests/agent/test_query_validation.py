from pke.agent.api import AgentAPI
from pke.agent.errors import AgentErrorResponse
from pke.parser.python_adapter import PythonAdapter



def test_missing_task():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    api = AgentAPI(
        project
    )


    response = api.query(
        task="",
        target="login"
    )


    assert isinstance(
        response,
        AgentErrorResponse
    )


    assert response.error.code == (
        "TASK_REQUIRED"
    )



def test_missing_target():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    api = AgentAPI(
        project
    )


    response = api.query(
        task="modifica",
        target="unknown"
    )


    assert isinstance(
        response,
        AgentErrorResponse
    )


    assert response.error.code == (
        "TARGET_NOT_FOUND"
    )