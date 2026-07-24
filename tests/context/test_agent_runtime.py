from pke.context.agent_selector import AgentSelector
from pke.context.agent_profile import AgentProfile
from pke.context.context_profile import ContextProfile


def test_agent_selector_returns_named_agent():


    agent = AgentSelector().select(
        "fix login bug"
    )


    assert agent.name == "debug"



def test_agent_contains_context_profile():


    agent = AgentSelector().select(
        "security audit"
    )


    assert agent.context_profile.name == "security"



def test_custom_agent_profile():


    agent = AgentProfile(

        name="custom",

        context_profile=ContextProfile(
            name="custom"
        )

    )


    assert agent.context_profile.name == "custom"