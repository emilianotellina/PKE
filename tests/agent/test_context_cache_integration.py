from pke.agent.context_query import ContextQuery
from pke.parser.python_adapter import PythonAdapter



def test_context_query_uses_cache():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)
"""
    )


    query = ContextQuery(
        project
    )


    first = query.execute(

        task="analizza login",

        target="login"

    )


    second = query.execute(

        task="analizza login",

        target="login"

    )


    assert first is second



def test_context_query_cache_different_target():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)


def logout(user):

    return True
"""
    )


    query = ContextQuery(
        project
    )


    first = query.execute(

        task="analizza",

        target="login"

    )


    second = query.execute(

        task="analizza",

        target="logout"

    )


    assert first is not second