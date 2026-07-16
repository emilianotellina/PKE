from pke.parser import PythonAdapter

from pke.csr.relation import RelationType



def test_parse_function():


    source = """

def login(user):

    token = authenticate(user)

    return token

"""


    graph = PythonAdapter().parse(
        source
    )


    functions = graph.find(
        node_type="function"
    )


    assert len(functions) == 1


    function = functions[0]


    assert function.name == "login"



def test_parse_call():


    source = """

def login(user):

    token = authenticate(user)

"""


    graph = PythonAdapter().parse(
        source
    )


    calls = graph.find(
        node_type="call"
    )


    assert len(calls) == 1


    target = graph.children(
        calls[0],
        RelationType.TARGET
    )


    assert target[0].name == "authenticate"