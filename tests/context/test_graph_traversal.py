from pke.context.context_graph import ContextGraph
from pke.context.graph_traversal import GraphTraversal



def test_graph_traversal_depth():


    graph = ContextGraph()



    graph.add_relation(
        "login",
        "calls",
        "authenticate"
    )



    graph.add_relation(
        "authenticate",
        "calls",
        "validate_token"
    )



    traversal = GraphTraversal()



    result = traversal.walk(
        graph,
        "login",
        depth=2
    )



    assert "login" in result

    assert "authenticate" in result

    assert "validate_token" in result



def test_graph_traversal_depth_limit():


    graph = ContextGraph()



    graph.add_relation(
        "login",
        "calls",
        "authenticate"
    )



    graph.add_relation(
        "authenticate",
        "calls",
        "validate_token"
    )



    result = GraphTraversal().walk(
        graph,
        "login",
        depth=1
    )



    assert "login" in result

    assert "authenticate" in result

    assert "validate_token" not in result



def test_graph_traversal_cycle():


    graph = ContextGraph()



    graph.add_relation(
        "a",
        "calls",
        "b"
    )


    graph.add_relation(
        "b",
        "calls",
        "a"
    )



    result = GraphTraversal().walk(
        graph,
        "a",
        depth=10
    )


    assert result.count("a") == 1

    assert result.count("b") == 1