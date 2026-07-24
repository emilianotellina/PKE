from pke.context.context_profile_selector import ContextProfileSelector



def test_selector_debug_profile():


    profile = ContextProfileSelector().select(

        "fix login bug"

    )


    assert profile.name == "debug"

    assert profile.prioritize_risks



def test_selector_security_profile():


    profile = ContextProfileSelector().select(

        "security audit"

    )


    assert profile.name == "security"



def test_selector_default_profile():


    profile = ContextProfileSelector().select(

        "random task"

    )


    assert profile.name == "default"