from pke.parser import PythonAdapter
from pke.csr import CSRInspector

def test_inspect_assignment():

    graph = PythonAdapter().parse(
        """
def login(user):
    token = authenticate(user)
    return token
"""
    )

    output = CSRInspector(graph).inspect()

    assert "authenticate" in output
    assert "token" in output
    assert "user" in output