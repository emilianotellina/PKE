from pke.agent.api import AgentAPI
from pke.parser.python_adapter import PythonAdapter



def test_multi_candidate():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)


def authenticate(user):

    return True
"""
    )


    api = AgentAPI(
        project
    )


    response = api.query(
        task="modifica login"
    )


    assert len(
        response.candidates
    ) > 0


    assert response.candidates[0].symbol == "login"