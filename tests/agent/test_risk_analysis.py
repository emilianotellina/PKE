from pke.agent.risk_analyzer import RiskAnalyzer



def test_risk_analyzer():


    analyzer = RiskAnalyzer()


    metrics = {

        "login": {

            "fan_out": 10,

            "complexity": 3,

            "criticality": 9,

            "instability": 0.8

        }

    }


    risks = analyzer.analyze(
        None,
        "login",
        metrics
    )


    assert "high fan-out function" in risks

    assert "critical function" in risks

    assert "unstable dependency" in risks