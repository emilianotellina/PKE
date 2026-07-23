from pke.context.context_graph import ContextGraph



def test_context_graph():


    graph = ContextGraph()


    graph.add_relation(
        "login",
        "calls",
        "authenticate"
    )


    assert "login" in graph.nodes

    assert "authenticate" in graph.nodes


    assert (
        "authenticate"
        in graph.nodes["login"].relations["calls"]
    )