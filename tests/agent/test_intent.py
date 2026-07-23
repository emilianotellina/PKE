from pke.agent.intent import TaskIntentAnalyzer



def test_intent_modify():


    analyzer = TaskIntentAnalyzer()


    result = analyzer.analyze(
        "modifica autenticazione login"
    )


    assert result.action == "modify"


    assert result.domain == (
        "authentication"
    )


    assert "login" in result.keywords



def test_intent_add():


    analyzer = TaskIntentAnalyzer()


    result = analyzer.analyze(
        "aggiungi controllo password"
    )


    assert result.action == "add"