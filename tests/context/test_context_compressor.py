from pke.context.context import SymbolContext
from pke.context.context_compressor import ContextCompressor



def test_context_compressor_generates_summary():


    items = [

        (
            SymbolContext(
                name="database"
            ),
            80
        ),

        (
            SymbolContext(
                name="repository"
            ),
            60
        )

    ]


    result = ContextCompressor().compress(
        items
    )


    assert "(summary)" in result

    assert "database" in result

    assert "repository" in result





def test_context_compressor_keeps_scores():


    items = [

        (
            SymbolContext(
                name="authenticate"
            ),
            90
        )

    ]


    result = ContextCompressor().compress(
        items
    )


    assert "authenticate" in result

    assert "90" in result





def test_context_compressor_respects_budget():


    items = [

        (
            SymbolContext(
                name="very_long_function_name"
            ),
            100
        ),

        (
            SymbolContext(
                name="another_function"
            ),
            80
        )

    ]


    result = ContextCompressor().compress(
        items,
        budget=3
    )


    assert "(summary)" in result

    assert len(
        result.split()
    ) <= 3





def test_context_compressor_empty():


    result = ContextCompressor().compress(
        []
    )


    assert result == ""