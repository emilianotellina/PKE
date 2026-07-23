from pke.agent.query import query
from pke.parser.python_adapter import PythonAdapter



def test_query_analyzer():


    project = PythonAdapter().parse(
        """
def login(user):

    token = authenticate(user)

    return token
"""
    )


    result = query(
        project,
        task="modifica autenticazione",
        target="login"
    )


    assert "login" in result.functions

    assert result.context is not None