from pke.context.context_engine import ContextEngine
from pke.context.context import AIContext, SymbolContext



def test_context_engine_contains_graph():


    class FakeBuilder:


        def build(
            self,
            *args,
            **kwargs
        ):

            context = AIContext()


            context.symbols.append(

                SymbolContext(

                    name="login",

                    calls=[
                        "authenticate"
                    ]

                )

            )


            return context



    engine = ContextEngine()


    engine.builder = FakeBuilder()


    result = engine.build(
        project=None,
        target="login"
    )


    assert "graph" in result


    assert "login" in result["graph"]