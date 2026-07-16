from pke.parser import PythonAdapter



def test_binary_expression():

    graph = PythonAdapter().parse(
        """
def test():
    x = a + b
"""
    )


    nodes = graph.find(
        node_type="binary_operation"
    )


    assert len(nodes) == 1



def test_attribute():

    graph = PythonAdapter().parse(
        """
def test(user):
    x = user.name
"""
    )


    nodes = graph.find(
        node_type="attribute_access"
    )


    assert len(nodes) == 1



def test_index():

    graph = PythonAdapter().parse(
        """
def test(items):
    x = items[0]
"""
    )


    nodes = graph.find(
        node_type="index_access"
    )


    assert len(nodes) == 1