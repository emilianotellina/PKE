from pke.agent.api import AgentAPI
from pke.parser.python_adapter import PythonAdapter



def test_disable_risks():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)
"""
    )


    api = AgentAPI(
        project
    )


    response = api.query(

        task="analizza login",

        target="login",

        options={
            "include_risks": False
        }

    )


    assert response.context.risks == []



def test_custom_tokens():


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

        task="analizza login",

        target="login",

        options={
            "max_tokens": 100
        }

    )


    assert response.context.llm_context is not None