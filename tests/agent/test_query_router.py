from pke.agent.query_router import QueryRouter
from pke.parser.python_adapter import PythonAdapter



def test_query_router():


    project = PythonAdapter().parse(
        """
def login(user):

    return authenticate(user)


def logout():

    return True
"""
    )


    router = QueryRouter()


    result = router.route(
        project,
        "modifica login"
    )


    assert len(result) > 0

    assert result[0]["symbol"] == "login"