from pke.context.context_profile_registry import ContextProfileRegistry
from pke.context.context_profile_selector import ContextProfileSelector



def test_registry_returns_debug_agent():


    registry = ContextProfileRegistry()


    profile = registry.get(
        "debug"
    )


    assert profile.name == "debug"

    assert profile.expand_callers is True



def test_registry_returns_security_agent():


    registry = ContextProfileRegistry()


    profile = registry.get(
        "security"
    )


    assert profile.name == "security"

    assert profile.prioritize_risks is True



def test_registry_lists_named_agents():


    registry = ContextProfileRegistry()


    names = [

        item.name

        for item

        in registry.list()

    ]


    assert "debug" in names

    assert "security" in names



def test_selector_uses_registry():


    selector = ContextProfileSelector()


    profile = selector.select(
        "fix login bug"
    )


    assert profile.name == "debug"