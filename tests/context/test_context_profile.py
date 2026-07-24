from pke.context.context_profile import ContextProfile
from pke.context.context_profile_analyzer import ContextProfileAnalyzer



def test_context_profile_serialization():


    profile = ContextProfile(
        name="debug",
        prioritize_risks=True
    )


    data = profile.to_dict()


    assert data["name"] == "debug"

    assert data["prioritize_risks"] is True



def test_profile_analyzer_debug():


    profile = ContextProfileAnalyzer().analyze(

        "fix login bug"

    )


    assert profile.name == "debug"

    assert profile.expand_callers is True

    assert profile.prioritize_risks is True



def test_profile_analyzer_explain():


    profile = ContextProfileAnalyzer().analyze(

        "explain authentication"

    )


    assert profile.name == "explain"

    assert profile.include_docs is True