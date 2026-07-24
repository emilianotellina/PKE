from pke.agent.context_query import ContextQuery
from pke.context.context_profile import ContextProfile
from pke.context.context_profile_selector import ContextProfileSelector



def test_explicit_profile_overrides_selector():


    selector = ContextProfileSelector()


    selected = selector.select(
        "fix login bug"
    )


    assert selected.name == "debug"



    custom = ContextProfile(
        name="security"
    )


    assert custom.name == "security"



def test_selector_accepts_profile_name():


    selector = ContextProfileSelector()


    profile = selector.registry.get(
        "security"
    )


    assert profile.name == "security"



def test_selector_debug_profile_configuration():


    selector = ContextProfileSelector()


    profile = selector.select(
        "fix login bug"
    )


    assert profile.name == "debug"

    assert profile.prioritize_risks is True

    assert profile.expand_callers is True



def test_selector_security_profile_configuration():


    selector = ContextProfileSelector()


    profile = selector.select(
        "security audit"
    )


    assert profile.name == "security"

    assert profile.prioritize_risks is True

    assert profile.prioritize_dependencies is True