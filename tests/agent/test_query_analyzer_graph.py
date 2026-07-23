from pke.agent.query import query
from pke.parser.python_adapter import PythonAdapter



def test_query_analyzer_call_chain():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)


def authenticate(user):

    return validate_token(user)


def validate_token(user):

    return True
"""
    )


    result = query(
        project,
        task="modifica autenticazione",
        target="login"
    )


    assert "login" in result.functions

    assert "authenticate" in result.functions

    assert "validate_token" in result.functions