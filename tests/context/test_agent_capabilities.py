from pke.context.agent_registry import AgentRegistry



def test_debug_agent_capabilities():


    agent = AgentRegistry().get(
        "debug"
    )


    assert agent.has_capability(
        "bug_analysis"
    )


    assert agent.has_capability(
        "risk_analysis"
    )



def test_security_agent_capabilities():


    agent = AgentRegistry().get(
        "security"
    )


    assert agent.has_capability(
        "vulnerability_detection"
    )


    assert agent.has_capability(
        "risk_analysis"
    )



def test_agent_to_dict_contains_capabilities():


    agent = AgentRegistry().get(
        "security"
    )


    data = agent.to_dict()


    assert "capabilities" in data


    assert "risk_analysis" in data["capabilities"]