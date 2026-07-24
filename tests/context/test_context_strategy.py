from pke.context.context_strategy import ContextStrategyAnalyzer



def test_context_strategy_explain():


    analyzer = ContextStrategyAnalyzer()


    strategy = analyzer.analyze(
        "explain login"
    )


    assert strategy.include_docs

    assert strategy.expand_dependencies

    assert strategy.max_depth == 2



def test_context_strategy_bug_fix():


    analyzer = ContextStrategyAnalyzer()


    strategy = analyzer.analyze(
        "fix authentication bug"
    )


    assert strategy.expand_callers

    assert strategy.include_side_effects

    assert strategy.max_depth == 3



def test_context_strategy_refactor():


    analyzer = ContextStrategyAnalyzer()


    strategy = analyzer.analyze(
        "rename login function"
    )


    assert strategy.expand_callers

    assert strategy.include_tests