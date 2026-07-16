from pke.parser import PythonAdapter



def test_parse_if():


    source = """

def check(x):

    if x:

        return x

"""


    graph = PythonAdapter().parse(
        source
    )


    nodes = graph.find(
        node_type="if"
    )


    assert len(nodes) == 1



def test_parse_for():


    source = """

def process(items):

    for item in items:

        return item

"""


    graph = PythonAdapter().parse(
        source
    )


    nodes = graph.find(
        node_type="for"
    )


    assert len(nodes) == 1