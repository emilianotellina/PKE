from pke.parser.python_adapter import PythonAdapter
from pke.agent.context_query import ContextQuery



def test_context_query_end_to_end():


    graph = PythonAdapter().parse(
        """
def authenticate():

    return True


def login():

    token = authenticate()

    return token
"""
    )


    query = ContextQuery(
        graph
    )


    result = query.execute(

        task="fix login bug",

        target="login"

    )


    assert result is not None


    assert result.context is not None


    assert result.engine_context is not None


    assert result.engine_context["target"] == "login"


    assert result.engine_context["fusion"]


    assert result.impact is not None