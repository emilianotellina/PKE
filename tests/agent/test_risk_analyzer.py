from pke.agent.risk_analyzer import RiskAnalyzer



class FakeFunction:


    name = "login"


    calls = [

        "authenticate",

        "save",

        "notify",

        "audit",

        "cache",

        "metrics"

    ]


    called_by = list(
        range(11)
    )


    dependencies = [

        "database",

        "redis",

        "api",

        "logger",

        "config",

        "queue"

    ]


    side_effects = [

        "write database"

    ]



class FakeProject:


    functions = [

        FakeFunction()

    ]



def test_risk_analyzer_detects_function_risks():


    risks = RiskAnalyzer().analyze(

        FakeProject(),

        "login"

    )


    assert "high fan-out function" in risks

    assert "high fan-in function" in risks

    assert "many dependencies" in risks

    assert "function has side effects" in risks