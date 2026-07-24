from pke.context.agent_registry import AgentRegistry
from pke.context.agent_profile import AgentProfile



def test_registry_returns_debug_agent():


    registry = AgentRegistry()


    agent = registry.get(
        "debug"
    )


    assert agent.name == "debug"

    assert agent.context_profile.name == "debug"



def test_registry_returns_security_agent():


    registry = AgentRegistry()


    agent = registry.get(
        "security"
    )


    assert agent.name == "security"

    assert agent.context_profile.name == "security"



def test_registry_lists_agents():


    registry = AgentRegistry()


    names = [

        item.name

        for item

        in registry.list()

    ]


    assert "debug" in names

    assert "security" in names



def test_register_custom_agent():


    registry = AgentRegistry()


    agent = AgentProfile(

        name="custom"

    )


    registry.register(
        agent
    )


    assert registry.contains(
        "custom"
    )


    assert registry.get(
        "custom"
    ).name == "custom"