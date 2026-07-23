from pke.agent.context_query import ContextQuery
from pke.parser.python_adapter import PythonAdapter



def test_cache_invalidated_on_project_change():


    project1 = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    query1 = ContextQuery(
        project1
    )


    first = query1.execute(
        task="analizza login",
        target="login"
    )



    project2 = PythonAdapter().parse(
        """
def login(user):

    return False
"""
    )


    query2 = ContextQuery(
        project2
    )


    second = query2.execute(
        task="analizza login",
        target="login"
    )


    assert first is not second