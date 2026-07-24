from pke.context.agent_selector import AgentSelector



def test_selector_returns_debug_agent():


    agent = AgentSelector().select(
        "fix login bug"
    )


    assert agent.name == "debug"


    assert agent.context_profile.name == "debug"



def test_selector_returns_security_agent():


    agent = AgentSelector().select(
        "security audit"
    )


    assert agent.name == "security"


    assert agent.context_profile.name == "security"



def test_selector_returns_refactor_agent():


    agent = AgentSelector().select(
        "refactor authentication"
    )


    assert agent.name == "refactor"



def test_selector_returns_explain_agent():


    agent = AgentSelector().select(
        "explain login flow"
    )


    assert agent.name == "explain"



def test_selector_returns_default_agent():


    agent = AgentSelector().select(
        "create documentation"
    )


    assert agent.name == "default"