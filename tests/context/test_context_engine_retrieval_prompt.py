from pke.context.context_engine import ContextEngine


class FakeFormatter:

    def format_optimized(
        self,
        optimized
    ):

        return "base prompt"



def test_context_engine_adds_retrieved_documents():

    engine = ContextEngine()

    engine.formatter = FakeFormatter()


    result = engine._append_retrieved_documents(

        "base prompt",

        [
            "Function.md",
            "File.md"
        ]

    )


    assert "Retrieved Knowledge" in result

    assert "Function.md" in result

    assert "File.md" in result