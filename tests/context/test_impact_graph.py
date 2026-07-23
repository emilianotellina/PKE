from pke.context.impact_graph import ImpactGraph



def test_impact_graph_creates_nodes():


    graph = ImpactGraph()


    graph.add_relation(

        "login",

        "calls",

        "authenticate"

    )


    assert graph.contains(
        "login"
    )


    assert graph.contains(
        "authenticate"
    )



def test_impact_graph_keeps_relations():


    graph = ImpactGraph()


    graph.add_relation(

        "login",

        "depends_on",

        "database"

    )


    relations = graph.get_relations(

        "login",

        "depends_on"

    )


    assert relations == [

        "database"

    ]



def test_impact_graph_serialization():


    graph = ImpactGraph()


    graph.add_relation(

        "login",

        "called_by",

        "controller"

    )


    data = graph.to_dict()


    assert "login" in data

    assert "controller" in data

    assert (

        "called_by"

        in data["login"]["relations"]

    )