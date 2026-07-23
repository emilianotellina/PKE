from pke.agent.prompt import PromptBuilder
from pke.agent.api import AgentAPI
from pke.parser.python_adapter import PythonAdapter



def test_prompt_builder():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)
"""
    )


    response = AgentAPI(
        project
    ).query(
        task="modifica login",
        target="login"
    )


    prompt = PromptBuilder().build(
        response
    )


    text = prompt.to_text()


    assert "# Task" in text

    assert "modifica login" in text

    assert "# Target" in text

    assert "login" in text

    assert "# Context" in text