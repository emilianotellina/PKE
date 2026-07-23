from pke.context.impact_graph import ImpactGraph
from pke.context.impact_analyzer import ImpactAnalyzer



def test_impact_analyzer_finds_affected_nodes():


    graph = ImpactGraph()


    graph.add_relation(

        "login",

        "called_by",

        "controller"

    )


    graph.add_relation(

        "login",

        "depends_on",

        "database"

    )


    result = ImpactAnalyzer().analyze(

        graph,

        "login"

    )


    assert "controller" in result["affected"]

    assert "database" in result["affected"]



def test_impact_analyzer_builds_paths():


    graph = ImpactGraph()


    graph.add_relation(

        "login",

        "called_by",

        "controller"

    )


    result = ImpactAnalyzer().analyze(

        graph,

        "login"

    )


    assert [

        "login",

        "controller"

    ] in result["paths"]



def test_impact_analyzer_calculates_risk():


    graph = ImpactGraph()


    graph.add_relation(

        "login",

        "called_by",

        "a"

    )


    graph.add_relation(

        "login",

        "called_by",

        "b"

    )


    graph.add_relation(

        "login",

        "called_by",

        "c"

    )


    graph.add_relation(

        "login",

        "called_by",

        "d"

    )


    result = ImpactAnalyzer().analyze(

        graph,

        "login"

    )


    assert result["risk_level"] == "high"