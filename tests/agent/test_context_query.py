from pke.agent.query import query
from pke.parser.python_adapter import PythonAdapter


def test_context_query():

    project = PythonAdapter().parse(
        """
def login(user):
    return authenticate(user)
"""
    )

    result = query(
        project,
        task="modifica autenticazione",
        target="login",
    )

    assert result.task == "modifica autenticazione"
    assert result.target == "login"
    assert result.context is not None